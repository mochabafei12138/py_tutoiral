# 注意：list,dict和set都是可变的数据类型，所以都可以进行增删改的操作

# 一、增
# 1.add(element)，element只能是不可变的数据类型，如果element是一个可迭代对象，整体加入
s1 = {11,22,33}
print(s1)
s1.add(44)
print(s1)
s1.add('abc')
print(s1)
# s1.add([45,7,8])  # TypeError: unhashable type: 'list'
s1.add((45,7,8))
print(s1)

# 注意：集合中的元素只能是不可变的数据类型          *******
# s2 = {34,'fa',(45,6,7),[6,67,8]}
# print(s2)

# 2.update(x),x只能是iterable
s1 = {11,22,33}
print(s1)
# s1.update(44)  # 'int' object is not iterable
s1.update('abc')
print(s1)
s1.update([45,7,8,9])
print(s1)
s1.update({'x':10,'y':20})  # 如果x是字典，则只能添加key
print(s1)

# 二、删
# 1.remove(x):x表示要删除的元素         *******
s1 = {34,6,67,8,9}
print(s1)
s1.remove(67)
print(s1)

# 2.pop()：因为集合是无序的，没有索引，所以pop表示随机删除一个元素
s1 = {34,6,67,8,9}
print(s1)
s1.pop()
print(s1)

# 3.discard()：和remove用法相同，但是如果被删除的元素不存在，remove会报错，但是disacard不会报错
s1 = {34,6,67,8,9}
print(s1)
# s1.remove(100)  # KeyError: 100
# print(s1)

s1.discard(100)
print(s1)

# 4.clear()
s1 = {34,6,67,8,9}
print(s1)
s1.clear()
print(s1)   # set()

# 三、查
s1 = {34,6,67,8,9}
print(len(s1))
print(max(s1))
print(min(s1))

s2 = s1.copy()
print(s1 is s2)

# int()/float()/bool()/str()/list()/tuple()/dict()/set()
# 注意：自定义变量名时，不要和上述系统功能重名，否则会导致系统的功能失效
# list = [34,6,7]

s = 'abc'
list1 = list(s)   # TypeError: 'list' object is not callable可调用的
print(list1)