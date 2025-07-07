# 1.{}
a = {'fafg','vdfgv'}
print(a,type(a))   # {'fafg', 'vdfgv'} <class 'set'>
b = {'a':10,'b':20}
print(b,type(b))  # {'a': 10, 'b': 20} <class 'dict'>

c = {}   # 空字典
print(c,type(c))  # {} <class 'dict'>
d = set()  # 空集合
print(d,type(d))

# 2.key和value的数据类型
# a.key:只能是不可变的数据类型【int float bool  tuple str】,不能使用可变的数据类型【list dict set 】
d21 = {10:34,34.5:56,False:23,'abv':6,(45,7):67}
print(d21)
# d22 = {[34,6,7]:567}
# print(d22)  # TypeError: unhashable type: 'list'

# b.value:可以是任意类型
d21 = {10:34,34.5:5.6,False:True,'abv':'faf',(45,7):[7,8,9]}
print(d21)

# 3.key和value是否可以重复
# a.key:每个字典里的key都是唯一的，如果出现了多个相同的key,后面的value会覆盖之前的value
d31 = {'name':'张三','age':10,'name':'李四'}
print(d31)  # {'name': '李四', 'age': 10}

# b.value:可以重复
d32 = {'张三':100,'李四':100}
print(d32)

# 4.字典是无序的
'''
列表/元组/字符串：都是通过索引访问其中的元素/字符,都是有序的
字典：通过key获取value

字典本质上是无序的
    在Python3.7之前，输出字典的结果显示就是无序的
    在Python3.7之后，输出字典的结果显示是有序的，但本质上是无序的，容易误导大家
'''
# 集合是无序的
set1 = {45,7,8,9,80,23,34,6}
print(set1)  # {34, 6, 7, 8, 9, 45, 80, 23}
