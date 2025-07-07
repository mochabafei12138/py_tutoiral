### 一、异常和错误

#### 1.概念

> ​	Python有两种错误很容易辨认：语法错误和异常
>
> ​	Python 的语法错误或者称之为解析错误，是初学者经常碰到的，比如缺少冒号等
>
> ​	在程序运行过程中，总会遇到各种各样的错误，有的错误是程序编写有问题造成的，这种错误我们通常称之为bug，bug是必须修复的；有的错误是用户输入造成的，这种错误可以通过检查用户输入来做相应的处理；还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了，这类错误被称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出
>
> ```Python
> print('start~~~')
> list1 = [4,5,7,8]
> num = int(input('请输入一个数字：'))  # ValueError: invalid literal for int() with base 10: 'raqrq'
> print(list1[num])   # IndexError: list index out of range
> print('end~~~~~~')
> 
> '''
> 注意：
>     a.一般情况下，当程序运行的时候出现的错误被称为异常【Exception】
>     b.异常一般使用类表示，比如：IndexError表示索引越界的异常类【列表，元组，字符串】
>     c.所有异常类的父类是BaseException或者Exception
>     d.异常的特点：当程序运行的过程中遇到了异常，而且该异常未被处理，程序会被终止在异常的代码处，后面的代码将没有执行的机会
>     e.在Python中，处理异常的思想：暂时跳过异常的代码，让后面的代码有执行的机会
>     f.异常在代码中的出现按只是一种可能性
> '''
> ```

#### 2.常见异常【面试题】

> AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
> IOError 输入/输出异常；基本上是无法打开文件
> ImportError 无法引入模块或包；基本上是路径问题或名称错误
> IndentationError 语法错误（的子类） ；代码没有正确对齐
> IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
> KeyError 试图访问字典里不存在的键
> KeyboardInterrupt Ctrl+C被按下
> NameError 使用一个还未被赋予对象的变量
> SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
> TypeError 传入对象类型与要求的不符合
> UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
> 导致你以为正在访问它
> ValueError 传入一个调用者不期望的值，即使值的类型是正确的
>
> ```Python
> # 【面试题】请列举Python常见的异常，至少5种
> 
> # 1.NameError 使用一个还未被赋予对象的变量
> # print(num)   # NameError: name 'num' is not defined
> 
> # 2.ValueError 传入一个调用者不期望的值，即使值的类型是正确的
> # num = int(input('请输入一个数字：'))   # ValueError: invalid literal for int() with base 10: 'agAG'
> 
> # 3.TypeError 传入对象类型与要求的不符合
> # print('faf' + 19)   # TypeError: can only concatenate str (not "int") to str
> # print(19 + 'fagg')    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
> 
> # 4.AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
> # print('abc'.reverse())   # AttributeError: 'str' object has no attribute 'reverse'
> # class Person():
> #     def __init__(self,name,score):
> #         self.name = name
> #         self.score = score
> # p = Person('小明',10)
> # print(p.scope)
> 
> # 5.UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
> # a = 10
> # def func():
> #     a += 1    # UnboundLocalError: local variable 'a' referenced before assignment
> # func()
> # print(a)
> 
> # def func1():
> #     num = 10
> #     def func2():
> #         print(num)  # UnboundLocalError: local variable 'num' referenced before assignment
> #         num = 20
> #     func2()
> # func1()
> 
> # 6.MoudleNotFoundError:导入模块的时候，路径有误
> # import  aaaa    # ModuleNotFoundError: No module named 'aaaa'
> 
> # 7.FileNotFoundError:文件路径不存在
> # f = open(r'file.txt','r',encoding='utf-8')  # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
> 
> # 8.KeyError 试图访问字典里不存在的键
> # dic = {'a':10}
> # print(dic['b'])   # KeyError: 'b'
> ```

#### 3.异常处理方式

> 处理异常的本质：没有从根本上解决问题【修改代码】，只是将异常忽略，可以让后面的代码继续执行

##### 3.1try-except-finally/else捕获【重点掌握】

