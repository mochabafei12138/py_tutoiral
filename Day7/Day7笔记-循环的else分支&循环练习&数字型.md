### 一、循环语句

#### 1.循环的else分支

> ```Python
> 语法：
> while  xxx:
>     xxx
> else:
>     xxx
> 
> for 变量 in 容器：
>     xxx
> else:
>     xxx
> 
> for 变量 in 容器：
>     if xxx:
>         xxx
>     else：
>         xxx
> else:
>     xxx
> ```
>
> 注意：如果while或for中的break执行了，则循环的else分支不会被执行；如果while或for中的break未被执行，则循环的else分支会被执行
>
> ```Python
> # 注意：Python中的循环语句也是有else分支的，不光if语句中有else分支
> 
> 
> # 1.for-else/while-else
> # a.当if的条件按不成立时，才会执行else分支
> n = 7
> if n < 5:
>     print('yes')
> else:
>     print('no')
> 
> # b.无论while或for循环的分支是否执行，一般情况下else分支都会执行
> n = 0
> while n > 10:
>     print(n)
>     n += 1
> else:
>     print('while~~~~else')
> 
> for n in range(10):
>     print('~~~~~~',n)
> else:
>     print('for~~~else')
> 
> print('*' * 50)
> 
> # c.for/while【break】-----else
> # 注意：如果在while或for中出现break且break会被执行，则循环的else分支不会被执行，反之，如果break不会被执行，则else分支会被执行
> n = 0
> while n < 10:
>     print(n)
>     if n == 2:
>         break
>     n += 1
> else:
>     print('while~~~~else')
> 
> for n in range(10):
>     print('~~~~~~',n)
>     if n > 20:
>         break
> else:
>     print('for~~~else')
> ```

#### 2.循环练习&Day6作业讲解

> ```Python
> '''
> while:不确定次数
> for:确定次数/确定范围
> '''
> 
> # 1. 求1-2+3-4………+97-98+99-100的结果
> # 方式一
> r11 = 0
> for n in range(1,101):
>     if n % 2 == 1:
>         r11 += n
>     else:
>         r11 -= n
> print(r11)
> 
> # 方式二
> r21 = 0
> for n1 in range(1,101,2):
>     r21 += n1
> r22 = 0
> for n2 in range(2,101,2):
>     r22 += n2
> print(r21 - r22)
> 
> # 方式三
> r31 = 0
> for n3 in range(1,101):
>     if n3 % 2 == 0:
>         n3 = -n3
>     r31 += n3
> print(r31)
> 
> # 2. 求15的阶乘
> # 注意：乘法：1  求和：0
> r21 = 1
> for n in range(1,16):
>     r21 *= n
> print(r21)
> 
> # 3. 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13⽶）
> # 注意：不确定循环次数的情况下，建议使用while死循环+break
> paper = 0.08 / 1000
> count = 0
> while True:
>     count += 1   # 计数
>     # 每次对折，高度变成原来的2倍
>     paper *= 2
>     if paper >= 8848.13:
>         break
> print(count)
> 
> 
> # 4. 输出9行内容:第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
> '''
> 1
> 12
> 123
> 1234
> ....
> 123456789
> '''
> # 外层循环：控制行
> for row in range(1,10):
>     # 内层循环：控制每一行的列
>     for col in range(1,row + 1):
>         print(col,end='')
>     print()
> 
> # 扩展：
> '''
> *
> **
> ***
> ****
> *****
> '''
> # 方式一
> for row in range(1,6):
>     for col in range(1,row + 1):
>         print('*',end='')
>     print()
> 
> # 方式二
> for row in range(1,6):
>     print('*' * row)   # 字符串  *  数字：表示将指定字符串重复指定次数，形成一个新的字符串
> 
> # 5. 从控制台输入一个数，判断该数是否是质数
> # 质数：只能被1和它本身整除的数，最小的质数是2
> # 方式一：计数法
> # num = input('请输入一个数：')
> # if num.isdigit():  # 非负数
> #     num = int(num)
> #     if num < 2:
> #         print(f'{num}不是质数')
> #     else:
> #         count = 0
> #         # 10----->在2~9之间查找，是否有其他的数可以整除10
> #         # 67----->在2~66之间查找，是否有其他的数可以整除67
> #         for n in range(2,num):
> #             if num % n == 0:
> #                 count += 1
> #         # if count:
> #         #     print(f'{num}不是质数',count)
> #         # else:
> #         #     print(f'{num}是质数',count)
> #
> #         if count == 0:
> #             print(f'{num}是质数',count)
> #         else:
> #             print(f'{num}不是质数',count)
> # else:
> #     print('输入有误')
> 
> # 方式二：假设法
> # num = input('请输入一个数：')
> # if num.isdigit():
> #     num = int(num)
> #     if num < 2:
> #         print(f'{num}不是质数')
> #     else:
> #         result = True   # 不管num是不是质数，都假设它是
> #         for n in range(2,num):
> #             if num % n == 0:
> #                 result = False
> #                 # 只要得到了结果，循环就可以提前结束
> #                 break
> #         if result:
> #             print(f'{num}是质数')
> #         else:
> #             print(f'{num}不是质数')
> # else:
> #     print('输入有误')
> 
> # 方式三：for【break】-else
> # num = input('请输入一个数：')
> # if num.isdigit():
> #     num = int(num)
> #     if num < 2:
> #         print(f'{num}不是质数')
> #     else:
> #         for n in range(2,num):
> #             if num % n == 0:
> #                 print(f'{num}不是质数')
> #                 break
> #         else:
> #             print(f'{num}是质数')
> # else:
> #     print('输入有误')
> 
> # 6. 统计101~200中质数的个数，并且输出所有的质数
> count = 0
> # 获取数字
> for num in range(101,201):
>     # 判断num是否是质数
>     count1 = 0
>     for n in range(2,num):
>         if num % n == 0:
>             count1 += 1
>     if count1 == 0:
>         print(num)
>         count += 1
> print(count)
> 
> count = 0
> for num in range(101,201):
>     result = True
>     for n in range(2,num):
>         if num % n == 0:
>             result = False
>             break
>     if result:
>         print(num)
>         count += 1
> print(count)
> 
> count = 0
> for num in range(101,201):
>     for n in range(2, num):
>         if num % n == 0:
>             break
>     else:
>         print(num)
>         count += 1
> print(count)
> 
> # 1. 求1/1! + 1/2! + 1/3! + ..... 1/20!的结果
> '''
> 1/1! + 1/2! + 1/3! + ..... 1/20!
> 1/1 + 1/1*2 + 1/1*2*3 + ..... 1/1*2*3*4....*20
> '''
> # 方式一
> total = 0
> for num in range(1,21):
>     # 求分母的阶乘
>     fac = 1
>     for n in range(1, num + 1):
>         fac *= n
>     # 求和
>     total += 1 / fac
> print(total)
> 
> # 方式二
> fac = 1
> total = 0
> for num in range(1,21):
>     fac *= num   # 利用num的递增，求分母的乘法记录下来
>     total += 1 / fac
> print(total)
> 
> # 2. 编写一个程序：可以不断的输⼊数字，直到输入的数字是0时打印 over 后结束程序
> # while True:
> #     num = input('请输入数字：')
> #     if num == '0':
> #         print('over')
> #         break
> 
> # 3. 模拟用户的登录过程，让用户输入自己的用户名和密码，
> # 如果用户名为admin，密码为abc123,则表示登录成功，允许错误三次，如果三次输入错误，则禁止登录
> # 方式一：for
> # for i in range(3):
> #     username = input('请输入用户名：')
> #     password = input('请输入密码：')
> #     if username == 'admin' and password == 'abc123':
> #         print('登录成功！')
> #         break
> #     else:
> #         if i == 2:
> #             continue
> #         print('用户名或密码输入有误，请重新输入')
> # else:
> #     print('已经错误3次，禁止输入')
> 
> # 方式二：while
> n = 0
> while n <= 2:
>     username = input('请输入用户名：')
>     password = input('请输入密码：')
>     if username == 'admin' and password == 'abc123':
>         print('登录成功！')
>         break
>     else:
>         n += 1
>         if n == 3:
>             continue
>         print('用户名或密码输入有误，请重新输入')
> else:
>     print('已经错误3次，禁止输入')
> ```

