"""
元素：     11   22  33  44  55  66  77  88  99
正数索引：  0    1   2   3   4   5   6   7   8     0~8
负数索引： -9   -8  -7  -6   -5  -4  -3  -2  -1    -9~-1

索引的取值范围：
    正数索引：0~len(x) - 1
    负数索引：-len(x) ~ -1
"""

numlist = [11,22,33,44,55,66,77,88,99]
# len(x):获取列表中元素的个数  或者 获取列表的长度
print(len(numlist))

# 1.获取元素
# 语法：列表[索引]
print(numlist[0])
print(numlist[-9])

print(numlist[4])
print(numlist[-5])

print(numlist[8])
print(numlist[-1])

# 问题：索引一定不能越界, IndexError: list index out of range
# print(numlist[9])
# print(numlist[-10])

# 2.修改元素
# 语法：列表[索引] = 值
print(numlist)
numlist[3] = 'abc'
print(numlist)

numlist[-1] = 100
print(numlist)