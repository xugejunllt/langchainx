# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("pdf_loader_demo.pdf")
# pages = loader.load()
# print(len(pages)) # 33，与 pdf页数一致
# print(pages[0])
# """
# Document(page_content='page_content='Published as a conference...', metadata={'source': 'pdf_loader_demo.pdf', 'page': 0})
# """


from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("pdf_loader_demo.pdf", extract_images=True)
pages = loader.load()
print(pages[5].page_content)
"""
Published as a conference paper at ICLR 2023
Type Deﬁnition ReAct CoT
SuccessTrue positive Correct reasoning trace and facts 94% 86%
False positive Hallucinated reasoning trace or facts 6% 14%
FailureReasoning error Wrong reasoning trace (including failing to recover from repetitive steps) 47% 16%
Search result error Search return empty or does not contain useful information 23% -
Hallucination Hallucinated reasoning trace or facts 0% 56%
Label ambiguity Right prediction but did not match the label precisely 29% 28%
Table 2: Types of success and failure modes of ReAct andCoT on HotpotQA, as well as their
percentages in randomly selected examples studied by human.
...
"""
