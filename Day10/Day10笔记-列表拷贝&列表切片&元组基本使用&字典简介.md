### Day9作业讲解

>  ```Python
>  # 1.
>  lst = []
>  #  在lst列表中依次追加10个数值[8, 93, 66, 83, 100, 95, 77, 93, 85, 98]
>  sublist = [8, 93, 66, 83, 100, 95, 77, 93, 85, 98]
>  # lst.append(sublist)
>  # print(lst)  # [[8, 93, 66, 83, 100, 95, 77, 93, 85, 98]]
>  
>  # for num in sublist:
>  #     lst.append(num)
>  # print(lst)
>  
>  lst.extend(sublist)   # 打碎加入
>  print(lst)  # [8, 93, 66, 83, 100, 95, 77, 93, 85, 98]
>  
>  # 2.
>  # a. 生成一个存放1-100之间个位数为3的数据列表
>  list_a = [n for n in range(1,101) if n % 10 == 3]
>  print(list_a)
>  
>  # b. 利用列表推导式将已知列表中的整数提取出来
>  list_b = [True, 17, "hello", "bye", 98, 34, 21]
>  new_list_b = [ele for ele in list_b if type(ele) == int]
>  print(new_list_b)
>  
>  # c.利用列表推导式存放指定列表中字符串的长度
>  list_c =  ["good", "nice", "see you", "bye"]
>  # len()
>  new_list_c = [len(s) for s in list_c]
>  print(new_list_c)
>  
>  # d.生成一个列表，其中的元素为'0-1'，'1-2'，'2-3'，'3-4'，'4-5'
>  list_d1 = [str(n) + '-' + str(n + 1) for n in range(5)]
>  print(list_d1)
>  list_d2 = [f'{n}-{n + 1}' for n in range(5)]
>  print(list_d2)
>  
>  # 3.根据products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号,
>  # 就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。注意：本题可以自由发挥
>  products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
>  # print('============','欢迎进入xxx自助购物超市','============')
>  # 扩展：xxx.center(width,ch):将xxx字符串居中显示，两端用ch填充，最终字符串的长度为width
>  print('欢迎进入xxx自助购物超市'.center(50,'='))
>  # 购物车
>  shop_car = []
>  while True:
>      print('商品信息如下：')
>      for i,pro in enumerate(products):
>          print(f'    编号{i}:名称：{pro[0]},价格:{pro[1]}')
>      # 询问用户想买什么，用户选择一个商品编号
>      choice = input('请输入需要购买的商品的编号【输入q退出】：')
>      # 扩展：
>      '''
>      xxx.lower():将xxx字符串转化为小写
>      xxx.upper():将xxx字符串转化为大写
>      print('ffaa'.lower())  # 'ffaa'
>      print('HFRDggq'.lower())  # hfrdggg
>      '''
>      # if choice == 'q' or choice == 'Q':
>      if choice.lower() == 'q':
>          print('购买完毕，退出系统')
>          break
>      if choice.isdigit():
>          choice = int(choice)
>          if choice in range(len(products)):
>              # 添加到购物车
>              shop_car.append(products[choice])
>              print('添加成功!')
>          else:
>              print('暂无此商品')
>      else:
>          print('输入有误')
>  if shop_car:
>      print(f'购物车列表为：{shop_car}')
>  else:
>      print('没有购买任何商品')
>  ```

### 一、列表进阶

#### 1、切片操作【面试题】

