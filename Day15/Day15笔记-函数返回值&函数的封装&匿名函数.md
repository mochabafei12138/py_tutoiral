### 一、函数基础【重点掌握】

#### 1.关键字参数和不定长参数

> ```Python
> # 1.关键字参数
> # 注意：默认参数主要体现在函数的定义中【声明】，关键字参数主要体现在函数的调用中
> def func1(a,b,c):
>     print('11111',a,b,c)
> # 必须参数的缺点：必须按照顺序传参，否则可能会匹配不上
> func1(10,20,30)
> # 关键字的优点：可以不按照形参的顺序传参。根据关键字就可以识别,关键字一定要和形参保持一致
> func1(b=20,c=30,a=10)
> func1(10,20,c=30)
> 
> # 默认参数和关键字参数常用于系统函数
> print(45,67,7)  # 默认参数sep
> print(34,7,23,sep='=')
> list1 = [23,5,5]
> list1.sort(reverse=True)
> 
> print("*" * 30)
> 
> # 2.不定长参数/可变参数
> # a.*x:x会被当作元组处理
> def f1(*n):
>     print(n,type(n))  # <class 'tuple'>
> # 在调用函数的时候，不定长参数可以处理任意数量的参数
> f1()   # ()
> f1(10)
> f1('abc')   # ('abc',)
> f1(34,56,8,9,34,6,7,'faf','fag',True)  # (34, 56, 8, 9, 34, 6, 7, 'faf', 'fag', True)
> 
> # 练习：求任意多个数字的和
> def get_total(*n):
>     total = sum(n)
>     print(total)
> get_total(34,6,87)
> get_total(2,6,8,90)
> 
> # b.**x:x会被当作字典处理
> def f2(**n):
>     print(n,type(n))   # <class 'dict'>
>     for k,v in n.items():
>         print(k,v)
> 
> f2()   # {}
> # 在调用函数的过程中，给**x进行传参，要按照key=value的形式传参，而且key必须是以变量的形式存在，最终该变量会被识别为字符串
> f2(x=10,y=20,z=30)  # {'x': 10, 'y': 20, 'z': 30}
> 
> # c.
> # 注意：在同一个函数中，*只能出现一次，**也只能出现一次
> # 错误写法
> # def f3(*n1,*n2):
> #     print(n1,n2)
> # def f3(**n1,**n2):
> #     print(n1,n2)
> # *和**可以同时出现
> def f3(*n1,**n2):
>     print(n1,n2)
> f3()
> f3(435,6,67)
> f3(a=45,b=123)
> f3(34,6,7,8,name='张三',age=18)
> 
> # 如果*和**同时出现，经常会使用*args,**kwargs
> def f3(*args,**kwargs):
>     pass
> ```

#### 2.值传递和引用传递

> 【面试题】简述值传递和引用传递的区别
> 值传递：传参的时候，传递的是不可变的数据类型，如：int/float/str/tuple/bool,当形参发生修改【修改的是变量的指向】，对实参没有影响
> 引用传递：传参的时候，传递的是可变的数据类型，如：list/dict/set等，当形参中的元素发生修改【修改列表，字典等可变数据类型中的元素】，则实参会随着修改
>
> ```Python
> # 1.值传递
> def f1(n):  # 形参
>     n = 'abc'   # 重新赋值
> 
> # 实参
> a1 = (234,5,7)
> f1(a1)
> print(a1)
> 
> # 2.引用传递
> def f2(n):  # 形参
>     n[0] = 100  # 修改其中的元素
> 
> # 实参
> a2 = [234,5,7]
> f2(a2)    # n = a2,引用赋值
> print(a2)   # [100, 5, 7]
> # 实参是可变的数据类型，在函数内部对该数据内部的元素进行修改，想要对实参没有影响的话，则需要拷贝
> ```

#### 3.返回值

> ```
> def xxx(形参):
>     函数体【某个特殊的功能】
>     return 返回值
> ```
>
> 返回值：表示函数的运算结果，在哪里调用函数，返回值就返回到哪里
>
> ```Python
> # 所谓函数的返回值，本质上是return的使用，return只能使用在函数中
> 
> # 1.一个函数没有设置返回值，默认返回None
> def f1():
>     print('11111')
> r1 = f1()
> print(r1)   # None
> 
> # 2.return可以单独作为一条语句，表示结束函数,所以在return的后面且和return对齐的情况下，不书写任何语句
> # a
> def f2():
>     print('2222')
>     return
>     # print('over')    # 永远没有机会执行
>     # print('over')
>     # print('over')
> f2()
> 
> # b.书写在return的后面但是和return没有对齐的语句，有执行的可能性，但是，一旦return被执行了，则后面的语句全都没有执行的机会，哪怕书写在循环中
> def f2(n):
>     print('222222')
>     if n:
>         print('yes')
>     else:
>         print('no')
>         return
>     print('over')       # 可能会执行
> f2(0)
> 
> # 3.break/return/exit()三者的区别    *****
> # a.break:结束当前循环
> def f3():
>     print('start~~~~~')
>     for n in range(5):
>         for m in range(3):
>             if n == 2:
>                 break
>             print(n,m)
>     print('end~~~~~~~')
> f3()
> print('over~~~~')
> 
> print('*' * 50)
> 
> # b.retutn:结束当前函数
> def f3():
>     print('start~~~~~')
>     for n in range(5):
>         for m in range(3):
>             if n == 2:
>                 return
>             print(n,m)
>     print('end~~~~~~~')
> f3()
> print('over~~~~')
> 
> print('*' * 50)
> 
> # 扩展c.exit(): 结束程序
> def f3():
>     print('start~~~~~')
>     for n in range(5):
>         for m in range(3):
>             if n == 2:
>                 exit()
>             print(n,m)
>     print('end~~~~~~~')
> f3()
> print('over~~~~')
> ```

