# -*- coding: utf-8 -*-
"""
@Author: Chenxr
@Date:   2025/9/26 01:15
@Last Modified by:   Chenxr
@Last Modified time: 2025/9/26 01:15
@Description: 
"""
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging
import os

# 设置USER_AGENT环境变量
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_vector_store_from_web(url, chunk_size=500, chunk_overlap=50):
    """
    从网页创建向量存储

    Args:
        url: 网页URL
        chunk_size: 文本块大小
        chunk_overlap: 文本块重叠大小

    Returns:
        FAISS向量存储对象
    """
    try:
        # 1. 加载网页文档（修复features参数问题）
        logger.info(f"开始加载网页: {url}")

        # 修复：移除bs_kwargs中的features参数，使用默认设置
        loader = WebBaseLoader(
            web_paths=[url],  # 使用web_paths而不是web_path
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(id="UCAP-CONTENT")
                # 移除features参数，让BeautifulSoup自动选择解析器
            )
        )

        docs = loader.load()

        if not docs or len(docs) == 0:
            raise ValueError("未从网页中提取到任何内容")

        logger.info(f"成功加载文档，原始内容长度: {len(docs[0].page_content)} 字符")

        # 2. 分割文档
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
        )

        documents = text_splitter.split_documents(docs)
        logger.info(f"文档分割完成，共 {len(documents)} 个文本块")

        # 3. 初始化嵌入模型
        embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002"
        )

        # 4. 创建向量存储
        logger.info("开始创建向量存储...")
        vector_store = FAISS.from_documents(
            documents=documents,
            embedding=embeddings
        )

        logger.info("向量存储创建成功!")
        return vector_store

    except Exception as e:
        logger.error(f"创建向量存储时出错: {str(e)}")
        raise

# 替代方案：如果上述方法仍有问题，可以使用更简单的配置
def create_vector_store_simple(url, chunk_size=500, chunk_overlap=50):
    """
    简化版的向量存储创建函数
    """
    try:
        logger.info(f"使用简化方法加载网页: {url}")

        # 方法1：完全移除bs_kwargs，使用默认解析
        loader = WebBaseLoader(web_paths=[url])

        # 或者方法2：只保留必要的解析器设置
        # loader = WebBaseLoader(
        #     web_paths=[url],
        #     bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_="content"))  # 根据实际HTML结构调整
        # )

        docs = loader.load()

        if not docs:
            raise ValueError("未从网页中提取到任何内容")

        logger.info(f"成功加载文档，内容长度: {len(docs[0].page_content)} 字符")

        # 分割文档
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        documents = text_splitter.split_documents(docs)
        logger.info(f"文档分割完成，共 {len(documents)} 个文本块")

        # 创建向量存储
        embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
        vector_store = FAISS.from_documents(documents, embeddings)

        logger.info("向量存储创建成功!")
        return vector_store

    except Exception as e:
        logger.error(f"简化方法也出错: {str(e)}")
        # 尝试最基本的加载方式
        return create_vector_store_minimal(url)

def create_vector_store_minimal(url):
    """
    最简版本的向量存储创建
    """
    try:
        logger.info("尝试最简方法...")

        # 最简配置，不使用任何bs_kwargs
        loader = WebBaseLoader(web_paths=[url])
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        documents = text_splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
        vector_store = FAISS.from_documents(documents, embeddings)

        return vector_store

    except Exception as e:
        logger.error(f"所有方法都失败: {str(e)}")
        raise

def search_similar_documents(vector_store, query, k=3):
    """
    在向量存储中搜索相似文档
    """
    try:
        similar_docs = vector_store.similarity_search(query, k=k)
        logger.info(f"找到 {len(similar_docs)} 个相关文档")
        return similar_docs
    except Exception as e:
        logger.error(f"搜索文档时出错: {str(e)}")
        return []

# 使用示例
if __name__ == "__main__":
    url = "https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm"

    try:
        # 首先尝试修复后的方法
        vector_store = create_vector_store_from_web(url)

        # 如果仍有问题，使用简化方法
        # vector_store = create_vector_store_simple(url)

        # 测试搜索功能
        query = "借款合同"
        similar_docs = search_similar_documents(vector_store, query)

        print(f"\n查询: '{query}'")
        print("相关文档:")
        for i, doc in enumerate(similar_docs):
            print(f"{i+1}. {doc.page_content[:200]}...")

    except Exception as e:
        print(f"处理过程中出错: {e}")
        print("尝试检查以下可能的问题:")
        print("1. 网络连接是否正常")
        print("2. 网页URL是否有效")
        print("3. OpenAI API密钥是否正确设置")
        print("4. 尝试使用不同的HTML解析方式")