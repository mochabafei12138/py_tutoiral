### Day15作业讲解

> ```Python
> # 4.封装一个函数 验证指定数是否是质数
> def isprime(num):
>     if num < 2:
>         return False
>     else:
>         for n in range(2,num):
>             if num % n == 0:
>                 return False
>         else:
>             return True
> print(isprime(10))
> print(isprime(15))
> print(isprime(17))
> 
> # 7.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数
> def get_count(*num):
>     avg_num = sum(num) / len(num)
>     count = 0
>     for n in num:
>         if n > avg_num:
>             count += 1
>     return avg_num,count
> print(get_count(3,4,56,7,8))
> print(get_count(2,45,7,98,90))
> ```

### 一、函数进阶

#### 1.匿名函数应用

> ```Python
> # 1.思考题【面试题】请写出下面代码执行的结果，并说明原因
> def func():
>     lst = []
>     for x in range(5):
>         print(x)   # 0 ~4
>         lst.append(lambda n:x * n)  # 搞清楚列表中的元素是什么?------->其中的元素是匿名函数【本质上是函数的定义】
>     print(lst)  # [<function func.<locals>.<lambda> at 0x0000024CF441C430>.....]
>     # 此时列表中添加的是函数的定义，这些函数还未被调用，所以x * n还未被执行
>     return lst
> r = func()  # [<function func.<locals>.<lambda> at 0x0000024CF441C430>.....]
> # print(r)
> # print(r[0])  # 获取列表中的第0个元素，是一个函数
> # print(r[0](2))  # 调用第0个函数，2表示给该函数传参
> # 下面代码输出的结果，并说明原因
> # 开始调用函数，此时x * n才会被执行，这种情况下，for循环已经执行完毕，x最后只能取到4
> print(r[0](2))
> print(r[1](2))
> print(r[2](2))
> print(r[3](2))
> print(r[4](2))
> 
> '''
> 正常思维/错误结果：0  2 4 6 8
> 正确结果：8 8 8 8 8
> 为什么是上述结果：
> '''
> 
> # 2.匿名函数作为其他函数的参数使用
> # a.lst.sort(reverse=False,key=None)
> # 1>lst.sort()默认情况下，如果lst中的元素支持大小比较，则可以直接排序
> lst1 = [45,67,8,9,0]
> lst1.sort()
> print(lst1)
> 
> lst1 = [45,67,8,9,0]
> lst1.sort(reverse=True)
> print(lst1)
> 
> lst1 = ['45','fa','DG','vw','237']
> lst1.sort()
> print(lst1)
> 
> # 2>在lst.sort()中设置key参数，用途一：用于给列表中的元素自定义排序规则，用途二：如果列表中的元素不支持大小比较，自己设置比较规则
> # students = [
> # {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
> # '15300022839'},
> # {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
> # '15300022838'},
> # {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
> # '15300022839'},
> # {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
> # '15300022428'},
> # {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
> # '15300022839'},
> # {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
> # '15300022839'}
> # ]
> # 错误写法：
> # students.sort()   # TypeError: '<' not supported between instances of 'dict' and 'dict'
> '''
> sort的工作原理
> 列表中的元素支持大小比较：
>     将列表中的元素俩俩之间进行大小的比较，如果符合条件，则交换元素的位置
> 列表中的元素不支持大小比较：
>     If a key function is given, apply it once to each list item and sort them,
>         ascending or descending, according to their function values.
>     a.key的值必须是一个函数，key=func
>     b.会依次将列表中的元素传递给func,会自动调用func，给func设置返回值，该返回值表示排序的规则,而注意：该函数一定要支持大小比较
>     c.如果函数存在，则直接使用，但是只能使用函数名，格式：key=函数名
>       如果函数不存在，则需要先定义函数【def或lambda】，然后再使用
> '''
> # 需求1：将列表中的字符串按照长度排序
> lst1 = ['45454','fa','DG525542','vw55','237']
> lst1.sort(key=len)
> print(lst1)  # ['fa', '237', 'vw55', '45454', 'DG525542']
> 
> lst1 = ['45454','fa','DG525542','vw55','237']
> lst1.sort(key=len,reverse=True)
> print(lst1)  # ['DG525542', '45454', 'vw55', '237', 'fa']
> 
> # 需求2：将下面列表中的元素按照成绩进行降序排序
> students = [
> {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
> '15300022838'},
> {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
> '15300022428'},
> {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
> '15300022839'},
> {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
> '15300022839'}
> ]
> # 不推荐
> # def rule(x):
> #     return x['score']
> # students.sort(key=rule,reverse=True)
> # print(students)
> 
> # 推荐                *********
> students.sort(key=lambda x:x['score'],reverse=True)
> print(students)
> 
> # b.max/min(value....key=None),通过给key赋值一个函数func，可以自定义查找最大值的规则，func的返回值就是规则
> # 需求：获取年龄最大的人的姓名
> dic = {'herry':20,'tom':18,'bob':22,'jack':25,'jerry':23}
> # 默认表示对字典中的所有的key求最大值
> print(max(dic))   # tom，等价于max(['herry','tom'....'jerry'])
> 
> def rule(x):
>     return dic[x]
> print(max(dic,key=rule))  # jack
> 
> print(max(dic,key=lambda ele:dic[ele]))  # jack
> ```

