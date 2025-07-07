print('start')

# 1.无参无返回值
def func1():
    print('ok~~~11111')

# 2.有参无返回值
def func2(a,b):
    print('ok~~~~~2222',a,b)

# 3.无参有返回值
def func3():
    print('ok~~~33333')
    return  'abc'

# 4.有参有返回值
def func4(num1,num2,num3):
    print('ok~~~~~4444',num1,num2,num3)
    return num1 + num2 + num3

print('end')


'''
注意：
    1.函数名就相当于变量名，字母尽量小写，不同单词之间使用下划线分隔
    2.当函数定义完毕之后，只有当该函数被使用【被调用】的时候，函数【函数体】才会被执行
    3.函数的定义就相当于将指定的函数加载到计算机内存中
'''