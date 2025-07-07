# 定义类
class Person():
    # 类属性
    num = 10
    # 限制对象属性的动态绑定
    __slots__ = ('name','age','hobby')
    # 定义实例属性
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    # 类中的函数
    # 实例函数
    def func1(self,a,b):
        print('1111',a,b)
    # 类函数
    @classmethod
    def func2(cls,a):
        print('22222',a)
    # 静态函数
    @staticmethod
    def func3(num1,num2):
        print('333333',num1,num2)

# 创建对象/实例化对象/类的实例化
p = Person('aaa',10,'dance')
# 访问属性
print(Person.num)
print(p.num)
print(p.name,p.age,p.hobby)
# 调用函数
p.func1(5,8)

Person.func2(34)
p.func2(34)

Person.func3(45,7)
p.func3(45,8)
