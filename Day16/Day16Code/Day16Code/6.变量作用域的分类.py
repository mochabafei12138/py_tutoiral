# 1.变量作用域的分类
# a.单层循环
# num1 = 10      # 全局作用域：全局变量---->在当前py文件中都可以访问该变量
# def func1():
#     num2 = 20  # 局部作用域：局部变量---->只能在当前函数中被访问
#     print(num1,num2)
# func1()
# print(num1)

# b.嵌套函数
num1 = 10       # 全局作用域：全局变量------》在当前py文件中都可以访问该变量
def func1():
    num2 = 20   # 函数作用域：局部变量-----》此处定义的变量在外部函数中都可以访问，包括内部函数
    def func2():
        num3 = 30   # 局部作用域：局部变量-----》此处定义的变量只能在内部函数中被访问
        print('local:',num1,num2, num3)
    func2()
    print('enclosing:',num1,num2)
func1()
print('global:',num1)

# c.当不同作用域内的变量重名
# 注意：当不同作用域内的变量重名，在访问的时候遵循【就近原则】
num = 10
def func1():
    num = 20
    def func2():
        num = 30
        print('local:',num)   # 30
    func2()
    print('enclosing:',num)    # 20
func1()
print('global:',num)   # 10

# 2.
'''
会引入新的作用域：函数，类，模块
不会引入新的作用域：if  for  while  try-except   with .....
'''
n = 12
if n > 10:
    a = 66
    print(a)
print(a)

def func():
    b = 88
    print(b)
func()
# print(b)   # NameError: name 'b' is not defined





