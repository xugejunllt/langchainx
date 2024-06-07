# from langchain.document_loaders import TextLoader
from ragas.testset.generator import TestsetGenerator
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

loader = TextLoader('SteveJobsSpeech.txt', encoding='utf-8')
documents = loader.load()

generator_llm = ChatOpenAI()
critic_llm = ChatOpenAI()
embeddings = OpenAIEmbeddings()

generator = TestsetGenerator.from_langchain(
    generator_llm,
    critic_llm,
    embeddings
)

testset = generator.generate_with_langchain_docs(documents, test_size=8)

df = testset.to_pandas()
# 将数据集保存到 csv 文件中
df.to_csv('testset.csv')
