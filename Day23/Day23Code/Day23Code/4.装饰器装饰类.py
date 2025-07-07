# 1.装饰器装饰函数
def wrapper(func):  # func表示需要被装饰的函数
    def inner():
        func()      # 调用被装饰的函数【原函数】
        print('new~~~')  # 新增的功能
    return inner

@wrapper            # 调用外部函数wrapper
def a():
    print('aaaaa')
print(a)   # <function wrapper.<locals>.inner at 0x000001DF7EDCC430>
a()      # 调用inner

print('*' * 50)

# 2.装饰器装饰类
def wrapper(cls):  # cls表示需要被装饰的类
    def inner(*args,**kwargs):
        c = cls(*args,**kwargs)      # 类(),创建对象：调用类中的构造函数__new__,__init__,所以此处的参数需要和__init__中的参数保持一致
        print('new~~~')  # 新增的功能
        return c
    return inner

@wrapper            # 调用外部函数wrapper
class A():
    def __init__(self,name,age):
        self.name = name
        self.age = age
print(A)   # <function wrapper.<locals>.inner at 0x000001DF7EDCC430>
a1 = A('111',10)        # 调用inner,a1中存储的是inner的返回值，为了符合最初创建对象的语法，则给inner设置返回值
print(a1)

a2 = A('222',20)
print(a2)

print(a1 is a2)  # False
