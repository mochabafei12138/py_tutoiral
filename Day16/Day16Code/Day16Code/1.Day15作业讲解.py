# 4.封装一个函数 验证指定数是否是质数
def isprime(num):
    if num < 2:
        return False
    else:
        for n in range(2,num):
            if num % n == 0:
                return False
        else:
            return True
print(isprime(10))
print(isprime(15))
print(isprime(17))

# 7.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数
def get_count(*num):
    avg_num = sum(num) / len(num)
    count = 0
    for n in num:
        if n > avg_num:
            count += 1
    return avg_num,count
print(get_count(3,4,56,7,8))
print(get_count(2,45,7,98,90))