> ```Python
> '''
> 根据具体的需求，try-except-finally/else有不同的书写形式
>     a.try-except                *****
>     b.try-excpet-else
>     c.try-except-finally        *****
>     d.try-finally
>     e.try-except-except......
> '''
> 
> '''
> try:
>     代码1
> except 异常码  as e:
>     代码2
> finally:
>     代码3
>     
> 注意：
>     a.将可能存在异常的代码书写在 【代码1】处，监测起来
>     b.如果【代码1】出现异常，肯定会匹配执行相应的【代码2】，如果【代码1】没有异常，则所有的except会被跳过
>     c.不管【代码1】是否有异常，【代码3】永远都会执行
>     d.except出现一次，且明确了异常码，则只能处理一种异常
>     e.当try中的代码出现异常，同样，try中的代码会终止在异常处，后面的代码无法执行
> '''
> 
> # 1.try-except
> # print('start~~~')
> # try:
> #     num = int(input('请输入一个数字：'))
> #     print('over~~~~~~~')
> # # 此处的e是一个对象，该对象对应的类是ValueError，当代码出现了异常，则异常的对象就会被自动创建出来
> # except ValueError as e:  # e = ValueError()
> #     # 在异常类中，已经重写了__str__,所以当输出对象的时候，不是默认的地址，而是错误描述信息
> #     print(e)   # invalid literal for int() with base 10: 'wyw'
> # print('end~~~~~~')
> 
> # # 2.try-except-except......
> # '''
> # a.try中如果存在多种异常，都会处理其中的一个异常
> # b.类似于if的多分支，如果try中的代码出现异常，会从上往下依次匹配相应的except语句
> # '''
> # print('start~~~')
> # try:
> #     list1 = [4,5,7,8]
> #     num = int(input('请输入一个数字：'))
> #     print(list1[num])
> # except ValueError as e:
> #     print('ValueError',e)
> # except IndexError as e:
> #     print('IndexError',e)
> # print('end~~~~~~')
> 
> # 3.try-except + 父类【BaseException/Exception】
> # 如果try中代码不确定异常的类型，则可以直接使用父类捕获，任何类型的异常都可以捕获
> # print('start~~~')
> # try:
> #     list1 = [4,5,7,8]
> #     num = int(input('请输入一个数字：'))
> #     print(list1[num])
> # except Exception as e:
> #     print('父类~~~',e)
> #
> # print('end~~~~~~')
> 
> 
> # 4.try-except ：省略异常的类型
> # print('start~~~')
> # try:
> #     list1 = [4,5,7,8]
> #     num = int(input('请输入一个数字：'))
> #     print(list1[num])
> # except:
> #     print('出现了异常')
> #
> # print('end~~~~~~')
> 
> # # 5.try-except-else
> # # try-except中的else执行的时机：只有当try中的代码没有异常的时候，else代码块才会被执行
> # print('start~~~')
> # try:
> #     list1 = [4,5,7,8]
> #     num = int(input('请输入一个数字：'))
> #     print(list1[num])
> # except Exception as e:
> #     print('父类~~~',e)
> # else:
> #     print('else被执行了~~~~')
> #
> # print('end~~~~~~')
> 
> # 6.try-except-finally
> # try-except中的finally执行的时机：不管try中的代码是否有异常，finally代码块都会被执行
> # print('start~~~')
> # try:
> #     list1 = [4,5,7,8]
> #     num = int(input('请输入一个数字：'))
> #     print(list1[num])
> # except Exception as e:
> #     print('父类~~~',e)
> # finally:
> #     print('finally被执行了~~~~')
> #
> # print('end~~~~~~')
> 
> # 【面试题】如果函数中出现了try-except-finally,且try或except代码块中出现了return，finally语句仍然会正常执行
> # def func():
> #     try:
> #         list1 = [4,5,7,8]
> #         num = int(input('请输入一个数字：'))
> #         return list1[num]
> #     except Exception as e:
> #         print('父类~~~',e)
> #         return
> #     finally:
> #         print('finally被执行了~~~~')
> # func()
> 
> # 7.函数中出现异常的捕获方式
> # 方式一：在函数体中捕获
> def func():
>     try:
>         list1 = [4,5,7,8]
>         num = int(input('请输入一个数字：'))
>         print(list1[num])
>     except Exception as e:
>         print('父类~~~',e)
> func()
> 
> # 方式二：捕获函数的调用
> def func():
>     list1 = [4,5,7,8]
>     num = int(input('请输入一个数字：'))
>     print(list1[num])
> 
> try:
>     func()
> except Exception as e:
>     print('父类~~~', e)
> 
> ```

##### 3.2raise抛出

> ```Python
> '''
> Python异常处理的方式：捕获和抛出
> '''
> 
> # 1.根据具体的问题创建异常对象
> # try:
> #     list1 = [4,6,7,89,9]
> #     print(list1[20])
> # except IndexError as e:
> #     print(e)
> 
> # 2.可以通过异常的类创建异常的对象，控制代码的执行
> # 语法：raise 异常类('描述信息')，注意：raise常用于自定义异常中
> print('start~~~~')
> try:
>     raise IndexError('索引越界问题')
> except Exception as e:
>     print(e)
> print('end~~~~~~')
> 
> ```

##### 3.3assert断言

> ```Python
> # assert
> # 语法：assert 表达式,异常描述信息
> # 工作原理：如果表达式成立，则代码正常执行，但是如果表达式不成立，则会出现AssertionError
> def div(x,y):
>     assert y != 0,'y不能为0'
>     return x / y
> r = div(3,0)
> print(r)
> ```

#### 4.自定义异常

> ```Python
> # 为了解决实际生活中的特定场景，系统的异常类满足不了需求，则需要自定义异常
> 
> # 1.自定义一个类，继承自BaseException或Exception
> # class CustomException(BaseException):
> #     # 2.书写构造函数，在其中定义实例属性
> #     def __init__(self,msg):
> #         # 调用父类的构造函数，主要是为了使用异常类的机制
> #         super().__init__()
> #         self.msg = msg
> #
> #     # 3.重写__str__函数
> #     def __str__(self):
> #         return self.msg
> #
> #     # 4.定义一个实例函数，用来解决出现的问题
> #     def handle(self):
> #         print('问题已解决')
> #
> # try:
> #     raise CustomException('出现了异常')
> # except CustomException as e:
> #     print(e)
> #     e.handle()
> 
> # 练习：
> class LateException(BaseException):
>     def __init__(self, msg):
>         super().__init__()
>         self.msg = msg
> 
>     def __str__(self):
>         return self.msg
> 
>     def handle(self):
>         print('下次一定在八点之前起床')
> hour = float(input('请输入你起床的时间：'))
> try:
>     if hour >= 8:
>         raise LateException('上课/上班迟到了')
>     else:
>         print('正常上课/上班')
> except LateException as e:
>     print(e)
>     e.handle()
> ```