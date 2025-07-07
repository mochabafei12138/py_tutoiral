# 闭包：如果两个函数嵌套定义，如果在内部函数中访问了外部函数中的变量，则构成一个闭包   *********
# 闭包的常见写法
# a.内外部函数均无参
def func1():
    n1 = 10
    def func2():
        n2 = 20
        print(n1 + n2)
    return func2
f = func1()
print('外部函数调用完毕')  # 当外部函数被调用完毕之后，按理n1会被销毁
f()         # 但是，在函数的嵌套定义中，由于内部函数访问了外部函数中的变量，所以当外部函数调用完毕之后，内部函数仍然可以访问到外部函数中的变量

# b.外部函数有参
# a,b和n1都属于外部函数中的变量，只要这三者中的任何一个被func2访问，则都会构成闭包
def func1(a,b):
    n1 = 10
    def func2():
        n2 = 20
        print(n1 + n2,a,b)
    return func2
f = func1(3,2)
f()

# c.内外部函数有参
def func1(a,b):
    n1 = 10
    def func2(num1,num2,num3):
        n2 = 20
        print(n1 + n2,a,b,num1,num2,num3)
    return func2
f = func1(3,2)
f(55,66,77)   # 注意：相当于调用的是func2，所以一定要注意和func2的参数保持匹配

# d.内外部函数有参,内部函数有返回值
def func1(a,b):
    n1 = 10
    def func2(num1,num2,num3):
        n2 = 20
        print(n1 + n2,a,b,num1,num2,num3)
        return n1 + n2
    return func2
f = func1(3,2)
r = f(55,66,77)
print(r)

# 注意：虽然是函数嵌套定义，虽然是闭包，但是内外部函数本质上和普通函数的用发完全相同，默认参数，关键字参数，不定长参数和返回值都一样使用