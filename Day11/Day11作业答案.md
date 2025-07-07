### 基础编程题

1.已知字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能

	a.遍历字典 dic 中所有的key
	b.遍历字典 dic 中所有的value
	c.循环遍历字典 dic 中所有的key和value
	d.添加一个键值对"k4","v4",输出添加后的字典 dic
	e.删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
	f.删除字典 dic 中 'k5' 对应的值，若不存在，使其不报错，并返回None
	g.获取字典 dic 中“k2”对应的值
	h.已知字典dic2 = {'k1':"v111",'a':"b"} 编写程序，使得dic2 = {'k1':"v111",'k2':"v2",'k3':"v3",'k4': 'v4','a':"b"}

```Python
dic = {"k1": "v1", "k2": "v2", "k3": "v3"}

#a
for key in dic:
    print(key)

#b
for value in dic.values():
    print(value)

#c
for key,value in dic.items():
    print(key,value)

#d
dic["k4"] = "v4"
print(dic)

#e
dic.pop("k1")
print(dic)

#f
if dic.get("k5"):
    result = dic.pop("k5")
    print(result)
else:
    print(None)

#g
value = dic["k2"]

#h
dic2 = {'k1':"v111",'a':"b"}
for key,value in dic2.items():
    dic[key] = value
print(dic)
```

2.已知列表list1 = [11,22,11,33,44,55,66,55,66],统计列表中每个元素出现的次数，生成一个字典，结果为{11:2,22:1.....}

```Python
# 方式一
dict1 = {}
for num in list1:
    if num not in dict1:
        dict1[num] = list1.count(num)
print(dict1)

# 方式二
dict1 = {}
for num in list1:
    if num not in dict1:
        dict1[num] = 1     # 增加键值对
    else:
        dict1[num] += 1    # 修改指定键对应的值
print(dict1)
```

3.已知如下列表students，在列表中保存了6个学生的信息，根据要求完成下面的题目

```python
students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]
```

```
a.统计不及格学生的个数
b.打印不及格学生的名字和对应的成绩
c.统计未成年学生的个数
d.打印手机尾号是8的学生的名字
e.打印最高分和对应的学生的名字
f.删除性别不明的所有学生
```

```Python
# a.统计不及格学生的个数
# b.打印不及格学生的名字和对应的成绩
list1 = []
for stu_dict in students:
    if stu_dict['score'] < 60:
        list1.append([stu_dict['name'],stu_dict['score']])
print(f"不及格学生的个数:{len(list1)},分别为:{list1}")

# c.统计未成年学生的个数
count = 0
for stu_dict in students:
    if stu_dict['age'] < 18:
        count += 1
print(f"未成年学生的个数:{count}")

# d.打印手机尾号是8的学生的名字
print("手机尾号是8的学生的名字如下：")
for stu_dict in students:
    if stu_dict['tel'][-1] == '8':   # endswith()
        print(stu_dict['name'])

# e.打印最高分和对应的学生的名字
max_score = max([stu_dict['score'] for stu_dict in students])
for stu_dict in students:
    if stu_dict['score'] == max_score:
        print(stu_dict['name'])

# f.删除性别不明的所有学生
# for stu_dict in students[:]:
#     if stu_dict['gender'] == "不明":
#         students.remove(stu_dict)
# print(students)

# for stu_dict in students.copy():
#     if stu_dict['gender'] == "不明":
#         students.remove(stu_dict)
# print(students)

# import  copy
# for stu_dict in copy.copy(students):
#     if stu_dict['gender'] == "不明":
#         students.remove(stu_dict)
# print(students)

# new_students = []
# for stu_dict in students:
#     if stu_dict['gender'] != "不明":
#         new_students.append(stu_dict)
# print(new_students)

new_students = [stu_dict for stu_dict in students if stu_dict['gender'] != "不明"]
print(new_students)
```

4.dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]，去除列表中成绩小于70的字典 【列表推导式完成】

```
结果为： [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}]
```

```Python
dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]
new_list = [subdict for subdict in dict_list if subdict['成绩'] >= 70]
```

