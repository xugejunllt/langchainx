from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

texts = [
    "我家的狗全身大部分都是黑色的，但尾巴是白色的，特别喜欢出去玩",
    "我家狗狗身上黑乎乎的，就尾巴那一块儿白，它老爱往外跑",
    "我家的猫全身黑色，也很喜欢出门",
    "夏天特别适合游泳"
]

vector_store = Chroma.from_texts(texts, embedding=OpenAIEmbeddings())

question = "简单描述下我家的狗"

'''语义相似性搜索（similarity）'''
retriever = vector_store.as_retriever(search_type ="similarity", search_kwargs={"k": 3})
# print(retriever.get_relevant_documents(question))
print(retriever.invoke(question))


'''限制相似度阈值（similarity_score_threshold）'''
retriever = vector_store.as_retriever(search_type ="similarity_score_threshold", search_kwargs={"k": 3, "score_threshold": 0.78})
# print(retriever.get_relevant_documents(question))
print(retriever.invoke(question))


'''最大边际相关性搜索（MMR）'''
retriever = vector_store.as_retriever(search_type ="mmr", search_kwargs={"k": 2})
# print(retriever.get_relevant_documents(question))
print(retriever.invoke(question))
