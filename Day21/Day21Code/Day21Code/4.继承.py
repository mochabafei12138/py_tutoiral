
# 1.单继承
# 在Python中，object是所有类的根类
# 父类
class Person():  # 在此处的()中什么都不写，默认的父类仍然是object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print('showing')

# 子类
class Worker(Person):
    pass
# a.当子类中未定义__init__，则创建子类对象，默认会调用父类中的构造函数，所以要注意和父类中的__init__的参数匹配【子类继承了父类中的__init__】
# w = Worker()  # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
w = Worker('小王',20)
print(w.name,w.age)
w.show()

class Student(Person):
    def study(self):
        print('study~~~~')
stu = Student('小明',19)
print(stu.name,stu.age)
stu.show()
stu.study()

# b.如果子类中定义了__init__函数，则创建子类对象，优先会调用子类中的__init__
class Doctor(Person):
    def __init__(self,name,age,kind):
        # 在子类的__init__中调用父类的__init__
        # 方式一：super(当前类，self).__init__(参数列表)
        # super(Doctor,self).__init__(name,age)
        # 方式二：super().__init__(参数列表)
        # super().__init__(name,age)
        # 方式三：父类类名.__init__(self,参数列表)
        Person.__init__(self,name,age)

        self.kind = kind
    def assist(self):
        print('assist~~~~')

# d = Doctor() # TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'kind'
d = Doctor('王大夫',45,'外科')
print(d.kind)
# 当子类对象需要访问父类中提取出来的属性时，无法访问，解决方案：在子类的__init__中调用父类中的__init__
print(d.name,d.age)  # AttributeError: 'Doctor' object has no attribute 'name'
d.show()
d.assist()

# 2.多继承
# a
class Flyable():
    def fly(self):
        print('flying')
class Runable():
    def run(self):
        print('running')
class Bird(Flyable,Runable):
    pass

bird = Bird()
bird.fly()
bird.run()

# b.
# class FatherClass1():
#     def __init__(self,num):
#         self.num = num
#     def func(self):
#         print('11111')
#
# class FatherClass2():
#     def __init__(self,value):
#         self.value = value
#     def func(self):
#         print('2222')
#
# class SubClass(FatherClass1,FatherClass2):
#     pass

# 当一个类有多个父类，且子类中未定义构造函数，则创建子类对象，默认情况下调用的时父类列表中第一个父类中的__init__,多个父类中出现重名的函数也是这种原理
# sc = SubClass(45)
# sc.func()

# c
class FatherClass1():
    def __init__(self,num):
        self.num = num
    def func(self):
        print('11111')

class FatherClass2():
    def __init__(self,value):
        self.value = value
    def func(self):
        print('2222')

class SubClass(FatherClass1,FatherClass2):
    def __init__(self,num,value,a,b):
        # 在多继承中，在子类的__init__中调用父类的__init__,只能使用方式三，可以区分父类
        FatherClass1.__init__(self, num)
        FatherClass2.__init__(self, value)
        self.a = a
        self.b = b

sc = SubClass(34,6,7,8)
print(sc.a,sc.b)
print(sc.num,sc.value)