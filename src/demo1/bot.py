from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import os
proxy_url = 'http://new.lishiming.net:15888'
os.environ['http_proxy'] = os.environ['https_proxy'] = proxy_url

vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings(openai_api_key="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"))
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
prompt_template_str = """
你是问答任务的助手。使用以下检索到的上下文来回答问题。如果你不知道答案，就说你不知道。最多使用三个句子并保持答案简洁。
问题: {question}
上下文: {context}
答案:
"""
prompt_template = PromptTemplate.from_template(prompt_template_str)


llm = ChatOpenAI(openai_api_key="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", model_name="gpt-3.5-turbo",
                 temperature=0)


# docs = retriever.invoke("发生争议如何解决？")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
)
app = FastAPI(
    title="消费者权益智能助手",
    version="1.0",
)
# 3. Adding chain route
add_routes(
    app,
    rag_chain,
    path="/consumer_ai",
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
