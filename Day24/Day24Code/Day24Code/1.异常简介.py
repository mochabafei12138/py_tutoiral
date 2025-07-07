print('start~~~')
list1 = [4,5,7,8]
num = int(input('请输入一个数字：'))  # ValueError: invalid literal for int() with base 10: 'raqrq'
print(list1[num])   # IndexError: list index out of range
print('end~~~~~~')

'''
注意：
    a.一般情况下，当程序运行的时候出现的错误被称为异常【Exception】
    b.异常一般使用类表示，比如：IndexError表示索引越界的异常类【列表，元组，字符串】
    c.所有异常类的父类是BaseException或者Exception
    d.异常的特点：当程序运行的过程中遇到了异常，而且该异常未被处理，程序会被终止在异常的代码处，后面的代码将没有执行的机会
    e.在Python中，处理异常的思想：暂时跳过异常的代码，让后面的代码有执行的机会
    f.异常在代码中的出现按只是一种可能性
'''