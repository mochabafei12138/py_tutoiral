# 1.自定义函数的重写
# class Animal():
#     def style(self):
#         print('walking')
# class Cat(Animal):
#     pass
# class Dog(Animal):
#     pass
# class Pig(Animal):
#     pass
# class Bird(Animal):
#     def style(self):
#         print('flying')
# class Fish(Animal):
#     def style(self):
#         print('swimming')

# 2.系统函数的重写
# a.
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'name:{self.name},age:{self.age}')

p = Person('小明',10)
# 注意1：当输出对象时，默认会调用魔术函数__str__,__str__是object中的函数，该函数默认返回当前对象在计算机中的地址
print(p)    # <__main__.Person object at 0x0000026DE30C5FD0>
print(p.__str__())  # <__main__.Person object at 0x0000026DE30C5FD0>

# b
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'name:{self.name},age:{self.age}')

    # 注意2：当重写__str__时，返回值必须是一个字符串，表示一个对象的字符串描述信息，一般是和当前对象相关的属性信息
    def __str__(self):
        # TypeError: __str__ returned non-string (type NoneType)
        return f'name:{self.name},age:{self.age}'

p = Person('小明',10)
print(p)
print(p.__str__())

# c.
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'name:{self.name},age:{self.age}')

    # 方式一：只重写__repr__
    # def __repr__(self):
    #     return f'name:{self.name},age:{self.age}'
    # 方式二：
    def __str__(self):
        return f'name:{self.name},age:{self.age}'
    __repr__ = __str__

p = Person('小明',10)
print(p)  # 输出对象的时候，调用子类中重写之后的__str__
print(p.__str__())
# 注意3：当将对象作为作为存储在列表等容器中时，输出列表，元素仍然以地址的形式呈现，则重写__repr__
lst = [p]
print(lst)   # 前：[<__main__.Person object at 0x000001A553037FD0>]  后：[name:小明,age:10]

# 3.注意4：当子类中重写了父类中的函数，创建子类对象调用函数，优先调用的是子类中的函数
# a.如果在子类的构造函数中需要用到父类中绑定的属性，则可以在子类的构造函数中调用父类中的构造函数
class A():
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
b = B(23,4)

# b.当在子类重写之后的函数中需要用到父类中对应函数中的功能，则可以在子类函数中调用父类中的函数
class Animal():
    def style(self):
        print('walking')
class Bird(Animal):
    def style(self):
        # super(Bird,self).style()
        # super().style()
        Animal.style(self)
        print('flying')
bird = Bird()
bird.style()