> 【面试题】什么是切片，请举例说明
>
> 切片：根据指定的区间，指定的步长，在列表，元组或字符串等有序集合中进行截取，形成一个新的列表，元组或字符串
>
> ```
> 语法：
> 	xx[start:end:step]，注意：xx表示列表，元组或字符串
>
>     start:开始索引，可以省略，默认为0，不省略的情况下包含在内
>
>     end:结束索引，可以省略，默认为索引的结束【len - 1  或 -len】,不省略的情况下不包含在内
>
>     step：表示步长，可以省略，默认为1
> ```
>
> 索引：
> ​    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>
> 注意：切片之后会得到一个新的列表，对原列表没有任何影响,相当于是列表的拷贝
>
> ```Python
> """
>    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>   10   20  30  40  50  60  70  80   90
> """
> """
> 注意：
>     a.切片之后会得到一个新的列表，对原列表没有任何影响,相当于是列表的拷贝
>     b.在切片操作中，只要符合切片的语法，哪怕索引越界都不会报错，区别无非是列表是否为空
> """
> ```
>
> ```python
> """
> 规律1：如果start和end同正负
>     第一步：计算start+step
>     第二步：判断第一步计算的结果是否在给定的start和end区间内
>     第三步：如果在区间内，则按照规律获取元素；如果不在区间内，则直接得结果[]
> """
> """
> 规律2：如果start和end一个为正，一个为负
>     第一步：查看start的正负，索引的使用和start的正负保持一致
>     第二步：如果start为正，则使用正数索引【将end的索引等价转换为正数索引】
>            如果start为负，则使用负数索引【将end的索引等价转换为负数索引】
>     第三步：使用规律1
> """
> """
> 规律3：如果start和end都被省略，观察step的正负
>     a.如果step为正数，则从左往右进行获取【顺序获取】
>     b.如果step为负数，则从右往左进行获取【倒序获取】  
> """
> """
> 规律4：列表[start::step]
>     a.如果step为正数，则从左往右进行获取【顺序获取】
>     b.如果step为负数，则从右往左进行获取【倒序获取】  
> """
> ```

