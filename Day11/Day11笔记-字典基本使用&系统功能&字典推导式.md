### Day10作业讲解

> ```Python
> # 1.已知列表list1 = ['mon','sun','sat','fri','thu','wed'],list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除
> list1 = ['mon','sun','sat','fri','thu','wed']
> list2 = ['sun','wed','thu','abc']
> 
> # 问题代码一
> # for ele in list2:
> #     list1.remove(ele)
> # print(list1)
> 
> # 优化:删除列表元素之前，最好判断确保元素在列表中存在，然后执行删除操作
> # for ele in list2:
> #     if ele in list1:
> #         list1.remove(ele)
> # print(list1)
> 
> # 问题代码二
> # for ele1 in list1:
> #     for ele2 in list2:
> #         if ele1 == ele2:
> #             list1.remove(ele1)
> # print(list1)
> 
> # 优化：遍历a列表，然后从a列表删除元素，此时一定要对a列表进行备份
> for ele1 in list1[:]:  # list1.copy()   copy.copy(list1)   copy.deepcopy(list1)
>     for ele2 in list2:
>         if ele1 == ele2:
>             list1.remove(ele1)
> print(list1)
> 
> # 5.如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有的素数保存到列表中，并找出其中的"孪生数"
> # a.查找所有的质数
> prime_list = []
> for num in range(2,101):
>     for n in range(2,num):
>         if num % n == 0:
>             break
>     else:
>         prime_list.append(num)
> print(prime_list)
> 
> result_list = []
> for i in range(1,len(prime_list)):
>     if prime_list[i] - prime_list[i - 1] == 2:
>         result_list.append((prime_list[i - 1],prime_list[i]))
> print(result_list)
> ```

### 二、字典【重点掌握】

#### 1.概念

> 列表和元组的使用缺点：当存储的数据要动态添加、删除的时候，我们一般使用列表，但是列表有时会遇到一些麻烦,定位元素比较麻烦
>
> ```python
> # 一个列表/元组保存5个学生的成绩，
> score_list = [66,100,70,78,99]
> score_tuple = (66,100,70,78,99)
> ```
>
> 解决方案：既能存储多个数据，还能在访问元素的很方便的定位到需要的元素，采用字典
>
> ```python
> # 一个字典保存5个学生的成绩，
> score_dict = {"小明":66,"小花":100,"jack":70,"tom":70,"bob":99}
> ```

> 字典习惯使用场景【不是绝对的】：
>
> - 列表更适合保存相似数据，比如多个商品、多个姓名、多个时间
> - 字典更适合保存不同数据 或者 需要定位数据，比如一个商品的不同信息、一个人的不同信息

> ```Python
> # 除了列表之外，Python中另一个比较重要的数据类型是字典
> 
> # 1.需求：存储5个学生的成绩
> # 用列表表示，问题：如果需要定位或匹配数据，则用列表存储有缺陷
> scores_list = [88,99,60,59,100]
> print(scores_list)
> 
> # 解决：字典【dict】
> # 语法：dic = {key1:value1,key2:value2.......}
> scores_dict = {'张三':88,'李四':99,'小明':60,'王五':59,'小花':100}
> print(scores_dict)
> 
> # 2.访问字典中的键值
> # a.获取值，
> # 方式一：语法：字典[key]
> # 注意：通过索引获取列表中的元素，通过key获取字典中对应的value
> # 需求：获取小明的成绩
> score1 = scores_dict['小明']
> print(score1)
> 
> # 缺点：如果访问了一个不存在的key，则报错KeyError: '小丽'
> # score2 = scores_dict['小丽']
> 
> # 方式二：字典.get(key),推荐
> score1 = scores_dict.get('小明')
> print(score1)
> 
> # 优点：当key不存在时，不会报错，会返回None
> score2 = scores_dict.get('小丽')
> print(score2)
> 
> # b.修改值
> # 注意：字典和列表一样，都属于可变的数据类型，但是在字典中，一般修改的是指定key对应的值
> # 语法：字典[key] = 值
> 
> # 1>当key存在时，表示修改指定key对应的值
> print(scores_dict)
> scores_dict['小明'] = 80
> print(scores_dict)
> 
> # 2>当key不存在时，表示向字典中添加一对键值对   *******
> scores_dict['小丽'] = 77
> print(scores_dict)
> ```

