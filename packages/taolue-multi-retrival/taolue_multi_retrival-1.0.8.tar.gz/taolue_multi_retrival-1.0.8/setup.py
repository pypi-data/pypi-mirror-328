from setuptools import setup, find_packages

setup(
    name='taolue_multi_retrival',  # 包名
    version='1.0.8',  # 版本号
    packages=["taolue_multi_retrival"],  # 自动查找包
    author='zhaowang',
    author_email='zhaowang@stonehg.com',
    description='韬略问答Agent多跳策略的多轮检索模块',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.10',  # 指定支持的Python版本
    install_requires=["jieba","loguru","Requests","retrying","setuptools","transformers"]
)