# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
subject1 = ('stu1','stu3','stu4','stu6','stu7','stu9')
subject2 = ('stu1','stu2','stu3','stu5')
subject3 = ('stu1','stu3','stu5','stu6','stu7','stu8','stu9')

# a.求选课学生总共有多少人
s1 = set(subject1 + subject2 + subject3)
print(len(s1))

# b.求只选了第一个学科的人的数量和对应的名字
# 方式一
new_names = []
for stu in subject1:
    if stu not in subject2 and stu not in subject3:
        new_names.append(stu)
print(new_names)
print(len(new_names))

# 方式二
s2 = set(subject1) - set(subject2) - set(subject3)
print(s2)
print(len(s2))

# c.求只选了一门学科的学生的数量和对应的名字
# 统计每个学生选修的科目数
subject = subject1 + subject2 + subject3
count_dict = {}
for stu in subject:
    count_dict[stu] = subject.count(stu)
print(count_dict)
one_list = []
for stu,count in count_dict.items():
    if count == 1:
        one_list.append(stu)
print(one_list)

# d.求只选了两门学科的学生的数量和对应的名字
two_list = []
for stu,count in count_dict.items():
    if count == 2:
        two_list.append(stu)
print(two_list)

# e.求选了三门学生的学生的数量和对应的名字
three_list = []
for stu,count in count_dict.items():
    if count == 3:
        three_list.append(stu)
print(three_list)