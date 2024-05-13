def remove_underscores(s):
    # 找到所有下划线的位置
    underscores = [i for i, c in enumerate(s) if c == '_']
    print(underscores)
    print(underscores[-2])
    print(underscores[-4])

    # 检查是否有足够的下划线
    if len(underscores) < 4:
        return s  # 如果下划线数量不足，直接返回原始字符串

    # 找到倒数第二个和倒数第四个下划线的位置
    second_last_underscore = underscores[-2]
    fourth_last_underscore = underscores[-4]

    # 清除倒数第二个下划线和倒数第四个下划线之间的部分
    print(s[second_last_underscore:])
    print(s[:fourth_last_underscore])
    return s[:fourth_last_underscore] + s[second_last_underscore:]


# 示例字符串
s = "CTF_AB39585_BD_A_TY_800_V1_900_V2"
# 调用函数并打印结果
print(remove_underscores(s))