#### 4.函数的封装

> ```
> def xxx(形参):
> 	函数体【某个特殊的功能】
> 	return 返回值
> ```
>
> 封装函数：
> 1.是否需要设置形参：查看需求中是否有未知项参与运算【数量】
> 2.是否需要设置返回值：查看需求运算完毕之后是否有结果
>
> ```Python
> # 1.需求：打印10遍九九乘法表
> # 2.需求：打印指定行数的九九乘法表
> # 3.需求：判断一个数是否是偶数
> # 4.封装一个函数 验证一个年是否是闰年
> # 5.封装一个函数 获取指定月的天数
> # 6.封装一个函数，获取多个数中的最大值和平均值
> 
> # 1.需求：打印10遍九九乘法表
> def print_mul():
>     for row in range(1,10):
>         for col in range(1,row + 1):
>             print(f'{col}*{row}={row * col}',end=' ')
>         print()
> for _ in range(10):
>     print_mul()
> 
> # 2.需求：打印指定行数的九九乘法表
> def print_mul(n):
>     for row in range(1,n + 1):
>         for col in range(1,row + 1):
>             print(f'{col}*{row}={row * col}',end=' ')
>         print()
> print_mul(6)
> print_mul(3)
> 
> # 3.需求：判断一个数是否是偶数
> # 注意：当封装函数的时候，但凡涉及到判断的，最终的结果返回布尔值，同时，在封装函数的过程中，尽量不要使用print
> def is_even(num):
>     # if num % 2 == 0:
>     #     return True
>     # else:
>     #     return False
> 
>     # 推荐
>     if num % 2 == 0:
>         return True
>     return False
> 
>     # 不推荐
>     # return num % 2 == 0
> 
> print(is_even(10))
> print(is_even(17))
> 
> # 4.封装一个函数 验证一个年是否是闰年
> def is_leapyear(year):
>     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
>         return True
>     return False
> print(is_leapyear(2024))
> 
> # 5.封装一个函数 获取指定月的天数
> def days(year,month):
>     if month in [1,3,5,7,8,10,12]:
>         return 31
>     elif month in [4,6,9,11]:
>         return 30
>     else:
>         if is_leapyear(year):   # 判断year是否是闰年，返回布尔值，布尔值可以作为if的条件
>             return 29
>         return 28
> print(days(2024,2))
> print(days(2024,1))
> 
> # 6.封装一个函数，获取多个数中的最大值和平均值
> # 注意：return xx：只返回一个数据
> # return xx,xx,xx:返回多个数据，最终会被处理为元组
> def get_num(*num):
>     max_num = max(num)
>     avg_num = sum(num) / len(num)
>     return max_num,avg_num
> r = get_num(34,6,7,89,9,1,4,5,7)
> print(r)
> ```

### 二、函数进阶

#### 1.匿名函数【重点掌握】

> 概念：不再使用def这种标准形式定义函数，而是使用lambda表达式来创建函数，该函数没有函数名，被称为匿名函数
>
> 语法：lambda  形参列表:返回值  
>
> 说明：
>
> ​	a.lambda只是一个表达式，用一行代码实现一个简单的逻辑，可以达到对函数的简化【优点】
>
> ​	b.lambda主体是一个表达式，而不是一个代码块，只能封装有限的逻辑【缺点】
>
> ​	c.lambda拥有自己的命名空间，不能访问自有列表之外或者全局命名空间里的参数
>
> ```Python
> # 1.
> # 标准函数的定义
> def f1(n):
>     print('函数被调用了~~~')
>     return n + 1
> print(f1)   # <function f1 at 0x00000228F1D7F040>
> r1 = f1(6)  # 函数的调用
> print(r1)   # 函数的返回值
> 
> # 匿名函数/lambda表达式，语法：lambda  形参列表:返回值
> f2 = lambda n: n + 1
> print(f2)   # <function <lambda> at 0x000002860924C3A0>
> r2 = f2(8)  # 调用函数
> print(r2)   # 函数的返回值
> 
> # 2.注意：在匿名函数中，返回值涉及到判断，可以借助于三目运算符实现
> def is_even(num):
>     if num % 2 == 0:
>         return True
>     return False
> r21 = is_even(10)
> print(r21)
> 
> is_even2 = lambda  num: True if num % 2 == 0 else False
> r22 = is_even2(13)
> print(r22)
> 
> # 3.在匿名函数中，同样可以使用默认参数，关键字参数和不定长参数
> f31 = lambda x,y=0:x ** 2 + y ** 2
> print(f31(2))
> print(f31(2,3))
> print(f31(x=4,y=5))
> 
> f32 = lambda *x:sum(x)
> print(f32(34,65,7,8))
> 
> f33 = lambda **x:x['a']
> print(f33(a=23,b=45,c=67))
> 
> # 4.匿名函数定义完之后可以直接调用
> print((lambda *x:sum(x))(456,7,8,9))
> 
> # 使用场景：匿名函数常用于作为其他函数的参数使用，max()/sort()/高阶函数
> 
> # 思考题【面试题】
> def func():
>     lst = []
>     for x in range(5):
>         lst.append(lambda n:x * n)
>     return lst
> r = func()
> # 下面代码输出的结果，并说明原因
> print(r[0](2))
> print(r[1](2))
> print(r[2](2))
> print(r[3](2))
> print(r[4](2))
> ```


