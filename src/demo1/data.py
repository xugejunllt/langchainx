# load
import bs4
from langchain_community.document_loaders import WebBaseLoader
# split
from langchain.text_splitter import RecursiveCharacterTextSplitter
# vector storage
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

loader = WebBaseLoader(
    web_path="https://www.gov.cn/jrzg/2013-10/25/content_2515601.htm",
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
        class_=("p1")
    ))
)
docs = loader.load()
print(docs)

# split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(len(splits))
print(len(splits[0].page_content))

proxy_url = 'http://new.lishiming.net:15888'
os.environ['http_proxy'] = os.environ['https_proxy'] = proxy_url
embeddings = OpenAIEmbeddings(openai_api_key="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")
# vector storage
db = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")
# db = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(), persist_directory="./chroma_db")
