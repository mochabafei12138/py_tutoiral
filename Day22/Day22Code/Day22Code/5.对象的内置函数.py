# 1.id():获取一个对象的内存地址

# 2.type():获取一个对象的数据类型

# 3.isinstance():判断一个对象的数据类型是否是指定类型   ******
print(isinstance(45,str))
print(type(45) == str)

# 练习
lst = ['faf',24,6,False,34,True,'535',18]
l1 = [ele for ele in lst if isinstance(ele,int)]  # 涉及到继承，继承自int或int都会挑选
print(l1)  # [24, 6, False, 34, True, 18]
l2 = [ele for ele in lst if type(ele) == int]  # 精确匹配，只挑选int
print(l2)  # [24, 6, 34, 18]

# 4.issubclass(类1，类2)：判断类1和类2直接是否具有继承关系
class Animal():
    pass
class Cat(Animal):
    pass
class SmallCat(Cat):
    pass
print(issubclass(Cat,Animal))