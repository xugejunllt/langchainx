from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=1,
    chunk_overlap=0
)

text = '666666\n\n333\n\n22'
print(splitter.split_text(text))
"""
['666666', '333', '22']
"""
