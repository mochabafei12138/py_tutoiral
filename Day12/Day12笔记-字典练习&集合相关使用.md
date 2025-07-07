### Day11作业讲解

> ```Python
> students = [
> {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
> '15300022838'},
> {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
> '15300022428'},
> {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
> '15300022839'},
> {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
> '15300022839'}
> ]
> # b.打印不及格学生的名字和对应的成绩，并统计个数
> # 方式一
> count = 0
> for stu in students:
>     if stu['score'] < 60:
>         count += 1
>         print(f'{stu["name"]}:{stu["score"]}')
> print(count)
> 
> # 方式二
> stus_list= [[stu["name"],stu["score"]] for stu in students if stu['score'] < 60]
> print(stus_list)
> print(len(stus_list))
> 
> # 方式三
> stus_dict = {stu["name"]:stu["score"] for stu in students if stu['score'] < 60}
> print(stus_dict)
> print(len(stus_dict))
> 
> # d.打印手机尾号是8的学生的名字
> # 方式一
> # for stu in students:
> #     if int(stu['tel']) % 10 == 8:
> #         print(stu['name'])
> 
> # 方式二
> for stu in students:
>     if stu['tel'][-1] == '8':
>         print(stu['name'])
> 
> # 方式三
> names_list = [stu['name'] for stu in students if stu['tel'][-1] == '8']
> print(names_list)
> 
> # f.删除性别不明的所有学生
> # 方式一
> new_students = []        # 定义一个空列表
> for stu in students:    # 遍历已知列表
>     if stu['gender'] != '不明':   # 条件
>         new_students.append(stu)  # 向列表添加元素
> print(new_students)
> 
> # 方式二
> new_students = [stu for stu in students if stu['gender'] != '不明']
> print(new_students)
> 
> # 方式三
> for stu in students[:]:
>     if stu['gender'] == '不明':
>         students.remove(stu)
> 
> # 3.dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]，去除列表中成绩小于70的字典 【列表推导式完成】
> dict_list = [{'科目':'政治', '成绩':98},
>     {'科目':'政治', '成绩':100},
>     {'科目':'政治', '成绩':54},
>     {'科目':'政治', '成绩':60},
>     {'科目':'政治', '成绩':55},
>     {'科目':'政治', '成绩':95}]
> 
> # 方式一
> # 问题代码
> new_list1 = [dict_list.remove(dic) for dic in dict_list[:] if dic['成绩'] < 70]
> # print(new_list1)  # [None]
> print(dict_list)
> # 注意：列表推导式本质是添加元素，xxx.append()/xxx.remove()的返回值都是None
> 
> # 正确写法
> new_list2 = [dic for dic in dict_list if dic['成绩'] >= 70]
> print(new_list2)
> ```

### 一、字典练习

> ```
> 写一个学生作业情况录入并查询的小程序
> a.录入学生作业情况：字典添加
> b.查看学生作业情况：字典查询
> c.录入时允许输入3次，3次输入不正确提示失败次数过多，禁止继续录入
> ```

