import jieba.posseg as pseg

def extract_key_info(text):
    """
    通过词性标注和去停用词提取有效信息
    
    Args:
        text: 输入文本
    Returns:
        set: 有效词汇集合
    """
    # 词性标注
    words = pseg.cut(text)
    
    # 有效词性列表
    valid_pos = {'n', 'nr', 'ns', 'nt', 'nz', 'vn', 'an'}
    
    # 停用词列表
    stop_words = {'的', '是', '在', '和', '与', '及', '了', '等', '中', '为', '被', '较', '将', '由', '对', '到'}
    
    # 提取有效词汇
    valid_words = set()
    for word, pos in words:
        if (pos in valid_pos or len(word) >= 2) and word not in stop_words:
            valid_words.add(word)
    
    return valid_words

def find_complete_info_texts(text_list, allowed_loss=2):
    """
    找出信息最完整的文本，允许少量信息损失
    
    Args:
        text_list: 文本列表
        allowed_loss: 允许丢失的词数
    """
    # 计算每个文本的有效信息量
    text_info = []
    all_words = set()
    
    # 首先收集所有有效词汇
    for text in text_list:
        words = extract_key_info(text)
        text_info.append((text, words, len(words)))
        all_words.update(words)
    
    # 按信息量排序
    text_info.sort(key=lambda x: x[2], reverse=True)
    
    # 选择互补的文本
    selected_texts = []
    covered_words = set()
    total_words = len(all_words)
    
    for text, words, _ in text_info:
        new_words = words - covered_words
        if new_words:
            # 计算信息覆盖率
            coverage_before = len(covered_words) / total_words
            coverage_after = len(covered_words | words) / total_words
            
            # 如果新增加的覆盖率超过阈值，或者是第一个文本，则选择该文本
            if not selected_texts or (coverage_after - coverage_before) > allowed_loss/total_words:
                selected_texts.append(text)
                covered_words.update(words)
        
        # 如果已经达到足够的覆盖率，就停止
        if len(all_words - covered_words) <= allowed_loss:
            break
    
    return selected_texts

def main(example_list):
    result = find_complete_info_texts(example_list, allowed_loss=2)
    print("包含主要信息的文本：")
    print(result)

if __name__ == "__main__":
    # example_list = [
    #     "Info: 第11航空队第3联队第517空运中队飞行员罗伯特·费雷尔robertferrell美阿拉斯加美国空军学院美国空军",
    #     "Info: 第11航空队第3联队第517空运中队飞行员罗伯特·费雷尔robertferrell",
    #     "Info: 第11航空队第3联队第517空运中队飞行员罗伯特·费雷尔robertferrell单太平洋空军第尔",
    #     "Info: 第5l作战大队指挥官马修·盖特克matthewc.gaetke盖特克美国空军男白人队",
    #     "Info: 第11航空队第3联队第517空运中队飞行员罗伯特·费雷尔robertferrell太平洋空军第航队3联队中队国尔",
    #     "Info: 第51作战大队指挥官马修·盖特克matthewc美国印太平洋空军第7航空队",
    #     "Info: 1.马修·盖特克matthewc.gaetke单位美国太平洋空军第7航空队岗位第51作战大队指挥官美国空军",
    #     "Info: 第11航空队第3联队第517空运中队飞行员罗伯特·费雷尔robertferrell美国印太令部太平洋空军",
    #     "Info: 罗伯特·费雷尔robertferrell太平洋空军第3联队第517空运中队飞行员美国空军白人",
    #     "Info: 第11航空队第3联队第517空运中队飞行��罗伯特·费雷尔robertferrell太平洋空军第11航空队第3联队空运中队"
    # ]
    example_list = [
                    "Info: 第8医疗大队高级士官长入伍时间1996年2月2月入伍",
                    "Info: 第8维修中队高级士官长丹尼尔·鲍尔斯danielpowers美国空军第七航空队鲍尔斯1978年",
                    "Info: 第8队高级士官长入伍时间1996年2月2月入伍",
                    "Info: 空军第8维修中队高级士官长入伍时间1998年9月入伍1998年9月入伍",
                    "Info: 第8维修中队高级士官长丹尼尔·鲍尔斯danielpowers尔·鲍尔斯鲍尔斯年1998年入伍",
                    "Info: 第空队第维修大队高级士官长入伍时间1999年1月入",
                    "Info: 第8维修中队高级士官长丹尼尔·鲍尔斯danielpowers1998年入伍",
                    "Info: 第8维修中队高级士官长丹尼尔·鲍尔斯danielpowers入伍时间1998年9月入伍",
                    "Info: 第8维修中队高级士官长丹尼尔·鲍尔斯danielpowers丹尼尔·鲍尔斯2023年2月19日",
                    "Info: 丹尼尔·鲍尔斯第8维修中队高级士官长2023年2月19日daniels8年1998年9入伍"
                ]
    import time
    start_time = time.time()
    main(example_list)
    end_time = time.time()
    print(f"运行时间: {end_time - start_time} 秒")