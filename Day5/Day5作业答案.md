### 基础编程题

1. 计算从1到1000以内所有奇数的和并输出

   ```python
   sum1 = 0
   num1 = 1
   while num1 <= 1000:
       if num1 % 2 != 0:
           sum1 += num1
       num1 += 1
   print(sum1)
   ```

2. 统计1到100之间可以被7整除的数的个数

   ```python
   count2 = 0
   num2 = 1
   while num2 <= 100:
       if num2 % 7 == 0:
           count2 += 1
       num2 += 1
   print(count2)
   ```

3. 计算从1到100以内所有奇数的和

   ```python
   sum3 = 0
   num3 = 1
   while num3 <= 100:
       if num3 % 2 != 0:
           sum3 += num3
       num3 += 1
   ```

4. 计算从1到100以内所有能被3或者17整除的数的和并输出

   ```python
   num4 = 1
   sum4 = 0
   while num4 <= 100:
       if num4 % 3 == 0 or num4 % 17 == 0:
           sum4 += num4
       num4 += 1 
   print(sum4)
   ```

5. 计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数

   ```python
   num5 = 1
   count5 = 0
   while num5 <= 100:
       #if (num5 % 3 == 0 or num5 % 7 == 0) and not(num5 % 3 == 0 and num5 % 7 == 0):
       if (num5 % 3 == 0 or num5 % 7 == 0) and num5 % 21 != 0:
           count5 += 1
       num5 += 1
   ```

6. 计算1到500以内能被7整除但不是偶数的数的个数

   ```python
   num6 = 1
   count6 = 0
   while num6 <= 500:
       if num6 % 7 == 0 and num6 % 2 != 0:
           count6 += 1
       num6 += 1
   ```

7. 计算从1到1000以内所有能同时被3，5和7整除的数的和并输出

   ```python
   num7 = 1
   sum7 = 0
   while num7 <= 1000:
       if num7 % 3 == 0 and num7 % 5 == 0 and num7 % 7 == 0:
           sum7 += num7
       num7 += 1
   ```

8. 统计100以内个位数是2并且能够被3整除的数的个数

   ```python
   count8 = 0
   num8 = 0
   while num8 < 100:
       if num8 % 10 == 2 and num8 % 3 == 0:
           count8 += 1
       num8 += 1
   ```

### 中级编程题

1. 输入任意一个正整数，求他是几位数？注意: 不能使用字符串，只能用循环

   ```Python
   # 思路:看一个正整数是几位数，就看这个数整除几次10以后会变成0
   # 例如:123//10->12;12//10->1;1//10->0 (3次)
   # 2345//10->234;234//10->23;23//10->2;2//10->0 (4次)
   num = input('请输⼊一个正整数:')
   num1 = int(num)
   count1 = 1
   while num1 // 10 != 0:
       count1 += 1
       num1 //= 10
   print("%s是一个%d位数"% (num,count1))
   ```

2. 3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？不考虑小数

   ```Python
   l = 3000
   n = 0
   while l >= 5:
       l /= 2
       n += 1
   print(n)
   ```

3. 打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字⽴方和等于该数本身。例如:153是 ⼀个⽔仙花数,因为  `1³ + 5³ + 3³ ` 等于 153

   ```Python
   num = 100
   while num < 1000:
       gw = num % 10  # 3
       sw = num % 100 // 10  # 5
       bw = num // 100

       total = gw ** 3 + sw ** 3 + bw ** 3
       if total == num:
           print(num,"是水仙花数")
       num += 1
   ```

   

 