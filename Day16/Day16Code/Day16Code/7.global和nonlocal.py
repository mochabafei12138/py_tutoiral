# 1.global
# a
# 注意：不同作用域内的变量重名，二者是两个不同的变量，相互之间没有任何影响
n = 5
def f():
    n = 9
f()
print(n)  # 5

# b.【面试题】阅读下面的代码，写出代码执行的结果
# 错误代码
# a = 5
# def func():
#     a += 1   # UnboundLocalError: local variable 'a' referenced引用/访问 before assignment赋值
# func()
# print(a)

'''
分析：
    a.a += 1，等价于a = a + 1
    b.a = a + 1的执行顺序：先计算a + 1,将结果赋值给a
    c.当全局和局部同时出现a = xxx的语法，则认为是定义了不同作用域内重名的变量，访问的原则是就近原则
    d.a = a + 1,要先计算a + 1，而a又就近要访问局部的变量，此时会出现矛盾，所以导致代码报错
'''

# 正确写法
# 思路一：两个不同的变量
a = 5
def func():
    a = 6
    a += 1   # 给局部变量a重新赋值
    print('内部:',a)
func()
print(a)    # 5

# 思路二：同一个变量
a = 5
def func():
    # 声明下面代码中使用到的a变量来自于全局变量
    global a
    a += 1
    print('内部:',a)   # 6
func()
print(a)    # 6

# c.global应用在嵌套函数中
# 下面代码中的m是两个不同的变量
m = 20
def f1():
    m = 60  # 定义了一个新的变量
    def f2():
        print('ok')
    f2()
f1()
print(m)  # 20

# 下面代码中的m是同一个变量
m = 20
def f1():
    global m
    m = 60    # 对全局变量m做了重新赋值
    def f2():
        print('ok')
    f2()
f1()
print(m)  # 60

# 2.nonlocal
# local:局部
# nonlocal:不是局部，特指的是函数作用域
# 使用场景：必须是嵌套定义的函数，发生在函数作用域和局部作用域之间
# a.
# 错误写法
# def f1():
#     name = '123'
#     def f2():
#         name += 'abc'   # name = name + 'abc' UnboundLocalError: local variable 'name' referenced before assignment
#         print('内部：',name)
#     f2()
#     print('外部:',name)
# f1()

# 正确写法
# 思路一：两个不同的变量
def f1():
    name = '123'
    def f2():
        name = '456'   # 定义了新的变量
        name += 'abc'   # 相当于给局部作用域的变量做出重新赋值
        print('内部：',name)  # 456abc
    f2()
    print('外部:',name)   # 123
f1()

# 思路二：同一个变量
def f1():
    name = '123'
    def f2():
        nonlocal name
        name += 'abc'   # 相当于给函数作用域内的name进行重新赋值
        print('内部：',name)  # 123abc
    f2()
    print('外部:',name)   # 123abc
f1()

# 3.
x = 10
def f1():
    x = 20
    def f2():
        x = 30
        print('内部：',x)
    f2()
    print('外部:',x)
f1()
print('全局:',x)
'''
内部： 30
外部: 20
全局: 10
'''
x = 10
def f1():
    global x
    x = 20   # 给全局变量x重新赋值
    def f2():
        x = 30
        print('内部：',x)
    f2()
    print('外部:',x)
f1()
print('全局:',x)
'''
内部： 30
外部: 20
全局: 20
'''
# global和nonlocal无法同时使用
x = 10
def f1():
    global x
    x = 20   # 给全局变量x重新赋值
    def f2():
        # nonlocal x   # SyntaxError: no binding for nonlocal 'x' found
        x = 30   # 给函数作用域内的变量重新赋值
        print('内部：',x)
    f2()
    print('外部:',x)
f1()
print('全局:',x)