### Day7作业讲解

> ```Python
> # 1.要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
> '''
> emp_num = 0
> salary_sum = 0
> salary_detail = ''  # 薪资明细
> while True:
>     salary = input(f'请输入第{emp_num}位员工的薪资,输入q结束退出：')
>     # 程序结束的出口
>     if salary == 'q' or salary == 'Q':
>         print('退出操作')
>         break
>     salary = float(salary)
>     if salary < 0:   # 目前考虑理想化的状态，如果要校验浮点数，则需要借助于正则表达式
>         print('薪资小于0，请重新输入')
>         continue
>     # 计数
>     emp_num += 1
>     # 求薪资总和
>     salary_sum += salary
>     # 薪资明细
>     salary_detail += str(salary) + ';'    # +在字符串之间表示拼接
> 
> if emp_num:
>     print(f'录入员工的数量：{emp_num}，平均薪资:{salary_sum / emp_num}，薪资明细:{salary_detail}')
> else:
>     print('未录入员工薪资')
> '''
> 
> # 3.假设某人有100,000现金.每经过一次路口需要进行一次交费. 交
> # 费规则为当他现金大于50,000时每次需要交5%,如果现金小于等于50,000时每次交5,000.请写一程序计算此人可以经过多少次这个路口
> money = 100000
> count = 0
> while money >= 5000:
>     count += 1
>     if money >= 50000:
>         money -= money * 0.05
>     elif money <= 50000:
>         money -= 5000
> print(f'此人可以经过{count}次这个路口')
> ```

### 一、随机数功能

> ```Python
> # 1.randint(a,b)：步长固定为1，无法自定义，是一个闭区间
> # 2.choice(seq):seq:序列,常用列表，元组或字符串
> # 3.randrange(start,stop,step):step默认为1，可以自定义，是前闭后开区间
> # 4.sample(seq,k):从seq中随机获取k个数据，得到一个列表
> # 5.random()：获取0~1之间的随机浮点数，前闭后开区间
> # 6.uniform(a,b):获取a~b之间的随机浮点数
> ```

> ```Python
> # 扩展
> # 导入模块和使用模块功能的语法
> # 方式一
> # import  random
> # r = random.randint(1,100)
> # r = random.choice(range(100))
> 
> # 方式二
> # from random import *      # *表示所有
> # r = randint(1,100)
> # r = choice(range(100))
> 
> 
> from random import  *
> # 1.randint(a,b)：步长固定为1，无法自定义，是一个闭区间
> r1 = randint(1,100)
> print(r1)
> r11 = randint(1,100)
> 
> # 2.choice(seq):seq:序列,常用列表，元组或字符串
> # seq:序列，Python中的列表，字符串，元组等有序的数据类型都可以表示序列
> r21 = choice([34,7,8,9])
> print(r21)
> r22 = choice((34,7,8,9))
> print(r22)
> r23 = choice('abcd')
> print(r23)
> r24 = choice(range(1,101))
> print(r24)
> r24 = choice(range(1,101,2))
> print(r24)
> 
> # 3.randrange(start,stop,step):step默认为1，可以自定义，是前闭后开区间
> r31 = randrange(1,100)
> print(r31)
> r32 = randrange(1,100,2)
> print(r32)
> 
> # 练习：
> # a.获取20~80之间的一个整数随机数
> print(randint(20,80))
> print(choice(range(20,81)))
> print(randrange(20,81))
> # b.获取20~80之间的一个偶数随机数
> print(choice(range(20,81,2)))
> print(randrange(20,81,2))
> 
> # 4.sample(seq,k):从seq中随机获取k个数据，得到一个列表   *******
> r41 = sample([34,1,67,89,900,23,6,7,8],2)
> print(r41)
> r41 = sample((34,1,67,89,900,23,6,7,8),2)
> print(r41)
> r41 = sample('1234567890',5)
> print(r41)
> r41 = sample(range(100),4)
> print(r41)
> 
> # 5.random()：获取0~1之间的随机浮点数，前闭后开区间
> r51 = random()
> print(r51)
> 
> # 6.uniform(a,b):获取a~b之间的随机浮点数
> r61 = uniform(1,100)
> '''
> 工作原理：
>     def uniform(self, a, b):
>         "Get a random number in the range [a, b) or [a, b] depending on rounding."
>         return a + (b - a) * self.random()
> '''
> 
> # 练习
> # 获取20~100之间的浮点数随机数
> r1 = uniform(20,100)
> print(r1)
> # [0,1)---->[0,80)--->[20,100)
> r2 = random() * 80 + 20
> print(r2)
> ```

