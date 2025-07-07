# is 和 is not

'''
【面试题】
==：比较两个变量的值/内容是否相同
is:比较两个变量的地址是否相同
'''

# 1.不可变的数据类型：int/float/bool/str/tuple/bytes/NoneType
a = 10
b = 10
print(a == b)
print(a is b)

print(id(a),id(b),id(10))
print(id(a) == id(b))  # 等价于is的结果

c = 20
print(a == c)
print(a is c)


# 2.可变的数据类型：list/dict/set
list1 = [44,55,66]
list2 = [44,55,66]
print(list1 == list2)   # True
print(list1 is list2)   # False
print(id(list1) == id(list2))

list3 = list1
print(list1 == list3)  # True
print(list1 is list3)  # True
print(id(list1) == id(list3))

print(list1,list2,list3)

'''
结论：
    如果两个变量的值相同，这两个变量的地址不一定相同
    如果两个变量的地址相同，则这两个变量中存储的数据一定相同
'''