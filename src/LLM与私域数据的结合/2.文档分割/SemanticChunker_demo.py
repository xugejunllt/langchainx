from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import CacheBackedEmbeddings
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'

text = """
LangChain is a framework for developing applications powered by language models. It enables applications that:

Are context-aware: connect a language model to sources of context (prompt instructions, few shot examples, content to ground its response in, etc.)
Reason: rely on a language model to reason (about how to answer based on provided context, what actions to take, etc.)
This framework consists of several parts.

LangChain Libraries: The Python and JavaScript libraries. Contains interfaces and integrations for a myriad of components, a basic run time for combining these components into chains and agents, and off-the-shelf implementations of chains and agents.
LangChain Templates: A collection of easily deployable reference architectures for a wide variety of tasks.
LangServe: A library for deploying LangChain chains as a REST API.
LangSmith: A developer platform that lets you debug, test, evaluate, and monitor chains built on any LLM framework and seamlessly integrates with LangChain.
"""

text_splitter = SemanticChunker(embeddings = OpenAIEmbeddings())
chunks = text_splitter.split_text(text)
print(len(chunks)) # 2
print(chunks)
"""
['\nLangChain is a framework for developing applications powered by language models. It enables applications that:\n\nAre context-aware: connect a language model to sources of context (prompt instructions, few shot examples, content to ground its response in, etc.)\nReason: rely on a language model to reason (about how to answer based on provided context, what actions to take, etc.)\nThis framework consists of several parts. LangChain Libraries: The Python and JavaScript libraries.', 
 'Contains interfaces and integrations for a myriad of components, a basic run time for combining these components into chains and agents, and off-the-shelf implementations of chains and agents. LangChain Templates: A collection of easily deployable reference architectures for a wide variety of tasks. LangServe: A library for deploying LangChain chains as a REST API. LangSmith: A developer platform that lets you debug, test, evaluate, and monitor chains built on any LLM framework and seamlessly integrates with LangChain. ']
"""
