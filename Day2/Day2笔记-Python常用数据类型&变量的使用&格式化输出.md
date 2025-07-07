### 上堂回顾

> 1.软件的安装和环境配置【重点掌握】
>
> 2.计算机简介
>
> ​	软件系统和硬件系统
>
> ​	软件系统：系统软件和应用软件
>
> 3.Python简介
>
> ​	分为Python2.x和Python3.x
>
> ​	建议安装的版本:3.8以上
>
> 4.基本语法【重点掌握】
>
> ​	注释：常用
>
> ​	关键字和标识符，**注意1：自定义标识符的时候千万不要和关键字重名**
>
> 5.print()和input()【重点掌握】
>
> ​	二者是系统功能
>
> ​	问题：自定义标识符是否可以和系统功能的名字重名
>
> ​	**注意2：自定义标识符的时候千万不要和系统功能的名字重名，否则会导致系统的功能失效**

### Day1作业讲解

> ```
> 2.下列关于Python语⾔说法错误的是（C）
> 
> A. Python是解释型语言
> 
> B. Python是⾯向对象语⾔
> 
> C. Python2.x和Python3.x是完全兼容的---->不兼容
> 
> D. Python是跨平台的语言
> 
> 3.下列关于print函数用法错误的是（D）
> 
> A. print(100)
> 
> B. print(100, 200)
> 
> C. print(100, 'hello world!')
> 
> D. print(10 20)  ----->输出多个数据的时候，数据之间使用逗号隔开
> 
> 
> 
> 4.Python中单行注释的符号是（ ）, 多⾏注释的符号是（ ）。
> 
> 5.Python程序文件扩展名是( )。  .py
> 
> 6.在Python中，给多行代码同时添加注释的快捷键是（ ）。   ctrl + /
> 
> 7.在Python中，布尔类型有（2 ）个值，分别是（True 和False ）。注意：T和F一定要大写
> 
> Ture------>True
> 
> 
> 
> 8.简述标识符的规则和规范。
> 
> 9.请写出Python语言有哪些特点。
> 
> 10.请写出Python常⻅的应用领域。
> 
> 
> 
> 11.从控制台分别输入姓名，年龄和爱好，并按照指定格式输出到控制台上
> 
> ﻿运行效果：
> 
> 请输入姓名：张三
> 
> 请输入年龄：18
> 
> 请输入爱好：吹牛逼
> 
> 我是张三，今年18，爱好吹牛逼
> ```

> ```Python
> # 输入：input
> # 将输入的数据存储在标识符
> name = input('请输入姓名：')
> age = input('请输入年龄：')
> hobby = input('请输入爱好：')
> # 输出
> print('我是',name,'今年',age,'爱好',hobby)  # 我是 张三 今年 18 爱好 吹牛逼
> print('我是',name,'今年',age,'爱好',hobby,sep='')  # 我是张三今年18爱好吹牛逼
> print('我是',name,',','今年',age,',','爱好',hobby,sep='')  # 我是张三,今年18,爱好吹牛逼
> ```

### 问题说明

> 1.Python环境
>
> ​	Python3.11/12和Anaconda2021：二者都是Python环境，
>
> ​	原生Python：其中没有多余的第三方库，后期如果用到第三方库，用到一个，就需要手动安装一个
>
> ​	Anaconda：其中包含了绝大多数的第三方库，但是偶尔也会不存在，需要手动安装
>
> 2.环境变量的配置
>
> ​	方式一：此电脑----》右键，属性----》高级系统设置-----》环境变量
>
> ​	方式二：win+r----->输入control system------>高级系统设置-----》环境变量
>
> **3.Python解释器**
>
> ​	问题：No Python interpreter is selected 
>
> ![解释器缺失2](Day2-images\解释器缺失2.png)
>
> ​	问题：invalid Python interpreter  selected for the project
>
> ![解释器缺失1](Day2-images\解释器缺失1.png)
>
> ​	解决方案：打开pycharm-----》左上角file--------》settings--------》Project:xxx------》Python interpreter

> 4.创建工程说明
>
> ![创建工程说明](Day2-images\创建工程说明.png)

### 一、数据类型【重点掌握】

> ​	顾名思义，计算机就是用来做数学计算的机器，因此，计算机程序理所当然的可以处理各种数值。但是，计算机能处理的远远不止数值，还可以处理文本，图形，音频，视频，网页等各种各样的数据，而处理不同的数据，需要使用不同的数据类型来进行表示

