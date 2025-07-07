'''
根据具体的需求，try-except-finally/else有不同的书写形式
    a.try-except                *****
    b.try-excpet-else
    c.try-except-finally        *****
    d.try-finally
    e.try-except-except......
'''

'''
try:
    代码1
except 异常码  as e:
    代码2
finally:
    代码3
    
注意：
    a.将可能存在异常的代码书写在 【代码1】处，监测起来
    b.如果【代码1】出现异常，肯定会匹配执行相应的【代码2】，如果【代码1】没有异常，则所有的except会被跳过
    c.不管【代码1】是否有异常，【代码3】永远都会执行
    d.except出现一次，且明确了异常码，则只能处理一种异常
    e.当try中的代码出现异常，同样，try中的代码会终止在异常处，后面的代码无法执行
'''

# 1.try-except
# print('start~~~')
# try:
#     num = int(input('请输入一个数字：'))
#     print('over~~~~~~~')
# # 此处的e是一个对象，该对象对应的类是ValueError，当代码出现了异常，则异常的对象就会被自动创建出来
# except ValueError as e:  # e = ValueError()
#     # 在异常类中，已经重写了__str__,所以当输出对象的时候，不是默认的地址，而是错误描述信息
#     print(e)   # invalid literal for int() with base 10: 'wyw'
# print('end~~~~~~')

# # 2.try-except-except......
# '''
# a.try中如果存在多种异常，都会处理其中的一个异常
# b.类似于if的多分支，如果try中的代码出现异常，会从上往下依次匹配相应的except语句
# '''
# print('start~~~')
# try:
#     list1 = [4,5,7,8]
#     num = int(input('请输入一个数字：'))
#     print(list1[num])
# except ValueError as e:
#     print('ValueError',e)
# except IndexError as e:
#     print('IndexError',e)
# print('end~~~~~~')

# 3.try-except + 父类【BaseException/Exception】
# 如果try中代码不确定异常的类型，则可以直接使用父类捕获，任何类型的异常都可以捕获
# print('start~~~')
# try:
#     list1 = [4,5,7,8]
#     num = int(input('请输入一个数字：'))
#     print(list1[num])
# except Exception as e:
#     print('父类~~~',e)
#
# print('end~~~~~~')


# 4.try-except ：省略异常的类型
# print('start~~~')
# try:
#     list1 = [4,5,7,8]
#     num = int(input('请输入一个数字：'))
#     print(list1[num])
# except:
#     print('出现了异常')
#
# print('end~~~~~~')

# # 5.try-except-else
# # try-except中的else执行的时机：只有当try中的代码没有异常的时候，else代码块才会被执行
# print('start~~~')
# try:
#     list1 = [4,5,7,8]
#     num = int(input('请输入一个数字：'))
#     print(list1[num])
# except Exception as e:
#     print('父类~~~',e)
# else:
#     print('else被执行了~~~~')
#
# print('end~~~~~~')

# 6.try-except-finally
# try-except中的finally执行的时机：不管try中的代码是否有异常，finally代码块都会被执行
# print('start~~~')
# try:
#     list1 = [4,5,7,8]
#     num = int(input('请输入一个数字：'))
#     print(list1[num])
# except Exception as e:
#     print('父类~~~',e)
# finally:
#     print('finally被执行了~~~~')
#
# print('end~~~~~~')

# 【面试题】如果函数中出现了try-except-finally,且try或except代码块中出现了return，finally语句仍然会正常执行
# def func():
#     try:
#         list1 = [4,5,7,8]
#         num = int(input('请输入一个数字：'))
#         return list1[num]
#     except Exception as e:
#         print('父类~~~',e)
#         return
#     finally:
#         print('finally被执行了~~~~')
# func()

# 7.函数中出现异常的捕获方式
# 方式一：在函数体中捕获
def func():
    try:
        list1 = [4,5,7,8]
        num = int(input('请输入一个数字：'))
        print(list1[num])
    except Exception as e:
        print('父类~~~',e)
func()

# 方式二：捕获函数的调用
def func():
    list1 = [4,5,7,8]
    num = int(input('请输入一个数字：'))
    print(list1[num])

try:
    func()
except Exception as e:
    print('父类~~~', e)

