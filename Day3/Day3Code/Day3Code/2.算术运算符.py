m = 8
n = 3

# 1. + -
print(m + n)
print(m - n)

print(8.0 + 3)
print(8 + 3.0)
print(8.0 - 3.0)

# 2.*  /
print(m * n)
print(m / n)

# 只要是/运算，结果都是浮点数
print(10 / 5)   # 2.0

print(8.0 * 3)
print(8 * 3.0)
print(8.0 * 3.0)

# 3.//:整除或取整
print(m // n)   # 2

print(5.0 / 2)
print(5.0 // 2)   # 2.0

# 4.%:求余或取模
print(m % n)   # 8整除3之后的余数

print(13 // 3)
print(13 % 3)
print(13.0 % 3)

# 5.**：求幂或求次方
print(m ** n)
print(5.0 ** 3)
# 扩展：m ** n 等价于pow(m,n)
print(pow(m,n))

# 6.优先级
# 算术运算符的优先级：**  >  *和/ // %  >  +和-
print(2 + 4 * 5)  # 22
print(2 * 5 ** 3)  # 250

print((2 * 5) ** 3)  # 1000