> 【面试题】Python中常用的数据类型：
>
> - 数字型：整型【int】,浮点型【float】,复数【complex】
> - 布尔型：bool
> - 字符串型：str
> - 列表：list
> - 元组：tuple
> - 字典：dict
> - 集合：set
> - 字节：bytes
> - 空值：NoneType

> ```Python
> 
> # 前期掌握数字，字符串，布尔
> # 1. 数字型：整型【int】,浮点型【float】,复数【complex】
> # 数字:number
> n1 = 88   # int
> n2 = 89.23  # float
> n3 = 3 + 10j   # 数学上：3 + 10i,了解
> print(n1,n2,n3)
> 
> # 2. 布尔型：bool
> # 注意1：常用于表示结果只有两种的情况，如：成立或不成立，是或不是
> # 注意2：只有两个值，分别是True和False,如果和数字进行数学运算，被当成1和0使用
> b1 = True
> b2 = False
> print(b1,b2)
> print(b1 + 1)   # 2
> print(b2 + 1)   # 1
> 
> # 3. 字符串型：str
> # 只要是文本，都可以表示成字符串，如：姓名，密码，爱好，描述等
> # 注意1：字符串中可以包含数字，字母，特殊符号，中文，简单来说，只要键盘上可以敲出来的内容，都可以在字符串中表示
> # 注意2：可以用单引号，也可以用双引号，甚至可以用三引号
> # 注意3：在一个引号中，敲回车，仅仅是为了折行，本质还是同一行
> s1 = '454' \
>      'fjhgk' \
>      '&^%4' \
>      '计算机'
> s2 = "454fjhgk&^%4计算机"
> print(s1)
> print(s2)
> s31 = '''454
> fjhgk
> &^%4
> 计算机'''
> s32 = """454
> fjhgk
> &^%4
> 计算机"""
> print(s31)
> print(s32)
> 
> # 后期会陆续着重讲解
> # 4.列表：list
> l1 = [34,6,78,9,0]
> print(l1)
> 
> # 5. 元组：tuple
> t1 = (34, 6, 78, 9, 0)
> print(t1)
> 
> # 6. 字典：dict
> # xx:xx
> d1 = {'a':10,'x':99}
> print(d1)
> d2 = {66:'qafaq',True:19}
> print(d2)
> 
> # 7. 集合：set
> set1 = {'a','x',45,7,8}
> print(set1)
> 
> # 8. 字节：bytes
> # 在Python中，图片，音视频等都会被表示成字节【二进制】
> by1 = b'hfj3fhjahf'
> print(by1)
> by2 = b"4562hjghnvg"
> print(by2)
> 
> # 9. 空值：NoneType
> # 注意1：只有一个值，是None
> # 注意2：区分None和''的区别，二者不等价
> n = None
> print(n)
> ```

### 二、变量【重点掌握】

#### 1.定义变量

> 程序在运行的过程中，表示的值可以随时发生改变的标识符
>
> 在程序设计中，变量是一种存储数据的载体【容器】
>
> 语法：变量名  =   值
>
> 说明：变量名其实就是一个标识符
>
> ```Python
> # 1.定义变量
> # 注意1：书写规范：遇到符号，如：=，+，- 等，在符号的前后添加空格
> '''
> name :变量名,是一个标识符【规则和规范】
> =：赋值运算符
> '张三':值/数据
> 
> 含义：将'张三'数据赋值给name变量，name中存储了'张三'
> '''
> # Python中的代码是从上往下依次执行的，所以后期代码中使用name，相当于使用‘张三’
> name = '张三'
> print(name)
> 
> # 2.在定义变量的同时，可以声明变量的类型，后期才会用到【好处：后期会用到某些数据类型中的功能，有了类型的声明之后，系统功能可以自动提示】
> num:int = 10
> hobby:str = '唱歌'
> 
> # 3.定义多个变量
> # a.多个变量具有相同的值
> # num1 = 10
> # num2 = 10
> # num3 = 10
> 
> # 简化
> num1 = num2 = num3 = 10
> print(num1,num2,num3)
> 
> # b.多个变量具有不同的值
> # score1 = 10
> # score2 = 34
> # score3 = 69
> 
> # 工作原理：数据和变量是从左往右一一对应的关系
> score1,score2,score3 = 10,34,69
> print(score1,score2,score3)
> 
> # 问题1：
> # score1,score2,score3,score4 = 10,34,69  # ValueError: not enough values to unpack (expected 4, got 3)
> # score1,score2,score3 = 10,34,69,878     # ValueError: too many values to unpack (expected 3)
> # 注意：默认情况下，定义多个不同值的变量，则变量的数量和数据的数量一定要保持一致
> 
> # 问题2：
> num1,num2 = 45,66
> print(num1,num2)
> 
> num3,num3 = 19,38
> print(num3)
> 
> # 等价于
> num3 = 19
> num3 = 38
> print(num3)
> ```

