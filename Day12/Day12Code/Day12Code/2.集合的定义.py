# 1.空集合
set1 = set()  # {}表示字典

# 2.非空集合
# a.去重的             ******
set2 = {34,5,3,5,5,5,5,5}
print(set2)

# b.无序的
set2 = {34,5,3,78,100,28}
print(set2)   # {34, 3, 100, 5, 28, 78}

# 注意：因为集合是无序的，所以集合没有索引
# 遍历集合,只能使用下面的方式
for ele in set2:
    print(ele)

# 练习：去除一个列表中的重复元素    ******
numlist = [34,45,67,8,99,8,34,8,67,67,34]
# 方式一
new_list1 = []
for num in numlist:
    if num not in new_list1:
        new_list1.append(num)
print(new_list1)   # [34, 45, 67, 8, 99]

# 方式二
new_list2 = list(set(numlist))
print(new_list2)

