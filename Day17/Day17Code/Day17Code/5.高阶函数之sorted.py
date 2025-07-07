'''
sorted(iterable,reverse,key=func)
'''

'''
【面试题】lst.sort()和sorted()之间的区别
1.二者的调用方式不同
    lst.sort(reverse,key)，sorted(lst,reverse,key)
2.返回值不同
    lst.sort()返回None,是在原列表内部直接排序的
    sorted()返回一个新的列表，对原列表没有任何影响
3.二者默认情况下都是升序，如果要降序，都是设置reverse=True
4.sort只能列表调用，但是sorted可以适用于任意的可迭代对象
5.二者默认的情况下，都只针对列表中的元素可以比较大小的情况，如果要自定义排序规则，则都要设置key=func
'''

# 1.二者的调用方式不同，返回值不同
# 升序
lst = [34,5,34,5,56,7,19,4]
lst.sort()
print(lst)

lst = [34,5,34,5,56,7,19,4]
new_list = sorted(lst)
print(new_list)

# 降序
lst = [34,5,34,5,56,7,19,4]
lst.sort(reverse=True)
print(lst)

lst = [34,5,34,5,56,7,19,4]
new_list = sorted(lst,reverse=True)
print(new_list)

# 2.key=func
list1 = ['4gh','34m577457','faf5bb','2355']
list1.sort(key=len)
print(list1)

list1 = ['4gh','34m577457','faf5bb','2355']
new_list1 = sorted(list1,key=len)
print(new_list1)

# 练习
students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]
# 对年龄进行升序
students1 = students.copy()
# students1.sort(key=lambda dic:dic['age'])
# print(students1)

# new_students1 = sorted(students1,key=lambda dic:dic['age'])
# print(new_students1)

# 对成绩进行降序
# students1.sort(reverse=True,key=lambda dic:dic['score'])
# print(students1)

new_students1 = sorted(students1,reverse=True,key=lambda dic:dic['score'])
print(new_students1)

