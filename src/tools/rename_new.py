import os
import zipfile
import platform

# 指定zip文件路径
zip_path = 'MR1047.zip'
# 指定解压后文件存放的目录
extract_path = 'output'

# 要添加到文件名前的固定值
prefix = 'PW_0_'

# 解压zip文件
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # 获取当前平台的默认编码，通常是utf-8
    zip_ref.extractall(extract_path)

def ensure_directory_structure(path):
    # ""“确保路径存在，如果不存在则创建”""
    if not os.path.exists(path):
        os.makedirs(path, encoding='utf-8')

def rename_files_in_folder(folder_path, prefix):
    # ""“递归遍历文件夹，重命名文件”""
    # 遍历文件夹中的所有文件和文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 构造完整的文件路径
            file_path = os.path.join(root, file)
            # 构造新的文件名，给原始文件名添加前缀
            new_filename = f"{prefix}{file}"
            # 构造完整的新文件路径
            new_file_path = os.path.join(root, new_filename)
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f'Renamed "{file_path}" to "{new_file_path}"')

# 对解压目录中的文件进行重命名
rename_files_in_folder(extract_path, prefix)

print('文件重命名完成。')