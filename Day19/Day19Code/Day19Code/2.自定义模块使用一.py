# 一、import xxxx
# import:导入，实际是把指定模块中的函数，变量或类进行加载

# 1.import  模块名
# a.导入系统模块
# 写法一
# import  random
# import math
# import string

# 写法二
import  random,math,string

r1 = random.randint(1,10)   # random是模块名，randint是函数名
r2 = math.sqrt(9)   # math是模块名，sqrt是函数名

# b.导入自定义模块
import aaa.a1
# import bbb.bb.b1

# 注意：不同模块中出现了重名的变量，函数或者类，没关系，因为通过import xxx访问的路径不同
# print(aaa.a1.name)
# print(bbb.bb.b1.name)
# aaa.a1.func()
# bbb.bb.b1.func()

'''
记住：只要观察当前py文件和要被导入的py文件之间的关系
假设：
    当前py文件：a.py
    要被导入的py文件:b.py

情况一：a.py 和 b.py的上级目录平级，导入格式：import xxx.....xx.b
情况二：a.py 和 b.py直接平级，导入格式：import b
'''
import d1

# 调用b1.py模块中的所有函数
# bbb.bb.b1.func()
# bbb.bb.b1.func1()
# bbb.bb.b1.func2()
# bbb.bb.b1.func3()

# 2.import  模块名 as  别名
# 常用于给模块起别名，方便调用，特别是自定义模块中，路径层级关系比较复杂的情况下
import bbb.bb.b1 as b
print(b.name)
b.func()
b.func1()
b.func2()
b.func3()

# 数据分析三剑客一般都是会用as起别名
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 注意：模块名一定要遵循标识符的规则和规范，不能数字开头，不能出现中文，不能使用_之外的特殊符号，不能使用关键字
# import 4.time模块  # 错误写法