> ```Python
> """
>    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>   10   20  30  40  50  60  70  80   90
> """
> """
> 注意：
>     a.切片之后会得到一个新的列表，对原列表没有任何影响,相当于是列表的拷贝
>     b.在切片操作中，只要符合切片的语法，哪怕索引越界都不会报错，区别无非是列表是否为空
> """
> numlist = [10,20,30,40,50,60,70,80,90]
> 
> # 一、基本使用【掌握】
> # 1.注意1：明确end的情况下，end不包含在内
> print(numlist[1:6])   # 前闭后开区间， [20, 30, 40, 50, 60]
> print(numlist[1:6:1])  #  [20, 30, 40, 50, 60]
> print(numlist[1:6:2]) # [20, 40, 60]
> print(numlist)
> 
> # 2.注意2：end省略的情况下，从指定索引取到结尾，此时end包含在内
> print(numlist[1:])  # [20, 30, 40, 50, 60, 70, 80, 90]
> 
> # 从左往右全部获取，拷贝列表，[10, 20, 30, 40, 50, 60, 70, 80, 90]
> print(numlist[::1])
> print(numlist[::])
> print(numlist[:])   # ********
> 
> # 从右往左全部获取，逆序拷贝列表,[90, 80, 70, 60, 50, 40, 30, 20, 10]
> print(numlist[::-1])  # *******
> 
> # 3.【面试题】
> # print(numlist[100])    # 不是切片，是访问列表中元素的语法，会索引越界，IndexError: list index out of range
> print(numlist[100:])     # 是切片【至少出现一个冒号】，结果是[]
> 
> # 二、规律用法【了解】
> # 1.
> """
> 规律1：如果start和end同正负
>     第一步：计算start+step
>     第二步：判断第一步计算的结果是否在给定的start和end区间内
>     第三步：如果在区间内，则按照规律获取元素；如果不在区间内，则直接得结果[]
> """
> """
>    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>   10   20  30  40  50  60  70  80   90
> """
> # 注意：不管索引为正为负，只要end不省略，则end对应的元素都取不到
> print(numlist[1:6:1])   # [20,30,...60]
> print(numlist[1:6:-1])  # []
> 
> print(numlist[6:1:1])   # []
> print(numlist[6:1:-1])  # [70,60...30]
> 
> print(numlist[-1:-6:1])   # []
> print(numlist[-1:-6:-1])  # [90.80....50]
> 
> print(numlist[-6:-1:1])  # [40,50...80]
> print(numlist[-6:-1:-1]) # []
> 
> # 2.
> """
> 规律2：如果start和end一个为正，一个为负
>     第一步：查看start的正负，索引的使用和start的正负保持一致
>     第二步：如果start为正，则使用正数索引【将end的索引等价转换为正数索引】
>            如果start为负，则使用负数索引【将end的索引等价转换为负数索引】
>     第三步：使用规律1
> """
> """
>    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>   10   20  30  40  50  60  70  80   90
> """
> print(numlist[-1:6:1])   # [-1:-3:1]---->[]
> print(numlist[-1:6:-1])  # [-1:-3:-1]---->[90,80]
> 
> print(numlist[-6:1:1])   # [-6:-8:1]--->[]
> print(numlist[-6:1:-1])  # [-6:-8:-1]--->[40,30]
> 
> print(numlist[1:-6:1])  # [1:3:1]--->[20,30]
> print(numlist[1:-6:-1])  # [1:3:-1]--->[]
> 
> print(numlist[6:-1:1])   # [6:8:1]--->[70,80]
> print(numlist[6:-1:-1])  # []
> 
> # 3.
> """
> 规律3：如果start和end都被省略，观察step的正负
>     a.如果step为正数，则从左往右进行获取【顺序获取】
>     b.如果step为负数，则从右往左进行获取【倒序获取】  
> """
> print(numlist[:])
> print(numlist[::-1])
> 
> # 4.
> """
> 规律4：列表[start::step]
>     a.如果step为正数，则从左往右进行获取【顺序获取】
>     b.如果step为负数，则从右往左进行获取【倒序获取】  
> """
> """
>    0   1   2   3   4   5   6   7     8
>   -9   -8  -7  -6  -5  -4  -3  -2   -1
>   10   20  30  40  50  60  70  80   90
> """
> print(numlist[6::-1])  # [60,50...10]
> print(numlist[6::1])   # [70,80,90]
> 
> print(numlist[-6::-1])  # [40...10]
> print(numlist[-6::1])   # [40,50,..90]
> 
> # 练习：
> names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
> # a.取出names列表中索引4-7的元素
> # for i in range(4,8):
> #     print(names[i])
> 
> print(names[4:8])
> 
> # b.取出names列表中索引2-10的元素，步长为2
> # for i in range(2,11,2):
> #     print(names[i])
> 
> print(names[2:11:2])
> 
> # c.取出names列表中最后3个元素
> for i in range(-3,0):   # range(-1,-3,-1)
>     print(names[i])
> 
> print(names[-1:-4:-1])
> print(names[len(names)-3:])
> ```

#### 2、列表拷贝【面试题】