### 二、列表【重点掌握】

#### 1.概念

> 普通类型：使用变量存储数据，但是，缺点:一个变量每次只能存储一个数据 ,num = 10  
>
> 思考：如果一次性存储多个数据，怎么做？
>
> 实际问题：定义5个人的年龄，求他们的平均年龄，按照以前的方式解决：
>
> ```Python
> age1 = 18
> age2 = 14
> age3 = 20
> age4 = 19
> age5 = 16
> 
> avg_age = (age1 + age2 + age3 + age4 + age5) / 5 
> ```
>
> 继续思考：如果要存储100，甚至1000个人的年龄呢？
>
> 解决方案：此时采用定义普通变量的方式会显得很麻烦，而Python提供了一种解决方案，使用列表进行多个数据的存储
>
> ```Python
> age_list = [18,14,20,19,16]
> avg_age = sum(age_list) / len(age_list)
> ```
>
> 作用：列表相当于是一个容器，可以同时存储多种类型的数据
>
> 本质：列表是一个有序的，可以存储重复元素的集合
>
> 说明：有序指的就是有顺序【数据的存放的顺序和底层存储的顺序是相同的】

#### 2.基本使用

##### 2.1定义列表及列表的特点

> 定义一个列表相当于定义一个列表类型的变量
>
> 变量名  =   值
>
> 语法：列表名   =  [数据1,数据2,数据3.......]
>
> 说明：
>
> ​	a.列表名其实就是一个变量名【标识符】，注意：尽量不要直接使用list【系统有一个功能list(x)】，使用listxxx或xxxlist
>
> ​	b.[]是列表特有的表示方式
>
> ​	c.数据1,数据2,数据3被称为元素【element：元素】
>
> ​	d.列表中的元素会被自动编号，从0开始，该编号被称为索引，下标或者角标
>
> ​	e.索引的取值范围：0 ~  (元素个数 - 1)
>
> ​		       			   -1  ~  -元素个数
>
> ```Python
> # 1.空列表
> # 注意1：定义列表，变量名尽量不要直接使用list,因为有系统功能list()
> list1 = []
> print(list1)
> 
> # 2.非空列表
> # 列表特点
> # a.有序的，注意：有序指的就是有顺序【数据的存放的顺序和底层存储的顺序是相同的】
> list2 = [34,6,7,8,90,34,7,8]
> print(list2)
> 
> # b.同一个列表可以存储不同类型的数据，注意：列表中可以存储Python中所有的数据类型
> list3 = [23,45.7,False,'agag',[45,6,7],(46,78)]
> print(list3)
> 
> # c.列表允许存储重复元素
> list4 = [3,4,5,5,5,5,5,5]
> print(list4)
> 
> # 4.列表是可变的   *******
> list5 = [23,45.7,False,'agag',[45,6,7],(46,78)]
> print(list5)
> list5[0] = 100
> print(list5)
> ```

##### 2.2列表元素访问

> ```python
> """
> 元素：     11   22  33  44  55  66  77  88  99
> 正数索引：  0    1   2   3   4   5   6   7   8
> 负数索引： -9   -8  -7  -6   -5  -4  -3  -2  -1
> 
> 索引的取值范围：
>     正数索引：0~len(x) - 1
>     负数索引：-len(x) ~ -1
> """
> ```

> ```Python
> """
> 元素：     11   22  33  44  55  66  77  88  99
> 正数索引：  0    1   2   3   4   5   6   7   8     0~8
> 负数索引： -9   -8  -7  -6   -5  -4  -3  -2  -1    -9~-1
> 
> 索引的取值范围：
>     正数索引：0~len(x) - 1
>     负数索引：-len(x) ~ -1
> """
> 
> numlist = [11,22,33,44,55,66,77,88,99]
> # len(x):获取列表中元素的个数  或者 获取列表的长度
> print(len(numlist))
> 
> # 1.获取元素
> # 语法：列表[索引]
> print(numlist[0])
> print(numlist[-9])
> 
> print(numlist[4])
> print(numlist[-5])
> 
> print(numlist[8])
> print(numlist[-1])
> 
> # 问题：索引一定不能越界, IndexError: list index out of range
> # print(numlist[9])
> # print(numlist[-10])
> 
> # 2.修改元素
> # 语法：列表[索引] = 值
> print(numlist)
> numlist[3] = 'abc'
> print(numlist)
> 
> numlist[-1] = 100
> print(numlist)
> ```