> ```Python
> '''
> 写一个学生作业情况录入并查询的小程序
> a.录入学生作业情况：字典添加
> b.查看学生作业情况：字典查询
> c.录入时允许输入3次，3次输入不正确提示失败次数过多，禁止继续录入
> '''
> # 格式
> homeworks = {
>     'tom':{'2020.1.1':'未交','2021.1.8':'已交'},
>     'bob':{'2020.1.1':'未交','2021.1.8':'未交'}
> }
> choice = {'1':'查询','2':'录入'}
> while True:
>     user_choice = input('请输入你的选择，1为查询学生作业，2为录入学生作业,输入q退出：')
>     if user_choice.lower() == 'q':
>         print('欢迎再次使用')
>         # 结束的是while死循环
>         break
>     if choice.get(user_choice) == '查询':
>         name = input('请输入学生的姓名:')
>         if name in homeworks:
>             print(f'{name}的作业情况为:{homeworks[name]}')
>         else:
>             print('查询学生不存在')
>     elif choice.get(user_choice) == '录入':
>         state = {'0': '未交', '1': '已交'}
>         for i in range(3):
>             name = input('请输入学生的姓名：')
>             date = input('请输入提交作业的时间：')
>             input_state = input('请输入学生作业的状态，0为未交，1为已交：')
>             if state.get(input_state):  # 如果key不存在，get会返回None
>                 if name == '' or date == '':
>                     print('学生姓名或日期不能为空')
>                 else:
>                     # 判断学生信息在homeworks中在不在，在则修改，不在则添加
>                     if name in homeworks:
>                         # 方式一：用子字典中的键值对更新原字典
>                         homeworks[name].update({date: state[input_state]})  # 学生存在，更新子字典
>                         # 方式二：向指定字典中添加指定键值对
>                         # homeworks[name][date] = state[input_state]
>                     else:
>                         homeworks[name] = {date: state[input_state]}  # 学生不存在，则添加新的key-value
> 
>                     print(f'{name}的作业情况为：{homeworks[name]}')
>                     print(f'所有学生的作业情况为：{homeworks}')
>                     # 一切输入正确的情况下，则提前结束for循环
>                     break
>             else:
>                 print('学生作业状态有误')
>     else:
>         print('选择输入有误')
> ```

### 二、集合

> Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
>
> set与dict类似，但是与dict的区别在于只是一组key的集合，不存储value
>
> 本质：无序且无重复元素的集合
>
> 表示：{}，注意：如果直接使用{}则默认表示字典

#### 1.集合的定义

> ```Python
> # 1.空集合
> set1 = set()  # {}表示字典
> 
> # 2.非空集合
> # a.去重的             ******
> set2 = {34,5,3,5,5,5,5,5}
> print(set2)
> 
> # b.无序的
> set2 = {34,5,3,78,100,28}
> print(set2)   # {34, 3, 100, 5, 28, 78}
> 
> # 注意：因为集合是无序的，所以集合没有索引
> # 遍历集合,只能使用下面的方式
> for ele in set2:
>     print(ele)
> 
> # 练习：去除一个列表中的重复元素    ******
> numlist = [34,45,67,8,99,8,34,8,67,67,34]
> # 方式一
> new_list1 = []
> for num in numlist:
>     if num not in new_list1:
>         new_list1.append(num)
> print(new_list1)   # [34, 45, 67, 8, 99]
> 
> # 方式二
> new_list2 = list(set(numlist))
> print(new_list2)
> ```

#### 2.集合间的运算

> ```Python
> s1 = {1,3,4}
> s2 = {3,4,5}
> # 1.交集:& 或者intsersection()
> print(s1 & s2)
> print(s1.intersection(s2))
> 
> # 2.并集：| 或者  union()
> print(s1 | s2)
> print(s1.union(s2))
> 
> # 3.差集：- 或者  difference()
> print(s1 - s2)
> print(s1.difference(s2))
> 
> ```

#### 3.集合的系统功能

