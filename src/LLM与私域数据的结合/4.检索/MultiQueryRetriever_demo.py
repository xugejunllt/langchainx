from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'
texts=["""
You are an AI language model assistant. Your task is 
    to generate 3 different versions of the given user 
    question to retrieve relevant documents from a vector  database. 
    By generating multiple perspectives on the user question, 
    your goal is to help the user overcome some of the limitations 
    of distance-based similarity search. Provide these alternative 
    questions separated by newlines. Original question: {question}
"""]

# texts = [...]
vector_store = Chroma.from_texts(texts, embedding=OpenAIEmbeddings())
vector_store_retriever = vector_store.as_retriever(search_type ="mmr", search_kwargs={"k": 2})

multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store_retriever, llm=ChatOpenAI()
)


import logging

logging.basicConfig()
# 注意下面的 logger 名称不能写错
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

print(multi_query_retriever.invoke("简单描述下我家的狗"))
