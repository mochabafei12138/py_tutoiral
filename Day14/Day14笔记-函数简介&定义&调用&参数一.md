### Day13作业讲解

> ```Python
> # 6.实现将字符串  "1,2,3"   变成列表 ["1","2","3"]
> s = '1,2,3'
> r = s.split(',')    # 分割字符串，返回一个列表
> print(r)
> 
> # 2.输入用户名，判断用户名是否合法，用户名的要求：必须由数字和字母且只能有数字和字母，并且第一个字符是大写字母
> # 例如：  'Abc'  — 不合法    '123'  — 不合法   'abc123'  — 不合法    'Abc123ahs' — 合法
> # import  string
> # username = input('请输入用户名：')
> # letters_count = 0
> # digits_count = 0
> # if username[0] in string.ascii_uppercase:   # username[0].isupper()
> #     for ch in username:
> #         if ch in string.ascii_letters:
> #             letters_count += 1
> #         elif ch in string.digits:  # ch.isdigit()
> #             digits_count += 1
> #     if digits_count == 0 or letters_count + digits_count != len(username):
> #         print(f'{username}不合法')
> #     else:
> #         print(f'{username}合法')
> # else:
> #     print(f'{username}不合法')
> 
> # 4.如下字符串:  "01#张三#60-02#李四#90-03#王五#70", 每一部分表示  学号#姓名#分数，提取学生信息存放于列表中，列表形式如下：
> # 结果显示为:
> # [{"学号":'02', '姓名':'李四', '分数':90}, {"学号":'03', '姓名':'王五', '分数':70}, {"学号":'01', '姓名':'张三', '分数':60}]
> data = "01#张三#60-02#李四#90-03#王五#70"
> # 方式一
> data_list = []
> stu_list = data.split('-')
> for stu in stu_list:
>     info_list = stu.split('#')
>     data_list.append(dict(zip(['学号','姓名','成绩'],info_list)))
> print(data_list)
> 
> # 方式二
> data_list = []
> stu_list = data.split('-')
> for stu in stu_list:
>     dic = {}   # 将dic定义在循环中，是为了每次循环进来，创建一个新的字典
>     info_list = stu.split('#')
>     dic['学号'] = info_list[0]
>     dic['姓名'] = info_list[1]
>     dic['成绩'] = info_list[2]
>     data_list.append(dic)
> print(data_list)
> ```

### 一、列表元组字典集合字符串的总结

> |          |        列表list         | 元组tuple |           字典dict           |      集合set       |      字符串str       |
> | :------: | :---------------------: | :-------: | :--------------------------: | :----------------: | :------------------: |
> | 是否可变 |          可变           |  不可变   |             可变             |        可变        |        不可变        |
> | 是否有序 |          有序           |   有序    |             无序             |        无序        |         有序         |
> | 是否去重 |         可重复          |  可重复   |     key去重，value可重复     |        去重        |        可重复        |
> | 数据类型 |        任意类型         | 任意类型  | key不可变数据，value任意类型 |     不可变数据     |        ------        |
> |    增    |  append/extend/insert   |  ------   |            update            |     add/update     |       -------        |
> |    删    |    remove/pop/clear     |  ------   |             pop              | remove/pop/discard |       -------        |
> |    改    |      reverse/sort       |  -------  |          ---------           |      --------      |       -------        |
> |    查    | min/max/count/index/len |  同列表   |    keys/values/items/len     |    max/min/len     | count/index/find/len |
> | 其他操作 |   +   *    in    copy   | +  *   in |          in   copy           |     in   copy      |     +   *    in      |

> 思维导图：xmind

### 二、函数/方法【重点掌握】

> function:函数/功能
>
> method:方法
>
> 1.基本使用【重点掌握】
>
> ​	概念
>
> ​	定义
>
> ​	调用
>
> ​	参数和返回值
>
> ​	函数的基本封装
>
> 2.进阶使用
>
> ​	匿名函数
>
> ​	闭包
>
> ​	变量的作用域
>
> ​	迭代器
>
> ​	高阶函数
>
> ​	装饰器
>
> ​	函数递归

#### 1.概述

