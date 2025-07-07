"""
a.函数的定义
def  函数名(形参):
	pass

b.函数的调用
函数名(实参)

函数调用的本质：就是使用函数的过程，当然，同时需要注意传参的问题
传参：在调用函数的过程中，实参给形参赋值的过程
形参：形式参数，出现在函数的声明部分，实际上是一个变量，等待实参赋值【注意：形参本身可以赋值】
实参：实际参数，出现在函数的调用部分，实际上是一个数据【常量，变量，表达式】，目的是为了给形参赋值
"""

# 1.无参无返回值
# 注意1：一定要先定义函数，然后再调用函数
# func1()    # NameError: name 'func1' is not defined
# 注意2：在代码执行的过程中，一旦遇到某个函数的调用，则会先执行对应函数中的代码块，函数执行完毕之后，回到调用函数的地方，代码继续向下执行
print('start~~~~~')
def func1():
    print('ok~~~11111')
# 注意3：形参为空，则调用函数的时候，实参也为空，但是,()不能省略
func1()
print('end~~~~~~')

# 2.有参无返回值
def func2(a,b):
    print('ok~~~~~2222',a,b)
# 注意4：形参不为空，则调用函数的时候，实参也不能为空
# func2()  # TypeError: func2() missing 2 required positional arguments: 'a' and 'b'
func2(10,20)

# 3.无参有返回值
def func3():
    print('ok~~~33333')
    return  'abc'
# 注意5：如果一个函数有返回值，当函数调用完毕，函数的返回值就可以在后面的代码中使用
r3 = func3()   # r3中存储的是func3函数调用完毕之后的返回值
print('返回值：',r3)

# 调用函数之后，直接输出函数的返回值
print(func1())      # 无返回值，默认为None
print(func3())      # 有返回值，为abc

# 4.有参有返回值
def func4(num1,num2,num3):
    print('ok~~~~~4444',num1,num2,num3)
    return num1 + num2 + num3
r4 = func4(3,34,67)
print(r4)

print('*' * 30)

# 5.函数之间可以相互调用
def f1():
    f2()
    print('1111')
def f2():
    print('222222')
    f3()
def f3():
    print('333333')

f1()   # 该段代码执行的入口
# 231

# 6.问题代码
# a.恶意调用
# def a():
#     print('aaaaaa')
#     a()
# a()

# b.
def b():
    print('bbbb')
    c()
def c():
    print('ccccc')
    b()

b()