# 1.pass
# pass:通过，也是一个关键字，没有实际意义，但是可以用来完善程序的结构，常用于代码块中
# 说明：Python中所有的代码块想要结构完整，则必须至少书写一条语句，或者用pass暂时占位
# 注意：一般用于if  while for 函数 类 等代码块中都可以使用pass暂时占位
if 1:
    pass
else:
    print('no')

for n in range(10):
    pass
print('over')


# 注意：break和continue使用的前提是循环语句
# 2.break
# a.
'''
注意：
    a.break单独作为一条语句使用
    b.如果break应用在单层循环【while和for】中，在满足条件的情况下，表示结束循环，哪怕该循环还有无数次没有执行
    c.如果break应用在内层循环中，在满足条件的情况下，结束的是当前循环【就近原则】
'''
n = 0
while n < 10:
    print(n)
    if n == 3:   # 充当条件
        break
    n += 1

print('*' * 50)

# b.
n = 0
while n < 5:
    m = 0
    while m < 3:
        print(n,m)
        if n == 3:
            break
        m += 1
    n += 1

print('*' * 50)

n = 0
while n < 5:
    m = 0
    while m < 3:
        print(n, m)
        if m == 1:
            break
        m += 1
    n += 1

print('*' * 50)

# 3.continue
# 死循环
# n = 0
# while n < 10:
#     print(n)
#     if n == 3:
#         continue
#     n += 1
#     print('over~~~~~~')

# 使用场景：只有某次循环未被执行完，其他次循环正常执行
n = 0
while n < 10:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
    print('over~~~~~~')