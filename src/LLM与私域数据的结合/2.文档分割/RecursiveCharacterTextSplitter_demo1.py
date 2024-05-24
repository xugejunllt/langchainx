from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=5,
    chunk_overlap=1
)

# 下面text是一段测试RecursiveCharacterTextSplitter的文本
text = "This is a test text for the RecursiveCharacterTextSplitter. It is a long text with many words."
print(splitter.split_text(text))
"""
['This', 'is a', 'test', 'text', 'for', 'the', 'Recu', 'ursiv', 'veCha', 'aract', 'terTe', 'extSp', 'plitt', 'ter.', 'It', 'is a', 'long', 'text', 'with', 'many', 'word', 'ds.']
"""
