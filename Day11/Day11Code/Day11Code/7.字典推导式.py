'''
列表推导式：[新列表中的元素 for循环  if语句]
字典推导式：{key:value for循环  if语句}
'''

# 1.已知字典dict1 = {'a':10,'b':20},交换dict1中的key和value，生成一个一个新的字典new_dict1
dict1 = {'a':10,'b':20}
# 方式一
new_dict1 = {}
for key,value in dict1.items():
    new_dict1[value] = key
print(new_dict1)

# 方式二
new_dict1 = {value:key for key,value in dict1.items()}
print(new_dict1)

# 练习：生成一个字典{1:1,2:4,3:9,4:16,5:25}
dict2 = {n:n ** 2 for n in range(1,6)}
print(dict2)

# 2.如果有if条件
dict3 = {n:n ** 2 for n in range(1,10) if n % 2 == 0}
print(dict3)

# 3.
list4 = [m + n for m in 'abc' for n in '123']
print(list4)  # 9  ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

dict4 = {m:n for m in 'abc' for n in '123'}
print(dict4)  # {'a': '3', 'b': '3', 'c': '3'}