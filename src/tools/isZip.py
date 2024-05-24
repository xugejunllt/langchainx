

def is_zip(file_path):
    with open(file_path, 'rb') as f:
        return f.read(2) == b'PK'


# 使用示例
file_path = 'pdf_loader_demo.pdf'
if is_zip(file_path):
    print("The file is a ZIP file.")
else:
    print("The file is not a ZIP file.")
