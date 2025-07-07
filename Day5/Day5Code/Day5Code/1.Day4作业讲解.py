# 4.从控制台输入一个年份，判断该年是否是闰年，是闰年的条件: 能被4整除但是不能被100整除或者能够被400整除的年
# year = int(input('请输入一个年份：'))
# if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f'{year}是平年')

# 7.从控制台输入三个数，输出最大的值
# 常规：分情况讨论
# 简化思维：假设法【非常好用】
# num1,num2,num3 = eval(input('请输入三个数，用逗号隔开:'))
# max_value = num1   # 假设num1为最大值
# if num2 > num1:
#     max_value = num2   # 推翻假设，给max_value重新赋值
# if num3 > max_value:
#     max_value = num3
# print(max_value)

# 8.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”，
# 例如：153 = 1的三次方 + 5的三次方 + 3的三次方，则153是水仙花数
# 方式一
# num = int(input('请输入一个三位数：'))
# gw = num % 10
# sw = num // 10 % 10
# bw = num // 100
# if num == gw ** 3 + bw ** 3 + sw ** 3:
#     print(f'{num}是水仙花数')
# else:
#     print(f'{num}不是水仙花数')

# 方式二
# num = input('请输入一个三位数：')   # str
# bw = int(num[0])    # str---->int
# sw = int(num[1])
# gw = int(num[2])
# if int(num) == gw ** 3 + bw ** 3 + sw ** 3:
#     print(f'{num}是水仙花数')
# else:
#     print(f'{num}不是水仙花数')


# 9.回文数【五位数】：对称的数,如12421  45754
# 方式一和方式二:上述和水仙花数的两种方式都可以实现
# 方式三：
num = input('请输入一个五位数：')
# 扩展：name,name[::-1]表示将name做了逆序/反转/翻转
# print(num)   # abcd
# print(num[::-1])  # dcba
if num == num[::-1]:
    print(f'{num}是回文数')
else:
    print(f'{num}不是回文数')