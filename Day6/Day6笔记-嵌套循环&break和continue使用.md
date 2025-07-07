### Day5作业讲解

> ```Python
> # 2.统计1到100之间可以被7整除的数的个数
> # 问题一：书写while语句的过程中，非常容易书写死循环
> # 错误写法
> # n = 1
> # count = 0
> # while n <= 100:
> #     if n % 7 == 0:
> #         count += 1
> #         n += 1   # 将递增的语法写在了if语句中
> # 正确写法
> n = 1
> count = 0
> while n <= 100:
>     if n % 7 == 0:
>         count += 1
>     n += 1
> print(count)
> 
> # 问题二:将for和while语法混淆了
> # n = 1
> count = 0
> for n in range(1,101):
>     if n % 7 == 0:
>         count += 1
>     # n += 1
> print(count)
> 
> # 问题三：求整除或者倍数的情况下，注意一个数的最小倍数是它本身
> count = 0
> for n in range(0,101,7):   # 改正：range(7,101,7)
>     count += 1
> print(count)
> 
> # 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
> count = 0
> for n in range(1,100):
>     # if (n % 7 == 0 or n % 3 == 0) and not (n % 7 == 0 and n % 3 == 0):
>     # if (n % 7 == 0 or n % 3 == 0) and (n % 21 != 0):
>     if (n % 7 == 0 and n % 3 != 0) or (n % 7 != 0 and n % 3 == 0):
>         count += 1
> print(count)
> 
> # 问题：重复计数了
> count = 0
> for n in range(1,100):
>     if n % 3 == 0:
>         count += 1
>     if n % 7 == 0:
>         count += 1
>     if n % 21 == 0:
>         count += 1
> print(count)
> 
> # 6.计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
> total = 0   # 说明：不建议sum表示变量名，系统中有个功能sum()
> for n in range(1,1000):
>     if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
>         total += n
> print(total)
> 
> total = 0
> for n in range(1,1000):
>     if n % (3 * 5 * 7) == 0:
>         total += n
> print(total)
> 
> # 1. 输入任意一个正整数，求他是几位数？注意: 不能使用字符串，只能用循环
> # 思路：对10进行整除运算，结果为0停止计算
> # 如：673：673 // 10---》67  67 // 10---》6 6 // 10 ----》0
> # num1 = input('请输入一个正整数：')
> # if num1.isdigit():
> #     num = int(num1)
> #     count = 1
> #     while num // 10 != 0:   # 判断
> #         count += 1
> #         num //= 10    # 重新赋值
> #     print(f'{num1}是{count}位数')
> # else:
> #     print('输入有误')
> 
> # 2. 3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？不考虑小数
> l = 3000
> day = 0
> while l >= 5:
>     day += 1
>     l /= 2
> print(day)
> 
> # 3. 打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字⽴方和等于该数本身。例如:153是 ⼀个⽔仙花数,因为  1³ + 5³ + 3³ 等于 153
> # 方式一
> for num in range(100,1000):
>     gw = num % 10
>     sw = num // 10 % 10
>     bw = num // 100
>     if num == gw ** 3 + bw ** 3 + sw ** 3:
>         print(num)
> 
> # 方式二
> for num in range(100,1000):
>     num = str(num)
>     bw = int(num[0])
>     sw = int(num[1])
>     gw = int(num[2])
>     if int(num) == gw ** 3 + bw ** 3 + sw ** 3:
>         print(num)
> ```

### 一、循环【重点掌握】

#### 1.嵌套循环&九九乘法表

> 类似于嵌套if语句 
>
> 语法：
>
> ```
> while 表达式1：
> 	while 表达式2：
> 		语句
> 		
> for 变量1 in 容器1:
> 	for 变量2 in  容器2：
> 		语句
> 		
> while 表达式1：
>     for 变量1 in 容器1:
>     	语句
>     	
> for 变量1 in 容器1:
> 	while 表达式1：
> 		语句
> ```

> ```Python
> # 应用：打印九九乘法表
> """
> 1*1=1
> 1*2=2 2*2=4
> 1*3=3 2*3=6 3*3=9
> 1*4=4 2*4=8 3*4=12 4*4=16
> ......
> 
> 1*9=9 2*9=18 3*9=27  ......     7*9=63 8*9=72 9*9=81
> 
> 规律：
>     a.行数的取值范围：1~9
>     b.每一行中列数的取值范围：1~当前行数
>     c.格式：列*行=乘积
> """
> ```