#### 2.函数的本质

> 1.函数本质是一个变量，函数名其实就是一个变量名	
>
> 2.一个函数可以作为另一个函数的参数或返回值使用,只需要传递或返回函数名即可
>
> ```Python
> # 1.函数本质是一个变量，函数名其实就是一个变量名
> # a.系统函数，如：abs()
> print(abs)   # 函数本身，<built-in内置/内建 function abs>
> print(abs(-23))  # 函数调用，获取返回值
> 
> f1 = abs    # 将abs作为数据赋值给f1变量,f1中存储的是可以求绝对值的函数
> print(f1)   # <built-in function abs>
> print(f1(-18))
> 
> # b.自定义函数
> def func():
>     print('1111111')
> print(func)   # 函数本身，<function func at 0x0000020280F4F040>
> func()   # 函数的调用
> 
> f11 = func
> print(f11)    # <function func at 0x0000020280F4F040>
> f11()
> 
> # c.注意：既然函数名相当于一个变量名，所以可以给该变量重新赋值,但是会导致系统的功能失效
> # 所以自定义变量的时候，除了要避开关键字之外，还要避开系统函数名
> # print(abs,type(abs))
> # abs = 'abc'
> # print(abs,type(abs))
> # print(abs(-50))  # TypeError: 'str' object is not callable可调用的，注意：只有function或method才能被调用，其他类型都无法调用
> 
> # 尽量不要使用list/tuple/dict/set等命名变量,一般给这些系统的函数名添加前缀或后缀区分
> print(list('abc'))
> list = [23,5,56,8,9]
> # print(list('fea'))  # TypeError: 'list' object is not callable
> 
> 
> # 2.一个函数可以作为另一个函数的参数或返回值使用,只需要传递或返回函数名即可
> # a.作为参数使用
> def func(a,b,f):
>     print(a,b,f)
>     # 在函数体中，f是当作函数被调用的，所以传参的时候一定要给f传一个函数，且该函数必须有一个参数
>     total = f(a) + f(b)   # 等价于abs(a) + abs(b)
>     return total
> 
> print(func(34,-67,abs))  # a = 34   b = -67   f = abs
> 
> # b.
> def func():
>     return sum   # 返回函数本身
> r = func()  # r = sum
> print(r)  # <built-in function sum>
> 
> def func():
>     return sum([1,2])   # 返回函数调用的返回值
> r = func()  # r = 3
> print(r)   # 3
> ```

#### 3.函数的嵌套定义

