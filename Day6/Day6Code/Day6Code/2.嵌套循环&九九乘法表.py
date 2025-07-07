# 1.基本语法
# a
n = 0
while n < 5:
    print(n)
    n += 1
m = 0
while m < 3:
    print(m)
    m += 1

print('*' * 30)

# b
# 注意：在代码执行的过程中，但凡遇到循环语句，都是先把当前循环执行完毕，然后代码才会向下执行
n = 0
while n < 5:
    m = 0        # 外层循环每次执行进来，m都会被重置为0
    while m < 3:
        print(n,m)
        m += 1
    n += 1
# 15

print('*' * 30)

for n in range(5):
    for m in range(3):
        print(n,m)

print('*' * 30)

# 思考：m = 0定义在外层循环的外面，将不会再被重置
n = 0
m = 0
while n < 5:
    while m < 3:
        print(n,m)
        m += 1
    n += 1

# 2.打印九九乘法表
# 应用：打印九九乘法表
"""
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
1*4=4 2*4=8 3*4=12 4*4=16
......

1*9=9 2*9=18 3*9=27  ......     7*9=63 8*9=72 9*9=81

规律：
    a.行数的取值范围：1~9
    b.每一行中列数的取值范围：1~当前行数
    c.格式：列*行=乘积
"""
# 外层循环：控制行数
row = 1
while row <= 9:
    # 内层循环：控制每一行的列
    col = 1
    while col <= row:
        print(f'{col}*{row}={col * row}',end=' ')
        col += 1
    row += 1
    # 换行
    print()

for row in range(1,10):
    for col in range(1,row + 1):
        print(f'{col}*{row}={col * row}', end=' ')
    # 换行
    print()