> ```Python
> 
> # 关注列表的地址问题
> # 复习地址问题
> # a.id()
> n1 = 45
> n2 = 67
> print(id(n1),id(n2))
> print(id(n1) == id(n2))
> 
> # b.is
> print(n1 is n2)
> 
> # c.==:判断值是否相同
> print(n1 == n2)
> 
> # 一、引用赋值
> # 本质：用一个变量给另一个变量赋值
> # a.一维列表
> list1 = [45,7,9]
> list2 = list1
> print(id(list1),id(list2))
> print(id(list1[0]))
> print(list1 == list2)   # True
> print(list1 is list2)   # True
> list1[0] = 88
> 
> print(id(list1),id(list2))
> print(id(list1[0]))
> print(list1)   # [88, 7, 9]
> print(list2)   # [88, 7, 9]
> 
> # b.二维列表
> list1 = [[3,5,6],[56,89,9]]
> list2 = list1
> print(list1 == list2) # True
> print(list1 is list2)  # True
> list1[0][1] = 100
> print(list1)
> print(list2)
> 
> '''
> 总结1：只要是引用赋值【=】，不管是几维列表，多个变量共用同一个地址，所以通过其中一个变量修改列表中的元素，其他变量访问的列表也会随着更改
>       所以如果要对列表进行备份【拷贝】，要达到一个列表被修改，另一个列表不受影响的目的，则千万不能使用引用赋值
> '''
> 
> # c
> list1 = [45,7,9]
> # list2 = list1    # list2和list1共用同一个地址，其中存储的是同一个对象
> list3 = [45,7,9] # list3和list1是不同的地址，其中存储的是不同的对象【 [45,7,9]但凡重新书写一次，则表示重新开辟了一份新的空间】
> print(list1 == list3)  # True
> print(list1 is list3)  # False
> 
> list1[0] = 88
> print(list1)  #  [88, 7, 9]
> print(list3)  #  [45, 7, 9]
> 
> print('*' * 50)
> 
> # 二、浅拷贝:切片/列表.copy()/copy.copy(列表)
> import copy
> # a.一维列表
> list1 = [45,7,9]
> # list2 = list1.copy()
> # list2 = list1[:]
> list2 = copy.copy(list1)
> print(id(list1),id(list2))
> print(list1 == list2)   # True
> print(list1 is list2)   # False
> list1[0] = 88
> print(list1)   # [88, 7, 9]
> print(list2)   # [45, 7, 9]
> 
> # b.二维列表
> list1 = [[3,5,6],[56,89,9]]
> # list2 = list1.copy()
> # list2 = list1[:]
> list2 = copy.copy(list1)
> print(id(list1),id(list2))
> print('~~~~~~',id(list1[0]),id(list2[0]))
> print('~~~~~~',id(list1[1]),id(list2[1]))
> print(list1 == list2)  # True
> print(list1 is list2)  # False
> list1[0][1] = 100  # 修改的是内层列表中的元素
> print(list1)  # [[3, 100, 6], [56, 89, 9]]
> print(list2)   # [[3, 100, 6], [56, 89, 9]]
> 
> # 注意：虽然是二维列表，但是修改的是外层列表中的元素，所以结果不受影响
> list1 = [[3,5,6],[56,89,9]]
> list2 = list1.copy()
> list1[0] = 34
> print(list1)  # [34,[56,89,9]]
> print(list2)  # [[3, 5, 6], [56, 89, 9]]
> 
> '''
> 浅拷贝
> 总结：
>     如果修改外层列表中的元素，一个列表访问到的元素发生改变，对另一个列表没有影响
>     如果修改内层列表中的元素，一个列表访问的元素发生改变，另一个列表随着改变
>     
>     如果两个列表变量的地址相同，则一个修改元素，另一个也会随着改
>     如果两个列表变量的地址不同，则相互之间没有影响
> '''
> print('*' * 50)
> 
> # 三、深拷贝：copy.deepcopy()
> # a.一维列表
> list1 = [45,7,9]
> list2 = copy.deepcopy(list1)
> print(id(list1),id(list2))
> print(list1 == list2)   # True
> print(list1 is list2)   # False
> list1[0] = 88
> print(list1)
> print(list2)
> 
> # b.二维列表
> list1 = [[3,5,6],[56,89,9]]
> list2 = copy.deepcopy(list1)
> print(id(list1),id(list2))
> print('~~~~~~',id(list1[0]),id(list2[0]))
> print('~~~~~~',id(list1[1]),id(list2[1]))
> print(list1 == list2)  # True
> print(list1 is list2)  # False
> list1[0][1] = 100
> print(list1)  # [[3, 100, 6], [56, 89, 9]]
> print(list2)
> 
> list1 = [[3,5,6],[56,89,9]]
> list2 = copy.deepcopy(list1)
> list1[0] = 34
> print(list1)
> print(list2)
> 
> # 【面试题】代码阅读题
> # 1.
> a = [2,5,7]
> b = [88,99]
> c = [a,b]   # 引用赋值
> d = c.copy()  # 浅拷贝
> e = copy.deepcopy(c)  # 深拷贝
> 
> a[0] = 100
> print(c)  # [[100, 5, 7], [88, 99]]
> print(d)  # [[100, 5, 7], [88, 99]]
> print(e)  # [[2, 5, 7], [88, 99]]
> 
> # 2.
> datalist = [[23,5],66,[22,33,44]]
> list1 = datalist.copy()
> list2 = copy.deepcopy(datalist)
> datalist[0] = 11
> print(list1)   # [[23, 5], 66, [22, 33, 44]]
> print(list2)   # [[23, 5], 66, [22, 33, 44]]
> 
> datalist = [[23,5],66,[22,33,44]]
> list1 = datalist.copy()
> list2 = copy.deepcopy(datalist)
> datalist[-1].append(55)
> print(list1)   # [[23, 5], 66, [22, 33, 44, 55]]
> print(list2)  # [[23, 5], 66, [22, 33, 44]]
> 
> 
> '''
> 总结：
>     如果达到真正意义上的拷贝，如果是一维列表，则建议使用切片[:]或者列表.copy()
>                          如果是二维以上的列表，则建议使用copy.deepcopy()
>                          
>     应用场景：删除列表元素的时候
>     如果遍历a列表，删除a列表中的元素，则一定要对a列表进行备份，否则会删不干净
>     如果遍历a列表，删除b列表中的元素，不需要考虑备份问题
> '''
> list1 = [24,6,2,6,89,0,2,2,2,2,2]
> for n in list1[:]:     # *******
>     if n == 2:
>         list1.remove(2)
> print(list1)
> 
> list1 = [24,6,2,6,89,0,2,2,2,2,2]
> for n in list1.copy():
>     if n == 2:
>         list1.remove(2)
> print(list1)
> 
> list1 = [24,6,2,6,89,0,2,2,2,2,2]
> for n in copy.copy(list1):
>     if n == 2:
>         list1.remove(2)
> print(list1)
> 
> list1 = [24,6,2,6,89,0,2,2,2,2,2]
> for n in copy.deepcopy(list1):
>     if n == 2:
>         list1.remove(2)
> print(list1)
> ```

