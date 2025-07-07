### Day16作业讲解

> ```Python
> # 4.写出下面代码的输出结果并说明原因
> list1 = ['a', 'b', 'c', 'd', 'e']
> # 注意：只要符合切片的语法，不会报错，比如列表。返回的结果无非就是空和非空的区别
> print(list1[10:])   # []
> 
> # 5.写出下面代码的输出结果并说明原因
> str1 = 'hello python'
> str1.title()
> # 注意：字符串是不可变的数据类型，所以但凡调用了字符串更改的函数，返回一个新的字符串，对原字符串没有任何影响
> print(str1)  # hello python
> 
> str1 = 'hello python'
> str1 = str1.title()
> # 如果调用了字符串的函数，并对原变量进行了重新赋值，结果就是函数的返回值
> print(str1)  # Hello Python
> 
> # 8.在控制台中录入，所有学生名字，如果姓名重复，则提示"姓名已经存在"，不添加到列表中，如果录入空字符串，则倒序打印所有学生
> stus_list = []
> def func():
>     while True:
>         name = input('请输入学生的名字【无任何输入则退出】：')   # '':空字符串  ' '：非空字符串
>         if not name:
>             stus_list.reverse()
>             print(stus_list)
>             break
> 
>         if name in stus_list:
>             print('姓名已经存在')
>         else:
>             stus_list.append(name)
> func()
> 
> 
> # 10.有如下商品价格：568，239，368，425，121，219，834，1263，26，请输入随意一个价格区间进行商品的筛选，
> # 并能够对筛选出的商品进行从大到小和从小到大进行排序，并求出这个区间的商品的平均价格
> price_list = [568,239,368,425,121,219,834,1263,26]
> min_price,max_price = eval(input('请输入两个数字表示价格区间：'))
> result_list = []
> for price in price_list:
>     if price in range(min_price,max_price):
>         result_list.append(price)
> 
> if result_list:
>     new_list = result_list.copy()
>     # 升序
>     new_list.sort()
>     print(new_list)
> 
>     # 降序
>     new_list.reverse()  # new_list.sort(reverse=True)
>     print(new_list)
> 
>     # 平均价格
>     avg_price = sum(result_list) / len(result_list)
> else:
>     print('没有符合给定区间的价格数据')
> ```

### 二、高阶函数【重点掌握】

> 函数的本质：函数是一个变量，函数名是一个变量名，一个函数可以作为另一个函数的参数或返回值使用
>
> 如果A函数作为B函数的参数，B函数调用完成之后，会得到一个结果，则B函数被称为高阶函数
>
> 常用的高阶函数：map(),reduce(),filter(),sorted()

#### 1.map()

