from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
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

refine_chain = load_summarize_chain(llm=ChatOpenAI(model_name="gpt-3.5-turbo-1106"), input_key="input_documents",
                                    chain_type="refine", refine_prompt=prompt)

# refine_chain = load_summarize_chain(llm=ChatOpenAI(), chain_type="refine", prompt=prompt)
print(refine_chain({"input_documents": docs[:10]}, return_only_outputs=True))
