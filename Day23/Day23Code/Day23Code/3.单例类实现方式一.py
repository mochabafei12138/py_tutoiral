# 1.普通类
class Person():
    pass
p1 = Person()
p2 = Person()
print(p1 is p2)  # False
print(id(p1) == id(p2))  # Flase

print('*' * 50)

# 2.单例类
'''
__new__
__init__
'''
class Person():
    # 定义一个类属性，用于表示当前类可以创建的唯一的对象
    # 因为此类属性无需在类的外面被访问修改，则设置为私有属性
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('new~~~')
        # 只要super().__new__(cls)被执行一次，则会创建出一个新的对象
        # 判断__instance的值，如果为None，则重新赋值为对象并返回，如果非空则直接返回
        if not cls.__instance:
            print('if~~~~')
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,name,age):
        print('init~~~~',name,age)
        self.name = name
        self.age = age
p1 = Person('张三',10)  # 创建对象
p2 = Person('李四',20)   # 获取第一次创建的对象，此处的李四和20相当于给对象的name和age属性重新赋值
print(p1 is p2)  # True
print(id(p1) == id(p2))   # True

print(p1.name,p2.name)   # 李四

p1.name = 'Jack'
print(p1.name,p2.name)