> ```Python
> def func1():
> 	def func2():
> 		xxx
> # func1：外部函数
> # func2：内部函数
> # func1和func2的参数，返回值的使用和最基本的使用完全相同   
> ```
>
> ```Python
> # 1.函数嵌套定义的意义
> # 需求：在func2中访问到n1的值，并和n2进行求和
> # 错误写法
> '''
> 错误原因：
>     a.一个函数被调用之后，其中的变量才会被定义出来，此时才会在计算机的内存中开辟空间
>     b.当一个函数调用完毕，其中的变量会被销毁
> '''
> # def func1():
> #     n1 = 10
> # def func2():
> #     n2 = 20
> #     print(n1 + n2)   # NameError: name 'n1' is not defined
> # func2()
> 
> # 解决方案
> # 方案一：将n1设置为func1的返回值，在func2中调用func1
> # def func1():
> #     n1 = 10
> #     return n1
> # def func2():
> #     n2 = 20
> #     r = func1()
> #     print(r + n2)
> # func2()
> 
> # 方案二：函数的嵌套定义
> # def func1():
> #     n1 = 10
> #     def func2():
> #         n2 = 20
> #         print(n1 + n2)
> # func1()
> # func2()   # func2相当于func1中的变量，只要在func1的外部访问，都访问不到  NameError: name 'func2' is not defined
> 
> # 2.嵌套函数的调用
> # 方式一：在外部函数中直接调用内部函数
> def func1():
>     print('外部~~~~11111')
>     n1 = 10
>     def func2():
>         n2 = 20
>         print(n1 + n2)
>         print('内部~~~111111')
>     func2()    # 调用内部函数func2
>     print('外部~~~~222222')
> func1()
> 
> # 方式二：将内部函数作为外部函数的返回值返回
> def func1():
>     print('外部~~~~11111')
>     n1 = 10
>     def func2():
>         n2 = 20
>         print(n1 + n2)
>         print('内部~~~111111')
> 
>     print('外部~~~~222222')
> 
>     # 一个函数作为另一个函数的返回值使用，只需要书写函数名即可,因为要返回函数本身，在func1的外面可以间接的调用内部函数
>     return func2
> 
> f = func1()   # f = func2
> print(f)  # <function func1.<locals>.func2 at 0x0000019A60BFF040>
> f()  # 相当于调用的是func2
> ```

#### 4.闭包【重点掌握】

> ​	函数只是一段可执行代码，编译后就“固化”了，每个函数在内存中只有一份实例，得到函数的入口点便可以执行函数了。函数还可以嵌套定义，即在一个函数内部可以定义另一个函数，有了嵌套函数这种结构，便会产生闭包问题
>
> 闭包：如果两个函数嵌套定义，如果在内部函数中访问了外部函数中的变量，则构成一个闭包
>
> ```Python
> # 闭包：如果两个函数嵌套定义，如果在内部函数中访问了外部函数中的变量，则构成一个闭包   *********
> # 闭包的常见写法
> # a.内外部函数均无参
> def func1():
>     n1 = 10
>     def func2():
>         n2 = 20
>         print(n1 + n2)
>     return func2
> f = func1()
> print('外部函数调用完毕')  # 当外部函数被调用完毕之后，按理n1会被销毁
> f()         # 但是，在函数的嵌套定义中，由于内部函数访问了外部函数中的变量，所以当外部函数调用完毕之后，内部函数仍然可以访问到外部函数中的变量
> 
> # b.外部函数有参
> # a,b和n1都属于外部函数中的变量，只要这三者中的任何一个被func2访问，则都会构成闭包
> def func1(a,b):
>     n1 = 10
>     def func2():
>         n2 = 20
>         print(n1 + n2,a,b)
>     return func2
> f = func1(3,2)
> f()
> 
> # c.内外部函数有参
> def func1(a,b):
>     n1 = 10
>     def func2(num1,num2,num3):
>         n2 = 20
>         print(n1 + n2,a,b,num1,num2,num3)
>     return func2
> f = func1(3,2)
> f(55,66,77)   # 注意：相当于调用的是func2，所以一定要注意和func2的参数保持匹配
> 
> # d.内外部函数有参,内部函数有返回值
> def func1(a,b):
>     n1 = 10
>     def func2(num1,num2,num3):
>         n2 = 20
>         print(n1 + n2,a,b,num1,num2,num3)
>         return n1 + n2
>     return func2
> f = func1(3,2)
> r = f(55,66,77)
> print(r)
> 
> # 注意：虽然是函数嵌套定义，虽然是闭包，但是内外部函数本质上和普通函数的用发完全相同，默认参数，关键字参数，不定长参数和返回值都一样使用
> ```

#### 5.变量的作用域【重点掌握】

##### 5.1作用域的分类

