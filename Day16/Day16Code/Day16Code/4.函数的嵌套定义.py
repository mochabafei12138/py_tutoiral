# 1.函数嵌套定义的意义
# 需求：在func2中访问到n1的值，并和n2进行求和
# 错误写法
'''
错误原因：
    a.一个函数被调用之后，其中的变量才会被定义出来，此时才会在计算机的内存中开辟空间
    b.当一个函数调用完毕，其中的变量会被销毁
'''
# def func1():
#     n1 = 10
# def func2():
#     n2 = 20
#     print(n1 + n2)   # NameError: name 'n1' is not defined
# func2()

# 解决方案
# 方案一：将n1设置为func1的返回值，在func2中调用func1
# def func1():
#     n1 = 10
#     return n1
# def func2():
#     n2 = 20
#     r = func1()
#     print(r + n2)
# func2()

# 方案二：函数的嵌套定义
# def func1():
#     n1 = 10
#     def func2():
#         n2 = 20
#         print(n1 + n2)
# func1()
# func2()   # func2相当于func1中的变量，只要在func1的外部访问，都访问不到  NameError: name 'func2' is not defined

# 2.嵌套函数的调用
# 方式一：在外部函数中直接调用内部函数
def func1():
    print('外部~~~~11111')
    n1 = 10
    def func2():
        n2 = 20
        print(n1 + n2)
        print('内部~~~111111')
    func2()    # 调用内部函数func2
    print('外部~~~~222222')
func1()

# 方式二：将内部函数作为外部函数的返回值返回
def func1():
    print('外部~~~~11111')
    n1 = 10
    def func2():
        n2 = 20
        print(n1 + n2)
        print('内部~~~111111')

    print('外部~~~~222222')

    # 一个函数作为另一个函数的返回值使用，只需要书写函数名即可,因为要返回函数本身，在func1的外面可以间接的调用内部函数
    return func2

f = func1()   # f = func2
print(f)  # <function func1.<locals>.func2 at 0x0000019A60BFF040>
f()  # 相当于调用的是func2