#### 2.变量的使用

> 变量命名法：所有字母全部小写，不同单词之间使用下划线连接
>
> 常量命名法：所有字母全部大写，不同单词之间使用下划线连接
>
> ```Python
> # 1.变量的重新赋值
> name = '张三'     # 如果一个变量在代码中第一次出现，则称为定义，‘张三’被称为初始值
> print(name)
> 
> name = '李四'     # 如果一个变量在代码中不是第一次出现，则表示重新赋值，'李四'被称为重新赋的值
> print(name)
> 
> # 2.常量
> # 变量命名法：所有字母全部小写，不同单词之间使用下划线连接
> # 常量命名法：所有字母全部大写，不同单词之间使用下划线连接
> stu_name = '尼古拉斯.赵四'
> 
> # 众所周知，圆周率是一个典型的常量，所以在Python中也用常量的方式表示
> PI = 3.14
> print(PI)
> 
> # 注意：Python中没有任何的机制阻止你干坏事，全凭自觉,常量的本质还是一个变量，只是一个标记
> PI = 'abc'
> print(PI)   # abc
> 
> # 3.type(x):获取数据x的数据类型
> num1 = 12
> print(type(num1))   # <class 'int'>
> 
> data1 = 'abc'
> print(type(data1))  # <class 'str'>
> 
> list1 = [4,5,7]
> print(type(list1))  # <class 'list'>
> 
> # 注意1：
> a1 = 88
> a2 = '88'
> print(a1,a2)  # 88 88
> print(type(a1),type(a2))  # <class 'int'> <class 'str'>
> 
> # 注意2：但凡通过input从控制台输入的内容，不管你输入了什么，全部都是字符串
> # age = input('请输入你的年龄：')   # 18
> # print(age,type(age))   # 18 <class 'str'>
> 
> # 注意3：类型可以直接比较，比较运算符：==
> print(type(a1) == int)
> print(type(a1) == str)
> print(type(a1) == type(a2))
> ```

#### 3.内存中的变量

> ```Python
> # 1.使用了一个未被定义的变量，则会报错
> # print(num)    # NameError: name 'num' is not defined
> 
> # 2.定义变量的本质：在计算机的内存中开辟了一份空间，该空间中存储了一个指定的数据
> # id(x):获取数据x在计算机内存中的地址
> 
> # 注意1：获取一个变量的地址，本质上获取的是该变量中存储的数据的地址
> name = '张三'
> print(name,id(name))
> name = '李四'
> print(name,id(name))
> 
> # 注意2：如果两个变量的地址相同，则这两个变量中存储的数据是相同的数据
> # 张三 和明明的身份证号相同，则说明是同一个人
> num1 = 10
> num2 = 10
> print(id(num1),id(num2))
> 
> # 注意3：如果两个变量中存储的数据相同，则这两个变量的地址不一定相同
> # 张三 和张三 -----》身份证号不一定相同
> list1 = [11,22,33]
> list2 = [11,22,33]
> print(id(list1),id(list2))
> ```

#### 4.变量的应用

