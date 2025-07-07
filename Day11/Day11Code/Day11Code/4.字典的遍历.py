info_dict = {'name':'张三','age':18,'hobby':'dance'}

# 注意：通过key可以直接获取value【字典[key]】,但是value无法直接直接获取key,只能通过遍历字典，然后比对获取

# 方式一：遍历所有的key，xxx.keys()
# print(info_dict.keys())
for key in info_dict.keys():
    print(key,info_dict[key])

# 方式二：遍历所有的key              ********
for key in info_dict:
    print(key,info_dict[key])

# 方式三：遍历所有的value
# print(info_dict.values())
for value in info_dict.values():
    print(value)

# 方式四：同时遍历key和value         ********
# print(info_dict.items())
for key,value in info_dict.items():
    print(key,value)