> 变量的作用域指的是变量可以使用的范围
>
> 程序的变量并不是在任意位置都可以访问，访问权限取决于这个变量是在哪里定义的
>
> 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。
>
> 【面试题】Python的作用域一共有4种，分别是
>
> ​	L:Local,局部作用域，如果嵌套定义的前提下，特指内部函数
>
> ​	E:Enclosing,函数作用域【外部函数中】
>
> ​	G:Global,全局作用域
>
> ​	B:Built-in,内建作用域【内置作用域】  num = int("244")
>
> ```Python
> # 1.变量作用域的分类
> # a.单层循环
> # num1 = 10      # 全局作用域：全局变量---->在当前py文件中都可以访问该变量
> # def func1():
> #     num2 = 20  # 局部作用域：局部变量---->只能在当前函数中被访问
> #     print(num1,num2)
> # func1()
> # print(num1)
> 
> # b.嵌套函数
> num1 = 10       # 全局作用域：全局变量------》在当前py文件中都可以访问该变量
> def func1():
>     num2 = 20   # 函数作用域：局部变量-----》此处定义的变量在外部函数中都可以访问，包括内部函数
>     def func2():
>         num3 = 30   # 局部作用域：局部变量-----》此处定义的变量只能在内部函数中被访问
>         print('local:',num1,num2, num3)
>     func2()
>     print('enclosing:',num1,num2)
> func1()
> print('global:',num1)
> 
> # c.当不同作用域内的变量重名
> # 注意：当不同作用域内的变量重名，在访问的时候遵循【就近原则】
> num = 10
> def func1():
>     num = 20
>     def func2():
>         num = 30
>         print('local:',num)   # 30
>     func2()
>     print('enclosing:',num)    # 20
> func1()
> print('global:',num)   # 10
> 
> # 2.
> '''
> 会引入新的作用域：函数，类，模块
> 不会引入新的作用域：if  for  while  try-except   with .....
> '''
> n = 12
> if n > 10:
>     a = 66
>     print(a)
> print(a)
> 
> def func():
>     b = 88
>     print(b)
> func()
> # print(b)   # NameError: name 'b' is not defined
> ```

##### 5.2global和nonlocal【面试题】

> 【面试题】
> 二者都是使用在变量重名的前提下
> global:全局的，在局部变量中【单层函数】 或者  函数作用域中【嵌套函数】声明一个变量来自于全局变量，对全局变量做出指定的操作【一般指的是对变量重新赋值】
> nonlocal:不是局部的，如果出现了函数的嵌套定义，在内部函数中需要使用函数作用域中的变量
>
> ```Python
> # 1.global
> # a
> # 注意：不同作用域内的变量重名，二者是两个不同的变量，相互之间没有任何影响
> n = 5
> def f():
>     n = 9
> f()
> print(n)  # 5
> 
> # b.【面试题】阅读下面的代码，写出代码执行的结果
> # 错误代码
> # a = 5
> # def func():
> #     a += 1   # UnboundLocalError: local variable 'a' referenced引用/访问 before assignment赋值
> # func()
> # print(a)
> 
> '''
> 分析：
>     a.a += 1，等价于a = a + 1
>     b.a = a + 1的执行顺序：先计算a + 1,将结果赋值给a
>     c.当全局和局部同时出现a = xxx的语法，则认为是定义了不同作用域内重名的变量，访问的原则是就近原则
>     d.a = a + 1,要先计算a + 1，而a又就近要访问局部的变量，此时会出现矛盾，所以导致代码报错
> '''
> 
> # 正确写法
> # 思路一：两个不同的变量
> a = 5
> def func():
>     a = 6
>     a += 1   # 给局部变量a重新赋值
>     print('内部:',a)
> func()
> print(a)    # 5
> 
> # 思路二：同一个变量
> a = 5
> def func():
>     # 声明下面代码中使用到的a变量来自于全局变量
>     global a
>     a += 1
>     print('内部:',a)   # 6
> func()
> print(a)    # 6
> 
> # c.global应用在嵌套函数中
> # 下面代码中的m是两个不同的变量
> m = 20
> def f1():
>     m = 60  # 定义了一个新的变量
>     def f2():
>         print('ok')
>     f2()
> f1()
> print(m)  # 20
> 
> # 下面代码中的m是同一个变量
> m = 20
> def f1():
>     global m
>     m = 60    # 对全局变量m做了重新赋值
>     def f2():
>         print('ok')
>     f2()
> f1()
> print(m)  # 60
> 
> # 2.nonlocal
> # local:局部
> # nonlocal:不是局部，特指的是函数作用域
> # 使用场景：必须是嵌套定义的函数，发生在函数作用域和局部作用域之间
> # a.
> # 错误写法
> # def f1():
> #     name = '123'
> #     def f2():
> #         name += 'abc'   # name = name + 'abc' UnboundLocalError: local variable 'name' referenced before assignment
> #         print('内部：',name)
> #     f2()
> #     print('外部:',name)
> # f1()
> 
> # 正确写法
> # 思路一：两个不同的变量
> def f1():
>     name = '123'
>     def f2():
>         name = '456'   # 定义了新的变量
>         name += 'abc'   # 相当于给局部作用域的变量做出重新赋值
>         print('内部：',name)  # 456abc
>     f2()
>     print('外部:',name)   # 123
> f1()
> 
> # 思路二：同一个变量
> def f1():
>     name = '123'
>     def f2():
>         nonlocal name
>         name += 'abc'   # 相当于给函数作用域内的name进行重新赋值
>         print('内部：',name)  # 123abc
>     f2()
>     print('外部:',name)   # 123abc
> f1()
> 
> # 3.
> x = 10
> def f1():
>     x = 20
>     def f2():
>         x = 30
>         print('内部：',x)
>     f2()
>     print('外部:',x)
> f1()
> print('全局:',x)
> '''
> 内部： 30
> 外部: 20
> 全局: 10
> '''
> x = 10
> def f1():
>     global x
>     x = 20   # 给全局变量x重新赋值
>     def f2():
>         x = 30
>         print('内部：',x)
>     f2()
>     print('外部:',x)
> f1()
> print('全局:',x)
> '''
> 内部： 30
> 外部: 20
> 全局: 20
> '''
> # global和nonlocal无法同时使用
> x = 10
> def f1():
>     global x
>     x = 20   # 给全局变量x重新赋值
>     def f2():
>         # nonlocal x   # SyntaxError: no binding for nonlocal 'x' found
>         x = 30   # 给函数作用域内的变量重新赋值
>         print('内部：',x)
>     f2()
>     print('外部:',x)
> f1()
> print('全局:',x)
> ```

