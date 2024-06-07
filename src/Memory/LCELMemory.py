from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

template_str = """
You are a chatbot having a conversation with a human.
Previous conversation:
{chat_history}
Human: {question}
AI:"""
prompt_template = PromptTemplate.from_template(template_str)
llm = ChatOpenAI(temperature=0)
memory_chain = prompt_template | llm

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


from langchain_core.runnables.history import RunnableWithMessageHistory

with_message_history = RunnableWithMessageHistory(
    memory_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history",
)

# 调用invoke方法执行链时，需要指定本次的session_id。
print(with_message_history.invoke(
    {"question": "你好，我是jack"},
    config={"configurable": {"session_id": "abc123"}},
))

print(with_message_history.invoke(
    {"question": "我的名字叫什么?"},
    config={"configurable": {"session_id": "abc123"}},
))