> ​	在一个完整的项目中，某些功能可能会被反复使用，如果将反复出现的代码封装成函数，以后如果要继续使用该功能则直接使用函数即可，另外，如果要修改需求，只需要修改函数即可
>
> 本质：对某些特殊功能的封装
>
> 【面试题】优点：
>
> ​	a.简化代码结构，提高应用的模块性
>
> ​	b.提高了代码的复用性
>
> ​	c.提高了代码维护性
>
> ```Python
> # 需求：求一个圆的面积
> 
> # 1.
> r1 = 30
> area1 = 3.14 * r1 ** 2
> print(area1)
> 
> r2 = 5
> area2 = 3.14 * r2 ** 2
> print(area2)
> 
> r3 = 25
> area3 = 3.14 * r3 ** 2
> print(area3)
> 
> # 2.优化
> # 函数的本质：对某些功能的封装，形成了一个工具，该工具可以反复被使用
> def area(r):
>     return 3.14 * r ** 2
> print(area(30))
> print(area(5))
> print(area(25))
> 
> # 列表的系统功能【append/remove/reverse.....】、字符串的系统功能【replace/find/center.....】
> ```

#### 2.定义

> ```
> 语法：
> 	def  函数名(变量1，变量2....):
> 		    函数体
> 		    return   返回值
> ```
>
> 说明：
>
> ​	a.def是一个关键字，是definition的缩写，专门定义函数
>
> ​	b.函数名：遵循合法标识符的规则和规范即可，尽量做到见名知意，注意：和变量的定义类似，全部小写
>
> ​	c.(变量1，变量2....):被称为形式参数，是一个参数列表，都只是没有赋值的变量
>
> ​	d.函数体：封装某些特殊的功能
>
> ​	e.return是一个关键字，表示返回,注意：只能用在函数中，表示结束函数，可以单独使用，也可以携带数据，当携带数据，则表示该函数的返回值
>
> ​	f.返回值:常量，变量，表达式
>
> ​	g.函数的定义分为两部分：函数的声明和函数的实现
>
> ​	h.变量1，变量2.... 和 return   返回值 可以根据具体的需求选择性的省略
>
> ```Python
> print('start')
> 
> # 1.无参无返回值
> def func1():
>     print('ok~~~11111')
> 
> # 2.有参无返回值
> def func2(a,b):
>     print('ok~~~~~2222',a,b)
> 
> # 3.无参有返回值
> def func3():
>     print('ok~~~33333')
>     return  'abc'
> 
> # 4.有参有返回值
> def func4(num1,num2,num3):
>     print('ok~~~~~4444',num1,num2,num3)
>     return num1 + num2 + num3
> 
> print('end')
> 
> 
> '''
> 注意：
>     1.函数名就相当于变量名，字母尽量小写，不同单词之间使用下划线分隔
>     2.当函数定义完毕之后，只有当该函数被使用【被调用】的时候，函数【函数体】才会被执行
>     3.函数的定义就相当于将指定的函数加载到计算机内存中
> '''
> ```

#### 3.调用

> ```Python
> """
> a.函数的定义
> def  函数名(形参):
> 	pass
>
> b.函数的调用
> 函数名(实参)
>
> 函数调用的本质：就是使用函数的过程，当然，同时需要注意传参的问题
> 传参：在调用函数的过程中，实参给形参赋值的过程
> 形参：形式参数，出现在函数的声明部分，实际上是一个变量，等待实参赋值【注意：形参本身可以赋值】
> 实参：实际参数，出现在函数的调用部分，实际上是一个数据【常量，变量，表达式】，目的是为了给形参赋值
> """
> ```

