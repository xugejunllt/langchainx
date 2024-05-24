from langchain_text_splitters import Language,RecursiveCharacterTextSplitter
from langchain_text_splitters import S

code = """
def hello_world():
    print("Hello World!")

if __name__ == '__main__':
    hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)

python_chunks = python_splitter.split_text(code)
print(python_chunks)
"""
['def hello_world():\n    print("Hello World!")', "if __name__ == '__main__':\n    hello_world()"]
"""
