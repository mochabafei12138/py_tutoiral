# 2.统计1到100之间可以被7整除的数的个数
# 问题一：书写while语句的过程中，非常容易书写死循环
# 错误写法
# n = 1
# count = 0
# while n <= 100:
#     if n % 7 == 0:
#         count += 1
#         n += 1   # 将递增的语法写在了if语句中
# 正确写法
n = 1
count = 0
while n <= 100:
    if n % 7 == 0:
        count += 1
    n += 1
print(count)

# 问题二:将for和while语法混淆了
# n = 1
count = 0
for n in range(1,101):
    if n % 7 == 0:
        count += 1
    # n += 1
print(count)

# 问题三：求整除或者倍数的情况下，注意一个数的最小倍数是它本身
count = 0
for n in range(0,101,7):   # 改正：range(7,101,7)
    count += 1
print(count)

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
count = 0
for n in range(1,100):
    # if (n % 7 == 0 or n % 3 == 0) and not (n % 7 == 0 and n % 3 == 0):
    # if (n % 7 == 0 or n % 3 == 0) and (n % 21 != 0):
    if (n % 7 == 0 and n % 3 != 0) or (n % 7 != 0 and n % 3 == 0):
        count += 1
print(count)

# 问题：重复计数了
count = 0
for n in range(1,100):
    if n % 3 == 0:
        count += 1
    if n % 7 == 0:
        count += 1
    if n % 21 == 0:
        count += 1
print(count)

# 6.计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
total = 0   # 说明：不建议sum表示变量名，系统中有个功能sum()
for n in range(1,1000):
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        total += n
print(total)

total = 0
for n in range(1,1000):
    if n % (3 * 5 * 7) == 0:
        total += n
print(total)

# 1. 输入任意一个正整数，求他是几位数？注意: 不能使用字符串，只能用循环
# 思路：对10进行整除运算，结果为0停止计算
# 如：673：673 // 10---》67  67 // 10---》6 6 // 10 ----》0
# num1 = input('请输入一个正整数：')
# if num1.isdigit():
#     num = int(num1)
#     count = 1
#     while num // 10 != 0:   # 判断
#         count += 1
#         num //= 10    # 重新赋值
#     print(f'{num1}是{count}位数')
# else:
#     print('输入有误')

# 2. 3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？不考虑小数
l = 3000
day = 0
while l >= 5:
    day += 1
    l /= 2
print(day)

# 3. 打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字⽴方和等于该数本身。例如:153是 ⼀个⽔仙花数,因为  1³ + 5³ + 3³ 等于 153
# 方式一
for num in range(100,1000):
    gw = num % 10
    sw = num // 10 % 10
    bw = num // 100
    if num == gw ** 3 + bw ** 3 + sw ** 3:
        print(num)

# 方式二
for num in range(100,1000):
    num = str(num)
    bw = int(num[0])
    sw = int(num[1])
    gw = int(num[2])
    if int(num) == gw ** 3 + bw ** 3 + sw ** 3:
        print(num)







