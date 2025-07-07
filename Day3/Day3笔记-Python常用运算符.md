### Day2作业讲解

> ```Python
> # 2.已知数据’aaa‘,'bbb','ccc',用一个print输出，最终结果为aaa=bbb=ccc
> print('aaa','bbb','ccc',sep='=')
> print('%s=%s=%s' % ('aaa','bbb','ccc'))
> print('{}={}={}'.format('aaa','bbb','ccc'))
> print(f'{"aaa"}={"bbb"}={"ccc"}')
> 
> # 4.从控制台输入圆的半径，计算该圆的周长和面积，圆周率可以定义为3.14
> PI = 3.14
> r = float(input('请输入圆的半径：'))
> length = 2 * PI * r
> area = PI * r * r   # r ** 2 或者 pow(r,2)
> print(f'该圆的周长:{length:.2f},面积:{area:.2f}')
> ```

### 一、运算符和表达式【重点掌握】

#### 1.算术运算符

> | 运算符  |   说明    |
> | :--: | :-----: |
> |  +   |    加    |
> |  -   |    减    |
> |  *   |    乘    |
> |  /   |    除    |
> |  //  |   取整    |
> |  %   | 求余（取模）  |
> |  **  | 求幂(求次方) |
>

> ```Python
> """
> 注意：
>     a.如果整数和浮点数进行运算，结果都是浮点数，换句话说，但凡表达式中出现浮点数进行数学运算，结果都是浮点数
>     b.只要是/运算，结果都是浮点数
>     c.//的结果为/的结果的整数部分，不涉及四舍五入
>     d.算术运算符的优先级问题:**  》  *  / //  %  》 + -
> """
> ```

> ```Python
> m = 8
> n = 3
> 
> # 1. + -
> print(m + n)
> print(m - n)
> 
> print(8.0 + 3)
> print(8 + 3.0)
> print(8.0 - 3.0)
> 
> # 2.*  /
> print(m * n)
> print(m / n)
> 
> # 只要是/运算，结果都是浮点数
> print(10 / 5)   # 2.0
> 
> print(8.0 * 3)
> print(8 * 3.0)
> print(8.0 * 3.0)
> 
> # 3.//:整除或取整
> print(m // n)   # 2
> 
> print(5.0 / 2)
> print(5.0 // 2)   # 2.0
> 
> # 4.%:求余或取模
> print(m % n)   # 8整除3之后的余数
> 
> print(13 // 3)
> print(13 % 3)
> print(13.0 % 3)
> 
> # 5.**：求幂或求次方
> print(m ** n)
> print(5.0 ** 3)
> # 扩展：m ** n 等价于pow(m,n)
> print(pow(m,n))
> 
> # 6.优先级
> # 算术运算符的优先级：**  >  *和/ // %  >  +和-
> print(2 + 4 * 5)  # 22
> print(2 * 5 ** 3)  # 250
> 
> print((2 * 5) ** 3)  # 1000
> ```

#### 2.赋值运算符

> |           运算符           |   说明    |
> | :---------------------: | :-----: |
> |            =            | 简单赋值运算符 |
> | +=、-=、*=、/=、%=、//=、**=等 | 复合赋值运算符 |
>

> ```Python
> """
> 注意：
>     a.=用于定义变量或给变量重新赋值
>     b.=的右边只要是一个数据或可以计算结果的表达式，都可以给=左边的变量赋值
>     c.无论=右边的表达式多么复杂，永远都是先计算=右边表达式的结果，然后给=左边的变量赋值，换句话，=的优先级最低
>     d.+= -= *= /=  //=  %=  **=的工作原理：必须先定义变量，然后给该变量进行相应的运算，最后给该变量进行重新赋值
> """
> ```

> ```Python
> # 1.简单赋值运算符：=
> name = 'abc'    # 定义变量，将‘abc’赋值给name
> name = 'xyz'    # 重新赋值，将'xyz'赋值给name
> 
> # =的右边只要是一个数据或者可以计算结果的表达式，都可以给=左边的变量进行赋值
> n1 = True
> print(n1)
> n2 = 2 + 3 * 2 - 10 + 2 ** 10
> print(n2)  # 1022
> 
> # 【面试题】
> # 错误写法
> # n3 = (n2 = n1 + 10)
> # print(n3)
> '''
> 原因：
>     n2 = n1 + 10-----》将n1 + 10的结果赋值给n2
>     n3 = (n2 = n1 + 10)-----》只是将n1+10的结果赋值给了n2，但是n2 = n1 + 10整体没有结果，无法给n3赋值
> '''
> # 正确写法一
> # n2 = n1 + 10
> # n3 = n2
> # print(n3)
> 
> # 正确写法二
> n3 = (n2 == n1 + 10)
> print(n3)  # False
> 
> # 2.复合赋值运算符：+=  -=  *=  /=  //=  %=  **=
> m1 = 3
> m1 = 9    # 重新赋值
> print(m1)
> 
> n1 = 3
> n1 += 9  # 等价于n1 = n1 + 9,先计算n1 + 9,然后给n1进行重新赋值
> print(n1)
> 
> # 问题1：一定要书写成+=，而不是+ =
> a = 3
> a *= 10
> print(a)
> 
> # 问题2：在使用复合赋值运算符时，一定要先定义变量，然后才使用
> # b += 1   # NameError: name 'b' is not defined
> 
> ```

