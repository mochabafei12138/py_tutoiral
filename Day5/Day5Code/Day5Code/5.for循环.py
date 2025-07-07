# 1.遍历容器
s = 'fagag'
for m in s:
    print(m)
    print(chr(ord(m) - 32))

lst = [34,5,67,8]
for n in lst:
    print(n + 10)

"""
总结：for循环的执行次数由：容器中数据的个数  或者  容器的长度  决定
"""

# 问题：输出10次hello world
# 2.注意1：如果for循环仅仅是为了控制次数，而定义的变量在循环体中未被使用，则可以使用下划线代替变量名
for n in '0987654123':
    print('hello wolrd')

for _ in '0987654123':
    print('hello wolrd')

# 注意2：range(start,end,step):根据指定的区间和指定的步长生成一个容器，前闭后开区间
for n in range(10):  # 0-9
    print('hello wolrd',n)

for n in range(100):  # 0-99
    print('hello wolrd',n)

for n in range(0,100,2):  # 0-99之间的偶数
    print('hello wolrd',n)

for n in range(1,100,2):  # 1-99之间的奇数
    print('hello wolrd',n)

# 3.注意区分while语句和for语句
n = 0    # start
while n < 10:   # end
    print(n)
    n += 1   # step

for n in range(0,10,1):
    print(n)
    # n += 1  # 初学者容易和while语句混淆