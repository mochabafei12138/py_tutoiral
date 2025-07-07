# 扩展
# 导入模块和使用模块功能的语法
# 方式一
# import  random
# r = random.randint(1,100)
# r = random.choice(range(100))

# 方式二
# from random import *      # *表示所有
# r = randint(1,100)
# r = choice(range(100))


from random import  *
# 1.randint(a,b)：步长固定为1，无法自定义，是一个闭区间
r1 = randint(1,100)
print(r1)
r11 = randint(1,100)

# 2.choice(seq):seq:序列,常用列表，元组或字符串
# seq:序列，Python中的列表，字符串，元组等有序的数据类型都可以表示序列
r21 = choice([34,7,8,9])
print(r21)
r22 = choice((34,7,8,9))
print(r22)
r23 = choice('abcd')
print(r23)
r24 = choice(range(1,101))
print(r24)
r24 = choice(range(1,101,2))
print(r24)

# 3.randrange(start,stop,step):step默认为1，可以自定义，是前闭后开区间
r31 = randrange(1,100)
print(r31)
r32 = randrange(1,100,2)
print(r32)

# 练习：
# a.获取20~80之间的一个整数随机数
print(randint(20,80))
print(choice(range(20,81)))
print(randrange(20,81))
# b.获取20~80之间的一个偶数随机数
print(choice(range(20,81,2)))
print(randrange(20,81,2))

# 4.sample(seq,k):从seq中随机获取k个数据，得到一个列表   *******
r41 = sample([34,1,67,89,900,23,6,7,8],2)
print(r41)
r41 = sample((34,1,67,89,900,23,6,7,8),2)
print(r41)
r41 = sample('1234567890',5)
print(r41)
r41 = sample(range(100),4)
print(r41)

# 5.random()：获取0~1之间的随机浮点数，前闭后开区间
r51 = random()
print(r51)

# 6.uniform(a,b):获取a~b之间的随机浮点数
r61 = uniform(1,100)
'''
工作原理：
    def uniform(self, a, b):
        "Get a random number in the range [a, b) or [a, b] depending on rounding."
        return a + (b - a) * self.random()
'''

# 练习
# 获取20~100之间的浮点数随机数
r1 = uniform(20,100)
print(r1)
# [0,1)---->[0,80)--->[20,100)
r2 = random() * 80 + 20
print(r2)