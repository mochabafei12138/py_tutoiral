'''
注意：
    a.创建包：选中工程-----》右键----》new --->Python Package,特点：其中会自动包含一个__init__.py文件
    b.使用的过程中，包和普通文件夹的使用区别不大
    c.点模块名称：本质上指的是路径，此时的路径也就是被当作模块的py文件的路径，包括包或文件夹，其中的点表示的是路径的层级关系
    d.常说的模块本质上指的就是一个py文件
'''
# 导入系统模块
import random     # random.py
import math       # math.py

# 导入自定义模块,注意：一般情况下，导入模块的时候，实际包的概念已经包含在内了
# import a1         # a1.py   报错：ModuleNotFoundError: No module named 'a1'
import aaa.a1       # aaa/a1.py,aaa和当前py文件是平级
import bbb.bb.b1    # bbb/bb/b1.py

import aaa.module
import bbb.module