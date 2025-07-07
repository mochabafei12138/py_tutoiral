# 封装的本质：将类中的属性进行私有化
'''
公开属性：可以在当前类之外的任何地方直接访问的属性
私有属性：只能在当前类中被直接访问的属性
'''

# 1.属性未被私有化
class Animal1():
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

a1 = Animal1('大黄',3)
print(a1.name,a1.age)
a1.show()

a1.name = '小白'

print('*' * 30)

# 2.属性私有化     ******
# 作用：为了数据的安全性，不希望当前类以外的其他地方访问该属性
class Animal2():
    __slots__ = ('__name','__age')
    def __init__(self,name,age):
        # 当给对象动态绑定属性的时候，如果在属性名的前面添加两个下划线，则表示该属性被私有化了
        self.__name = name
        self.__age = age
    def show(self):
        print(self.__name,self.__age)

a2 = Animal2('大黄',3)
a2.show()
# print(a2.__name,a2.__age)  # AttributeError: 'Animal2' object has no attribute '__name'

print('*' * 30)

# 3.暴露给外界访问的函数
# a.
class Animal3():
    __slots__ = ('__name','__age')
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def show(self):
        print(self.__name,self.__age)

    # 获取值
    def func1(self):
        return self.__name
    # 修改值
    def func2(self,a):
        self.__name = a

    def func3(self):
        return self.__age
    def func4(self,b):
        if b < 0:
            b = -b
        self.__age = b

a3 = Animal3('大黄',3)
a3.show()
print(a3.func1())
a3.func2('旺财')
print(a3.func1())

print(a3.func3())
a3.func4(-45)
print(a3.func3())

print('*' * 30)

# b.装饰器实现
class Animal3():
    __slots__ = ('__name','__age')
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def show(self):
        print(self.__name,self.__age)

    # 获取值
    '''
    @property用来装饰获取私有化属性的函数，将该函数处理成属性使用
    '''
    @property
    def name(self):
        return self.__name
    # 修改值
    '''
     @xxx.setter用来装饰修改私有化属性的函数，将该函数处理成属性使用
     xxx:一定得是被@property装饰的函数名
     
     一般情况下，func1和func2这两处的函数名不会随意命名，建议命名为被私有化的属性的属性名
    '''
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age < 0:
            age = -age
        self.age  = age

a3 = Animal3('大黄',3)
a3.show()
print(a3.name)  # 大黄，调用的是被@property装饰的函数，a3.func1获取的是原func1函数的返回值
# print(a3.func1())   # TypeError: 'str' object is not callable

# print(a3.func2)
a3.name = '旺财'   # 调用的是被@xxx.setter装饰的函数
# a3.func2('旺财')     # TypeError: 'str' object is not callable
print(a3.name)
