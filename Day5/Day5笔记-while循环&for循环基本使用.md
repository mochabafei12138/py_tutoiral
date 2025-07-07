### Day4作业讲解

> ```Python
> # 4.从控制台输入一个年份，判断该年是否是闰年，是闰年的条件: 能被4整除但是不能被100整除或者能够被400整除的年
> # year = int(input('请输入一个年份：'))
> # if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0):
> #     print(f"{year}是闰年")
> # else:
> #     print(f'{year}是平年')
> 
> # 7.从控制台输入三个数，输出最大的值
> # 常规：分情况讨论
> # 简化思维：假设法【非常好用】
> # num1,num2,num3 = eval(input('请输入三个数，用逗号隔开:'))
> # max_value = num1   # 假设num1为最大值
> # if num2 > num1:
> #     max_value = num2   # 推翻假设，给max_value重新赋值
> # if num3 > max_value:
> #     max_value = num3
> # print(max_value)
> 
> # 8.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”，
> # 例如：153 = 1的三次方 + 5的三次方 + 3的三次方，则153是水仙花数
> # 方式一
> # num = int(input('请输入一个三位数：'))
> # gw = num % 10
> # sw = num // 10 % 10
> # bw = num // 100
> # if num == gw ** 3 + bw ** 3 + sw ** 3:
> #     print(f'{num}是水仙花数')
> # else:
> #     print(f'{num}不是水仙花数')
> 
> # 方式二
> # num = input('请输入一个三位数：')   # str
> # bw = int(num[0])    # str---->int
> # sw = int(num[1])
> # gw = int(num[2])
> # if int(num) == gw ** 3 + bw ** 3 + sw ** 3:
> #     print(f'{num}是水仙花数')
> # else:
> #     print(f'{num}不是水仙花数')
> 
> 
> # 9.回文数【五位数】：对称的数,如12421  45754
> # 方式一和方式二:上述和水仙花数的两种方式都可以实现
> # 方式三：
> num = input('请输入一个五位数：')
> # 扩展：name,name[::-1]表示将name做了逆序/反转/翻转
> # print(num)   # abcd
> # print(num[::-1])  # dcba
> if num == num[::-1]:
>     print(f'{num}是回文数')
> else:
>     print(f'{num}不是回文数')
> ```

### 一、if语句

#### 1.嵌套if语句

> 语法：
>
> ```
> if 条件1：
> 	语句1
> 	if 条件2：
> 		语句2
> ```
>
> 说明：当表达式1和表达式2的值都为真时，才会执行语句2
>
> 注意：单分支，双分支和多分支两两之间可以互相嵌套
>
> ```Python
> # 1.基本语法
> # 需求：从控制台输入一个数，判断一个数是否能同时被5和8整除
> # num = int(input('请输入一个数：'))
> # if num % 5 == 0 and num % 8 == 0:   # and实现的语句可以使用嵌套if语句等价转换
> #     print(f'{num}能被5和8同时整除')
> #
> # if num % 5 == 0:
> #     print(f'{num}能被5整除')
> #     if num % 8 == 0:
> #         print(f'{num}能被5和8同时整除')
> #
> # if num % 5 == 0:
> #     print(f'{num}能被5整除')
> #     if num % 8 == 0:
> #         print(f'{num}能被5和8同时整除')
> # else:
> #     print(f'{num}不能被5整除')
> #
> # if num % 5 == 0:
> #     print(f'{num}能被5整除')
> #     if num % 8 == 0:
> #         print(f'{num}能被5和8同时整除')
> #     else:
> #         print(f'{num}不能被5和8同时整除')
> # else:
> #     print(f'{num}不能被5整除')
> 
> '''
> 注意：
>     a.单分支，双分支和多分支两两之间可以互相嵌套
>     b.嵌套的过程中，一定不要注意缩进问题
>     c.理论上来说，嵌套的层数没有限制，但是，为了代码的可读性和后期的可维护性，建议嵌套的层数最多三层
> '''
> 
> # 2.扩展：实际应用
> num = input('请输入一个三位数：')
> '''
> x.isdigit():判断字符串x是否非空且全部由数字组成，如果是，则结果为True,如果不是，结果为False
> len(x):获取列表，元组或集合中元素的个数
>        获取字符串的长度  或者  获取字符串中字符的个数
> '''
> if num.isdigit():
>     if len(num) == 3:
>         num = int(num)
>         gw = num % 10
>         sw = num // 10 % 10
>         bw = num // 100
>         if num == gw ** 3 + bw ** 3 + sw ** 3:
>             print(f'{num}是水仙花数')
>         else:
>             print(f'{num}不是水仙花数')
>     else:
>         print(f'{num}不是一个三位数')
> else:
>     print('输入有误')
> ```

