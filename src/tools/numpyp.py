import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 使用布尔数组索引选择大于3的元素
mask = a > 3
t = type[mask]
print(type(a))
print(t)

result = a[mask]

print(mask)
print(result)
print(a[np.array([False, False, False, True, False])])


b = [1, 2, 3, 4, 5]
print(a == b)

c = np.array_split([1, 2, 3, 4, 5], 3)
print(f"split:{c}")

# arange & split
arr = np.arange(1, 13).reshape(3, 4)
print("原始数组：")
print(arr)
# 对数组按列进行拆分
sub_arrays = np.array_split(arr, 2, axis=1)
print("\n拆分后的子数组：")
for sub_arr in sub_arrays:
    print(sub_arr)


# reshape
d = np.array([[1, 2, 3],
              [4, 5, 6]])

# 将数组转换为2x3的形状
result_d = np.reshape(d, (2, 3))
print(f"reshap:{result_d}")
e = np.array([[1, 2, 3],
              [4, 5, 6]])

# 交换数组的维度
result_e = np.transpose(e)
print(f"transpose:{result_e}")


dot_a = np.array([[1, 2],
              [3, 4]])

dot_b = np.array([[5, 6],
              [7, 8]])

# 计算两个数组的矩阵乘法
result_dot = np.dot(dot_a, dot_b)

print(f"dot:{result_dot}")

# lexsort
# lexsort 函数使用键序列的最后一个键进行排序，然后使用倒数第二个键进行排序,以此类推，
# 直到使用第一个键进行排序。这样，最终得到的索引序列将使数组按照键序列逐级排序

lexsort_a = np.array([3, 1, 2])
lexsort_b = np.array([5, 4, 6])

# 根据a和b的值对数组进行排序
# indices = np.lexsort((lexsort_a, lexsort_b)) #1 0 2
indices = np.lexsort((lexsort_b, lexsort_a)) #1 2 0
print(f"indices:{indices}")

result_lexsort = lexsort_a[indices]
print(f"lexsort:{result_lexsort}")

# 创建一个包含姓名的字符串数组,
names = np.array(['Alice', 'Bob', 'Charlie', 'David'])

# 创建一个二维数组,分别代表上述学生的语文、数学、英语成绩
scores = np.array([[70, 85, 90],
                   [60, 75, 80],
                   [80, 90, 85],
                   [75, 80, 70]])

# 使用 lexsort 对数组进行排序、按
# sorted_indices = np.lexsort((scores[:, 1], scores[:, 2], scores[:, 0])) # 1 0 3 2
sorted_indices = np.lexsort((scores[:, 0], scores[:, 2], scores[:, 1])) # 1 3 0 2
print(f"sorted_indices:{sorted_indices}")

# 根据排序后的索引序列获取排序后的数组和姓名
sorted_scores = scores[sorted_indices]
sorted_names = names[sorted_indices]

print("Sorted Scores:")
print(sorted_scores)
print("\nSorted Names:")
print(sorted_names)