#### 3.关系运算符

> | 运算符  |  说明  |
> | :--: | :--: |
> |  ==  |  相等  |
> |  !=  | 不相等  |
> |      |      |
> |  >   |  大于  |
> |  <   |  小于  |
> |  >=  | 大于等于 |
> |  <=  | 小于等于 |
>

> ```Python
> """
> 注意：
>     a.关系运算符，也被称为条件运算符或比较运算符
>     b.=表示赋值，==表示比较
>     c.关系运算符运算的结果肯定是一个布尔值，表达式成立则结果为True，表达式不成立则结果为False
>     d.关系运算符一般结合if语句或while循环使用
> """
> ```

> ```Python
> # 1.基本使用
> m = 34
> n = 4
> print(m == n)
> print(m != n)
> print(m > n)
> print(m >= n)
> print(m < n)
> print(m <= n)
> 
> # 2.除了数字可以比较大小之外，字符串也可以比较大小
> # 字符串比较大小的工作原理：依据的时ASCII码
> # 虽然字符串可以比较大小，但是在实际应用中实际意义不大，使用最多的是==
> '''
> 常见ASCII码的大小规则：数字< 大写字母 < 小写字母。
> 1.数字比字母要小。如 “7”<“F”；
> 2.数字0比数字9要小，并按0到9顺序递增。如 “3”<“8” ；
> 3.字母A比字母Z要小，并按A到Z顺序递增。如“A”<“Z” ；
> 4.同个字母的大写字母比小写字母要小32。如“A”<“a” 。
> 5.几个常见字母的ASCII码大小： “A”为65；“a”为97；“0”为 48 
> '''
> print('a' > 'A')
> print('A' > '9')
> 
> # 扩展：chr(),ord()
> # chr():获取一个十进制数字在ASCII表中对应的字符
> print(chr(65))
> print(chr(97))
> 
> # ord():获取字符在ASCII表中对应的十进制
> print(ord('A'))
> print(ord('4'))
> ```

#### 4.逻辑运算符

> ​	逻辑运算符是用来做逻辑计算的，就像之前用到的比较运算符 ，每一次比较其实就是一次条件判断，都会得到一个相应的True或者False的值，而逻辑运算符的操作数就是一个用来做条件判断的表达式或者变量

> | 运算符  |  说明  |
> | :--: | :--: |
> | and  |  与   |
> |  or  |  或   |
> | not  |  非   |

> 重点：短路原则
>
> a.A and B,如果A为False，不需要计算B的值，整个表达式的结果为False
>
> b.A or B,如果A为True，不需要计算B的值，整个表达式的结果为True
>
> c.and和or混合使用
>
> ​	1>表达式从左往右运算，如果or的左侧为True，则会短路or后面所有的表达式【不管是and还是or连接】，整个表达式的结果为True
>
> ​	2>表达式从左往右运算,如果and的左侧为False,则短路后面所有的and，直到or出现，接着计算
>
> ​	3>如果or的左侧为False，或者and的左侧为True，则不能使用短路逻辑判断
>
> ```Python
> """
> 注意：
>     a.逻辑运算符主要用于进行逻辑判断，所以一般结合if语句或while循环使用较多
>     b.逻辑运算符结合关系运算符使用较多
>     c.表示假的数据：0   0.0   ""   []   ()    {}   None False等
>     d.not xx:不管xx是哪种数据类型，得到的结果肯定是布尔值
>       and和or得到的结果不一定是布尔值，根据具体参与运算的数据而定
> """
> ```