#### 2.三目运算符/三元运算符

> Python中本身没有三目运算符，我们可以通过if-else模拟三目运算符
> 优点：实现二选一的操作，可以简化if-else语句
> 缺点：三目运算符只有一行代码，所以只能实现简单的逻辑
>
> ```Python
> # 语法：r = a if 条件  else  b
> # 工作原理：如果条件成立，则r的结果是a,如果条件不成立，则r的结果是b
> 
> # 1.
> num = int(input('请输入一个数：'))
> if num % 2 == 0:
>     print('偶数')
> else:
>     print('奇数')
> 
> r = ''
> if num % 2 == 0:
>     r = '偶数'
> else:
>     r = '奇数'
> print(r)
> 
> r = '偶数' if num % 2 == 0 else '奇数'
> print(r)
> r = True if num % 2 == 0 else False
> print(r)
> 
> # 2.
> year = int(input('请输入一个年份：'))
> if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0):
>     print(f"{year}是闰年")
> else:
>     print(f'{year}是平年')
> 
> r1 = '闰年' if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) else '平年'
> print(r1)
> r1 = True if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) else False
> print(r1)
> ```

### 二、循环语句【重点掌握】

#### 1.概念

> 在生活中，循环指的是一个现象周期性或者重复性的出现
>
> ![循环情景](Day5-images/循环情景.png)
>
> 在编程中，在满足条件的情况下，反复执行某一段代码，在编程语言中出现的这种现象被称为循环，这段被重复执行的代码被称为循环体
>
> ![循环语句](Day5-images/循环语句.JPG)
>
> Python中提供的循环语句有：while语句和for语句

#### 2.while基本语法

> 语法：
>
> ```
> while 条件：
> 	循环体
> if  条件:
> 	语句
> ```
>
> 说明：当程序在从上往下执行的过程中，遇到while语句时，首先判断条件的值，如果表达式的值为假，则跳过整个while语句，程序继续向下执行；如果表达式的值为真，则执行对应的语句；执行完语句，再去计算表达式的值，如果表达式的值为假，则跳过整个while语句，程序继续向下执行；如果表达式的值为真，则执行对应的语句。。。如此循环往复，直到表达式的值为假，整个循环才停止
>
> ```Python
> """
> 总结：
>     a.while中的条件和if中的条件的使用完全相同，都可以是常量，变量或表达式
>     b.在条件成立的前提下，if中的语句只会执行一次，但是，while中的语句【循环体】会执行若干次
>     c.在大多数情况下，书写循环需要考虑的核心问题：控制循环的次数
>       让循环可以在合适的时机停止下来，否则形成死循环
> """
> ```

