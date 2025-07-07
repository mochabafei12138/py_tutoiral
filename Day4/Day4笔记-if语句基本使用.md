### Day3作业讲解

> ```Python
> 
> # 6.注意：布尔和数字进行数学运算时，被当成0和1使用，其他情况下，正常使用
> a = 100
> b = False
> print(a * b > -1)
> print(100 * False > -1)   # True
> 
> # 3.已知x = 3 == 3,执行结束后，变量x的值为（True）。
> # 注意：先计算3 == 3，结果为True,将True赋值给x
> x = 3 == 3
> print(x)
> 
> # 表达式 9 ** 0.5的值为（3.0）。
> # 注意：但凡右浮点数参与运算符，结果都是浮点数
> 
> # 从控制台输入一个三位数，分别拆分出个位数，十位数和百位数，将拆分结果输出，格式为：百位：xx,十位：xx，个位：xx
> # 方式一：算术运算符
> num = int(input('请输入一个三位数：'))  # 562
> gw = num % 10
> sw = num // 10 % 10   # num % 100 // 10
> bw = num // 100
> print(f'百位：{bw},十位：{sw}，个位：{gw}')   # int
> 
> # 方式二：字符串
> num = input('请输入一个三位数：')
> '''
> x[n]:x可以是字符串，列表或元组，n是从0开始的数字【索引】
> 如：
> s = 'abc'
> s[0] ----->'a'
> s[1]----->'b'
> s[2]----->'c'
> '''
> bw = num[0]
> sw = num[1]
> gw = num[2]
> print(f'百位：{bw},十位：{sw}，个位：{gw}')  # str
> 
> 
> '''
> 下列表达式的值为True的是（B）。
> A. 3>2>2                3>2 and 2>2 ----->True and False----->False
> B. 1 and 2 != 1         1 and True----->True
> C. not(11and 0!=1)      11 and True---->True   not True---->False
> D. 10 < 20 and 10 < 5     True and False---->False
> '''
> ```

### 一、分支语句【重点掌握】

> Python 中语句的结构：顺序结构，分支结构【if语句】，循环结构【while语句和for语句】

#### 1.概念

> 在生活中，所谓的判断，指的是如果某些条件满足才能做某件事情；条件不满足时则不能做
>
> ![判断情景](Day4-images/判断情景.png)
>
> 在编程中，判断所给定的条件是否满足，根据判断的结果对应执行不同的语句，Python中的分支语句只有if语句
>
> ![if语句](Day4-images/if语句.JPG)

#### 2.使用

##### 2.1if单分支

> 语法：
>
> ```
> if 条件：
> 	语句
> ```
>
> 说明：当程序执行到if语句时，首先判断“条件”的值，如果条件的值为“真”，则执行缩进的语句；如果条件的值为“假”，则跳过整个if语句继续向下执行
>
> ```Python
> """
> 总结：
>     a.在Python中，是通过缩进区分代码块的，在编写程序的过程中，要注意缩进对齐问题,
>       一个缩进一般是4个空格或一个tab键
>     b.if语句中的条件是常量，变量或表达式
>     c.Python中表示假的数据：0  0.0   False "" []  ()  {}  None等
>     d.if单分支的工作原理：如果条件成立，则执行代码块中的语句，
>       如果条件不成立，则整个if语句会被跳过，继续执行后面的代码
>     e.总结：代码块要么执行，要么不执行
> """
> ```

> ```Python
> # 1.基本语法
> print('start~~~~~')
> # a.if语句中的条件是常量，变量或表达式
> # b.Python中表示假的数据：0  0.0   False "" []  ()  {}  None等,在if语句中作为条件，都表示条件不成立
> if 'twt':
>     print('yes')
> 
> num = 0
> if num:
>     print('yes~~~1111')
> 
> num1 = 45
> num2 = 99
> if num1 == num2:
>     print('yes~~~2222')
> 
> print('end~~~~~~')
> 
> # 在Python中，是通过缩进区分代码块的，在编写程序的过程中，要注意缩进对齐问题,
> #  一个缩进一般是4个空格或一个tab键
> if 34:
>     print('wgwhwh')
> 
> print('=' * 50)
> 
> # 2.工作原理：代码块要么执行，要么不执行
> num1 = 45
> num2 = 90
> if num1 == num2:
>     print('yes~~~2222')
> 
> print('over')
> 
> # 3.应用
> # a.禁止未成年人进入网吧
> # age = int(input('请输入你的年龄：'))
> # if age < 18:
> #     print('未成年禁止进入网吧')
> 
> # b.从控制台输入一个数，判断该数是否是偶数
> num = int(input('请输入一个数：'))
> # 偶数---》2的倍数----》能被2整除-----》%
> 
> # 注意：=只使用在给变量赋值的语法中，==用于比较
> if num % 2 == 0:
>     print(f'{num}是偶数')
> ```

