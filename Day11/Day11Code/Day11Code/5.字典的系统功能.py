# 1.增
# a.字典[key] = value,当key不存在时，表示添加键值对
dict1 = {}
dict1['aa'] = 66
dict1['bb'] = 77
print(dict1)

# b.d1.update(d2):将d2中的键值对合并到d1中
info_dict = {'name':'张三','age':18,'hobby':'dance'}
sub_dict = {'a':10,'b':20}
info_dict.update(sub_dict)   # 类似于列表中的extend
print(info_dict)
print(sub_dict)

# 2.删
# a.xx.pop(key):通过指定的key删除对应的键值对
info_dict = {'name':'张三','age':18,'hobby':'dance'}
# 注意：从字典中删除键值对的时候，最好判断key是否存在
info_dict.pop('age')
print(info_dict)

# 优化
key = 'score'
if key in info_dict:
    info_dict.pop(key)
else:
    print('key不存在')

# b.clear():清空字典
info_dict = {'name':'张三','age':18,'hobby':'dance'}
info_dict.clear()
print(info_dict)

# c.del  xx[key]
info_dict = {'name':'张三','age':18,'hobby':'dance'}
del info_dict['name']
print(info_dict)

# 3.查
info_dict = {'name':'张三','age':18,'hobby':'dance'}
print(len(info_dict))
print(info_dict.keys())
print(info_dict.values())
print(info_dict.items())
# 注意：默认情况下，求的是所有的key的最值
print(max(info_dict))  # name
print(min(info_dict))  # age

# 4.copy()
# 注意：但凡是可变的数据类型，都有拷贝的功能，字典和列表的深浅拷贝的使用完全相同
# 【面试题】
d1 = {'a':34,'b':13}
d2 = d1.copy()
d1['a'] = 88
print(d1)
print(d2)     # {'a':34,'b':13}

import copy
d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
d4 = copy.deepcopy(d3)
d3['m'][-1] = 88
print(d3)    # {'aga':26,'hgh':132,'m':[1,2,88]}
print(d4)    # {'aga':26,'hgh':132,'m':[1,2,3]}

d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
d4 = copy.copy(d3)  # d3.copy()
d3['m'][-1] = 88
print(d3)  # {'aga': 26, 'hgh': 132, 'm': [1, 2, 88]}
print(d4)  # {'aga': 26, 'hgh': 132, 'm': [1, 2, 88]}