> ```Python
> # 1.基本语法
> # a
> n = 0
> while n < 5:
>     print(n)
>     n += 1
> m = 0
> while m < 3:
>     print(m)
>     m += 1
> 
> print('*' * 30)
> 
> # b
> # 注意：在代码执行的过程中，但凡遇到循环语句，都是先把当前循环执行完毕，然后代码才会向下执行
> n = 0
> while n < 5:
>     m = 0        # 外层循环每次执行进来，m都会被重置为0
>     while m < 3:
>         print(n,m)
>         m += 1
>     n += 1
> # 15
> 
> print('*' * 30)
> 
> for n in range(5):
>     for m in range(3):
>         print(n,m)
> 
> print('*' * 30)
> 
> # 思考：m = 0定义在外层循环的外面，将不会再被重置
> n = 0
> m = 0
> while n < 5:
>     while m < 3:
>         print(n,m)
>         m += 1
>     n += 1
> 
> # 2.打印九九乘法表
> # 应用：打印九九乘法表
> """
> 1*1=1
> 1*2=2 2*2=4
> 1*3=3 2*3=6 3*3=9
> 1*4=4 2*4=8 3*4=12 4*4=16
> ......
> 
> 1*9=9 2*9=18 3*9=27  ......     7*9=63 8*9=72 9*9=81
> 
> 规律：
>     a.行数的取值范围：1~9
>     b.每一行中列数的取值范围：1~当前行数
>     c.格式：列*行=乘积
> """
> # 外层循环：控制行数
> row = 1
> while row <= 9:
>     # 内层循环：控制每一行的列
>     col = 1
>     while col <= row:
>         print(f'{col}*{row}={col * row}',end=' ')
>         col += 1
>     row += 1
>     # 换行
>     print()
> 
> for row in range(1,10):
>     for col in range(1,row + 1):
>         print(f'{col}*{row}={col * row}', end=' ')
>     # 换行
>     print()
> ```

#### 2.break和continue

> 【面试题】break和continue的区别
> break:打断，表示结束当前循环【break书写在哪个循环中，就结束哪个循环，就近原则】
> continue:继续，表示结束当前循环的本次循环，继续下一次循环
>
> ```Python
> # 1.pass
> # pass:通过，也是一个关键字，没有实际意义，但是可以用来完善程序的结构，常用于代码块中
> # 说明：Python中所有的代码块想要结构完整，则必须至少书写一条语句，或者用pass暂时占位
> # 注意：一般用于if  while for 函数 类 等代码块中都可以使用pass暂时占位
> if 1:
>     pass
> else:
>     print('no')
> 
> for n in range(10):
>     pass
> print('over')
> 
> 
> # 注意：break和continue使用的前提是循环语句
> # 2.break
> # a.
> '''
> 注意：
>     a.break单独作为一条语句使用
>     b.如果break应用在单层循环【while和for】中，在满足条件的情况下，表示结束循环，哪怕该循环还有无数次没有执行
>     c.如果break应用在内层循环中，在满足条件的情况下，结束的是当前循环【就近原则】
> '''
> n = 0
> while n < 10:
>     print(n)
>     if n == 3:   # 充当条件
>         break
>     n += 1
> 
> print('*' * 50)
> 
> # b.
> n = 0
> while n < 5:
>     m = 0
>     while m < 3:
>         print(n,m)
>         if n == 3:
>             break
>         m += 1
>     n += 1
> 
> print('*' * 50)
> 
> n = 0
> while n < 5:
>     m = 0
>     while m < 3:
>         print(n, m)
>         if m == 1:
>             break
>         m += 1
>     n += 1
> 
> print('*' * 50)
> 
> # 3.continue
> # 死循环
> # n = 0
> # while n < 10:
> #     print(n)
> #     if n == 3:
> #         continue
> #     n += 1
> #     print('over~~~~~~')
> 
> # 使用场景：只有某次循环未被执行完，其他次循环正常执行
> n = 0
> while n < 10:
>     if n == 3:
>         n += 1
>         continue
>     print(n)
>     n += 1
>     print('over~~~~~~')
> ```

#### 3.循环综合练习

> ```python
> # 2.猜数字游戏
> '''
> 从控制台输入一个数，和程序产生的随机数进行比较
> 控制台输入的数  > 随机数 ，提示：你猜大了，往小了猜
> 控制台输入的数  < 随机数 ，提示：你猜小了，往大了猜
> 控制台输入的数  == 随机数 ，提示：恭喜你，猜对了
> 如果猜对，则游戏结束
> '''
> import  random
> '''
> 注意：
>     如果不确定循环的次数，则使用while,常用死循环while True结合break使用
>     如果确定循环的次数，则使用for【range()】,常用for
> '''
> random_num = random.randint(1,100)
> print(random_num)
> guess_count = 0
> while True:
>     input_num = input('请输入一个1~100之间的整数：')
>     if input_num.isdigit():
>         input_num = int(input_num)
>         if input_num in range(1,101):  # 成员运算符
>             guess_count += 1
>             if input_num > random_num:
>                 print('你猜大了，往小了猜')
>             elif input_num < random_num:
>                 print("猜小了，往大了猜")
>             else:
>                 print('恭喜你，猜对了')
>                 # 如果猜对，则游戏结束,使用break打断死循环
>                 break
>         else:
>             print('范围有误')
>     else:
>         print('输入有误')
> 
> print(f'总共猜了{guess_count}次')
> if guess_count > 7:
>     print('智商有点捉急啊，怪不得彩票中不了奖')
> ```