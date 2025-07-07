# 【面试题】需求：书写一个装饰器，同时装饰多个函数，给多个函数同时增加同一个新的功能
def wrapper(func):
    print('wrapper~~~~~~~~')
    def inner(*args,**kwargs):     # 打包
        print(args,kwargs)
        func(*args,**kwargs)  # 调用原函数,拆包
        print('new~~~~~')
    return inner

@wrapper
def a():
    print('aaa')

@wrapper
def b(m,n):
    print('bbbbb',m,n)

@wrapper
def c(num1,num2,num3):
    print('cccc',num1,num2,num3)

a()  # 调用inner
b(3,5)  # 调用inner
c(23,5,7)

'''
注意：
    a.一个装饰器装饰多个函数，则@xxx需要书写多次
    b.如果一个装饰器装饰多个不同的函数，为了满足不同函数的参数需求，则给装饰器的内部函数设置不定长参数，格式为：*xxx,**xxx
'''

# 案例/面试题：书写一个装饰器，可以统计任意一个函数的执行时间
import time
# print(time.time())  # 获取从1970.1.1 00：00：00到当前的时间戳【秒数】

def wrapper(func):
    def get_time(*args,**kwargs):
        start = time.time()
        func()
        end = time.time()
        return round(end - start,3)   # 保留小数点后3位
    return get_time

@wrapper
def check():
    for i in range(138232300):
        pass

r = check()
print(f'花费的时间为：{r}')