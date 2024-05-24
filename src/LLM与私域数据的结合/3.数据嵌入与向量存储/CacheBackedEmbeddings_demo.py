import time
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
import os

os.environ['OPENAI_API_KEY'] = 'sk-yAiO2z9iZxtcXS0QueiDgfqaUqIIjkkmSLFxZXn7mkD2Zimh'
os.environ['OPENAI_API_BASE'] = 'https://api.chatanywhere.com.cn/v1'
embeddings_model = OpenAIEmbeddings()
store = LocalFileStore("./cache/")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(embeddings_model, store)

text = "What's your name?"
start_time = time.time()
embedded1 = cached_embedder.embed_documents([text])
embedded1_end_time = time.time()
embedded1_cost_time = embedded1_end_time - start_time
print(f"Time taken for first embedding: {embedded1_cost_time} seconds")
embedded2 = cached_embedder.embed_documents([text])
print(f"Time taken for second embedding: {time.time() - embedded1_end_time} seconds")
