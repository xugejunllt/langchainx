from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

# 按页加载文档
loader = PyPDFLoader("任正非2018.pdf")
docs = loader.load()
prompt_template = """Write a concise summary of the following:


"{text}"

ANSWER IN THE TEXT ORIGINAL LANGUAGE!
CONCISE SUMMARY:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

stuff_chain = load_summarize_chain(llm=ChatOpenAI(), chain_type="stuff", prompt=prompt)
# 总结第一页内容
print(stuff_chain.invoke(docs[:3])["output_text"])
