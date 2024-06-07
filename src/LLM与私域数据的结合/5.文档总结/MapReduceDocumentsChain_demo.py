from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

loader = PyPDFLoader("任正非2018.pdf")
docs = loader.load()
print(f'加载pdf内容:{docs[:2]}')
result = [doc.page_content for doc in docs[:2]]
print(f'提取后的内容{result}')

prompt_template = """Write a concise summary of the following:


"{text}"

ANSWER IN THE TEXT ORIGINAL LANGUAGE!
CONCISE SUMMARY:"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

map_reduce_chain = load_summarize_chain(llm=ChatOpenAI(model_name="gpt-3.5-turbo-1106"), input_key="input_documents",
                                        chain_type="map_reduce", map_prompt=prompt, combine_prompt=prompt)
print(map_reduce_chain({"input_documents": docs[:10]}, return_only_outputs=True))
