import os
import zipfile
import shutil


# 需要提取的压缩包文件路径
# zip_filename = 'MR1047.zip'
# target = 'output1'


def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            # 解决中文文件名乱码问题
            # file_info.filename = file_info.filename.encode('cp437').decode('gbk')
            file_info.filename = file_info.filename.encode('utf-8').decode('utf-8')
            zip_ref.extract(file_info, extract_path)
    print(f"Extracted: {zip_path}")


def unzip_all_in_directory(directory):
    # 遍历directory下的所有文件和目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否为.zip
            if file.lower().endswith('.zip'):
                zip_path = os.path.join(root, file)
                # 定义解压路径为zip文件所在的目录
                extract_path = root + '/output'
                unzip_file(zip_path, extract_path)


unzip_all_in_directory(".")
