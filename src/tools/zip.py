import zipfile
import os
def compress_folder(folder_path, zip_name):
    # 创建一个压缩文件对象
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历文件夹
        for root, dirs, files in os.walk(folder_path):
            # 将文件夹添加到压缩文件中
            for file in files:
                file_path = os.path.join(root, file)
                # 将文件添加到压缩文件中
                zipf.write(file_path)

# 使用示例
folder_to_compress = 'output'
zip_file_name = 'output.zip.z'
compress_folder(folder_to_compress, zip_file_name)