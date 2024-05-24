from langchain_text_splitters import NLTKTextSplitter

splitter = NLTKTextSplitter(
    chunk_size=1,
    chunk_overlap=0
)


text = 'This is a test sentence for testing NLTKTextSplitter! It will be splitted to several sub sentences, let see how it works.'
print(splitter.split_text(text))
"""
['This is a test sentence for testing NLTKTextSplitter!', 'It will be splitted to several sub sentences, let see how it works.']
"""