#### 6.生成器和迭代器【面试题】

##### 6.1生成器

> 问题：
>
> ​	列表：一次性将所有的元素全部定义出来,如果只需要访问其中的前几个元素，大量的内存空间会被浪费
>
> 解决方案：
>
> ​	使用第n个元素，则只需要生成前n元素，在Python中，将这种一边使用，一般计算的机制被称为生成器(generator)，则在代码执行的过程中，大量的内存空间会被节约下来
>
> 生成器的定义方式有两种：
>
> ```
> a.将列表推导式中的[]改为()
> b.函数结合yield，定义函数生成器
> ```

##### 6.2可迭代对象和迭代器

> 【面试题】简述可迭代对象和迭代器之间的区别和联系
> 区别：
>
> ```
> 可迭代对象：Iterable,可以直接作用于for循环的对象【可以使用for循环遍历其中元素的对象】，
>     如：list,tuple,dict,set，str,range(),生成器等
> 迭代器:Iterator,可以直接作用于for循环,或者可以通过next()获取下一个元素的对象，
>     如：生成器
> ```
>
> 联系：
>
> ```
> 迭代器一定是可迭代对象，但是可迭代对象不一定是迭代器
> 但是，可以通过系统功能iter()将不是迭代器的可迭代对象转换为迭代器
> ```

