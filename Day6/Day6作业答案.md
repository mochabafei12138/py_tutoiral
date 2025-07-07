### 基础编程题

1. 求1-2+3-4………+97-98+99-100的结果

   ```Python
   n = 1
   total = 0
   while n <= 100:
       if n % 2 == 0:
           total -= n
       else:
           total += n
       n += 1
   print(total)
   ```

2. 求15的阶乘

   ```Python
   n = 1
   total = 1
   while n <= 15:
       total *= n
       n += 1
   print(total)
   ```

3. 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13⽶米）

   ```Python
   height = 0.08 / 1000
   count = 0
   while True:
       # 每次对折，高度变为原来的2倍
       height *= 2
       count += 1
       if height > 8848.13:
           break
   print("对折次数%d次" % (count))
   ```

4. 输出9行内容:第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789

   ```Python
   num1 = 1
   while num1 <= 10:
       num2 = 1
       while num2 <= num1:
           print(num2,end="")
           num2 += 1
       print()
       num1 += 1
   ```
   
5. 从控制台输入一个数，判断该数是否是质数

   ```Python
   num = input('请输入一个数：')
   if num.isdigit():
       num = int(num)
       if num < 2:
           print(f'{num}不是质数')
       else:
           result = True   # 不管num是不是质数，都假设它是
           for n in range(2,num):
               if num % n == 0:
                   result = False
                   # 只要得到了结果，循环就可以提前结束
                   break
           if result:
               print(f'{num}是质数')
           else:
               print(f'{num}不是质数')
   else:
       print('输入有误')
   ```

6. 统计101~200中质数的个数，并且输出所有的质数

   ```Python
   count = 0
   for num in range(101,201):
       # 假设num是一个质数
       result = True
       for n in range(2,num):
           if num % n == 0:
               # 说明假设错误，则将result重置为False
               result = False
               break
       if result:
           count += 1
           print(num)
   print("个数：",count)
   ```

### 中级编程题

1. 求1/1! + 1/2! + 1/3! + ..... 1/20!的结果

   ```Python
   total = 0   # 求和
   fac = 1     # 分母的阶乘
   for n in range(1,21):
       fac *= n
       total += 1 / fac
   print(total)
   ```

2. 编写一个程序：可以不断的输⼊数字，直到输入的数字是0时打印 over 后结束程序

   ```Python
   while True:
       num = input('请输入数字：')
       if num == '0':
           print('over')
           break
   ```
   
3. 模拟用户的登录过程，让用户输入自己的用户名和密码，如果用户名为admin，密码为abc123,则表示登录成功，允许错误三次，如果三次输入错误，则禁止登录

   ```Python
   for _ in range(3):
       username = input("请输入你的用户名：")
       pwd = input("请输入你的密码：")
       if username == 'admin' and pwd == 'abc123':
           print("登录成功！")
           break
       else:
           print("用户名或密码错误，请重新输入")
   else:
       print("输入错误三次，禁止登录")
   ```
