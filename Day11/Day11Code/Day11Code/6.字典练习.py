# 1.已知列表list1 = [34,56,87,78,98,9,34,345,78,9],统计每个元素出现的次数，生成一个字典
# key是列表中的元素，value是该元素在列表中出现的次数
list1 = [34,56,87,78,98,9,34,345,78,9]
# 方式一
dict1 = {}
for num in list1:
    if num not in dict1:
        dict1[num] = 1   # 添加键值对
    else:
        dict1[num] += 1   # 修改指定key对应的值
print(dict1)

# 方式二
dict1 = {}
for num in list1:
    dict1[num] = list1.count(num)
print(dict1)

# 2.已知列表,找出最大的年龄，及最大年龄的人的名字
list2 = [
    {'name':'张三','age':10},
    {'name':'李四','age':9},
    {'name':'aaa','age':12},
    {'name':'小明','age':14},
    {'name':'bbb','age':10},
    {'name':'王五','age':8},
    {'name':'ccc','age':14}
]
max_age = max([user_dict['age'] for user_dict in list2])
print(max_age)
names_list = []
for user_dict in list2:
    if user_dict['age'] == max_age:
        names_list.append(user_dict['name'])
print(f'最大年龄为{max_age},对应的人为:{names_list}')