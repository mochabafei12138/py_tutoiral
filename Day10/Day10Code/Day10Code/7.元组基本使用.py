# 1.定义
'''
列表的特点：有序的，允许元素重复，允许存储不同类型的数据，可变的
元组的特点：有序的，允许元素重复，允许存储不同类型的数据，不可变的
'''
# list
lst1 = [34,False,'abc',34,34]
print(lst1)
# tuple
t1 = (34,False,'abc',34,34)
print(t1)

# 注意：当元组中只有一个元素时，为了消除歧义，一定要在元素的后面添加逗号
lst2 = [10]
print(lst2,type(lst2))  # [10] <class 'list'>

t2 = (10)   # t2 = 10
print(t2,type(t2))  # 10 <class 'int'>
t2 = ('abc')  # 等价于 t2 = 'abc'
print(t2,type(t2))  # abc <class 'str'>

t2 = (10,)
print(t2,type(t2))  # (10,) <class 'tuple'>
t2 = ('abc',)
print(t2,type(t2))  # ('abc',) <class 'tuple'>

# 2.元组是不可变的，其中的元素一旦定义完成，不支持修改【更改，增加，删除】
t3 = (34,7,78,9)
print(t3)
# t3[0] = 100   # TypeError: 'tuple' object does not support item元素 assignment赋值【修改】

# 【面试题】
t4 = (34,5,65,[11,22])
print(id(t4[-1]))
t4[-1].append(33)  # 本质上修改的是列表，对元组没有任何影响
print(id(t4[-1]))
print(t4)   # (34, 5, 65, [11, 22, 33])

# 3.元组没有增删改的功能，列表中查的功能对于元组元组同样适用
t5 = (45,67,78,45,99,0,45)
print(len(t5))
print(max(t5))
print(min(t5))
print(t5.index(45))
print(t5.count(45))

# 问题：元组是否有拷贝的功能？---->但凡是不可变的数据类型，都没有拷贝的必要

# 4.列表和元组之间可以进行相互转化
list1 = [23,45]
tuple1 = tuple(list1)
print(tuple1)

tuple2 = (34,6,7)
list2 = list(tuple2)
print(list2)

s = 'abcd'
print(list(s))
print(tuple(s))

# 5.元组的索引，访问元组中的元素，元组的遍历，元组的切片等和列表的用法完全相同
