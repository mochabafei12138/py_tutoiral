# 1.一维列表
list1 = [34,67,8,9,'dada',False,34.1]

# 2.二维列表
list2 = [[12,4,6],[56,8,9,67,8,9],[3,5]]

# 3.二维列表中元素的访问
sublist1 = list2[0]
print(sublist1)
num1 = sublist1[1]
print(num1)

num2 = list2[-1][0]
print(num2)

# 3.遍历二维列表
# a.直接遍历元素
for sublist in list2:
    print(sublist)
    for num in sublist:
        print(num)

# 问题：
list3 = [[34,6,77],34,76,8,9,[34,6,8,9,90]]
for sublist in list3:
    print(sublist)
    if type(sublist) == list:
        for num in sublist:
            print(num)
    else:
        print(sublist)

# b.遍历索引
for i in range(len(list2)):  # 遍历外层列表
    print(i,list2[i])
    for j in range(len(list2[i])):     # 遍历内层列表
        print(list2[i][j])