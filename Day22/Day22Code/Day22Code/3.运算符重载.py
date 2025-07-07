# 1.+
'''
除了数字之外，其他数据类型但凡支持+的运算，底层都是调用了__add__
'''
# a
print('abc' + '123')   # str + str ---- >str
print('abc'.__add__('123'))

print([2,3] + [5,6])  # list + list --->list
print([2,3].__add__([5,6]))

# __dict__
# print(str.__dict__)
# print(list.__dict__)

# b
# class Person():
#     def __init__(self,age):
#         self.age = age
# p1 = Person(10)
# p2 = Person(23)
# print(p1 + p2)  # TypeError: unsupported operand type(s) for +: 'Person' and 'Person'
# print(Person.__dict__)

# c,如果一个类不支持+，则可以在类中重载__add__
class Person():
    def __init__(self,age):
        self.age = age
    # 重写：函数存在但是实现的需求不满足使用
    # 重载：不支持指定的运算，通过重载让支持运算
    def __add__(self, other):
        return Person(self.age + other.age)

    # 重写
    def __str__(self):
        return str(self.age)

p1 = Person(10)
p2 = Person(23)
# 问题1:Person + Person ----》int ,解决：Person + Person ----》Person
# 问题2：当__add__返回 Person(self.age + other.age)，输出p1 + p2结果为对象的地址， 解决：重写__str__
p = p1 + p2
print(p)   # 本质上相加两个人的属性【年龄】
# print(p.__str__())   # 33
# print(p1.__add__(p2))  # 33


# 2.
'''
> ---->__gt__   greater than
< ----> __lt__  less than
== ---> __eq__  equal
!= ---> __ne__  not equal
>= ---> __ge__
<= --->__le__
比较的结果都是布尔值，重载上述运算符时，返回值都设置为布尔值
'''
class Person():
    def __init__(self,age):
        self.age = age
    def __gt__(self, other):
        return self.age > other.age

p1 = Person(10)
p2 = Person(23)
print(p1 > p2)
print(p1.__gt__(p2))
print(Person.__dict__)