##### 2.2if双分支

> 语法：
>
> ```
> if 条件：
> 	语句1
> else：
> 	语句2
> ```
>
> 说明：当程序执行到if-else语句时，首先判断“条件”的值，如果条件的值为“真”，则执行语句1；如果条件的值为“假”，则执行语句2
>

> ```Python
> 在Python中产生随机数的方式：
> 方式一：
>      第一步：导入模块/导入库：import  random   
>      第二步：num = random.randint(start,end)，闭区间【包头包尾】,步长默认为1，无法自定义步长
> 方式二：
>      第一步：import  random   
>      第二步：num = random.choice(容器)，
>         range(start,end,step):相当于生成了一个容器，前闭后开区间【包头不包尾】，容器中的数据是指定的区间，指定的步长
>             start：开始数字，可以省略，默认为0
>             end：结束数字，不可以省略
>             step：步长，可以省略，默认为1，从start~end递增，则步长为正数，从start~end递减，则步长为负数
>             
> 举例：
>     random.randint(0,100):获取0~100之间的任意一个整数随机数
>     random.choice(range(100)):获取0~99之间的任意一个整数随机数
>     random.choice(range(1,100)):获取1~99之间的任意一个整数随机数
>     random.choice(range(1,100,2)):获取1~99之间的任意一个奇数随机数
>     random.choice(range(0,100,2)):获取0~99之间的任意一个偶数随机数
>     
>     random.choice(range(100,2)):错误写法，说明：如果end和step未被省略，则start也不能省略
> ```

> ```Python
> # 1.基本语法
> # a.双分支中条件的使用和单分支中完全相同
> # b.if-else双分支的特点：实现二选一的操作
> print('start~~~~~~')
> num1 = 45
> num2 = 45
> if num1 == num2:
>     print('yes~~~1111')
> else:
>     print('no~~~~~1111')
> print('end~~~~~~~')
> 
> # 2.应用
> # a.禁止未成年人进入网吧
> # age = int(input('请输入你的年龄：'))
> # if age < 18:
> #     print('未成年禁止进入网吧')
> # else:
> #     print('欢迎光临，请多多充值')
> 
> # b.从控制台输入一个数，判断该数是否是偶数
> # num = int(input('请输入一个数：'))
> # # 偶数---》2的倍数----》能被2整除-----》%
> # # 注意：=只使用在给变量赋值的语法中，==用于比较
> # if num % 2 == 0:
> #     print(f'{num}是偶数')
> # else:
> #     print(f'{num}是奇数')
> 
> # 3.随机数的获取
> import random
> # 方式一
> n1 = random.randint(1,100)  # 在1~100之间获取一个整数随机数，是闭区间
> print(n1)
> # 方式二
> n2 = random.choice(range(1,101,1))  # 在1~100之间获取一个整数随机数，前闭后开区间，等价于[1,2,3,4,5....100]
> print(n2)
> 
> # 获取0~100之间的任意一个整数随机数
> n3 = random.randint(0,100)
> n3 = random.choice(range(0,101,1))
> n3 = random.choice(range(101))
> # 其他用法
> n4 = random.choice(range(1,100)) #获取1~99之间的任意一个整数随机数,等价于[1,2,3....99]
> n5 = random.choice(range(1,100,2)) #获取1~99之间的任意一个奇数随机数,等价于[1,3,5.....99]
> n6 = random.choice(range(0,100,2)) #获取0~99之间的任意一个偶数随机数,等价于[0,2,4,6....98]
> 
> # 问题一：只省略start
> print(list(range(101,2)))   # []，原因：101被识别为start,2被识别为end,省略了step,等价于range(101,2,1)
> # print(random.choice(range(101,2)))  # 相当于要从一个空容器中取出一个数据，报错out of range
> 
> # 问题二：从start~end递增，则步长为正数，从start~end递减，则步长为负数
> print(list(range(1,101,2)))
> print(list(range(100,-1,-2)))   # 100~0
> 
> # 4.应用二
> # 模拟彩票中奖
> import random
> # random_num = random.randint(1,99)
> random_num = random.choice(range(1,100))
> print(random_num)
> input_num = int(input('请输入一个1~99之间的数字：'))
> if input_num == random_num:
>     print('恭喜你，中奖了！')
> else:
>     print('很遗憾，可以期待下次~~~~~')
> ```

