# 1.list.append(obj)在列表末尾添加新的元素,特点：obj表示任意类型   *******
list1 = [12,4,5]
print(list1)
list1.append(55)
list1.append(False)
list1.append('faf')
list1.append([45,67,9,0])
print(list1)  # [12, 4, 5, 55, False, 'faf', [45, 67, 9, 0]]

# 2.list.extend(iterable)在列表末尾一次性追加另一个序列中的多个值（用新列表中的元素扩展原来的列表）
# iterable:list tuple  dict set str等
list2 = [12,4,5]
print(list2)
list2.extend('abc')
list2.extend([45,7])
list2.extend((56,8))
print(list2)   # [12, 4, 5, 'a', 'b', 'c', 45, 7, 56, 8]
'''
注意：
    a.extend只能添加iterable类型的数据
    b.添加进去的数据不包含容器本身
'''

# 3.list.insert(index,obj)将数据插入到列表的指定索引处，原元素向后顺延
list3 = [34,8,10]
print(list3)
list3.insert(1,88)
print(list3)   # [34, 88, 8, 10]

# 需求：将数据插入到末尾
# 【面试题】注意：insert也可以实现追加元素的效果，当index >= len()
# list3.insert(4,'abc')
# print(list3)   # [34, 88, 8, 10, 'abc']

# 需求：将数据插入到开头
list3.insert(0,'abc')
print(list3)   # ['abc', 34, 88, 8, 10]