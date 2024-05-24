from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

llm = ChatOpenAI()
joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | llm
poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | llm
)

map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

output = map_chain.invoke({"topic": "bear"})
print()