##### 2.3if多分支

> 语法：
>
> ```python
> if 条件1：
> 	语句1
> elif 条件2：
> 	语句2
> elif 条件3：
> 	语句3
> ….
> elif 条件n：
> 	语句n
> else：
> 	语句m
>     
> else if  ---->elif
> ```
>
> 说明：当程序执行到if-elif语句时，首先计算条件1的值，如果条件1的值为真，那么执行语句1，执行完语句1则直接跳出整个if-elif语句，代码继续向下执行；
>
> ```Python
> """
> 注意：
>     a.如果需要操作的情况在3种及3种以上，则使用if多分支
>     b.if-elif...-else实现的是多选一的操作
>     c.不管多分支中有多少个条件成立，都只会执行其中的一个分支,哪个分支在最前面则执行哪个分支
>     d.else分支可以省略，但是，一般情况下，如果if和elif对应的所有的条件都不满足，则会执行else分支
>     e.if和elif的后面都需要添加条件，else的后面一定不要添加条件
> """
> ```

> ```Python
> # 1.基本语法
> # a.不加else
> # day = input('请输入一个表示星期的数字：')
> # if day == '1':
> #     print('星期一')
> # elif day == '2':
> #     print('星期二')
> # elif day == '3':
> #     print('星期三')
> # elif day == '4':
> #     print('星期四')
> # elif day == '5':
> #     print('星期五')
> # elif day == '6':
> #     print('星期六')
> # elif day == '7':
> #     print('星期日')
> 
> # b.加else
> # 注意1：在多分支中，else的作用:当if和elif后面的条件全都不成立时，才会执行else，else的后面一定不要添加条件
> # 注意2：多分支的特点：实现了多选一的操作，哪怕有多个条件成立，都只会执行其中的一个分支
> day = input('请输入一个表示星期的数字：')
> if day == '1':
>     print('星期一')
> elif day == '1':
>     print('星期二')
> elif day == '1':
>     print('星期三')
> elif day == '1':
>     print('星期四')
> elif day == '5':
>     print('星期五')
> elif day == '6':
>     print('星期六')
> elif day == '7':
>     print('星期日')
> else:
>     print('else~~~~~')
> 
> # 2.应用
> # 从控制台输入两个数，判断两个数的大小，输出较大的数，如果相等，则输出'相等'
> num1,num2 = eval(input('输入两个数，用逗号隔开：'))
> if num1 > num2:
>     print(num1)
> elif num1 < num2:
>     print(num2)
> else:
>     print('相等')
> ```

> 三者的区别
>
> 【面试题】if语句的单分支，双分支和多分支的区别
> 单分支：只能处理一种情况，特点：要么执行，要么不执行
> 双分支：处理两种情况，特点：实现二选一的操作
> 多分支：处理3种及3种以上的情况，特点：实现多选一的操作

##### 2.4练习

> ```Python
> # 1.从控制台输入一个数，判断该数是否是偶数，且是3的倍数
> # num = int(input('请输入一个数：'))
> # if num % 2 == 0 and num % 3 == 0:
> #     print(f"{num}是偶数，同时是3的倍数")
> # else:
> #     print('不符合')
> 
> # 2.模拟猜拳游戏
> import random
> player = int(input('请输入(0)剪刀，(1)石头，(2)布：'))
> print('玩家出的是:',player)
> computer = random.randint(0,2)   # random.choice(range(3))
> print('电脑出的是:',computer)
> if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
>     print('玩家胜利！')
> elif player == computer:
>     print('平局')
> else:
>     print('玩家失败')
> ```