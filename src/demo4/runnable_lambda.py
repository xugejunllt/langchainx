from langchain_core.runnables import RunnableLambda
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'


def report_to_log(llm_answer: str):
    print(f"Reporting {llm_answer} to log system")
    return llm_answer


prompt = PromptTemplate.from_template("answer the question: {question}\n\n answer:")
chain = prompt | OpenAI() | RunnableLambda(report_to_log) | StrOutputParser()
chain.invoke({"question": "whats 2 + 2?"})