### 二、数字类型

#### 1.数学功能【了解】

> 内置功能
>
> - abs(x):返回数字的绝对值
> - (x>y)-(x<y):比较大小，如：x=3,y=5
> - max(x1,x2,…):返回给定参数的最大值
> - min(x1,x2,…):返回给定参数的最小值
> - pow(x,y):求x的y次方的值
> - round(x,n):返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
> - sum(容器)：求容器中元素的和
>
> 导入math模块  import math;
>
> - ceil(x):返回x的上入整数，不能直接访问，需要通过math访问，即math.ceil(18.1)	
> - floor(x):返回x的下入整数，同ceil的用法
> - modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，同ceil的用法
> - sqrt(x):返回数字x的平方根，数字可以为负数，返回类型为实数【浮点型】，同ceil的用法
>
> 数学常量
>
>   math.pi ：圆周率
>   math.e ：自然常数
>
> ```Python
> # 1.
> # - abs(x):返回数字的绝对值
> print(abs(-34))
> # - max(x1,x2,…):返回给定参数的最大值     *****
> print(max(354,7,8,9,9,23,239))
> # - min(x1,x2,…):返回给定参数的最小值     *****
> print(min(354,7,8,9,9,23,239))
> # - pow(x,y):求x的y次方的值
> print(pow(5,3))  # 5 ** 3           ******
> # - round(x,n):返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
> print(round(35.6354))  # 36
> print(round(35.4354))  # 35
> print(round(35.6354))  # 36
> print(round(35.4354,2))  # 35.44
> 
> # - sum(容器)：求容器中元素的和        ******
> print(sum([45,67,78,8]))
> print(sum(range(1,101)))
> 
> # 2.导入math模块
> import  math     # 注意：自己创建py文件的时候，千万不要和系统的模块重名，如：math.py,random.py,会导致系统的模块失效
> # - ceil(x):返回x的上入整数，不能直接访问，需要通过math访问，即math.ceil(18.1),向上取整        ******
> print(math.ceil(19.98475))   # 20
> print(math.ceil(19.18475))   # 20
> 
> # - floor(x):返回x的下入整数，同ceil的用法，向下取整     ******
> print(math.floor(19.98475))   # 19
> print(math.floor(19.18475))   # 19
> 
> # - modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，同ceil的用法
> print(math.modf(45.6778))
> 
> # - sqrt(x):返回数字x的平方根，数字可以为负数，返回类型为实数【浮点型】，同ceil的用法
> print(math.sqrt(9))   # 3.0
> print(9 ** 0.5)   # 3.0
> ```