> ```Python
> # 1.and：与
> '''
> 真  and  真 ----》真
> 真  and  假----》假
> 假  and  真 ----》假
> 假  and  假 ----》假
> 
> 规律：一假为假，全真为真
> '''
> print('abc' and 1)
> print('abc' and 'xyz')
> print('abc' and [4,6,7])
> print('abc' and True)
> print('abc' and 34.6)
> print('abc' and 56)
> 
> print('abc' and 0)
> print('abc' and '')
> print('abc' and [])
> print('abc' and False)
> print('abc' and 0.0)
> print('abc' and {})
> 
> print('+++++++++')
> 
> print(0 and 1)
> print(0 and 'xyz')
> print(0 and [4,6,7])
> print(0 and True)
> print(0 and 34.6)
> print(0 and 56)
> 
> print(0 and 0)
> print(0 and '')
> print(0 and [])
> print(0 and False)
> print(0 and 0.0)
> print(0 and {})
> 
> '''
> 结论：A  and  B
>     a.如果A为真，则A and  B整个表达式的结果为B的值
>     b.如果A为假，则A and B整个表达式的结果为A的值，此时的B会被短路
> '''
> 
> # 2.or:或
> '''
> 真  or  真 ----》真
> 真  or  假----》真
> 假  or  真 ----》真
> 假  or  假 ----》假
> 
> 规律：一真为真，全假为假
> '''
> 
> print('abc' or 1)
> print('abc' or 'xyz')
> print('abc' or [4,6,7])
> print('abc' or True)
> print('abc' or 34.6)
> print('abc' or 56)
> 
> print('abc' or 0)
> print('abc' or '')
> print('abc' or [])
> print('abc' or False)
> print('abc' or 0.0)
> print('abc' or {})
> 
> print('+++++++++')
> 
> print(0 or 1)
> print(0 or 'xyz')
> print(0 or [4,6,7])
> print(0 or True)
> print(0 or 34.6)
> print(0 or 56)
> 
> print(0 or 0)
> print(0 or '')
> print(0 or [])
> print(0 or False)
> print(0 or 0.0)
> print(0 or {})
> 
> '''
> 结论：A  or  B
>     a.如果A为真，则A or  B整个表达式的结果为A的值，此时的B会被短路
>     b.如果A为假，则A or B整个表达式的结果为B的值
> '''
> 
> # 3.not:非
> # 注意：not x的结果一定是布尔值
> '''
> not 真----》假
> not  假----》真
> '''
> print(not 0)  # True
> print(not 'abc')   # False
> 
> # 问题一：
> print(not '0')   # False
> print(not 'False')   # False
> 
> # 问题二:优先级：关系运算符 > 逻辑运算符
> x = 45
> y = 23
> z = 100
> print(x < y and y == z)  # 只有两个表达式都成立时结果才是True
> print(x < y or y == z)   # 至少有一个表达式成立时结果就是True
> ```

#### 5.成员运算符

> in：如果在指定的序列中找到值，则返回True，否则返回False
>
> not in:如果在指定的序列中没有找到值，则返回True，否则返回False
>
> ```Python
> # in和not in
> 
> print('x' in 'xyz')  # True
> print('x' not in 'xyz')  # False
> 
> print(34  in [4,34,10])  # True
> print(34 not  in [4,34,10])  # False
> 
> 
> # 注意：一般结合if语句使用，for xx in xxx
> # 判断一个数据在一个容器中在不在的问题，如果存在，结果时True，反之结果就是False
> ```

#### 6.身份运算符

> 身份运算符用于比较两个对象的存储单元
>
> ​	is:判断两个标识符是不是引用自一个对象
>
> ​	is not:判断两个标识符是不是引用自不同对象
>
> ```Python
> # is 和 is not
> 
> '''
> 【面试题】
> ==：比较两个变量的值/内容是否相同
> is:比较两个变量的地址是否相同
> '''
> 
> # 1.不可变的数据类型：int/float/bool/str/tuple/bytes/NoneType
> a = 10
> b = 10
> print(a == b)
> print(a is b)
> 
> print(id(a),id(b),id(10))
> print(id(a) == id(b))  # 等价于is的结果
> 
> c = 20
> print(a == c)
> print(a is c)
> 
> 
> # 2.可变的数据类型：list/dict/set
> list1 = [44,55,66]
> list2 = [44,55,66]
> print(list1 == list2)   # True
> print(list1 is list2)   # False
> print(id(list1) == id(list2))
> 
> list3 = list1
> print(list1 == list3)  # True
> print(list1 is list3)  # True
> print(id(list1) == id(list3))
> 
> print(list1,list2,list3)
> 
> '''
> 结论：
>     如果两个变量的值相同，这两个变量的地址不一定相同
>     如果两个变量的地址相同，则这两个变量中存储的数据一定相同
> '''
> ```

#### 7.运算符优先级

> ​	当出现一个复杂的表达式，有可能多种运算符会混合在一起运算，就会涉及到运算符的优先级。具体如下：
>
> ![运算符优先级](Day3-images/运算符优先级.png)
>
> 注意：在实际项目开发中，当多种运算符进行混合运算时，强烈建议使用小括号来手动控制运算符的优先级，并且尽量将复杂的问题简单化，尽量分步执行
>
> ```Python
> # 1.**的优先级最高
> print(3 + 2 * 4 - 10 ** 2)
> 
> # 2.如果算术运算符和关系运算符混合运算，则算术运算符 > 关系运算符
> print(3 + 5 > 6 ** 2)
> 
> # 3.如果关系运算符和逻辑运算符混合使用，则关系运算符 > 逻辑运算符
> print(3 > 5 and 10 < 45)
> 
> # 4.在Python中可以连写关系运算符
> print(3 > 5 > 7)
> # 等价于
> print(3 > 5 and 5 > 7)
> 
> # 5.在实际应用中，当多种运算符混合使用时，强烈建议使用()来手动控制运算符的优先级，将复杂的问题尽量简单化，提高代码的可读性和可维护性
> ```