> ```Python
> """
> a.函数的定义
> def  函数名(形参):
> 	pass
> 
> b.函数的调用
> 函数名(实参)
> 
> 函数调用的本质：就是使用函数的过程，当然，同时需要注意传参的问题
> 传参：在调用函数的过程中，实参给形参赋值的过程
> 形参：形式参数，出现在函数的声明部分，实际上是一个变量，等待实参赋值【注意：形参本身可以赋值】
> 实参：实际参数，出现在函数的调用部分，实际上是一个数据【常量，变量，表达式】，目的是为了给形参赋值
> """
> 
> # 1.无参无返回值
> # 注意1：一定要先定义函数，然后再调用函数
> # func1()    # NameError: name 'func1' is not defined
> # 注意2：在代码执行的过程中，一旦遇到某个函数的调用，则会先执行对应函数中的代码块，函数执行完毕之后，回到调用函数的地方，代码继续向下执行
> print('start~~~~~')
> def func1():
>     print('ok~~~11111')
> # 注意3：形参为空，则调用函数的时候，实参也为空，但是,()不能省略
> func1()
> print('end~~~~~~')
> 
> # 2.有参无返回值
> def func2(a,b):
>     print('ok~~~~~2222',a,b)
> # 注意4：形参不为空，则调用函数的时候，实参也不能为空
> # func2()  # TypeError: func2() missing 2 required positional arguments: 'a' and 'b'
> func2(10,20)
> 
> # 3.无参有返回值
> def func3():
>     print('ok~~~33333')
>     return  'abc'
> # 注意5：如果一个函数有返回值，当函数调用完毕，函数的返回值就可以在后面的代码中使用
> r3 = func3()   # r3中存储的是func3函数调用完毕之后的返回值
> print('返回值：',r3)
> 
> # 调用函数之后，直接输出函数的返回值
> print(func1())      # 无返回值，默认为None
> print(func3())      # 有返回值，为abc
> 
> # 4.有参有返回值
> def func4(num1,num2,num3):
>     print('ok~~~~~4444',num1,num2,num3)
>     return num1 + num2 + num3
> r4 = func4(3,34,67)
> print(r4)
> 
> print('*' * 30)
> 
> # 5.函数之间可以相互调用
> def f1():
>     f2()
>     print('1111')
> def f2():
>     print('222222')
>     f3()
> def f3():
>     print('333333')
> 
> f1()   # 该段代码执行的入口
> # 231
> 
> # 6.问题代码
> # a.恶意调用
> # def a():
> #     print('aaaaaa')
> #     a()
> # a()
> 
> # b.
> def b():
>     print('bbbb')
>     c()
> def c():
>     print('ccccc')
>     b()
> 
> b()
> ```

#### 4.参数一

> 参数分类：
>
> - 必需参数
>
> - 默认参数
>
>   ```Python
>   # 1. 必需参数/必须参数
>   # 注意：必须参数，实参必须传参，实参和形参的数量保持一致
>   def func1(num1,num2):
>       print(num1,num2,num1 + num2)
>   func1(34,3)
>   
>   # 注意：调用函数传参的过程中，要注意需要的数据类型
>   def func2(name,age):
>       print('姓名:%s,年龄：%d' % (name,age))
>   # func2('张三','18')  # TypeError: %d format: a number is required, not str
>   func2('张三',18)
>   
>   # 注意：name:str表示给name参数声明类型
>   # ->int表示返回值类型为int
>   def func3(name:str) -> str:
>       print('333333')
>   func3('fafgqg4')
>   
>   # 2. 默认参数
>   def func1(num1=0,num2=0):
>       print(num1,num2,num1 + num2)
>   # 如果形参有默认值，则调用函数的时候根据需要可以不传参
>   func1()
>   func1(10)
>   func1(10,20)
>   
>   # 注意
>   def func1(num1,num2=0):
>       print(num1,num2,num1 + num2)
>   func1(7)
>   func1(7,10)
>   
>   # 多个参数，部分为必须参数，部分为默认参数，一定要将必须参数书写在默认参数的前面non-default argument follows default argument
>   # 错误写法
>   # def func1(num1- 关键字参数
>   - 不定长参数【可变参数】
>   
>   【面试题】简述值传递和引用传递的区别
>   
>   值传递：传参的时候，传递的是不可变的数据类型，如：int/float/str/tuple/bool,当形参发生修改【修改的是变量的指向】，对实参没有影响
>   
>   引用传递：传参的时候，传递的是可变的数据类型，如：list/dict/set等，当形参中的元素发生修改【修改列表，字典等可变数据类型中的元素】，则实参会随着修改
>   =0,num2):
>   #     print(num1,num2,num1 + num2)
>   ```



