
# 关注列表的地址问题
# 复习地址问题
# a.id()
n1 = 45
n2 = 67
print(id(n1),id(n2))
print(id(n1) == id(n2))

# b.is
print(n1 is n2)

# c.==:判断值是否相同
print(n1 == n2)

# 一、引用赋值
# 本质：用一个变量给另一个变量赋值
# a.一维列表
list1 = [45,7,9]
list2 = list1
print(id(list1),id(list2))
print(id(list1[0]))
print(list1 == list2)   # True
print(list1 is list2)   # True
list1[0] = 88

print(id(list1),id(list2))
print(id(list1[0]))
print(list1)   # [88, 7, 9]
print(list2)   # [88, 7, 9]

# b.二维列表
list1 = [[3,5,6],[56,89,9]]
list2 = list1
print(list1 == list2) # True
print(list1 is list2)  # True
list1[0][1] = 100
print(list1)
print(list2)

'''
总结1：只要是引用赋值【=】，不管是几维列表，多个变量共用同一个地址，所以通过其中一个变量修改列表中的元素，其他变量访问的列表也会随着更改
      所以如果要对列表进行备份【拷贝】，要达到一个列表被修改，另一个列表不受影响的目的，则千万不能使用引用赋值
'''

# c
list1 = [45,7,9]
# list2 = list1    # list2和list1共用同一个地址，其中存储的是同一个对象
list3 = [45,7,9] # list3和list1是不同的地址，其中存储的是不同的对象【 [45,7,9]但凡重新书写一次，则表示重新开辟了一份新的空间】
print(list1 == list3)  # True
print(list1 is list3)  # False

list1[0] = 88
print(list1)  #  [88, 7, 9]
print(list3)  #  [45, 7, 9]

print('*' * 50)

# 二、浅拷贝:切片/列表.copy()/copy.copy(列表)
import copy
# a.一维列表
list1 = [45,7,9]
# list2 = list1.copy()
# list2 = list1[:]
list2 = copy.copy(list1)
print(id(list1),id(list2))
print(list1 == list2)   # True
print(list1 is list2)   # False
list1[0] = 88
print(list1)   # [88, 7, 9]
print(list2)   # [45, 7, 9]

# b.二维列表
list1 = [[3,5,6],[56,89,9]]
# list2 = list1.copy()
# list2 = list1[:]
list2 = copy.copy(list1)
print(id(list1),id(list2))
print('~~~~~~',id(list1[0]),id(list2[0]))
print('~~~~~~',id(list1[1]),id(list2[1]))
print(list1 == list2)  # True
print(list1 is list2)  # False
list1[0][1] = 100  # 修改的是内层列表中的元素
print(list1)  # [[3, 100, 6], [56, 89, 9]]
print(list2)   # [[3, 100, 6], [56, 89, 9]]

# 注意：虽然是二维列表，但是修改的是外层列表中的元素，所以结果不受影响
list1 = [[3,5,6],[56,89,9]]
list2 = list1.copy()
list1[0] = 34
print(list1)  # [34,[56,89,9]]
print(list2)  # [[3, 5, 6], [56, 89, 9]]

'''
浅拷贝
总结：
    如果修改外层列表中的元素，一个列表访问到的元素发生改变，对另一个列表没有影响
    如果修改内层列表中的元素，一个列表访问的元素发生改变，另一个列表随着改变
    
    如果两个列表变量的地址相同，则一个修改元素，另一个也会随着改
    如果两个列表变量的地址不同，则相互之间没有影响
'''
print('*' * 50)

# 三、深拷贝：copy.deepcopy()
# a.一维列表
list1 = [45,7,9]
list2 = copy.deepcopy(list1)
print(id(list1),id(list2))
print(list1 == list2)   # True
print(list1 is list2)   # False
list1[0] = 88
print(list1)
print(list2)

# b.二维列表
list1 = [[3,5,6],[56,89,9]]
list2 = copy.deepcopy(list1)
print(id(list1),id(list2))
print('~~~~~~',id(list1[0]),id(list2[0]))
print('~~~~~~',id(list1[1]),id(list2[1]))
print(list1 == list2)  # True
print(list1 is list2)  # False
list1[0][1] = 100
print(list1)  # [[3, 100, 6], [56, 89, 9]]
print(list2)

list1 = [[3,5,6],[56,89,9]]
list2 = copy.deepcopy(list1)
list1[0] = 34
print(list1)
print(list2)

# 【面试题】代码阅读题
# 1.
a = [2,5,7]
b = [88,99]
c = [a,b]   # 引用赋值
d = c.copy()  # 浅拷贝
e = copy.deepcopy(c)  # 深拷贝

a[0] = 100
print(c)  # [[100, 5, 7], [88, 99]]
print(d)  # [[100, 5, 7], [88, 99]]
print(e)  # [[2, 5, 7], [88, 99]]

# 2.
datalist = [[23,5],66,[22,33,44]]
list1 = datalist.copy()
list2 = copy.deepcopy(datalist)
datalist[0] = 11
print(list1)   # [[23, 5], 66, [22, 33, 44]]
print(list2)   # [[23, 5], 66, [22, 33, 44]]

datalist = [[23,5],66,[22,33,44]]
list1 = datalist.copy()
list2 = copy.deepcopy(datalist)
datalist[-1].append(55)
print(list1)   # [[23, 5], 66, [22, 33, 44, 55]]
print(list2)  # [[23, 5], 66, [22, 33, 44]]


'''
总结：
    如果达到真正意义上的拷贝，如果是一维列表，则建议使用切片[:]或者列表.copy()
                         如果是二维以上的列表，则建议使用copy.deepcopy()
                         
    应用场景：删除列表元素的时候
    如果遍历a列表，删除a列表中的元素，则一定要对a列表进行备份，否则会删不干净
    如果遍历a列表，删除b列表中的元素，不需要考虑备份问题
'''
list1 = [24,6,2,6,89,0,2,2,2,2,2]
for n in list1[:]:     # *******
    if n == 2:
        list1.remove(2)
print(list1)

list1 = [24,6,2,6,89,0,2,2,2,2,2]
for n in list1.copy():
    if n == 2:
        list1.remove(2)
print(list1)

list1 = [24,6,2,6,89,0,2,2,2,2,2]
for n in copy.copy(list1):
    if n == 2:
        list1.remove(2)
print(list1)

list1 = [24,6,2,6,89,0,2,2,2,2,2]
for n in copy.deepcopy(list1):
    if n == 2:
        list1.remove(2)
print(list1)