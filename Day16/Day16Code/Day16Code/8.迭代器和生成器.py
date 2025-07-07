# 1.可迭代对象和迭代器
# isinstance(变量,类型)：判断指定的变量是否是指定的类型，返回布尔值

from collections.abc import  Iterable,Iterator

# a.可迭代对象Iterable
print(isinstance([45,67,8],Iterable))
print(isinstance((45,67,8),Iterable))
print(isinstance('faqfa',Iterable))
print(isinstance({'a':10},Iterable))
print(isinstance(range(10),Iterable))
# 全部都是True

# b.迭代器
print(isinstance([45,67,8],Iterator))
print(isinstance((45,67,8),Iterator))
print(isinstance('faqfa',Iterator))
print(isinstance({'a':10},Iterator))
print(isinstance(range(10),Iterator))
# 全部都是False

# c.通过系统功能iter()将不是迭代器的可迭代对象转换为迭代器
print(isinstance(iter([45,67,8]),Iterator))
print(isinstance(iter((45,67,8)),Iterator))
print(isinstance(iter('faqfa'),Iterator))
print(isinstance(iter({'a':10}),Iterator))
print(isinstance(iter(range(10)),Iterator))
# 全部都是True

# 2.生成器
# a.不管列表中有多少个元素，都会同时出现，占用内存空间
list1 = [34,56,76,78,9,23,5,56,7,123,34,7]
print(list1[0])
list2 = [n ** 2 for n in range(1000)]
print(list2[0],type(list2))   # <class 'list'>

# b.生成器：使用第n个元素，则只需要生成前n元素
# 方式一：将列表推导式中的[]改为()
r1 = (n ** 2 for n in range(1000))  # 注意：将列表推导式的[]改成().并不是元组推导式，而是生成器
print(type(r1))   # <class 'generator'>
print(r1)   # <generator object <genexpr> at 0x0000022826F67C10>

# 方式二：函数结合yield，定义函数生成器
# 注意：yield xx被执行一次，则表示给生成器中预定义了一个元素
def func1():
    yield  10
r1 = func1()
print(r1)  # <generator object func1 at 0x000001EA1AD87D60>

def func1():
    yield  10
    yield 20
    yield  30
r1 = func1()
print(r1)

def func1(n):
    for i in range(n):
        yield i ** 2
r1 = func1(10)
print(r1)

# c.如何访问生成器中的元素
# 1>for
# for n in r1:
#     print(n)

# 2>list(生成器)
# print(list(r1))

# 3>next(生成器)  推荐
# next()调用一次，表示从生成器中获取一个元素，按照顺序获取的，生成器是一个只出不进的容器
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# 当生成器中的元素全部获取完毕，接着再获取，则报错StopIteration
# print(next(r1))

# 使用next获取生成器中的所有元素，同时借助于循环
while True:
    try:
        ele = next(r1)
        print(ele)
    except StopIteration:
        print('生成器中的元素获取完毕')
        break


print(isinstance(r1,Iterable))   # True
print(isinstance(r1,Iterator))   # True