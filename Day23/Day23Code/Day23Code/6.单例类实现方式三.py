def singleton(cls):
    # 定义一个函数作用域的字典变量，key:被装饰的类，value:唯一的对象
    instance = {}
    def get_instance(*args,**kwargs):
        if not instance:
            # 向字典中添加键值对
            instance[cls] = cls(*args, **kwargs)  # 调用__init__
        return instance[cls]
    return get_instance

@singleton
class Person():
    def __init__(self,name,age):
        print('init~~~~~',name,age)
        self.name = name
        self.age = age

p1 = Person('张三',10)   # 调用get_instance
p2 = Person('李四',20)   # 调用get_instance
print(p1 is p2)  # True
print(id(p1) == id(p2))  # True

print(p1.name,p2.name)   # 张三

p1.name = 'Jack'
print(p1.name,p2.name)