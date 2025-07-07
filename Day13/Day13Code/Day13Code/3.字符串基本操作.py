# 1.字符串是有序的,所以可以通过索引访问其中的字符
str1 = 'abcdef'
print(str1[0])
print(str1[-1])
# print(str1[7])  # IndexError: string index out of range

print(str1[1:3])
print(str1[::-1])  # 将字符串进行反转/逆序

# 2.字符串的遍历
# 标识符：见名知意，使用简单英文单词或者缩写表示
# ch--->character:字符
for ch in str1:
    print(ch)

for i in range(len(str1)):
    print(str1[i])

for i,ch in enumerate(str1):
    print(i,ch)

# 3.转化
print(list(str1))
print(tuple(str1))

list1 = [34,6,7,8]
print(str(list1))  # 等价于'[34, 6, 7, 8]',但是没有意义

# 4.+   *
print(str1 + 'fagnaqg')   # 拼接
print(str1 * 3)
print('*' * 50)

# print(str1 + 3)  # TypeError: can only concatenate str (not "int") to str
# print(3 + str1)   # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 5.in 和 not in:用在字符串中，表示模糊查询，==表示精确查询
print('a' in str1)
print('b' not in str1)

# 6.特点：字符串是不可变的数据类型，和元组类似