#### 3.列表练习

##### 3.1编写小学生算术能力测试系统

> ```
> 设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以下功能：
> a.提供10道加、减、乘或除四种基本算术运算的题目；
> b.练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确并显示出相应的信息。
> ```

> ```Python
> '''
> 编写小学生算术能力测试系统
> 设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以下功能：
> a.提供10道加、减、乘或除四种基本算术运算的题目；
> b.练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确并显示出相应的信息。
> '''
> import  random
> 
> print('欢迎进入天才儿童答题系统'.center(40,'*'))
> 
> # 定义用来记录总的题目数和回答正确的数量
> count = 0
> right = 0
> 
> # 10道题目，循环10次
> while count < 10:
>     # 定义列表，表示加减乘除的符号
>     options = ['+','-','*','/']
>     # 随机产生运算符
>     op = random.choice(options)
>     # 随机产生0~100以内的运算数
>     num1 = random.randint(0,99)
>     num2 = random.randint(1,99)   # 除数不能为0
>     # 出题
>     print(f'{num1} {op} {num2} =')
>     # 等待用户输入答案
>     answer = input('请输入你的答案【输入q退出】：')
>     if answer.lower() == 'q':
>         break
> 
>     # 判断随机生成的运算符，并计算正确结果
>     if op == options[0]:
>         r = num1 + num2
>     elif op == options[1]:
>         r = num1 - num2
>     elif op == options[2]:
>         r = num1 * num2
>     else:
>         r = num1 / num2
> 
>     # 判断用户输入的结果是否正确，为了保持类型的一致，转换类型
>     if answer == str(r):
>         print('回答正确')
>         right += 1
>     else:
>         print('回答错误')
>     count += 1
> 
> # 计算正确率
> if count == 0:
>     percent = 0
> else:
>     percent = right / count
> print('答题结束，共回答%d道题,正确%d道题，正确率为%.2f%%' % (count,right,percent * 100))
> ```

