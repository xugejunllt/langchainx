# 将最相关的放在首尾，而把最不相关的放在中间位置，能有效提高 LLM 的响应质量。

from langchain_core.documents import Document
from langchain_community.document_transformers import (
    LongContextReorder,
)

# 模拟原始检索器返回的文档列表
docs = [Document(page_content="A"), Document(page_content="B"), Document(page_content="C"),
        Document(page_content="D"), Document(page_content="E"), Document(page_content="F"),
        Document(page_content="G")]

reordering = LongContextReorder()
reordered_docs = reordering.transform_documents(docs)
print(reordered_docs)
