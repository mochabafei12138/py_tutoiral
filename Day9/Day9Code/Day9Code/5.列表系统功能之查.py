
list1 = [34,6,87,9,34,6,8,12]

# 1.len(list)获取列表元素个数       ********
print(len(list1))
# 2.max(list)返回列表元素最大值
print(max(list1))
# 3.min(list)返回列表元素最小值
print(min(list1))
# 4.list.count(obj)统计某个元素在列表中出现的次数  ******
r1 = list1.count(34)
print(r1)

# 优化：删除列表中所有的6,则需要用到循环处理
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
c = list1.count(6)
for _ in range(c):
    list1.remove(6)
print(list1)

# 5.list.index(obj)从列表中找出某个值第一个匹配项的索引位置
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
i1 = list1.index(6)
print(i1)

# i2 = list1.index(10)   # ValueError: 10 is not in list
