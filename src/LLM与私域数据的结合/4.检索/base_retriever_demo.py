'''ContextualCompressionRetriever的解决思路是对检索到的文档进行一次 “裁剪”，只保留与查询问题强相关的文档内容。'''

from langchain.retrievers import ContextualCompressionRetriever
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

texts = [
    "LLM是一种基于大量文本数据训练的深度学习模型，它能够捕捉语言的复杂性和多样性。通过学习，LLM能够理解用户的输入，并生成连贯、准确的文本回复。这种模型通常具有数十亿甚至数万亿个参数，使其能够处理复杂的语言任务。LLM可以作为聊天机器人，提供24/7的客户支持，回答客户的常见问题，提高服务效率;程序员可以利用LLM辅助编写和优化代码，提高开发效率。随着技术的进步，LLM将在更多领域得到应用，为人们的工作和生活带来便利。同时，开发者也需要关注模型的伦理和社会责任问题，确保技术的健康发展。",
    "今天天气真好"]
vectorstore = Chroma.from_texts(texts, OpenAIEmbeddings())
# 使用语义相似度检索 top2 的文档
base_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
original_docs = base_retriever.invoke("LLM对程序员有什么帮助？")
print("original_docs: ", original_docs)

# contextual_compression_retriever = ContextualCompressionRetriever
# new_docs = ContextualCompressionRetriever.invoke("LLM对程序员有什么帮助？")
# print("new_docs: ", new_docs)
#
# multi_query_retriever = MultiQueryRetriever.from_llm(
#     retriever=vector_store_retriever, llm=ChatOpenAI()
# )