##### 2.3列表遍历

> ```Python
> numlist = [11,22,33,44,55,66,77,88,99]
> 
> # 遍历：将列表中的元素依次获取出来
> # print(numlist[0])
> # print(numlist[1])
> # print(numlist[2])
> # print(numlist[3])
> 
> # 方式一：只能获取到元素，适用于只操作元素的前提下   ******
> for num in numlist:
>     print(num)
> 
> # 方式二：获取到索引
> i = 0
> while i < len(numlist):
>     print(i,numlist[i])
>     i += 1
> 
> # 推荐for
> for i in range(len(numlist)):
>     print(i,numlist[i])
> 
> # 方式三：同时获取索引和元素
> # 思路：将列表转化为enumerate,本质上也是一个容器，但是该容器中同时存储了索引和元素
> # print(enumerate(numlist))   # <enumerate object at 0x00000283B9BBEFC0>
> # print(list(enumerate(numlist))) # [(0, 11), (1, 22), (2, 33), (3, 44), (4, 55), (5, 66), (6, 77), (7, 88), (8, 99)]
> for i,num in enumerate(numlist):   # 拆包
>     print(i,num)
> 
> 
> ```

##### 2.4列表使用练习

> ```python
> # 1.已知一个数字列表，打印列表中的偶数元素
> # 2.已知任意一个列表，打印列表中索引为偶数的元素
> # 3.已知一个数字列表,求列表中的元素和
> ```

> ```Python
> # 1.已知一个数字列表，打印列表中的偶数元素
> list1 = [34,6,7,78,9,23,5,67,8,10,3,4,7,9]
> for num in list1:
>     if num % 2 == 0:
>         print(num)
> 
> # 2.已知任意一个列表，打印列表中索引为偶数的元素
> list2 = ['a','faf',34,'hy',45,7,34,34,5]
> for i in range(len(list2)):
>     if i % 2 == 0:
>         print(list2[i])
> 
> for i,ele in enumerate(list2):
>     if i % 2 == 0:
>         print(ele)
> 
> # 3.已知一个数字列表,求列表中的元素和
> list3 = [34,6,7,78,9,23,5,67,8,10,3,4,7,9]
> 
> # 方式一
> total = 0
> for num in list3:
>     total += num
> print(total)
> 
> # 方式二：
> # 扩展：sum(iterable)，iterable表示容器，包括列表，元组，字符串，字典，集合，range()等
> total1 = sum(list3)
> print(total1)
> ```

##### 2.5列表基本操作

> ```Python
> # 1.+:添加元素/组合
> print(34 + 45)  # 数学元素
> print('12r' + 'abc')  # 字符串拼接
> l1 = [1,2,3]
> l2 = [4,67,8]
> l3 = l1 + l2
> print(l3)   # 生成了一个新的列表
> print(l1)
> print(l2)
> 
> # 在原列表的基础上新增元素     *****
> l4 = [45,7,9]
> num = 10
> l4 += [num]   # 错误写法：l4 += num
> print(l4)
> 
> # 2.*
> print('abc' * 3)
> print([23,5,6] * 3)  # 注意：生成了一个新的列表
> 
> # 3.in和not  in,一般结合if语句使用   ********
> # 注意：在删除元素之前，最好判断该元素在列表中是否存在，如果存在，再执行删除操作
> print(10 in [34,2,10])
> print(10 not in [34,23,4])
> 
> # 练习
> emp_num = 0
> salary_list = []  # 薪资明细
> while True:
>     salary = input(f'请输入第{emp_num}位员工的薪资,输入q结束退出：')
>     # 程序结束的出口
>     if salary == 'q' or salary == 'Q':
>         print('退出操作')
>         break
>     salary = float(salary)
>     if salary < 0:   # 目前考虑理想化的状态，如果要校验浮点数，则需要借助于正则表达式
>         print('薪资小于0，请重新输入')
>         continue
>     # 计数
>     emp_num += 1
>     # 薪资明细
>     salary_list += [salary]
> 
> if salary_list:
>     print(f'录入员工的数量：{emp_num}，平均薪资:{sum(salary_list) / len(salary_list)}，薪资明细:{salary_list}')
> else:
>     print('未录入员工薪资')
> ```