> ```Python
> # 1.【面试题】交换两个变量的值
> # 方式一:借助于第三个变量
> num1 = 10
> num2 = 20
> num3 = num1
> num1 = num2
> num2 = num3
> print(num1,num2)  # 20 10
> 
> # 方式二：Python特有的语法【推荐】
> num1 = 10
> num2 = 20
> num1,num2 = num2,num1
> print(num1,num2)
> 
> # 方式三：加减法【只适用于数据是数字的情况下】
> num1 = 10
> num2 = 20
> num2 = num1 + num2   # num2 = 30
> num1 = num2 - num1   # num1 = 20
> num2 = num2 - num1   # num2 = 10
> print(num1,num2)
> 
> num1 = 10
> num2 = 20
> num3 = num1 + num2    # num3 = 30
> num2 = num3 - num2    # num2 = 10
> num1 = num3 - num1    # num1 = 20
> print(num1,num2)
> 
> # 2.【面试题】打包和拆包
> # 打包
> # m1,m2,m3,m4 = 45,19,3   # ValueError: not enough values to unpack (expected 4, got 3)
> m1,m2,m3,*m4 = 45,19,3,45,7,9,123,6,8,90,32
> print(m1,m2,m3,m4)   # 45 19 3 [45, 7, 9, 123, 6, 8, 90, 32]
> m1,m2,*m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
> print(m1,m2,m3,m4)
> m1,*m2,m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
> print(m1,m2,m3,m4)
> *m1,m2,m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
> print(m1,m2,m3,m4)
> 
> # 问题：在同一个赋值中，*只能出现一次
> # m1,m2,*m3,*m4 = 45,19,3,45,7,9,123,6,8,90,32   # SyntaxError: multiple starred expressions in assignment
> # print(m1,m2,m3,m4)
> 
> # 拆包
> a1,a2,a3 = (45,7,8)
> print(a1,a2,a3)
> a1,a2,a3 = [45,7,8]
> print(a1,a2,a3)
> 
> # 3.重要扩展：
> # num1 = input('first num:')
> # num2 = input('second num:')
> # num3 = input('third num:')
> # print(num1,num2,num3)   # str
> 
> # eval(x):识别并转换字符串x,x一定得是Python中一个有效的语法，才能识别
> # r = input('请输入三个数据，用逗号隔开:')
> # print(type(r))   # <class 'str'>
> # r1 = eval(r)
> # print(r1)
> # print(type(r1))   # <class 'tuple'>
> 
> # 简化:拆包
> num1,num2,num3 = eval(input('请输入三个数据，用逗号隔开:'))
> print(num1,num2,num3)   # int
> ```

#### 5.删除变量

> 定义变量：从无到有，语法：变量名  = 值，是在计算机的内存中开辟空间的过程
> 删除变量：从有到无，语法：del  变量名，该变量在计算机内存中占用的空间被销毁的过程
>
> ```Python
> # 1.定义变量
> num = 20
> print(num)
> 
> # 2.删除变量
> del num
> print(num)   # NameError: name 'num' is not defined
> 
> # 注意1：变量在使用之前，一定要先定义，然后才能使用
> # 注意2：一个变量定义之后，在使用完毕或失去价值的情况下，可以将该变量删除，删除之后相当于该变量未被定义【空间会被释放】
> 
> ```

#### 6.变量的类型转换

