from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import InMemoryByteStore
from langchain.retrievers import MultiVectorRetriever
import uuid
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'
# 原始文档列表
docs = [
    Document(page_content="LangChain is a framework for developing applications powered by large language models (LLMs)"),
    Document(page_content="Build your applications using LangChain's open-source building blocks and components. Hit the ground running using third-party integrations and Templates.Use LangSmith to inspect, monitor and evaluate your chains, so that you can continuously optimize and deploy with confidence.Turn any chain into an API with LangServe")
]

# 用于存储原始文档列表
store = InMemoryByteStore()

vectorstore = Chroma(embedding_function=OpenAIEmbeddings())
# 指定子文档metadata 中标识对应大文档的 key
id_key = "doc_id"
# vectorstore：嵌入文档和从向量数据库中查询文档所使用的向量存储对象。
# BaseStore
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)
# 为每个原始文档指定一个 id
doc_ids = [str(uuid.uuid4()) for _ in docs]
# 用于分割原始文档为小文档
child_text_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
sub_docs = []
for i, doc in enumerate(docs):
    _id = doc_ids[i]
    _sub_docs = child_text_splitter.split_documents([doc])
    for _doc in _sub_docs:
        # 子文档 metadata 存储对应大文档的 id
        _doc.metadata[id_key] = _id
    sub_docs.extend(_sub_docs)
# 子文档嵌入存储到向量数据库中
retriever.vectorstore.add_documents(sub_docs)
# 原始文档存储到 docstore 中，docstore就是BaseStore
retriever.docstore.mset(list(zip(doc_ids, docs)))
# 先使用vectorstore查询获取子文档块列表，然后，通过子文档块中元信息的id_key对应的 value，在docstore找出对应的大文档。
print(retriever.vectorstore.similarity_search("LangServe"))
