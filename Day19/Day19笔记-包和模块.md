### 一、包和模块

#### 1.包

> 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"
>
> 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况
>
> ```
> Python package本质是一个文件夹【目录】，但是特殊之处在于在该目录下有一个文件，名为__init__.py，代表初始化，前期其中不写任何内容，后期会在其中书写项目的配置信息
> ```
>

> ```Python
> '''
> 注意：
>     a.创建包：选中工程-----》右键----》new --->Python Package,特点：其中会自动包含一个__init__.py文件
>     b.使用的过程中，包和普通文件夹的使用区别不大
>     c.点模块名称：本质上指的是路径，此时的路径也就是被当作模块的py文件的路径，包括包或文件夹，其中的点表示的是路径的层级关系
>     d.常说的模块本质上指的就是一个py文件
> '''
> # 导入系统模块
> import random     # random.py
> import math       # math.py
> 
> # 导入自定义模块,注意：一般情况下，导入模块的时候，实际包的概念已经包含在内了
> # import a1         # a1.py   报错：ModuleNotFoundError: No module named 'a1'
> import aaa.a1       # aaa/a1.py,aaa和当前py文件是平级
> import bbb.bb.b1    # bbb/bb/b1.py
> 
> import aaa.module
> import bbb.module
> ```

#### 2.自定义模块【重点掌握】

> 目前代码比较少，写在一个文件中还体现不出什么缺点，但是随着代码量越来越多，代码就越来越难以维护。
>
> ​	为了解决难以维护的问题，我们把很多相似功能的函数进行分组，分别放到不同的文件中。这样每个文件所包含的内容相对较少，而且对于每一个文件的大致功能可用文件名来体现。很多编程语言都是这么来组织代码结构。
>
> 注意：其实一个.py文件就是一个模块
>
> 优点：
>
> - 提高代码的可维护性
> - 提高了代码的复用度，当一个模块书写完毕，可以被多个地方引用
> - 引用其他的模块
> - 避免函数名和变量名的冲突

##### 2.1使用一

> ```Python
> # 一、import xxxx
> # import:导入，实际是把指定模块中的函数，变量或类进行加载
> 
> # 1.import  模块名
> # a.导入系统模块
> # 写法一
> # import  random
> # import math
> # import string
> 
> # 写法二
> import  random,math,string
> 
> r1 = random.randint(1,10)   # random是模块名，randint是函数名
> r2 = math.sqrt(9)   # math是模块名，sqrt是函数名
> 
> # b.导入自定义模块
> import aaa.a1
> # import bbb.bb.b1
> 
> # 注意：不同模块中出现了重名的变量，函数或者类，没关系，因为通过import xxx访问的路径不同
> # print(aaa.a1.name)
> # print(bbb.bb.b1.name)
> # aaa.a1.func()
> # bbb.bb.b1.func()
> 
> '''
> 记住：只要观察当前py文件和要被导入的py文件之间的关系
> 假设：
>     当前py文件：a.py
>     要被导入的py文件:b.py
> 
> 情况一：a.py 和 b.py的上级目录平级，导入格式：import xxx.....xx.b
> 情况二：a.py 和 b.py直接平级，导入格式：import b
> '''
> import d1
> 
> # 调用b1.py模块中的所有函数
> # bbb.bb.b1.func()
> # bbb.bb.b1.func1()
> # bbb.bb.b1.func2()
> # bbb.bb.b1.func3()
> 
> # 2.import  模块名 as  别名
> # 常用于给模块起别名，方便调用，特别是自定义模块中，路径层级关系比较复杂的情况下
> import bbb.bb.b1 as b
> print(b.name)
> b.func()
> b.func1()
> b.func2()
> b.func3()
> 
> # 数据分析三剑客一般都是会用as起别名
> import pandas as pd
> import numpy as np
> import matplotlib.pyplot as plt
> 
> # 注意：模块名一定要遵循标识符的规则和规范，不能数字开头，不能出现中文，不能使用_之外的特殊符号，不能使用关键字
> # import 4.time模块  # 错误写法
> ```

##### 2.2使用二 

> ```Python
> # 二、from xxxx import xxx
> # 1.from 模块名 import  变量名/函数名/类名
> # a.可以根据具体的需求导入需要的内容
> from aaa.a1 import name,func
> # 如果需要导入的变量，函数或者类有多个，用逗号隔开
> from bbb.bb.b1 import name,func,func1,func2
> from random import choice,randint,sample
> 
> 
> # 好处：通过from xxx import xxx的方式导入，访问变量或调用函数的时候，可以直接书写变量名或函数名
> r1 = randint(1,10)
> print(r1)
> func1()
> 
> # 问题一：没有导入的变量或函数无法访问
> # randrange()
> # func()
> 
> # 问题二：当不同模块中出现了重名的变量或者函数，此时相互之间会影响,只能访问到后导入的内容
> print(name)
> func()
> 
> # b.from xxx import * :从xxx模块中导入所有
> from math import  *
> from bbb.bb.b1 import  *
> 
> print(sqrt(9))
> print(floor(34.5))
> 
> 
> # 注意：自定义的py文件，文件名称一定不要和系统的模块重名，会导致系统的模块失效
> '''
> from random import choice,randint,sample
> ImportError: cannot import name 'choice' from 'random' (D:\Desktop\coding\Code\Day19Code\random.py)
> '''
> ```

