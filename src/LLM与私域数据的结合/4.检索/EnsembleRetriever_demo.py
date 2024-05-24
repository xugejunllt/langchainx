# 倒数排名融合（RRF）
# 根据 RRF 的公式，RRFscore(d) = Σ(1/(k + r(d)))，其中 k 是一个常数（在论文中 k 被设定为 60），r(d) 是文档在排名中的位置
# 这里简单解释下 BM25 搜索算法，它基于关键字搜索，结合词频（关键字出现的次数）、逆文档频率（关键词在整个文档中的罕见程度）、文档长度因子等因素来计算文档与查询的相关性得分

from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

doc_list_1 = [
    "I like apples",
    "I like oranges",
    "Apples and oranges are fruits",
]

bm25_retriever = BM25Retriever.from_texts(
    doc_list_1, metadatas=[{"source": 1}] * len(doc_list_1)
)
bm25_retriever.k = 2

doc_list_2 = [
    "I like apples",
    "You like apples",
    "You like oranges",
]

vectorstore = Chroma.from_texts(
    doc_list_2, OpenAIEmbeddings(), metadatas=[{"source": 2}] * len(doc_list_2)
)

chroma_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, chroma_retriever], weights=[0.5, 0.5]
)

docs = ensemble_retriever.get_relevant_documents("apples")
print(docs)