> map(func,iterable)，返回值是一个iterator【容器，迭代器】
>
> ​	func:函数
> 	iterable：可迭代对象【容器】，可以是多个，常用列表
>
> 功能：将iterable容器中的每一个元素传递给func,func返回一个结果，结果会成为iterator中的元素
>
>  容器----》func----》新的容器
>
> ```Python
> # 函数的本质：函数就是一个变量，函数名相当于是一个变量名，所以一个函数可以作为另一个函数的参数或返回值使用
> # 一个函数可以作为另一个函数的返回值的应用：函数可以嵌套定义【闭包】
> # 一个函数可以作为另一个函数的参数的应用：列表.sort(key=func) 或 max/min(key=func)
> 
> # 高阶函数：如果a函数作为b函数的参数使用，b函数最终返回一个结果,则将b函数称为高阶函数
> # 常用的高阶函数：map()/reduce()/filter()/sorted()
> 
> '''
> map:映射
> map(func,iterable),返回值是一个iterator【迭代器】
>     func：函数
>     iterable：可迭代对象，如：列表，元组，字符串等，此处的可迭代对象可以是多个
> 功能：将iterable中的每一个元素会自动传参给func函数，func会返回一个值，该值会称为iterator中的元素
> 简单来说：iterable-----》func----->iterator
> '''
> 
> # 1.生成一个容器，其中的元素是1 4 9 16 25 36 49 64 81
> # a.
> l1 = [n ** 2 for n in range(1,10)]
> print(l1)
> 
> # b.
> ge2 = (n ** 2 for n in range(1,10))
> print(ge2)
> 
> # c.
> def f(x):
>     return x ** 2
> r1 = map(f,range(1,10))
> print(r1)   # <map object at 0x000002A4BC297D90>
> # print(next(r1))
> # print(next(r1))
> # print(next(r1))
> l1 = list(r1)
> print(l1)
> 
> # d.*******
> r2 = map(lambda x:x ** 2,range(1,10))
> print(r2)
> print(list(r2))
> 
> # 练习；将1~100之间的5的倍数找出来，使用map实现
> list1 = [n for n in range(1,101) if n % 5 == 0]
> print(list1)
> 
> iter1 = map(lambda n:n,range(5,101,5))
> print(iter1)
> print(list(iter1))
> 
> # 2.
> # 注意1:map中的func函数需要设置几个参数，取决于有几个iterable参与运算
> # 注意2：当有多个iterable参与运算，则会自动调用func函数，将多个iterable相同位置处的元素同时传参给func
> def f2(m,n):
>     return m + n
> r1 = map(f2,[1,2,3],[4,5,6,8,2])
> print(r1)
> print(list(r1))
> 
> r2 = map(lambda m,n:m + n,[1,2,3],[4,5,6,8,2])
> print(r2)
> ```

#### 2.reduce()

> reduce(func,seq)
>
> ​	func:函数
> ​	seq:序列【容器】
>
> 功能：减少
>
> 首先将seq中的第0个元素和第1个元素传递给func,进行运算，返回结果1
> 接着，将 结果1 和第2个元素传递给func,进行运算，返回结果2
> 接着，将 结果2 和第3个元素传递给func,进行运算，返回结果3
> ....
> 直到所有的元素全部参与运算，表示运算结束
>
> ```Python
> '''
> reduce:减少
> functools.reduce(func,sequence),返回值是一个value
>     func：函数
>     sequence：序列，如：列表，元组，字符串
> 功能：首先将seq中的第0个和第1个元素传递给func，进行指定的运算，返回结果a
>      接着，将 结果a 和第2个元素传递给func，进行指定的运算，返回结果b
>      接着，将 结果b 和第3个元素传递给func，进行指定的运算，返回结果c
>      .....
>      直到seq中的所有元素全部参与运算，才会停止，最后得到一个结果n
> For example：
>     reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
>     计算过程：((((1+2)+3)+4)+5)
> '''
> 
> '''
> 注意：
>     a.func函数必须设置两个参数，设置1个返回值
>     b.区别于map，reduce使用之前一定要导入functools
> '''
> 
> from functools import  reduce
> 
> # 1.已知列表 [1, 2, 3, 4, 5],求其中所有元素的和
> list1 = [1, 2, 3, 4, 5]
> def f(x,y):
>     # print(x,y)
>     return x + y
> r1 = reduce(f,list1)
> print(r1)
> 
> r1 = reduce(lambda x,y:x + y,list1)
> print(r1)
> 
> # 练习1：用reduce求1~100之间所有整数的和
> print(reduce(lambda x,y:x + y,range(1,101)))
> 
> # 练习2：用reduce求15的阶乘
> print(reduce(lambda x,y:x * y,range(1,16)))
> 
> # 练习3：已知[3,1,7,4],得到3174
> '''
> 3 1--->31---->3 * 10 + 1
> 31 7--->317--->31 * 10 + 7
> 317 4---->3174---->317 * 10 + 4
> '''
> print(reduce(lambda x,y:x * 10 + y,[3,1,7,4]))
> 
> ```

#### 3.filter()