#### 2.定义字典

> 语法：**{键1:值1, 键2:值2, 键3:值3, ..., 键n:值n}**
>
> 说明：
>
> - 字典和列表类似，都可以用来存储多个数据
> - 在列表中查找某个元素时，是根据索引进行的；字典中找某个元素时，是根据键查找的（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
> - 字典中的每个元素都由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
> - **键可以使用数字、布尔值、元组，字符串等不可变数据类型，但是一般习惯使用字符串，切记不能使用列表等可变数据类型**,但是，值的数据类型没有限制
> - 每个字典里的key都是唯一的，如果出现了多个相同的key,后面的value会覆盖之前的value

> ```python
> # 【面试题】定义字典的方式有几种，举例说明
> # 1. {key1:value1,key2:value2....}         
> # 2. 字典[key]=value          
> # 3.dict(key1=value1,key2=value2....)
> # 4.dict([(key1,value1),(key2,value2)....])
> # 5.dict(zip([key1,key2......],[value1,value2.......]))        
> ```

> ```Python
> # 【面试题】定义字典的方式有几种，举例说明
> # 1. {key1:value1,key2:value2....}          *******
> dict1 = {'a':10,'b':20}
> print(dict1)
> 
> # 2. 字典[key]=value,当key不存在时，表示添加键值对     ******
> dict2 = {}
> dict2['aa'] = 66
> dict2['bb'] = 77
> print(dict2)
> 
> # 3.dict(key1=value1,key2=value2....)
> # 注意：key=value这种语法和变量的定义类似，最终变量名会被识别为字典中的key
> dict31 = dict(x=10,y=20,z=30)
> print(dict31)  # {'x': 10, 'y': 20, 'z': 30}
> 
> dict32 = {10:11,20:22}
> print(dict32) # {10: 11, 20: 22}
> # dict32 = dict(10=11,20=22)   # 不能被识别
> 
> # 4.dict([(key1,value1),(key2,value2)....])     ****
> dict4 = dict([('name','zhangsan'),('age',10)])
> print(dict4)
> # dict4 = dict([['name','zhangsan'],['age',10]])   # 列表是可变的
> # print(dict4)
> dict4 = dict((('name','zhangsan'),('age',10)))
> print(dict4)
> 
> # 5.dict(zip([key1,key2......],[value1,value2.......]))    **********
> # zip：映射，[key1,key2......]中的key和[value1,value2.......]中的value会一一对应
> dict5 = dict(zip(['a','b','c'],[45,7,89]))
> print(dict5)
> dict5 = dict(zip(['a','b','c','d'],[45,7,89]))
> print(dict5)
> dict5 = dict(zip(['a','b','c'],[45,7,89,56,7,8]))
> print(dict5)
> ```

#### 3.字典的使用

