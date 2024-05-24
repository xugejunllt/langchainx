from langchain_community.document_loaders import UnstructuredPDFLoader
import pytesseract

from unstructured.partition.auto import partition
import os
os.environ['OCR_AGENT'] = 'unstructured.partition.utils.ocr_models.tesseract_ocr'
ocr_agent = os.getenv('OCR_AGENT')
print(f"OCR_AGENT: {ocr_agent}")

# 默认 single 模式
loader = UnstructuredPDFLoader("pdf_loader_demo.pdf")
pages = loader.load()
# print(len(pages)) # 1

# elements = partition("pdf_loader_demo.pdf")
# print(elements)



# # elements 模式
# loader = UnstructuredPDFLoader("pdf_loader_demo.pdf", mode="elements")
# pages = loader.load()
# print(pages[10].page_content)
# """
# While large language models (LLMs) have demonstrated impressive performance across
# ...
# only one or two in-context examples.
# """