> ```Python
> # 1.可迭代对象和迭代器
> # isinstance(变量,类型)：判断指定的变量是否是指定的类型，返回布尔值
> 
> from collections.abc import  Iterable,Iterator
> 
> # a.可迭代对象Iterable
> print(isinstance([45,67,8],Iterable))
> print(isinstance((45,67,8),Iterable))
> print(isinstance('faqfa',Iterable))
> print(isinstance({'a':10},Iterable))
> print(isinstance(range(10),Iterable))
> # 全部都是True
> 
> # b.迭代器
> print(isinstance([45,67,8],Iterator))
> print(isinstance((45,67,8),Iterator))
> print(isinstance('faqfa',Iterator))
> print(isinstance({'a':10},Iterator))
> print(isinstance(range(10),Iterator))
> # 全部都是False
> 
> # c.通过系统功能iter()将不是迭代器的可迭代对象转换为迭代器
> print(isinstance(iter([45,67,8]),Iterator))
> print(isinstance(iter((45,67,8)),Iterator))
> print(isinstance(iter('faqfa'),Iterator))
> print(isinstance(iter({'a':10}),Iterator))
> print(isinstance(iter(range(10)),Iterator))
> # 全部都是True
> 
> # 2.生成器
> # a.不管列表中有多少个元素，都会同时出现，占用内存空间
> list1 = [34,56,76,78,9,23,5,56,7,123,34,7]
> print(list1[0])
> list2 = [n ** 2 for n in range(1000)]
> print(list2[0],type(list2))   # <class 'list'>
> 
> # b.生成器：使用第n个元素，则只需要生成前n元素
> # 方式一：将列表推导式中的[]改为()
> r1 = (n ** 2 for n in range(1000))  # 注意：将列表推导式的[]改成().并不是元组推导式，而是生成器
> print(type(r1))   # <class 'generator'>
> print(r1)   # <generator object <genexpr> at 0x0000022826F67C10>
> 
> # 方式二：函数结合yield，定义函数生成器
> # 注意：yield xx被执行一次，则表示给生成器中预定义了一个元素
> def func1():
>     yield  10
> r1 = func1()
> print(r1)  # <generator object func1 at 0x000001EA1AD87D60>
> 
> def func1():
>     yield  10
>     yield 20
>     yield  30
> r1 = func1()
> print(r1)
> 
> def func1(n):
>     for i in range(n):
>         yield i ** 2
> r1 = func1(10)
> print(r1)
> 
> # c.如何访问生成器中的元素
> # 1>for
> # for n in r1:
> #     print(n)
> 
> # 2>list(生成器)
> # print(list(r1))
> 
> # 3>next(生成器)  推荐
> # next()调用一次，表示从生成器中获取一个元素，按照顺序获取的，生成器是一个只出不进的容器
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> # 当生成器中的元素全部获取完毕，接着再获取，则报错StopIteration
> # print(next(r1))
> 
> # 使用next获取生成器中的所有元素，同时借助于循环
> while True:
>     try:
>         ele = next(r1)
>         print(ele)
>     except StopIteration:
>         print('生成器中的元素获取完毕')
>         break
> 
> 
> print(isinstance(r1,Iterable))   # True
> print(isinstance(r1,Iterator))   # True
> ```

#### 7.案例