#### 3.系统模块

##### 3.1time模块

> ```
> Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
> Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
> 时间间隔是以秒为单位的浮点小数。
> 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
> Python 的 time 模块下有很多函数可以转换常见日期格式
> ```
>
> 1>名词解释
>
> UTC，格林威治天文时间，世界标准时间，在中国为UTC+8
>
> DST：夏令时,表示时间的显示格式
>
> 2>时间的表示形式【掌握】
>
> 还需要掌握三种表示方式之间的相互转换
>
> a.时间戳
>
> ​	以浮点型表示的是一个以秒为单位的时间间隔，这个时间的基础值是1970.1.1的零点开始算起
>
>
> b.时间元组格式
>
> ​	采用Python的数据结构表示，这个元组有9个整型内容，分别表示不同的含义	
>
> ![元组格式](Day19-images/元组格式.png)
>
> c.格式化的时间字符串
>
> %Y:年
>
> %m:月份
>
> %d:天
>
> %H:时
>
> %M:分钟
>
> %S；秒
>
> ![格式化时间字符串](Day19-images/格式化时间字符串.png)

> ```Python
> # import time
> from time import  *
> 
> # 1.time():获取当前时间的时间戳   ******
> t1 = time()
> print(t1)
> 
> # 2.gmtime():获取UTC时间的元组形式
> t2 = gmtime()
> print(t2)
> 
> # 获取北京时间的元组形式
> t3 = localtime()
> print(t3)
> 
> # 3.strftime():将时间的元组形式转化为格式化字符串，格式可以自定义   ******
> t4 = strftime('%Y/%m/%d %H:%M:%S',t3)
> print(t4)
> t4 = strftime('%Y.%m.%d %H:%M:%S',t3)
> print(t4)
> t4 = strftime('%Y-%m-%d %H:%M:%S',t3)
> print(t4)
> 
> # 4.strptime():将时间的格式化字符串转化为时间的元组形式   *****
> # 注意：解析时间的字符串时，给定的format一定要和原字符串匹配，否则ValueError: time data '2024-02-29 21:02:54' does not match format '%Y.%m.%d %H:%M:%S'
> time_str = '2024-02-29 21:02:54'
> t5 = strptime(time_str,'%Y-%m-%d %H:%M:%S')
> print(t5)
> ```

##### 3.2.datetime模块

> ```Python
> import datetime
> from datetime import *
> 
> # 1.now():获取当前时间   *****
> d1 = datetime.now()    # datetime.datetime.now()
> print(d1)  # 2024-02-29 21:11:38.595202
> 
> # 2.datetime之间可以进行减法运算   *****
> d2 = datetime(2025,4,3,10,10,10,100)
> d3 = datetime(2025,4,4,10,45,10,100)
> d11 = d3 - d2
> print(d11)
> print(d11.days)
> print(d11.seconds)
> ```

##### 3.3os模块

> ```Python
> import  os
> 
> # 1.listdir():列出指定路径下所有的内容,返回一个列表，其中的元素是给定路径下所有文件及文件夹的名称
> '''
> 绝对路径：带有盘符的路径
> 相对路径：当前工程下，相当于当前py文件，没有盘符的路径，建议使用
> '''
> path = r'd:\Desktop\coding'
> r1 = os.listdir(path)
> print(r1)
> 
> # 2.join(父路径，子路径):拼接路径
> # d:\Desktop\coding\Day10
> base_path = r'd:\Desktop\coding'
> for name in r1:
>     sub_path = os.path.join(base_path,name)  # 会自动识别当前的操作系统，从而确定路径中使用/还是\
>     print(sub_path)
> 
> # 3.mkdir():创建文件夹
> # os.mkdir(r'ddd')
> 
> # 4.exists()；判断路径是否存在
> print(os.path.exists(r'd:\Desktop\coding\D34ay1'))
> print(os.path.exists(r'aaa'))
> 
> # 5.isfile():判断路径是否是文件
> # isdir():判断路径是否是文件夹
> print(os.path.isfile(r'd:\Desktop\coding\Day1'))
> print(os.path.isdir(r'd:\Desktop\coding\Day1'))
> ```

