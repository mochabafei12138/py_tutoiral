# 1.已知一个数字列表，打印列表中的偶数元素
list1 = [34,6,7,78,9,23,5,67,8,10,3,4,7,9]
for num in list1:
    if num % 2 == 0:
        print(num)

# 2.已知任意一个列表，打印列表中索引为偶数的元素
list2 = ['a','faf',34,'hy',45,7,34,34,5]
for i in range(len(list2)):
    if i % 2 == 0:
        print(list2[i])

for i,ele in enumerate(list2):
    if i % 2 == 0:
        print(ele)

# 3.已知一个数字列表,求列表中的元素和
list3 = [34,6,7,78,9,23,5,67,8,10,3,4,7,9]

# 方式一
total = 0
for num in list3:
    total += num
print(total)

# 方式二：
# 扩展：sum(iterable)，iterable表示容器，包括列表，元组，字符串，字典，集合，range()等
total1 = sum(list3)
print(total1)