> ```Python
> # 1.{}
> a = {'fafg','vdfgv'}
> print(a,type(a))   # {'fafg', 'vdfgv'} <class 'set'>
> b = {'a':10,'b':20}
> print(b,type(b))  # {'a': 10, 'b': 20} <class 'dict'>
> 
> c = {}   # 空字典
> print(c,type(c))  # {} <class 'dict'>
> d = set()  # 空集合
> print(d,type(d))
> 
> # 2.key和value的数据类型
> # a.key:只能是不可变的数据类型【int float bool  tuple str】,不能使用可变的数据类型【list dict set 】
> d21 = {10:34,34.5:56,False:23,'abv':6,(45,7):67}
> print(d21)
> # d22 = {[34,6,7]:567}
> # print(d22)  # TypeError: unhashable type: 'list'
> 
> # b.value:可以是任意类型
> d21 = {10:34,34.5:5.6,False:True,'abv':'faf',(45,7):[7,8,9]}
> print(d21)
> 
> # 3.key和value是否可以重复
> # a.key:每个字典里的key都是唯一的，如果出现了多个相同的key,后面的value会覆盖之前的value
> d31 = {'name':'张三','age':10,'name':'李四'}
> print(d31)  # {'name': '李四', 'age': 10}
> 
> # b.value:可以重复
> d32 = {'张三':100,'李四':100}
> print(d32)
> 
> # 4.字典是无序的
> '''
> 列表/元组/字符串：都是通过索引访问其中的元素/字符,都是有序的
> 字典：通过key获取value
> 
> 字典本质上是无序的
>     在Python3.7之前，输出字典的结果显示就是无序的
>     在Python3.7之后，输出字典的结果显示是有序的，但本质上是无序的，容易误导大家
> '''
> # 集合是无序的
> set1 = {45,7,8,9,80,23,34,6}
> print(set1)  # {34, 6, 7, 8, 9, 45, 80, 23}
> 
> ```

#### 4.字典的遍历

> ```Python
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> 
> # 注意：通过key可以直接获取value【字典[key]】,但是value无法直接直接获取key,只能通过遍历字典，然后比对获取
> 
> # 方式一：遍历所有的key，xxx.keys()
> # print(info_dict.keys())
> for key in info_dict.keys():
>     print(key,info_dict[key])
> 
> # 方式二：遍历所有的key              ********
> for key in info_dict:
>     print(key,info_dict[key])
> 
> # 方式三：遍历所有的value
> # print(info_dict.values())
> for value in info_dict.values():
>     print(value)
> 
> # 方式四：同时遍历key和value         ********
> # print(info_dict.items())
> for key,value in info_dict.items():
>     print(key,value)
> ```

#### 5.字典系统功能

> d1.update(d2):将d2中的键值对合并到d1中
>
> d1.pop(key):通过指定的key删除key-value对
>
> d.1clear():清空字典
>
> ```Python
> # 【面试题】
> d1 = {'a':34,'b':13}
> d2 = d1.copy()
> d1['a'] = 88
> print(d2)  
> 
> import copy
> d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
> d4 = copy.deepcopy(d3)
> d3['m'][-1] = 88
> print(d3)  
> print(d4) 
> 
> d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
> d4 = copy.copy(d3)  # d3.copy()
> d3['m'][-1] = 88
> print(d3) 
> print(d4) 
> ```

> ```Python
> # 1.增
> # a.字典[key] = value,当key不存在时，表示添加键值对
> dict1 = {}
> dict1['aa'] = 66
> dict1['bb'] = 77
> print(dict1)
> 
> # b.d1.update(d2):将d2中的键值对合并到d1中
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> sub_dict = {'a':10,'b':20}
> info_dict.update(sub_dict)   # 类似于列表中的extend
> print(info_dict)
> print(sub_dict)
> 
> # 2.删
> # a.xx.pop(key):通过指定的key删除对应的键值对
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> # 注意：从字典中删除键值对的时候，最好判断key是否存在
> info_dict.pop('age')
> print(info_dict)
> 
> # 优化
> key = 'score'
> if key in info_dict:
>     info_dict.pop(key)
> else:
>     print('key不存在')
> 
> # b.clear():清空字典
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> info_dict.clear()
> print(info_dict)
> 
> # c.del  xx[key]
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> del info_dict['name']
> print(info_dict)
> 
> # 3.查
> info_dict = {'name':'张三','age':18,'hobby':'dance'}
> print(len(info_dict))
> print(info_dict.keys())
> print(info_dict.values())
> print(info_dict.items())
> # 注意：默认情况下，求的是所有的key的最值
> print(max(info_dict))  # name
> print(min(info_dict))  # age
> 
> # 4.copy()
> # 注意：但凡是可变的数据类型，都有拷贝的功能，字典和列表的深浅拷贝的使用完全相同
> # 【面试题】
> d1 = {'a':34,'b':13}
> d2 = d1.copy()
> d1['a'] = 88
> print(d1)
> print(d2)     # {'a':34,'b':13}
> 
> import copy
> d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
> d4 = copy.deepcopy(d3)
> d3['m'][-1] = 88
> print(d3)    # {'aga':26,'hgh':132,'m':[1,2,88]}
> print(d4)    # {'aga':26,'hgh':132,'m':[1,2,3]}
> 
> d3 = {'aga':26,'hgh':132,'m':[1,2,3]}
> d4 = copy.copy(d3)  # d3.copy()
> d3['m'][-1] = 88
> print(d3)  # {'aga': 26, 'hgh': 132, 'm': [1, 2, 88]}
> print(d4)  # {'aga': 26, 'hgh': 132, 'm': [1, 2, 88]}
> ```

