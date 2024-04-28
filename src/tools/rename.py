import os
import zipfile

# 指定zip文件路径
# zip_path = 'MR1047.zip'
# zip_path = '*.zip'
# 指定解压后文件存放的目录
extract_path = 'output'

# 要添加到文件名前的固定值
prefix = 'PW_0_'


def rename_files_in_folder(folder_path, prefix):
    count = 0
    # 遍历指定文件夹中的所有项
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # 检查是否为文件，如果是文件则重命名
        if os.path.isfile(item_path):
            base, ext = os.path.splitext(item)
            new_filename = f"{prefix}{base}{ext}"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(item_path, new_file_path)
            count += count
            print(f'Renamed "{item}" to "{new_file_path}"')
        # 如果是文件夹，则递归调用该函数
        elif os.path.isdir(item_path):
            rename_files_in_folder(item_path, prefix)
    print(f'一共处理了"{count}"个文件')


def remove_last_char(filename, symbol):
    # 找到最后一个“-”的位置
    dash_index = filename.rfind(symbol)
    # 如果找到了“-”，则去除最后一个“-”
    if dash_index != -1:
        # 使用字符串切片去除最后一个“-”
        new_filename = filename[:dash_index] + filename[dash_index + 1:]
    else:
        # 如果没有找到“-”，则保持原样
        new_filename = filename
        print(f'存在没有"{symbol}"的数据')
    print(f'delete last-"{filename}" to "{new_filename}"')
    return new_filename


# 找到最深层次的
def rename_deepest_files(directory, prefix):
    count = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        if files:  # 确保当前目录不是空的
            # 由于os.walk默认按目录深度排序，topdown=False将从最深层的目录开始遍历
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):  # 确保是一个文件
                    count += 1
                    new_filename = f"{prefix}{file}"
                    new_file_path = os.path.join(root, new_filename)
                    if os.path.basename(root) == "资源图":
                        new_file_path = remove_last_char(new_file_path, 'H')
                    new_file_path_removed = remove_last_char(new_file_path, '-')
                    os.rename(file_path, new_file_path_removed)
                    print(f'Renamed "{file_path}" to "{new_file_path}" and to "{new_file_path_removed}"')
    print(f'一共处理了"{count}"个文件')


# 解压zip文件,支持中文
# with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#     for file_info in zip_ref.infolist():
#         #解决中文文件名乱码问题
#         file_info.filename = file_info.filename.encode('cp437').decode('gbk')
#         zip_ref.extract(file_info, extract_path)


# 解压zip文件
# with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#     zip_ref.extractall(extract_path)

# 解压zip文件
# with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#     # 遍历zip文件中的所有文件
#     for file_info in zip_ref.infolist():
#         # 获取文件名，decode参数设置为'cp437'来解决乱码问题
#         file_name = file_info.filename.encode('cp437').decode('utf-8')
#
#         # 创建文件的完整路径
#         file_path = os.path.join(extract_path, file_name)
#
#         # 确保目标文件夹存在
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#         # 解压文件
#         with zip_ref.open(file_info) as source, open(file_path, 'wb') as target:
#             # 写入文件
#             target.write(source.read())
#
# print('文件解压完成，中文文件名已正确处理。')


# 对解压目录中的文件进行重命名
# rename_files_in_folder(extract_path, prefix)
rename_deepest_files(extract_path, prefix)

# # 遍历解压后的文件，进行重命名
# for item in os.listdir(extract_path):
#     item_path = os.path.join(extract_path, item)
#
#     # 检查是否为文件，跳过文件夹
#     if os.path.isfile(item_path):
#         # 构造新的文件名，给原始文件名添加前缀
#         new_filename = f"{prefix}{item}"
#         # 构造完整的新文件路径
#         new_file_path = os.path.join(extract_path, new_filename)
#         # 重命名文件
#         os.rename(item_path, new_file_path)
#         print(f'Renamed "{item}" to "{new_file_path}"')

print('文件重命名完成。')