> int(x):将x转换为整型 
>
> float(x):将x转换为浮点型
>
> str(x):将x转换为字符串,x可以是任意类型
>
> bool(x):将x转换为布尔型
>
> ```Python
> # 1.int(x):将x转换为整型
> # x是float
> print(int(45.843))  # 45
> 
> # x是字符串，使用最多
> # 要求：字符串只能由正负号和数字组成，且正负号只能出现在字符串的开头的情况下，才能正确转化为整型
> s1 = '34641'
> print(s1,type(s1))
> n1 = int(s1)
> print(n1,type(n1))
> 
> s1 = '+34641'
> print(s1,type(s1))
> n1 = int(s1)
> print(n1,type(n1))
> 
> s1 = '-34641'
> print(s1,type(s1))
> n1 = int(s1)
> print(n1,type(n1))
> 
> # print(int('354+56')) # ValueError: invalid literal for int() with base 10: '354+56'
> # print(int('35ag456'))  # ValueError: invalid literal for int() with base 10: '35ag456'
> # print(int('35.456'))   # ValueError: invalid literal for int() with base 10: '35.456'
> 
> # 2.float(x):将x转换为浮点型
> # x可以是int
> print(float(45))  # 45.0
> 
> # x是字符串，使用较多
> # 要求：字符串只能由正负号、数字和小数点组成，且正负号只能出现在字符串的开头的情况下，才能正确转化为浮点型
> s1 = '34641'
> print(s1,type(s1))
> f1 = float(s1)
> print(f1,type(f1))
> 
> s1 = '346.41'
> print(s1,type(s1))
> f1 = float(s1)
> print(f1,type(f1))
> 
> s1 = '.34641'
> print(s1,type(s1))
> f1 = float(s1)
> print(f1,type(f1))   # 0.34641
> 
> s1 = '-34641.'
> print(s1,type(s1))
> f1 = float(s1)
> print(f1,type(f1))   # 34641.0
> 
> # 3.str(x):将x转换为字符串,x可以是任意类型
> num1 = 89
> print(type(num1))
> s1 = str(num1)
> print(type(s1))
> 
> # 4.bool(x):将x转换为布尔型,x可以是任意类型
> # 注意1：在Python中，所有的数据类型都可以转换为布尔
> # 注意2:表示空的数据转换完之后结果都是False,非空的数据转换完之后都是True
> # 注意3：常用的数据类型中，表示空的数据有：False,0,0.0,'',[],(),{},None，b''
> print(bool(0))     # int
> print(bool(0.0))   # float
> print(bool(''))    # 空str
> print(bool([]))    # 空list
> print(bool(()))    # 空tuple
> print(bool({}))    # 空字典
> print(bool(None))  # 空值
> 
> print(bool(45))
> print(bool(23.6))
> print(bool('faga'))
> print(bool([45,67,89]))
> print(bool((45,7,8)))
> print(bool({'a':19}))
> 
> # 5.应用
> # 需求1：假设高考数学总分为150分，请输入你的分数，计算还有多少分才能满分？
> # 错误写法，原因：但凡从控制台输入进来的数据，都是字符串
> # TOTAL_SCORE = 150
> # score = input('请输入你的高考数学成绩：')
> # print(TOTAL_SCORE - score)  # TypeError: unsupported operand type(s) for -: 'int' and 'str'
> 
> # 正确写法
> # a.
> # TOTAL_SCORE = 150
> # score = input('请输入你的高考数学成绩：')
> # print(TOTAL_SCORE - int(score))
> 
> # b.
> # TOTAL_SCORE = 150
> # score = input('请输入你的高考数学成绩：')
> # score = int(score)
> # print(TOTAL_SCORE - score)
> 
> # c.
> # TOTAL_SCORE = 150
> # score = int(input('请输入你的高考数学成绩：'))
> # print(TOTAL_SCORE - score)
> 
> # 需求2：从控制台分别输入两个数字，求该两个数字的和
> # num1 = input('请输入第一个数字：')
> # num2 = input('请输入第二个数字：')
> # print(num1 + num2)   # str + str---->str，+表示字符串的拼接
> 
> # a
> num1 = input('请输入第一个数字：')
> num2 = input('请输入第二个数字：')
> print(int(num1) + int(num2))
> 
> # b
> num1 = input('请输入第一个数字：')
> num2 = input('请输入第二个数字：')
> num1 = int(num1)
> num2 = int(num2)
> print(num1 + num2)
> 
> # c
> num1 = int(input('请输入第一个数字：'))
> num2 = int(input('请输入第二个数字：'))
> print(num1 + num2)
> 
> # d
> num1,num2 = eval(input('请输入两个数字，用逗号隔开：'))
> print(num1 + num2)
> ```

### 三、格式化输出【重点掌握】

> 格式化输出/格式化字符串：将多个数据按照指定的格式进行定义，最终得到一个字符串

