'''
while:不确定次数
for:确定次数/确定范围
'''

# 1. 求1-2+3-4………+97-98+99-100的结果
# 方式一
r11 = 0
for n in range(1,101):
    if n % 2 == 1:
        r11 += n
    else:
        r11 -= n
print(r11)

# 方式二
r21 = 0
for n1 in range(1,101,2):
    r21 += n1
r22 = 0
for n2 in range(2,101,2):
    r22 += n2
print(r21 - r22)

# 方式三
r31 = 0
for n3 in range(1,101):
    if n3 % 2 == 0:
        n3 = -n3
    r31 += n3
print(r31)

# 2. 求15的阶乘
# 注意：乘法：1  求和：0
r21 = 1
for n in range(1,16):
    r21 *= n
print(r21)

# 3. 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13⽶）
# 注意：不确定循环次数的情况下，建议使用while死循环+break
paper = 0.08 / 1000
count = 0
while True:
    count += 1   # 计数
    # 每次对折，高度变成原来的2倍
    paper *= 2
    if paper >= 8848.13:
        break
print(count)


# 4. 输出9行内容:第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
'''
1
12
123
1234
....
123456789
'''
# 外层循环：控制行
for row in range(1,10):
    # 内层循环：控制每一行的列
    for col in range(1,row + 1):
        print(col,end='')
    print()

# 扩展：
'''
*
**
***
****
*****
'''
# 方式一
for row in range(1,6):
    for col in range(1,row + 1):
        print('*',end='')
    print()

# 方式二
for row in range(1,6):
    print('*' * row)   # 字符串  *  数字：表示将指定字符串重复指定次数，形成一个新的字符串

# 5. 从控制台输入一个数，判断该数是否是质数
# 质数：只能被1和它本身整除的数，最小的质数是2
# 方式一：计数法
# num = input('请输入一个数：')
# if num.isdigit():  # 非负数
#     num = int(num)
#     if num < 2:
#         print(f'{num}不是质数')
#     else:
#         count = 0
#         # 10----->在2~9之间查找，是否有其他的数可以整除10
#         # 67----->在2~66之间查找，是否有其他的数可以整除67
#         for n in range(2,num):
#             if num % n == 0:
#                 count += 1
#         # if count:
#         #     print(f'{num}不是质数',count)
#         # else:
#         #     print(f'{num}是质数',count)
#
#         if count == 0:
#             print(f'{num}是质数',count)
#         else:
#             print(f'{num}不是质数',count)
# else:
#     print('输入有误')

# 方式二：假设法
# num = input('请输入一个数：')
# if num.isdigit():
#     num = int(num)
#     if num < 2:
#         print(f'{num}不是质数')
#     else:
#         result = True   # 不管num是不是质数，都假设它是
#         for n in range(2,num):
#             if num % n == 0:
#                 result = False
#                 # 只要得到了结果，循环就可以提前结束
#                 break
#         if result:
#             print(f'{num}是质数')
#         else:
#             print(f'{num}不是质数')
# else:
#     print('输入有误')

# 方式三：for【break】-else
# num = input('请输入一个数：')
# if num.isdigit():
#     num = int(num)
#     if num < 2:
#         print(f'{num}不是质数')
#     else:
#         for n in range(2,num):
#             if num % n == 0:
#                 print(f'{num}不是质数')
#                 break
#         else:
#             print(f'{num}是质数')
# else:
#     print('输入有误')

# 6. 统计101~200中质数的个数，并且输出所有的质数
count = 0
# 获取数字
for num in range(101,201):
    # 判断num是否是质数
    count1 = 0
    for n in range(2,num):
        if num % n == 0:
            count1 += 1
    if count1 == 0:
        print(num)
        count += 1
print(count)

count = 0
for num in range(101,201):
    result = True
    for n in range(2,num):
        if num % n == 0:
            result = False
            break
    if result:
        print(num)
        count += 1
print(count)

count = 0
for num in range(101,201):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        print(num)
        count += 1
print(count)

# 1. 求1/1! + 1/2! + 1/3! + ..... 1/20!的结果
'''
1/1! + 1/2! + 1/3! + ..... 1/20!
1/1 + 1/1*2 + 1/1*2*3 + ..... 1/1*2*3*4....*20
'''
# 方式一
total = 0
for num in range(1,21):
    # 求分母的阶乘
    fac = 1
    for n in range(1, num + 1):
        fac *= n
    # 求和
    total += 1 / fac
print(total)

# 方式二
fac = 1
total = 0
for num in range(1,21):
    fac *= num   # 利用num的递增，求分母的乘法记录下来
    total += 1 / fac
print(total)

# 2. 编写一个程序：可以不断的输⼊数字，直到输入的数字是0时打印 over 后结束程序
# while True:
#     num = input('请输入数字：')
#     if num == '0':
#         print('over')
#         break

# 3. 模拟用户的登录过程，让用户输入自己的用户名和密码，
# 如果用户名为admin，密码为abc123,则表示登录成功，允许错误三次，如果三次输入错误，则禁止登录
# 方式一：for
# for i in range(3):
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     if username == 'admin' and password == 'abc123':
#         print('登录成功！')
#         break
#     else:
#         if i == 2:
#             continue
#         print('用户名或密码输入有误，请重新输入')
# else:
#     print('已经错误3次，禁止输入')

# 方式二：while
n = 0
while n <= 2:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == 'abc123':
        print('登录成功！')
        break
    else:
        n += 1
        if n == 3:
            continue
        print('用户名或密码输入有误，请重新输入')
else:
    print('已经错误3次，禁止输入')