##### 3.2分配办公室

> 3个办公室，8位老师，随机分配办公室
>
> ```Python
> '''
> 分配办公室
> 3个办公室，8位老师，随机分配办公室
> '''
> import  random
> 
> # 定义列表，表示一个学校中的三个办公室
> schools = [[],[],[]]  # 三个小列表就是三个办公室，对应的索引为0 1 2
> # 定义列表，表示八位老师
> techers = ['李','张','姚','杨','赵','王','孙','周']
> 
> # 让老师抓阄
> # 遍历老师的列表
> for tea in techers:
>     # 产生办公室的随机数
>     room = random.randint(0,2)
>     # 让当前老师进入抓到的办公室
>     schools[room].append(tea)
> 
> for room in schools:
>     print(f'该办公室中老师的数量为{len(room)},分别是:')
>     for tea in room:
>         print(tea,end=',')
>     print()
> 
> # 扩展：'xxx'.join(iterable):当iterable中的元素为字符串时，用xx将这些元素进行拼接
> # 举例：l = ['a','b','c']----->'-'.join(l)---->'a-b-c'
> for room in schools:
>     result = ','.join(room)
>     print(f'该办公室中老师的数量为{len(room)},分别是:{result}')
> ```

##### 3.3后台管理员管理前台会员信息系统

> ```
> 后台管理员管理前台会员信息系统:
> 
> 1. 后台管理员只有一个用户: admin, 密码: admin
> 2. 当管理员登陆成功后， 可以管理前台会员信息.
> 3. 会员信息管理包含:
>       添加会员信息
>       删除会员信息
>       查看会员信息
>       退出
> ```

> ```Python
> '''
> 后台管理员管理前台会员信息系统
> 
> 1. 后台管理员只有一个用户: admin, 密码: admin
> 2. 当管理员登陆成功后， 可以管理前台会员信息.
> 3. 会员信息管理包含:
>       添加会员信息
>       删除会员信息
>       查看会员信息
>       退出
> '''
> # 定义列表，存储会员信息
> users_list = []
> # [[会员名称，会员密码]，]
> 
> print('管理员登录界面'.center(50,'*'))
> for i in range(3):
>     # 引导输入管理员的用户名和密码
>     admin_name = input('请输入管理员的用户名:')
>     admin_pwd = input('请输入管理员的密码：')
>     if admin_name == 'admin' and admin_pwd == 'admin':
>         print('管理员登录成功！')
>         print('欢迎进入xxx会员管理系统')
>         # 进入管理系统
>         # 因为进入管理系统之后，具体要做哪些操作，进行几次操作不确定
>         while True:
>             print('''********操作目录**********
>                     1.添加会员信息
>                     2.删除会员信息
>                     3.查看会员信息
>                     4.退出''')
>             # 引导管理员执行相应的操作
>             choice = input('请输入需要执行的操作：')
>             if choice == '1':
>                 print('添加会员信息'.center(50,'*'))
>                 user_name = input('请输入会员名：')
>                 user_pwd = input('请输入会员密码：')
>                 users_list.append([user_name,user_pwd])
>                 print('添加成功！')
>             elif choice == '2':
>                 print('删除会员信息'.center(50,'*'))
>                 user_name = input('请输入需要删除的会员名：')
>                 # 设定：如果查找到会员信息，只删除一个【其他的同名的会员信息不做处理】
>                 for user in users_list:
>                     if user[0] == user_name:
>                         users_list.remove(user)
>                         print('删除成功')
>                         break
>                 else:
>                     print('会员信息不存在')
>             elif choice == '3':
>                 print('查看会员信息'.center(50, '*'))
>                 for user in users_list:
>                     print(f'会员名：{user[0]},密码:{user[1]}')
>             elif choice == '4':
>                 print('欢迎再次使用')
>                 # 此处的break结束的是while死循环
>                 break  # 扩展：此处的break可以替换为exit()，表示退出程序
>                 # exit()
>             else:
>                 print('输入有误，暂无此操作，请输入正确的操作编号')
>         # 此处的break结束的是for循环
>         break
>     else:
>         if i == 2:
>             continue
>         print('管理员登录失败,请重新输入')
> else:
>     print('已经错误三次，禁止管理员登录')
> ```

