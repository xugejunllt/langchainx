filename = "example-image--_2021.jpg"

# 找到最后一个“-”的位置
dash_index = filename.rfind('-')

# 如果找到了“-”，则去除最后一个“-”
if dash_index != -1:
    # 使用字符串切片去除最后一个“-”
    new_filename = filename[:dash_index] + filename[dash_index+1:]
else:
    # 如果没有找到“-”，则保持原样
    new_filename = filename

print(new_filename)