#### 6.字典练习

> ```python
> # 1.已知列表list1 = [34,56,87,78,98,9,34,345,78,9],统计每个元素出现的次数，生成一个字典
> # key是列表中的元素，value是该元素在列表中出现的次数
> 
> # 2.已知列表,找出最大的年龄，及最大年龄的人的名字
> list2 = [
>     {'name':'张三','age':10},
>     {'name':'李四','age':9},
>     {'name':'aaa','age':12},
>     {'name':'小明','age':14},
>     {'name':'bbb','age':10},
>     {'name':'王五','age':8},
>     {'name':'ccc','age':14}
> ]
> ```

> ```Python
> # 1.已知列表list1 = [34,56,87,78,98,9,34,345,78,9],统计每个元素出现的次数，生成一个字典
> # key是列表中的元素，value是该元素在列表中出现的次数
> list1 = [34,56,87,78,98,9,34,345,78,9]
> # 方式一
> dict1 = {}
> for num in list1:
>     if num not in dict1:
>         dict1[num] = 1   # 添加键值对
>     else:
>         dict1[num] += 1   # 修改指定key对应的值
> print(dict1)
> 
> # 方式二
> dict1 = {}
> for num in list1:
>     dict1[num] = list1.count(num)
> print(dict1)
> 
> # 2.已知列表,找出最大的年龄，及最大年龄的人的名字
> list2 = [
>     {'name':'张三','age':10},
>     {'name':'李四','age':9},
>     {'name':'aaa','age':12},
>     {'name':'小明','age':14},
>     {'name':'bbb','age':10},
>     {'name':'王五','age':8},
>     {'name':'ccc','age':14}
> ]
> max_age = max([user_dict['age'] for user_dict in list2])
> print(max_age)
> names_list = []
> for user_dict in list2:
>     if user_dict['age'] == max_age:
>         names_list.append(user_dict['name'])
> print(f'最大年龄为{max_age},对应的人为:{names_list}')
> ```

#### 7.字典推导式

> ```Python
> '''
> 列表推导式：[新列表中的元素 for循环  if语句]
> 字典推导式：{key:value for循环  if语句}
> '''
> 
> # 1.已知字典dict1 = {'a':10,'b':20},交换dict1中的key和value，生成一个一个新的字典new_dict1
> dict1 = {'a':10,'b':20}
> # 方式一
> new_dict1 = {}
> for key,value in dict1.items():
>     new_dict1[value] = key
> print(new_dict1)
> 
> # 方式二
> new_dict1 = {value:key for key,value in dict1.items()}
> print(new_dict1)
> 
> # 练习：生成一个字典{1:1,2:4,3:9,4:16,5:25}
> dict2 = {n:n ** 2 for n in range(1,6)}
> print(dict2)
> 
> # 2.如果有if条件
> dict3 = {n:n ** 2 for n in range(1,10) if n % 2 == 0}
> print(dict3)
> 
> # 3.
> list4 = [m + n for m in 'abc' for n in '123']
> print(list4)  # 9  ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
> 
> dict4 = {m:n for m in 'abc' for n in '123'}
> print(dict4)  # {'a': '3', 'b': '3', 'c': '3'}
> ```