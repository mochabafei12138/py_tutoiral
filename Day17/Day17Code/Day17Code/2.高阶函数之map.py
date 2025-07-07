# 函数的本质：函数就是一个变量，函数名相当于是一个变量名，所以一个函数可以作为另一个函数的参数或返回值使用
# 一个函数可以作为另一个函数的返回值的应用：函数可以嵌套定义【闭包】
# 一个函数可以作为另一个函数的参数的应用：列表.sort(key=func) 或 max/min(key=func)

# 高阶函数：如果a函数作为b函数的参数使用，b函数最终返回一个结果,则将b函数称为高阶函数
# 常用的高阶函数：map()/reduce()/filter()/sorted()

'''
map:映射
map(func,iterable),返回值是一个iterator【迭代器】
    func：函数
    iterable：可迭代对象，如：列表，元组，字符串等，此处的可迭代对象可以是多个
功能：将iterable中的每一个元素会自动传参给func函数，func会返回一个值，该值会称为iterator中的元素
简单来说：iterable-----》func----->iterator
'''

# 1.生成一个容器，其中的元素是1 4 9 16 25 36 49 64 81
# a.
l1 = [n ** 2 for n in range(1,10)]
print(l1)

# b.
ge2 = (n ** 2 for n in range(1,10))
print(ge2)

# c.
def f(x):
    return x ** 2
r1 = map(f,range(1,10))
print(r1)   # <map object at 0x000002A4BC297D90>
# print(next(r1))
# print(next(r1))
# print(next(r1))
l1 = list(r1)
print(l1)

# d.*******
r2 = map(lambda x:x ** 2,range(1,10))
print(r2)
print(list(r2))

# 练习；将1~100之间的5的倍数找出来，使用map实现
list1 = [n for n in range(1,101) if n % 5 == 0]
print(list1)

iter1 = map(lambda n:n,range(5,101,5))
print(iter1)
print(list(iter1))

# 2.
# 注意1:map中的func函数需要设置几个参数，取决于有几个iterable参与运算
# 注意2：当有多个iterable参与运算，则会自动调用func函数，将多个iterable相同位置处的元素同时传参给func
def f2(m,n):
    return m + n
r1 = map(f2,[1,2,3],[4,5,6,8,2])
print(r1)
print(list(r1))

r2 = map(lambda m,n:m + n,[1,2,3],[4,5,6,8,2])
print(r2)