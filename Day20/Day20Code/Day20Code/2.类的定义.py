# 1.类是一种数据类型
# a
num = 10  # 定义一个变量
print(type(num))  # <class 'int'>

# b.
v = ValueError() # 创建一个对象
print(type(v))   # <class 'ValueError'>

# 2.类的定义
# a.函数的定义
# def func():
#     print('ok~~~~~func')

# b.类的定义
class Check():
    # 一般不会在类中print
    print('ok~~~~class')
class MyClass1():
    pass
class MyClass2:
    pass

# 通过类创建对象，语法：变量 = 类名()
m1 = MyClass1()
print(m1)
m2 = MyClass2()
print(m2,id(m2))
m22 = MyClass2()
print(m22,id(m22))

'''
总结：
    a.类和函数相比，函数必须调用才能执行其中的代码，但是类只要定义完毕，其中的内容就会被加载一遍
    b.在同一个py文件中，可以定义多个类，但是，如果要实现的需求较为复杂，一般会结合模块使用，在一个模块中定义一个类
    c.定义类的过程中，类名后面的()可以省略
    d.创建对象：变量 = 类名()，此处的()不能省略
    e.同一个类，默认情况下，可以创建无数个对象，每个对象都会被分配不同的地址
    f.直接输出对象，默认的情况下，会得到一个地址
'''


