# promptTemplate = """
# 以下<history>标签中是AI与Human的历史对话记录，参考历史上下文，回答用户输入的问题。
# 历史对话:
# <history>
# {chat_history}
# </history>
# Human: {question}
# AI:"""

from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os,time


os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

memory = ConversationBufferMemory(memory_key="chat_history")

template_str = """
You are a chatbot having a conversation with a human.
Previous conversation:
{chat_history}
Human: {question}
AI:"""

prompt_template = PromptTemplate.from_template(template_str)

llm = ChatOpenAI(temperature=0)
memory_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    verbose=True,  # verbose 表示打印详细过程
    memory=memory,
)


memory_chain.predict(question="你好，我是jack")
memory_chain.predict(question="你还记得我叫什么吗？")
memory_chain.predict(question="好的")

