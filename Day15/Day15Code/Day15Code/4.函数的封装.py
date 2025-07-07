# 1.需求：打印10遍九九乘法表
def print_mul():
    for row in range(1,10):
        for col in range(1,row + 1):
            print(f'{col}*{row}={row * col}',end=' ')
        print()
for _ in range(10):
    print_mul()

# 2.需求：打印指定行数的九九乘法表
def print_mul(n):
    for row in range(1,n + 1):
        for col in range(1,row + 1):
            print(f'{col}*{row}={row * col}',end=' ')
        print()
print_mul(6)
print_mul(3)

# 3.需求：判断一个数是否是偶数
# 注意：当封装函数的时候，但凡涉及到判断的，最终的结果返回布尔值，同时，在封装函数的过程中，尽量不要使用print
def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # 推荐
    if num % 2 == 0:
        return True
    return False

    # 不推荐
    # return num % 2 == 0

print(is_even(10))
print(is_even(17))

# 4.封装一个函数 验证一个年是否是闰年
def is_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
print(is_leapyear(2024))

# 5.封装一个函数 获取指定月的天数
def days(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if is_leapyear(year):   # 判断year是否是闰年，返回布尔值，布尔值可以作为if的条件
            return 29
        return 28
print(days(2024,2))
print(days(2024,1))

# 6.封装一个函数，获取多个数中的最大值和平均值
# 注意：return xx：只返回一个数据
# return xx,xx,xx:返回多个数据，最终会被处理为元组
def get_num(*num):
    max_num = max(num)
    avg_num = sum(num) / len(num)
    return max_num,avg_num
r = get_num(34,6,7,89,9,1,4,5,7)
print(r)