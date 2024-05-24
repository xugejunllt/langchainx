from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader("src/", glob="*.pdf", loader_cls=PyPDFLoader)

data = loader.load()
print(len(data))  # 33