> ```Python
> '''
> 后台管理员管理前台会员信息系统
> 
> 1. 后台管理员只有一个用户: admin, 密码: admin
> 2. 当管理员登陆成功后， 可以管理前台会员信息.
> 3. 会员信息管理包含:
>       添加会员信息
>       删除会员信息
>       查看会员信息
>       退出
> '''
> # 定义列表，存储会员信息
> users_list = []
> # [{'姓名':'xxx','密码':'xxxx'}，]
> 
> # 封装函数
> def add_user(name,pwd):
>     print('添加会员信息'.center(50, '*'))
>     users_list.append(dict(zip(['姓名','密码'],[name,pwd])))
>     print('添加成功！')
> def del_user(name):
>     print('删除会员信息'.center(50, '*'))
>     # 设定：如果查找到会员信息，只删除一个【其他的同名的会员信息不做处理】
>     for user in users_list:
>         if user['姓名'] == name:
>             users_list.remove(user)
>             print('删除成功')
>             break
>     else:
>         print('会员信息不存在')
> def show_user():
>     print('查看会员信息'.center(50, '*'))
>     for user in users_list:
>         print(f'会员名：{user["姓名"]},密码:{user["密码"]}')
> 
> def main():
>     print('管理员登录界面'.center(50, '*'))
>     for i in range(3):
>         # 引导输入管理员的用户名和密码
>         admin_name = input('请输入管理员的用户名:')
>         admin_pwd = input('请输入管理员的密码：')
>         if admin_name == 'admin' and admin_pwd == 'admin':
>             print('管理员登录成功！')
>             print('欢迎进入xxx会员管理系统')
>             # 进入管理系统
>             # 因为进入管理系统之后，具体要做哪些操作，进行几次操作不确定
>             while True:
>                 print('''********操作目录**********
>                         1.添加会员信息
>                         2.删除会员信息
>                         3.查看会员信息
>                         4.退出''')
>                 # 引导管理员执行相应的操作
>                 choice = input('请输入需要执行的操作：')
>                 if choice == '1':
>                     user_name = input('请输入会员名：')
>                     user_pwd = input('请输入会员密码：')
>                     add_user(user_name, user_pwd)
>                 elif choice == '2':
> 
>                     user_name = input('请输入需要删除的会员名：')
>                     del_user(user_name)
>                 elif choice == '3':
>                     show_user()
>                 elif choice == '4':
>                     print('欢迎再次使用')
>                     # 此处的break结束的是while死循环
>                     # break  # 扩展：此处的break可以替换为exit()，表示退出程序
>                     # exit()
>                     return
>                 else:
>                     print('输入有误，暂无此操作，请输入正确的操作编号')
>             # 如果前面使用的是break，则此处的break需要
>             # break
>         else:
>             if i == 2:
>                 continue
>             print('管理员登录失败,请重新输入')
>     else:
>         print('已经错误三次，禁止管理员登录')
> 
> main()   # 程序执行的入口
> ```
>
> ```Python
> '''
> 后台管理员管理前台会员信息系统
> 
> 1. 后台管理员只有一个用户: admin, 密码: admin
> 2. 当管理员登陆成功后， 可以管理前台会员信息.
> 3. 会员信息管理包含:
>       添加会员信息
>       删除会员信息
>       查看会员信息
>       退出
> '''
> # 定义列表，存储会员信息
> users_list = []
> # [{'姓名':'xxx','密码':'xxxx'}，]
> 
> def main():
>     # 封装函数
>     def add_user(name, pwd):
>         print('添加会员信息'.center(50, '*'))
>         users_list.append(dict(zip(['姓名', '密码'], [name, pwd])))
>         print('添加成功！')
> 
>     def del_user(name):
>         print('删除会员信息'.center(50, '*'))
>         # 设定：如果查找到会员信息，只删除一个【其他的同名的会员信息不做处理】
>         for user in users_list:
>             if user['姓名'] == name:
>                 users_list.remove(user)
>                 print('删除成功')
>                 break
>         else:
>             print('会员信息不存在')
> 
>     def show_user():
>         print('查看会员信息'.center(50, '*'))
>         for user in users_list:
>             print(f'会员名：{user["姓名"]},密码:{user["密码"]}')
> 
>     # 调用函数
>     print('管理员登录界面'.center(50, '*'))
>     for i in range(3):
>         # 引导输入管理员的用户名和密码
>         admin_name = input('请输入管理员的用户名:')
>         admin_pwd = input('请输入管理员的密码：')
>         if admin_name == 'admin' and admin_pwd == 'admin':
>             print('管理员登录成功！')
>             print('欢迎进入xxx会员管理系统')
>             # 进入管理系统
>             # 因为进入管理系统之后，具体要做哪些操作，进行几次操作不确定
>             while True:
>                 print('''********操作目录**********
>                         1.添加会员信息
>                         2.删除会员信息
>                         3.查看会员信息
>                         4.退出''')
>                 # 引导管理员执行相应的操作
>                 choice = input('请输入需要执行的操作：')
>                 if choice == '1':
>                     user_name = input('请输入会员名：')
>                     user_pwd = input('请输入会员密码：')
>                     add_user(user_name, user_pwd)
>                 elif choice == '2':
> 
>                     user_name = input('请输入需要删除的会员名：')
>                     del_user(user_name)
>                 elif choice == '3':
>                     show_user()
>                 elif choice == '4':
>                     print('欢迎再次使用')
>                     # 此处的break结束的是while死循环
>                     # break  # 扩展：此处的break可以替换为exit()，表示退出程序
>                     # exit()
>                     return
>                 else:
>                     print('输入有误，暂无此操作，请输入正确的操作编号')
>             # 如果前面使用的是break，则此处的break需要
>             # break
>         else:
>             if i == 2:
>                 continue
>             print('管理员登录失败,请重新输入')
>     else:
>         print('已经错误三次，禁止管理员登录')
> 
> main()   # 程序执行的入口
> ```