> ```Python
> # 1.基本语法
> # a.死循环
> # while 1:
> #     print('aaaaa~~~~~')
> # while True:
> #     print('aaaaa~~~~~')
> 
> # b.需求：输出10次hello world
> # 循环的目的是为了简化代码，让某一段代码只书写一次，但是可以多次执行
> # 注意：一般可以借助给一个变量重新赋值，让循环在某个合适的时机停止下来
> # 初始化表达式
> n = 0  #  0~9---->10个数----》10次
> # 条件表达式
> while n < 10:  # n <= 9
>     # 循环体
>     print('hello world')
>     # 循环之后的操作表达式
>     # 让n变化起来，递增
>     n += 1
> 
> print('over~~~~~~')
> 
> m = 9
> while m >= 0:
>     print('hello world')
>     m -= 1
> 
> '''
> 注意：
>     a.根据需求，一般情况下，如果规定了次数，一定注意避免书写死循环【n += 1】
>     b.死循环一般结合break使用
>     c.对于循环，一定要搞清楚代码执行的顺序
>       debug:打断点----》右键----》Debug-----》分步执行代码，查看代码执行的顺序
> '''
> ```

#### 3.for基本语法

> 语法：	
>
> ```
> for 变量名 in 容器：
> 	循环体
> ```
>
> 功能：for循环主要用于遍历任何容器，比如列表，字符串，元组，字典和集合等
>
> 遍历：指的是依次访问序列中的每一个元素，获取每个元素值
>
> 说明：按照顺序获取容器中的每个数据，赋值给变量名，再执行循环体，如此循环往复，直到取完容器中所有的数据为止
>
> ```Python
> """
> 注意：
>     1.for循环主要用于遍历任何容器，比如列表，字符串，元组，字典和集合，range()等
>     2.按照顺序获取序列中的每个元素，赋值给变量名，再执行循环体，如此循环往复，直到取完序列中所有的元素为止
>     3.for循环的执行次数由：容器中数据的个数  或者  容器的长度
> """
> ```

> ```Python
> # 1.遍历容器
> s = 'fagag'
> for m in s:
>     print(m)
>     print(chr(ord(m) - 32))
> 
> lst = [34,5,67,8]
> for n in lst:
>     print(n + 10)
> 
> """
> 总结：for循环的执行次数由：容器中数据的个数  或者  容器的长度  决定
> """
> 
> # 问题：输出10次hello world
> # 2.注意1：如果for循环仅仅是为了控制次数，而定义的变量在循环体中未被使用，则可以使用下划线代替变量名
> for n in '0987654123':
>     print('hello wolrd')
> 
> for _ in '0987654123':
>     print('hello wolrd')
> 
> # 注意2：range(start,end,step):根据指定的区间和指定的步长生成一个容器，前闭后开区间
> for n in range(10):  # 0-9
>     print('hello wolrd',n)
> 
> for n in range(100):  # 0-99
>     print('hello wolrd',n)
> 
> for n in range(0,100,2):  # 0-99之间的偶数
>     print('hello wolrd',n)
> 
> for n in range(1,100,2):  # 1-99之间的奇数
>     print('hello wolrd',n)
> 
> # 3.注意区分while语句和for语句
> n = 0    # start
> while n < 10:   # end
>     print(n)
>     n += 1   # step
> 
> for n in range(0,10,1):
>     print(n)
>     # n += 1  # 初学者容易和while语句混淆
> ```

#### 4.while和for使用练习

> ```python
> # 1.求1~100之间所有整数的和
> n = 1
> total = 0
> while n <= 100:
>     # print(n)
>     total += n     # 求和
>     n += 1
> print(total)
> 
> total = 0
> for n in range(1,101):
>     total += n
> print(total)
> 
> # 2.统计1~100之间3的倍数的个数
> n = 1
> count = 0
> while n <= 100:
>     if n % 3 == 0:
>         count += 1    # 计数
>     n += 1
> print(count)
> 
> count = 0
> for n in range(1,101):
>     if n % 3 == 0:
>         count += 1
> print(count)
> 
> n = 3
> count = 0
> while n <= 100:
>     count += 1
>     n += 3
> print(count)
> 
> count = 0
> for n in range(3,101,3):
>     count += 1
> print(count)
> ```
