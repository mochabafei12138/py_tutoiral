'''
filter:过滤
filter(func,iterable),返回值是一个iterator
    func：函数
    iterable：可迭代对象，如：列表，元组，字符串等，此处的可迭代对象可以是多个
功能：将iterable中的元素依次传递给func函数，根据func的返回值决定是否保留该元素，
    如果func的返回值为True，则表示当前元素需要保留，如果func的返回值为False，则表示当前元素需要过滤掉
'''

'''
注意：
    a.func必须设置一个参数
    b.func必须设置返回值，且返回值必须是布尔值
'''

# 1.将1~100之间的5的倍数找出来
# a.
l1 = [n for n in range(1,101) if n % 5 == 0]
print(l1)

# b.
def f(x):
    if x % 5 == 0:
        return True
    return False
r1 = filter(f,range(1,101))
print(r1)
print(list(r1))

# c
r2 = filter(lambda x:True if x % 5 == 0 else False,range(1,101))
print(r2)
print(list(r2))

r2 = filter(lambda x:x % 5 == 0,range(1,101))
print(r2)
print(list(r2))