> filter(func,iterable):过滤
>
> ​	func:函数
> 	iterable：可迭代对象
>
> 功能：将iterable中的元素依次传递给func,根据func的返回值决定是否保留该元素,如果func的返回值为True,则表示当前元素需要保留，如果为False，则表示过滤
>
> ```Python
> '''
> filter:过滤
> filter(func,iterable),返回值是一个iterator
>     func：函数
>     iterable：可迭代对象，如：列表，元组，字符串等，此处的可迭代对象可以是多个
> 功能：将iterable中的元素依次传递给func函数，根据func的返回值决定是否保留该元素，
>     如果func的返回值为True，则表示当前元素需要保留，如果func的返回值为False，则表示当前元素需要过滤掉
> '''
> 
> '''
> 注意：
>     a.func必须设置一个参数
>     b.func必须设置返回值，且返回值必须是布尔值
> '''
> 
> # 1.将1~100之间的5的倍数找出来
> # a.
> l1 = [n for n in range(1,101) if n % 5 == 0]
> print(l1)
> 
> # b.
> def f(x):
>     if x % 5 == 0:
>         return True
>     return False
> r1 = filter(f,range(1,101))
> print(r1)
> print(list(r1))
> 
> # c
> r2 = filter(lambda x:True if x % 5 == 0 else False,range(1,101))
> print(r2)
> print(list(r2))
> 
> r2 = filter(lambda x:x % 5 == 0,range(1,101))
> print(r2)
> print(list(r2))
> ```

#### 4.sorted()

> 【面试题】列表中的sort函数和高阶函数sorted的区别和联系
> 1.调用语法：
>
> ​	列表.sort(reverse,key=func),
>
> ​      	sorted(iterable,reverse,key=func)
>
> 2.结果：sort是在原列表内部排序的，sorted是生成了一个新的列表
> 3.二者默认情况下都是升序排序,如果要降序，则都是设置reverse=True
>
> 4.二者如果需要自定义排序规则，都是设置key=func
>
> ```python
> students = [
> {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
> '15300022838'},
> {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '静静', 'age': 16, 'score': 100, 'gender': '不明', 'tel':
> '15300022428'},
> {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
> '15300022839'},
> {'name': 'Bob', 'age': 18, 'score': 98, 'gender': '男', 'tel':
> '15300022839'}
> ]
> ```

> ```python
> '''
> sorted(iterable,reverse,key=func)
> '''
> 
> '''
> 【面试题】lst.sort()和sorted()之间的区别
> 1.二者的调用方式不同
>     lst.sort(reverse,key)，sorted(lst,reverse,key)
> 2.返回值不同
>     lst.sort()返回None,是在原列表内部直接排序的
>     sorted()返回一个新的列表，对原列表没有任何影响
> 3.二者默认情况下都是升序，如果要降序，都是设置reverse=True
> 4.sort只能列表调用，但是sorted可以适用于任意的可迭代对象
> 5.二者默认的情况下，都只针对列表中的元素可以比较大小的情况，如果要自定义排序规则，则都要设置key=func
> '''
> 
> # 1.二者的调用方式不同，返回值不同
> # 升序
> lst = [34,5,34,5,56,7,19,4]
> lst.sort()
> print(lst)
> 
> lst = [34,5,34,5,56,7,19,4]
> new_list = sorted(lst)
> print(new_list)
> 
> # 降序
> lst = [34,5,34,5,56,7,19,4]
> lst.sort(reverse=True)
> print(lst)
> 
> lst = [34,5,34,5,56,7,19,4]
> new_list = sorted(lst,reverse=True)
> print(new_list)
> 
> # 2.key=func
> list1 = ['4gh','34m577457','faf5bb','2355']
> list1.sort(key=len)
> print(list1)
> 
> list1 = ['4gh','34m577457','faf5bb','2355']
> new_list1 = sorted(list1,key=len)
> print(new_list1)
> 
> # 练习
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
> # 对年龄进行升序
> students1 = students.copy()
> # students1.sort(key=lambda dic:dic['age'])
> # print(students1)
> 
> # new_students1 = sorted(students1,key=lambda dic:dic['age'])
> # print(new_students1)
> 
> # 对成绩进行降序
> # students1.sort(reverse=True,key=lambda dic:dic['score'])
> # print(students1)
> 
> new_students1 = sorted(students1,reverse=True,key=lambda dic:dic['score'])
> print(new_students1)
> ```