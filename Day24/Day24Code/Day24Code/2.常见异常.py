# 【面试题】请列举Python常见的异常，至少5种

# 1.NameError 使用一个还未被赋予对象的变量
# print(num)   # NameError: name 'num' is not defined

# 2.ValueError 传入一个调用者不期望的值，即使值的类型是正确的
# num = int(input('请输入一个数字：'))   # ValueError: invalid literal for int() with base 10: 'agAG'

# 3.TypeError 传入对象类型与要求的不符合
# print('faf' + 19)   # TypeError: can only concatenate str (not "int") to str
# print(19 + 'fagg')    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 4.AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
# print('abc'.reverse())   # AttributeError: 'str' object has no attribute 'reverse'
# class Person():
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# p = Person('小明',10)
# print(p.scope)

# 5.UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# a = 10
# def func():
#     a += 1    # UnboundLocalError: local variable 'a' referenced before assignment
# func()
# print(a)

# def func1():
#     num = 10
#     def func2():
#         print(num)  # UnboundLocalError: local variable 'num' referenced before assignment
#         num = 20
#     func2()
# func1()

# 6.MoudleNotFoundError:导入模块的时候，路径有误
# import  aaaa    # ModuleNotFoundError: No module named 'aaaa'

# 7.FileNotFoundError:文件路径不存在
# f = open(r'file.txt','r',encoding='utf-8')  # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'

# 8.KeyError 试图访问字典里不存在的键
# dic = {'a':10}
# print(dic['b'])   # KeyError: 'b'