> 方式一：占位符         
>
> ```
> %d:可以匹配数字，一般匹配整型【整数】
> %f：可以匹配数字，一般匹配浮点型【小数】
> %s：可以匹配Python中的一切数据类型
> ```
>
> 方式二：format() 
>
> 方式三：f-string		
>
> ```Python
> # 一、占位符
> '''
> %d:可以匹配数字，一般匹配整型【整数】
> %f：可以匹配数字，一般匹配浮点型【小数】
> %s：可以匹配Python中的一切数据类型
> '''
> # 语法：'按照指定格式定义占位符' % (实际的数据)
> print('%d-%d-%d' % (34,6,8))
> print('%f~~~~%d~~~~%s~~~~~%f' % (89.24,66,'abc',66))
> print('姓名：%s,年龄：%d,成绩:%d' % ('张三',18,88))
> 
> # 问题1：占位符的数量和实际数据的数量一定要保持一致
> # print('%f~~~~%d~~~~%s~~~~~%f' % (89.24,66,'abc'))  # TypeError: not enough arguments for format string
> # print('%f~~~~%d~~~~%s' % (89.24,66,'abc',67,8))   # TypeError: not all arguments converted during string formatting
> 
> # 问题2：占位符和实际数据的类型要保持一致，特别是%d和%f
> print('姓名：%s,年龄：%d,体重:%f' % ('张三',18,65.5))
> # print('姓名：%s,年龄：%d,体重:%f' % ('张三','18',65.5))  # TypeError: %d format: a number is required, not str
> # print('姓名：%s,年龄：%d,体重:%f' % ('张三',18,'65.5'))   # TypeError: must be real number, not str
> print('姓名：%s,年龄：%s,体重:%s' % ('张三',18,'65.5'))
> 
> # 问题3：%.nd,n>=1,可以实现填充,填充的是0，如果省略.，则在左边填充空格
> print('学号:%d' % (1))
> print('学号:%.5d' % (1))   # 学号:00001
> print('学号:%.5d' % (16))  # 学号:00016
> print('学号:%5d' % (16))  # 学号:   16
> 
> # 问题4：%.nf，n >= 1,可以实现小数点后位数的保留，会涉及四舍五入    *******
> print('身高:%f' % (45.67899))
> print('身高:%.2f' % (45.67899))
> print('身高:%.f' % (45.67899))  # 46   如果省略n,则表示取整，会涉及四舍五入
> 
> # 二、format()
> # 语法：'通过{}设定格式'.format(value1,value2,value3.....)
> # 1.用法：字符串中的占位符由成对的{}表示，在{}内部，使用格式说明符来控制被替换的数据的格式
> print('{}-{}-{}'.format(34,6,8))
> 
> # 2.实际的数据有位置编号，如：34,6,8的位置编号分别为0,1,2
> print('{0}-{1}-{2}'.format(34,6,8))
> print('{2}-{0}-{1}'.format(34,6,8))
> print('{0}-{0}-{0}'.format(34,6,8))
> 
> # 3.通过关键字替换占位符
> print('我是{name}，今年{age}岁'.format(age=18,name='张三'))
> 
> # 4. {:.nf}表示保留小数点后n位
> print('数字：{}'.format(354.45656))
> print('数字：{:.2f}'.format(354.45656))
> print('数字：{:.2%}'.format(354.45656))  # 带有2位小数的百分比
> 
> # 5.填充
> print('{:>5}'.format(45))  # 将原数据右对齐，并在左侧填充空格，总长度达到5
> print('{:<5}'.format(45))  # 将原数据左对齐，并在右侧填充空格，总长度达到5
> print('{:^6}'.format(45))  # 将原数据居中，并在两侧填充空格，总长度达到6
> 
> # 三、f-string   常用
> # 语法：f'xxx{value1},xxx{value2}'
> print(f'{45}-{67}-{12}')
> 
> # 1.
> num1 = 45
> data = 'abc'
> print(f'{23}~~~{num1}~~~{False}~~~~{data}')
> # 注意：如果实际的数据是字符串，单双引号要岔开写
> print(f'{23}~~~{num1}~~~{False}~~~~{"abc"}')
> print(f"{23}~~~{num1}~~~{False}~~~~{'abc'}")
> 
> # 2.f'{xxx:.nf}'
> print(f'体重：{56.456756:.2f}')
> 
> # 3.填充
> data = 'Python'
> print(f'{data}')
> # 默认使用空格填充
> print(f'{data:>10}')  # 将原数据右对齐，并在左侧填充空格，总长度达到10
> print(f'{data:<10}')  # 将原数据左对齐，并在右侧填充空格，总长度达到10
> print(f'{data:^10}')  # 将原数据居中，并在两侧填充空格，总长度达到10
> # 使用指定的字符填充
> print(f'{data:*^10}')
> print(f'{data:%>10}')
> 
> # 四、练习
> '''
> 11.从控制台分别输入姓名，年龄和爱好，并按照指定格式输出到控制台上
> 运行效果：
> 请输入姓名：张三
> 请输入年龄：18
> 请输入爱好：吹牛逼
> 我是张三，今年18，爱好吹牛逼
> '''
> name = input('请输入姓名：')
> age = input('请输入年龄：')
> hobby = input('请输入爱好：')
> # 输出
> print('我是',name,'今年',age,'爱好',hobby)  # 我是 张三 今年 18 爱好 吹牛逼
> print('我是',name,'今年',age,'爱好',hobby,sep='')  # 我是张三今年18爱好吹牛逼
> print('我是',name,',','今年',age,',','爱好',hobby,sep='')  # 我是张三,今年18,爱好吹牛逼
> 
> # 优化
> print('我是%s,今年%s,爱好%s' % (name,age,hobby))
> print('我是{},今年{},爱好{}'.format(name,age,hobby))
> print(f'我是{name},今年{age},爱好{hobby}')
> ```