### 二、元组【了解】

#### 1.概念

> 和列表相似，本质上是一种有序的集合
>
> 元组和列表的不同之处：
>
> ​	a.列表:[]     元组：()
>
> ​	b.列表中的元素可以进行增加和删除操作，但是，元组中的元素不能修改【元素：一旦被初始化，将不能发生改变】

#### 2.元组基本操作

> 创建列表:
>
> ​	创建空列表：list1 = []
>
> ​	创建有元素的列表：list1 = [元素1，元素2，。。。。。]
>
> 创建元组
>
> ​	创建空元组：tuple1 = ()
>
> ​	创建有的元组：tuple1 = (元素1，元素2，。。。。)
>
> ```Python
> # 1.定义
> '''
> 列表的特点：有序的，允许元素重复，允许存储不同类型的数据，可变的
> 元组的特点：有序的，允许元素重复，允许存储不同类型的数据，不可变的
> '''
> # list
> lst1 = [34,False,'abc',34,34]
> print(lst1)
> # tuple
> t1 = (34,False,'abc',34,34)
> print(t1)
> 
> # 注意：当元组中只有一个元素时，为了消除歧义，一定要在元素的后面添加逗号
> lst2 = [10]
> print(lst2,type(lst2))  # [10] <class 'list'>
> 
> t2 = (10)   # t2 = 10
> print(t2,type(t2))  # 10 <class 'int'>
> t2 = ('abc')  # 等价于 t2 = 'abc'
> print(t2,type(t2))  # abc <class 'str'>
> 
> t2 = (10,)
> print(t2,type(t2))  # (10,) <class 'tuple'>
> t2 = ('abc',)
> print(t2,type(t2))  # ('abc',) <class 'tuple'>
> 
> # 2.元组是不可变的，其中的元素一旦定义完成，不支持修改【更改，增加，删除】
> t3 = (34,7,78,9)
> print(t3)
> # t3[0] = 100   # TypeError: 'tuple' object does not support item元素 assignment赋值【修改】
> 
> # 【面试题】
> t4 = (34,5,65,[11,22])
> print(id(t4[-1]))
> t4[-1].append(33)  # 本质上修改的是列表，对元组没有任何影响
> print(id(t4[-1]))
> print(t4)   # (34, 5, 65, [11, 22, 33])
> 
> # 3.元组没有增删改的功能，列表中查的功能对于元组元组同样适用
> t5 = (45,67,78,45,99,0,45)
> print(len(t5))
> print(max(t5))
> print(min(t5))
> print(t5.index(45))
> print(t5.count(45))
> 
> # 问题：元组是否有拷贝的功能？---->但凡是不可变的数据类型，都没有拷贝的必要
> 
> # 4.列表和元组之间可以进行相互转化
> list1 = [23,45]
> tuple1 = tuple(list1)
> print(tuple1)
> 
> tuple2 = (34,6,7)
> list2 = list(tuple2)
> print(list2)
> 
> s = 'abcd'
> print(list(s))
> print(tuple(s))
> 
> # 5.元组的索引，访问元组中的元素，元组的遍历，元组的切片等和列表的用法完全相同
> ```

### 三、字典简介

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