> add(x):x只能是不可变的数据类型
>
> update(x):x只能是可迭代对象【容器】，表示将x中的元素合并到集合中
>
> remove(x):x表示需要被删除的元素,如果x不存在，则直接报错
>
> pop():因为集合是无序的，表示随机删除一个
>
> discard(x):x表示需要被删除的元素，如果x不存在，不报错
>
> ```Python
> # 注意：list,dict和set都是可变的数据类型，所以都可以进行增删改的操作
> 
> # 一、增
> # 1.add(element)，element只能是不可变的数据类型，如果element是一个可迭代对象，整体加入
> s1 = {11,22,33}
> print(s1)
> s1.add(44)
> print(s1)
> s1.add('abc')
> print(s1)
> # s1.add([45,7,8])  # TypeError: unhashable type: 'list'
> s1.add((45,7,8))
> print(s1)
> 
> # 注意：集合中的元素只能是不可变的数据类型          *******
> # s2 = {34,'fa',(45,6,7),[6,67,8]}
> # print(s2)
> 
> # 2.update(x),x只能是iterable
> s1 = {11,22,33}
> print(s1)
> # s1.update(44)  # 'int' object is not iterable
> s1.update('abc')
> print(s1)
> s1.update([45,7,8,9])
> print(s1)
> s1.update({'x':10,'y':20})  # 如果x是字典，则只能添加key
> print(s1)
> 
> # 二、删
> # 1.remove(x):x表示要删除的元素         *******
> s1 = {34,6,67,8,9}
> print(s1)
> s1.remove(67)
> print(s1)
> 
> # 2.pop()：因为集合是无序的，没有索引，所以pop表示随机删除一个元素
> s1 = {34,6,67,8,9}
> print(s1)
> s1.pop()
> print(s1)
> 
> # 3.discard()：和remove用法相同，但是如果被删除的元素不存在，remove会报错，但是disacard不会报错
> s1 = {34,6,67,8,9}
> print(s1)
> # s1.remove(100)  # KeyError: 100
> # print(s1)
> 
> s1.discard(100)
> print(s1)
> 
> # 4.clear()
> s1 = {34,6,67,8,9}
> print(s1)
> s1.clear()
> print(s1)   # set()
> 
> # 三、查
> s1 = {34,6,67,8,9}
> print(len(s1))
> print(max(s1))
> print(min(s1))
> 
> s2 = s1.copy()
> print(s1 is s2)
> 
> # int()/float()/bool()/str()/list()/tuple()/dict()/set()
> # 注意：自定义变量名时，不要和上述系统功能重名，否则会导致系统的功能失效
> # list = [34,6,7]
> 
> s = 'abc'
> list1 = list(s)   # TypeError: 'list' object is not callable可调用的
> print(list1)
> ```

#### 4.集合练习

> ```
> 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
> a.求选课学生总共有多少人
> b.求只选了第一个学科的人的数量和对应的名字
> c.求只选了一门学科的学生的数量和对应的名字
> d.求只选了两门学科的学生的数量和对应的名字
> e.求选了三门学生的学生的数量和对应的名字
> ```
>
> ```Python
> # 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
> subject1 = ('stu1','stu3','stu4','stu6','stu7','stu9')
> subject2 = ('stu1','stu2','stu3','stu5')
> subject3 = ('stu1','stu3','stu5','stu6','stu7','stu8','stu9')
> 
> # a.求选课学生总共有多少人
> s1 = set(subject1 + subject2 + subject3)
> print(len(s1))
> 
> # b.求只选了第一个学科的人的数量和对应的名字
> # 方式一
> new_names = []
> for stu in subject1:
>     if stu not in subject2 and stu not in subject3:
>         new_names.append(stu)
> print(new_names)
> print(len(new_names))
> 
> # 方式二
> s2 = set(subject1) - set(subject2) - set(subject3)
> print(s2)
> print(len(s2))
> 
> # c.求只选了一门学科的学生的数量和对应的名字
> # 统计每个学生选修的科目数
> subject = subject1 + subject2 + subject3
> count_dict = {}
> for stu in subject:
>     count_dict[stu] = subject.count(stu)
> print(count_dict)
> one_list = []
> for stu,count in count_dict.items():
>     if count == 1:
>         one_list.append(stu)
> print(one_list)
> 
> # d.求只选了两门学科的学生的数量和对应的名字
> two_list = []
> for stu,count in count_dict.items():
>     if count == 2:
>         two_list.append(stu)
> print(two_list)
> 
> # e.求选了三门学生的学生的数量和对应的名字
> three_list = []
> for stu,count in count_dict.items():
>     if count == 3:
>         three_list.append(stu)
> print(three_list)
> ```

