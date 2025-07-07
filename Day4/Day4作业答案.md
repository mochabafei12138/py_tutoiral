### 编程题

1. 判断一个数是否能同时被5和8整除

   ```python
   n1 = input("请输入一个数：")
   # 注意：xxx.isdigit(),xxx必须是全数字组成的，问题：-3434经过isdigit判断，结果是False
   if n1.isdigit():
       n1 = int(n1)
       if n1 % 5 == 0 and n1 % 8 == 0:  # 注意：能用and连接的条件都可以转换为嵌套if语句
           print(f"{n1}能同时被5和8整除")
       else:
           print(f"{n1}不能同时被5和8整除")
   else:
       print("输入有误")
   ```

2. 模拟玩骰子游戏，根据骰子点数决定什么惩罚【例如：1.跳舞，2.唱歌....】

   ```python
   import random
   a = random.randint(1,6)
   if a == 1:
       print("跳舞")
   elif a == 2:
       print("唱歌")
   elif a == 3:
       print("真心话大冒险")
   elif a == 4:
       print("喝酒")
   elif a == 5:
       print("和异性陌生人握手")
   else:
       print("随机找个人打电话")
   ```

3. 从控制台输入一个年份，判断该年是否是闰年，是闰年的条件: 能被4整除但是不能被100整除或者能够被400整除的年

   ```python
   year = int(input("请输入一个年份："))
   if (year % 4 == 0 and year % 100 != 0)  or year % 400 == 0:
       print(f"{year}是闰年")
   else:
       print(f"{year}是平年")
   ```

4. 定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常!

   公式: `体重(kg)/身高(m)的平方值` 在18.5 ~ 24.9之间属于正常。

   ```python
   weight = float(input("请输入你的体重："))
   height = float(input("请输入你的身高："))
   standard = weight / height ** 2
   if 18.5 <= standard <= 24.9:
       print("指标正常")
   else:
       print("注意多锻炼身体啊")
   ```

5. x 为 0-99 取一个数,y 为 0-199 取一个数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y

   ```python
   import random
   x = random.choice(range(99))
   y = random.choice(range(199))
   if x > y:
       print(x)
   elif x == y:
       print(x + y)
   else:
       print(y)
   ```

6. 从控制台输入三个数，输出较大的值

   ```python
   # 思路：假设法：假设其中一个数为最大值，然后相互比较，推翻假设
   num1 = int(input("first:"))
   num2 = int(input("second:"))
   num3 = int(input("third:"))
   # 假设num1为最大值
   max_value = num1
   if num2 > num1:
       max_value = num2
   if num3 > max_value:
       max_value = num3
   print(f"num1,num2和num3的最大值为:{max_value}")
   ```

7. 从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”，例如：153 = 1的三次方 + 5的三次方 + 3的三次方，则153是水仙花数

   ```python
   num = int(input("请输入一个三位数："))
   bw = num // 100
   sw = num % 100 // 10
   gw = num % 10
   total = bw ** 3 + sw ** 3 + gw ** 3
   if num == total:
       print(f"{num}是一个水仙花数")
   else:
       print(f"{num}不是一个水仙花数")
   ```

8. 从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”，例如：11111   12321   12221

   ```python
   a = int(input("请输入一个五位数\n"))
   if a<9999 or a >100000 :
       print ("不符合要求")
   else:
       w = a // 10000
       q = (a - w * 10000) // 1000
       b = (a - w * 10000 - q * 1000) // 100
       s = (a - w * 10000- q * 1000 - b * 100) // 10
       g = a % 10

       if w == g and q == s :
           print(a,"是回文数")
       else:
          print(a,"不是回文数")
   ```
