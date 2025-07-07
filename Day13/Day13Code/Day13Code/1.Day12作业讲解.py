'''
1.定义一个电话簿，里头设置以下联系人：
'mayun':'13309283335',
'zhaolong':'18989227822',
'zhangmin':'13382398921',
'Gorge':'19833824743',
'Jordan':'18807317878',
'Curry':'15093488129',
'Wade':'19282937665'
现在输入人名，查询他的号码，如果人名存在，则输出电话号码，如果该人不存在，返回"not found"
'''
'''
# 方式一
info_dict = {
'mayun':'13309283335',
'zhaolong':'18989227822',
'zhangmin':'13382398921',
'Gorge':'19833824743',
'Jordan':'18807317878',
'Curry':'15093488129',
'Wade':'19282937665'
}
name = input('请输入需要查询的人名：')
# if name in info_dict.keys():  # 正确，但是没必要
if name in info_dict:  # 简化写法
    print(info_dict[name])
else:
    print('not found')

# 方式二
info_list = [
    {'mayun':'13309283335'},
    {'zhaolong':'18989227822'},
    {'zhangmin':'13382398921'},
    {'Gorge':'19833824743'},
    {'Jordan':'18807317878'},
    {'Curry':'15093488129'},
    {'Wade':'19282937665'}
]
name = input('请输入需要查询的人名：')
for dic in info_list:
    if name in dic:
        print(dic[name])
        break
else:
    print('not found')
'''

# 2.已知列表numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99],
# 生成一个字典，将大于66的数字保存在字典的第一个key中，将小于等于66的数字保存在字典的第二个key中
numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99]
# 方式一
key1 = []
key2 = []
for num in numlist:
    if num > 66:
        key1.append(num)
    else:
        key2.append(num)
dict1 = {'key1':key1,'key2':key2}
print(dict1)

# 方式二
dict1 = {'key1':[],'key2':[]}
for num in numlist:
    if num > 66:
        dict1['key1'].append(num)
    else:
        dict1['key2'].append(num)
print(dict1)

# 方式二
dict1 = {'key1':[num for num in numlist if num > 66],'key2':[num for num in numlist if num <= 66]}
print(dict1)
