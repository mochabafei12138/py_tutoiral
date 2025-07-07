# 1.已知列表list1 = ['mon','sun','sat','fri','thu','wed'],list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除
list1 = ['mon','sun','sat','fri','thu','wed']
list2 = ['sun','wed','thu','abc']

# 问题代码一
# for ele in list2:
#     list1.remove(ele)
# print(list1)

# 优化:删除列表元素之前，最好判断确保元素在列表中存在，然后执行删除操作
# for ele in list2:
#     if ele in list1:
#         list1.remove(ele)
# print(list1)

# 问题代码二
# for ele1 in list1:
#     for ele2 in list2:
#         if ele1 == ele2:
#             list1.remove(ele1)
# print(list1)

# 优化：遍历a列表，然后从a列表删除元素，此时一定要对a列表进行备份
for ele1 in list1[:]:  # list1.copy()   copy.copy(list1)   copy.deepcopy(list1)
    for ele2 in list2:
        if ele1 == ele2:
            list1.remove(ele1)
print(list1)

# 5.如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有的素数保存到列表中，并找出其中的"孪生数"
# a.查找所有的质数
prime_list = []
for num in range(2,101):
    for n in range(2,num):
        if num % n == 0:
            break
    else:
        prime_list.append(num)
print(prime_list)

result_list = []
for i in range(1,len(prime_list)):
    if prime_list[i] - prime_list[i - 1] == 2:
        result_list.append((prime_list[i - 1],prime_list[i]))
print(result_list)