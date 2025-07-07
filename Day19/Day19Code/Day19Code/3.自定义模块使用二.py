# 二、from xxxx import xxx
# 1.from 模块名 import  变量名/函数名/类名
# a.可以根据具体的需求导入需要的内容
from aaa.a1 import name,func
# 如果需要导入的变量，函数或者类有多个，用逗号隔开
from bbb.bb.b1 import name,func,func1,func2
from random import choice,randint,sample


# 好处：通过from xxx import xxx的方式导入，访问变量或调用函数的时候，可以直接书写变量名或函数名
r1 = randint(1,10)
print(r1)
func1()

# 问题一：没有导入的变量或函数无法访问
# randrange()
# func()

# 问题二：当不同模块中出现了重名的变量或者函数，此时相互之间会影响,只能访问到后导入的内容
print(name)
func()

# b.from xxx import * :从xxx模块中导入所有
from math import  *
from bbb.bb.b1 import  *

print(sqrt(9))
print(floor(34.5))


# 注意：自定义的py文件，文件名称一定不要和系统的模块重名，会导致系统的模块失效
'''
from random import choice,randint,sample
ImportError: cannot import name 'choice' from 'random' (D:\Desktop\coding\Code\Day19Code\random.py)
'''

