import requests
import traceback
from retrying import retry
from transformers import AutoTokenizer
from loguru import logger

def search_rerank_func_wrap(search_rerank_func):
    def wrapper(*args, **kwargs):
        # 用传入的函数
        docs = search_rerank_func(*args, **kwargs)
        doc_strs = [doc.document for doc in docs]
        return doc_strs
    return wrapper

def check_query(query: str):
    if not query: return None
    if "?" not in query and "？" not in query:
        query=query+"？"
    return query

def tokenize_words(words: list[str], tokenizer: AutoTokenizer):
    tokenized_text = sum([tokenizer.tokenize(word) for word in words], [])
    return tokenized_text

@retry(stop_max_attempt_number=3)
def invoke_labeler(query, chunks, labeler_url):

    url = labeler_url
    data = {
        "query": query,
        "chunks": chunks
    }
    try:
        response = requests.post(url, json=data)
    except Exception as e:
        logger.error(f"请求labeler失败，原因：{e} {traceback.format_exc()}")
        raise Exception(f"请求labeler失败，原因：{e} {traceback.format_exc()}")
    infos, labels= response.json()["data"].values()
    return infos, labels

def invoke_labeler_main(query, chunks, labeler_url):
    try:
        infos, labels = invoke_labeler(query, chunks, labeler_url)
    except Exception as e:
        return [""]*len(chunks), ["<TERMINATE>"]*len(chunks)
    return infos, labels
    

@retry(stop_max_attempt_number=3)
def invoke_filter(prev_query, info_list, filter_url):

    url = filter_url
    data = {
        "prev_query": prev_query,
        "info_list": info_list
    }
    try:
        response = requests.post(url, json=data)
    except Exception as e:
        logger.error(f"请求filter失败，原因：{e} {traceback.format_exc()}")
        raise Exception(f"请求filter失败，原因：{e} {traceback.format_exc()}")
    query_info_str, filtered_query= response.json()["data"].values()
    return query_info_str, filtered_query

def invoke_filter_main(prev_query, info_list, filter_url):
    try:
        query_info_str, filtered_query = invoke_filter(prev_query, info_list, filter_url)
    except Exception as e:
        return prev_query, prev_query
    return query_info_str, filtered_query
    

def merge_and_deduplicate_sentences(data):
    # 合并列表中的所有字符串
    combined_text = '。'.join(data)
    
    # 按照标点符号分句（包括问号）
    import re
    sentences = re.split(r'[。！？；，]', combined_text)
    
    # 去重并去除空字符串
    unique_sentences = list(dict.fromkeys([s.strip() for s in sentences if s.strip()]))
    
    # 重新组合为字符串
    result = ' '.join(unique_sentences)
    return result

def remove_duplicate_substrings(s):
    """
    去除字符串 s 中重复的子串（长度 >= 4），只保留第一个出现的子串。
    """
    n = len(s)
    seen = set()  # 用于记录已经出现过的子串
    result = []   # 用于存储最终结果

    i = 0
    while i < n:
        # 检查从 i 开始的所有可能的子串（长度 >= 4）
        found_duplicate = False
        for j in range(i + 4, n + 1):
            substring = s[i:j]
            if substring in seen:
                # 如果子串已经出现过，跳过整个子串
                i = j  # 移动指针到子串的末尾
                found_duplicate = True
                break
        if not found_duplicate:
            # 如果未找到重复子串，加入当前字符
            result.append(s[i])
            # 更新 seen 集合，记录所有以 s[i] 结尾的长度 >= 4 的子串
            for k in range(i + 1, min(i + 5, n + 1)):
                seen.add(s[i:k])

        i += 1

    return ''.join(result)

def process_next_query_info(next_query_info):
    """
    处理 next_query_info 列表中的每个元素，去除重复的子串。
    """
    return [remove_duplicate_substrings(item) for item in next_query_info]
