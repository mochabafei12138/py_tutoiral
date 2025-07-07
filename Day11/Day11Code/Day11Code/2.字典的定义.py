# 【面试题】定义字典的方式有几种，举例说明
# 1. {key1:value1,key2:value2....}          *******
dict1 = {'a':10,'b':20}
print(dict1)

# 2. 字典[key]=value,当key不存在时，表示添加键值对     ******
dict2 = {}
dict2['aa'] = 66
dict2['bb'] = 77
print(dict2)

# 3.dict(key1=value1,key2=value2....)
# 注意：key=value这种语法和变量的定义类似，最终变量名会被识别为字典中的key
dict31 = dict(x=10,y=20,z=30)
print(dict31)  # {'x': 10, 'y': 20, 'z': 30}

dict32 = {10:11,20:22}
print(dict32) # {10: 11, 20: 22}
# dict32 = dict(10=11,20=22)   # 不能被识别

# 4.dict([(key1,value1),(key2,value2)....])     ****
dict4 = dict([('name','zhangsan'),('age',10)])
print(dict4)
# dict4 = dict([['name','zhangsan'],['age',10]])   # 列表是可变的
# print(dict4)
dict4 = dict((('name','zhangsan'),('age',10)))
print(dict4)

# 5.dict(zip([key1,key2......],[value1,value2.......]))    **********
# zip：映射，[key1,key2......]中的key和[value1,value2.......]中的value会一一对应
dict5 = dict(zip(['a','b','c'],[45,7,89]))
print(dict5)
dict5 = dict(zip(['a','b','c','d'],[45,7,89]))
print(dict5)
dict5 = dict(zip(['a','b','c'],[45,7,89,56,7,8]))
print(dict5)