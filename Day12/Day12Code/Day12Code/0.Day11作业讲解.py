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
# b.打印不及格学生的名字和对应的成绩，并统计个数
# 方式一
count = 0
for stu in students:
    if stu['score'] < 60:
        count += 1
        print(f'{stu["name"]}:{stu["score"]}')
print(count)

# 方式二
stus_list= [[stu["name"],stu["score"]] for stu in students if stu['score'] < 60]
print(stus_list)
print(len(stus_list))

# 方式三
stus_dict = {stu["name"]:stu["score"] for stu in students if stu['score'] < 60}
print(stus_dict)
print(len(stus_dict))

# d.打印手机尾号是8的学生的名字
# 方式一
# for stu in students:
#     if int(stu['tel']) % 10 == 8:
#         print(stu['name'])

# 方式二
for stu in students:
    if stu['tel'][-1] == '8':
        print(stu['name'])

# 方式三
names_list = [stu['name'] for stu in students if stu['tel'][-1] == '8']
print(names_list)

# f.删除性别不明的所有学生
# 方式一
new_students = []        # 定义一个空列表
for stu in students:    # 遍历已知列表
    if stu['gender'] != '不明':   # 条件
        new_students.append(stu)  # 向列表添加元素
print(new_students)

# 方式二
new_students = [stu for stu in students if stu['gender'] != '不明']
print(new_students)

# 方式三
for stu in students[:]:
    if stu['gender'] == '不明':
        students.remove(stu)

# 3.dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]，去除列表中成绩小于70的字典 【列表推导式完成】
dict_list = [{'科目':'政治', '成绩':98},
    {'科目':'政治', '成绩':100},
    {'科目':'政治', '成绩':54},
    {'科目':'政治', '成绩':60},
    {'科目':'政治', '成绩':55},
    {'科目':'政治', '成绩':95}]

# 方式一
# 问题代码
new_list1 = [dict_list.remove(dic) for dic in dict_list[:] if dic['成绩'] < 70]
# print(new_list1)  # [None]
print(dict_list)
# 注意：列表推导式本质是添加元素，xxx.append()/xxx.remove()的返回值都是None

# 正确写法
new_list2 = [dic for dic in dict_list if dic['成绩'] >= 70]
print(new_list2)
