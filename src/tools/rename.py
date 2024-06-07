import os
import zipfile

# 指定zip文件路径
# zip_path = 'MR1047.zip'
# zip_path = '*.zip'
# 指定解压后文件存放的目录
extract_path = 'output'


# 要添加到文件名前的固定值
# prefix = 'PW_0_'


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


# 找到最深层次的 加前缀命名
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


# 对解压目录中的文件进行重命名
# rename_files_in_folder(extract_path, prefix)
# rename_deepest_files(extract_path, "")


def remove_underscores(s):
    # 找到所有下划线的位置
    underscores = [i for i, c in enumerate(s) if c == '_']

    # 检查是否有足够的下划线
    if len(underscores) < 4:
        return s  # 如果下划线数量不足，直接返回原始字符串
    # 找到倒数第二个和倒数第四个下划线的位置
    second_last_underscore = underscores[-2]
    fourth_last_underscore = underscores[-4]
    return s[:fourth_last_underscore] + s[second_last_underscore:]


def rename_underscores_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory, topdown=False):
        if files:  # 确保当前目录不是空的
            # 由于os.walk默认按目录深度排序，topdown=False将从最深层的目录开始遍历
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):  # 确保是一个文件
                    count += 1
                    # new_file_path = os.path.join(root, file)
                    new_file_path_removed = remove_underscores(file_path)
                    if os.path.exists(new_file_path_removed):
                        os.remove(new_file_path_removed)
                    os.rename(file_path, new_file_path_removed)
                    print(f'Renamed "{file_path}" to "{new_file_path_removed}"')
    print(f'一共处理了"{count}"个文件')


def rename_prefix_files(directory, prefix):
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
                    os.rename(file_path, new_file_path)
                    print(f'Renamed "{file_path}" to "{new_file_path}"')
    print(f'一共处理了"{count}"个文件')


# rename_underscores_files(extract_path)
rename_prefix_files(extract_path, "PW-0-")
print('文件重命名完成。')
