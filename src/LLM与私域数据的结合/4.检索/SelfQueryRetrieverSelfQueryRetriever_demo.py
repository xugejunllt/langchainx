from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

loader = PyPDFLoader("ReAct.pdf")
pages = loader.load()

Chroma.from_documents(documents=pages, embedding=OpenAIEmbeddings(), persist_directory="./chroma_db")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())

from langchain.chains.query_constructor.base import AttributeInfo
metadata_field_info = [
    AttributeInfo(
        name="page",
        description="The page number of the document.",
        type="integer",
    ),
    AttributeInfo(
        name="source",
        description="The source of the document.",
        type="string"
    )
]


from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import ChatOpenAI

# 文档内容描述
document_content_description = "SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS"
self_query_retriever = SelfQueryRetriever.from_llm(
    ChatOpenAI(),
    vectorstore,
    document_content_description,
    metadata_field_info,
    verbose = True
)

import logging
logging.basicConfig()
# 注意下面的 logger 名称不能写错
logging.getLogger("langchain.retrievers.self_query").setLevel(logging.INFO)

print(self_query_retriever.invoke("I want to query something about ReAct in page 2"))
