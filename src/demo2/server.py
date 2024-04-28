from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langserve import add_routes
import os
os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
rag_chain = (
    llm
    | StrOutputParser()
)
app = FastAPI(
  title="prompt教学",
  version="1.0",
)
# 3. Adding chain route
add_routes(
    app,
    rag_chain,
    path="/prompt_ai",
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
