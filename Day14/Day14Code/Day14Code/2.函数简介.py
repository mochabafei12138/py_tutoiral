# 需求：求一个圆的面积

# 1.
r1 = 30
area1 = 3.14 * r1 ** 2
print(area1)

r2 = 5
area2 = 3.14 * r2 ** 2
print(area2)

r3 = 25
area3 = 3.14 * r3 ** 2
print(area3)

# 2.优化
# 函数的本质：对某些功能的封装，形成了一个工具，该工具可以反复被使用
def area(r):
    return 3.14 * r ** 2
print(area(30))
print(area(5))
print(area(25))

# 列表的系统功能【append/remove/reverse.....】、字符串的系统功能【replace/find/center.....】