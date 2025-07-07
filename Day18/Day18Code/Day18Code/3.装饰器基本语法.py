# 1.闭包
# a
# def outer(n):
#     m = 10
#     def inner():
#         print(m,n)
#     inner()
# outer(20)

# b.
# def outer(n):
#     m = 10
#     def inner():
#         print(m,n)
#     return inner   # 切记：需要返回的是函数本身inner，所以不要写成inner()
# f = outer(20)   # 调用的是外部函数
# f()  # 相当于调用的是内部函数inner()


# 2.装饰器的基本语法
# 注意：自定义函数的过程中，函数名不要出现test,否则会自动调起系统的测试模块

# 已知函数：需要被装饰的函数
def a():
    print('春节快乐')

# 书写装饰器：给已知函数增加新的功能
# 基本流程
# a.书写一个闭包，给外部函数设置参数，该参数表示需要被装饰的函数，建议命名：f/fun/func
def outter(func):
    def inner():
        # b.为了吻合闭包的概念，在内部函数中访问外部函数中的变量func
        # func表示一个需要被装饰的函数，所以调用func
        # 调用原函数
        print('~~~',func)   # <function a at 0x0000010FB626F040>
        func()
        # 增加新的功能
        print('new~~~~~~')
    return inner
# c.使用装饰器。将已知的函数作为参数传递给装饰器
# f = inner   func = a
f = outter(a)  # 注意：一个函数作为另一个函数的参数或返回值使用，只需要使用函数名即可
print(f)   # <function outter.<locals>.inner at 0x0000022FD700C4C0>
f()

'''
总结：
    a.outter是装饰器的名称【外部函数的函数名】
    b.inner是装饰器的核心部分【调用原函数，增加新的功能】
    c.在inner中，调用原函数和新增功能没有先后顺序，可以根据具体的需求做出调整
'''

