# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
# 注意需要安装 langchain-chroma：pip install langchain-chroma
from langchain_chroma import Chroma
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

# 加载数据
loader = TextLoader('SteveJobsSpeech.txt', encoding='utf-8')
documents = loader.load()

# 分块数据
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# 数据嵌入向量化
vectorStore = Chroma.from_documents(chunks, OpenAIEmbeddings())

# 创建检索器
retriever = vectorStore.as_retriever()

# 接下来，使用上面生成的检索器，构造一个基础的 RAG 应用。
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

template = """
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
keep the answer concise.
Question: 
-------
{question}
------- 

Context: 
-------
{context} 
-------
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
rag_chain = (
    {"context": retriever,  "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(rag_chain.invoke("乔帮主这篇演讲的主旨是什么？"))

# 一个RAG系统，无非做两件事：检索数据、LLM生成答案--> 检索器+生成器
# RAGs是一个专门用于评估RAG的开源框架
# RAGs会通过 LLM 生成与预先给定答案相关的多个潜在问题，然后计算原始问题与这些问题之间的相似度。
# 在整体流程上，可以使用answer_similarity(答案语义相似度)和answer_correctness(答案正确性)作为评估 RAG 整体性能的指标。所有指标的分数在 [0, 1] 之间，得分越高表示性能越好。

from datasets import Dataset

# 问题
questions = [
    "Why did Steve Jobs's biological mother decide to put him up for adoption?",
    "How did Steve Jobs's calligraphy class at Reed College impact his future work?",
    "What event catalyzed the creation of Pixar and Steve Jobs's return to Apple?"
]
# 标准答案
ground_truths = [
    "She was a young, unwed college graduate who wanted her child to be raised by college graduates.",
    "The knowledge of typography he gained was later used to design the Macintosh computer with high-quality typography, influencing the industry.",
    "Being fired from Apple led to the founding of NeXT and Pixar, and eventually to his return to Apple after NeXT was acquired."
]

answers = []
contexts = []

for query in questions:
    # 添加LLM 输出结果
    answers.append(rag_chain.invoke(query))
    # 添加检索结果
    contexts.append([docs.page_content for docs in retriever.get_relevant_documents(query)])

# 构造评估数据集
dataset = Dataset.from_dict({
    "question": questions,
    "contexts": contexts,
    "answer": answers,
    "ground_truth": ground_truths
})

from ragas import evaluate
from ragas.metrics import context_recall

result = evaluate(
    dataset = dataset,
    metrics=[
        context_recall
    ]
)

df = result.to_pandas()
df.to_csv('context_recall.csv')
