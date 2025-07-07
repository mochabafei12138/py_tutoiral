### 一、会员管理系统

> 根据下面的需求描述，完成简单的用户管理系统，注意封装函数
>
> 1. 后台管理员只有一个用户: admin, 密码: admin
>
> 2. 当管理员登陆账号成功后， 可以管理前台会员信息.
>
> 3. 会员信息管理包含方法:
>    a.添加会员信息
>    b.删除会员信息
>    c.查看会员信息
>
> 4. 对会员按照年龄降序排序
>
> 5. 退出
>
>    ```
>    思路：
>    		1.输入用户名和密码 跟 管理员的账号密码匹配 不一致的话 登陆失败
>    		一致的话 提示登陆成功
>    		并列出 对应的 1 2 3 4 5的操作 输入对应的编号 执行对应的方法
>    		
>    		2.会员信息包含：
>    				会员编号(mid) ---- 编号是在10000到99999中随机选择一个 不能重复
>    				会员姓名(name)
>    				会员性别(sex)
>    				会员年龄(age)
>    				
>    				使用字典保存每个会员信息
>    						例如{'mid':10000, 'name':'乐乐','sex':'男', 'age':20}
>    				使用列表保存所有的会员
>    					例如[{'mid':10000, 'name':'乐乐','sex':'男', 'age':20},{'mid':10001, 'name':'美美','sex':'女', 'age':19}]
>    ```

> ```Python
> import  random
> 
> # 定义列表，存储会员信息
> users_list = []
> # [{},{}......]
> 
> # 一、封装函数
> def get_mid():
>     while True:
>         mid = str(random.randint(10000,99999))   # 后期查询的时候，从控制台输入会员号无需转化
>         if mid not in [dic['mid'] for dic in users_list]:
>             return mid
> def add_user(name,sex,age):
>     mid = get_mid()
>     print(f'你的会员号是:{mid}')
>     users_list.append(dict(zip(['mid','name','sex','age'],[mid,name,sex,age])))
>     print('添加成功！')
> def del_user(mid):
>     # 注意：如果确定列表中的元素是唯一的，则删除可以不做拷贝处理，如果要删除的元素在2个及以上，则需要拷贝
>     for user in users_list:
>         if user['mid'] == mid:
>             users_list.remove(user)
>             print('删除成功')
>             break
>     else:
>         print('会员信息不存在')
> def show_user(mid):
>     for user in users_list:
>         if user['mid'] == mid:
>             print(user)
>             break
>     else:
>         print('会员信息不存在')
> def sort_user():
>     #  方式一
>     # users_list.sort(key=lambda dic:dic['age'],reverse=True)
>     # print(users_list)
>     # 方式二
>     new_list = sorted(users_list,key=lambda dic:dic['age'],reverse=True)
>     print(new_list)
> 
> # 二、调用函数
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
>                         4.对会员信息排序
>                         5.退出''')
>                 # 引导管理员执行相应的操作
>                 choice = input('请输入需要执行的操作：')
>                 if choice == '1':
>                     print('添加会员信息'.center(50, '*'))
>                     name = input('请输入会员名：')
>                     sex = input('请输入会员性别：')
>                     age = int(input('请输入会员年龄：'))
>                     add_user(name, sex, age)
>                 elif choice == '2':
>                     print('删除会员信息'.center(50, '*'))
>                     mid = input('请输入需要删除的会员号：')
>                     del_user(mid)
>                 elif choice == '3':
>                     print('查看会员信息'.center(50, '*'))
>                     mid = input('请输入需要查找的会员号：')
>                     show_user(mid)
>                 elif choice == '4':
>                     print('对会员信息排序'.center(50, '*'))
>                     sort_user()
>                 elif choice == '5':
>                     print('欢迎再次使用')
>                     # 此处的break结束的是while死循环
>                     break  # 扩展：此处的break可以替换为exit()，表示退出程序
>                     # exit()
>                 else:
>                     print('输入有误，暂无此操作，请输入正确的操作编号')
>             # 此处的break结束的是for循环
>             break
>         else:
>             if i == 2:
>                 continue
>             print('管理员登录失败,请重新输入')
>     else:
>         print('已经错误三次，禁止管理员登录')
> 
> main()
> ```

### 二、函数递归【了解】

> 函数递归：函数调用自身
>
> 处理递归的关键：
>
> ​	a.需要找到一个临界值【让程序停止下来的条件】
> 	b.函数相邻两次调用之间的关系
>
> ```
> # 1.斐波那契数列
> # 需求：报一个数，返回斐波那契数列中该位置的数字
> """
> 1   2   3   4   5   6   7   8   9   10......
> 1   1   2   3   5   8  13   21  34  55......
> """
> 
> #2.求1~100之间所有整数的和
> ```

> ```Python
> # 1.恶意递归调用
> # def a():
> #     print('aaaa')
> #     a()
> # a()
> 
> # 2.
> # a.斐波那契数列
> # 需求：报一个数，返回斐波那契数列中该位置的数字
> """
> 1   2   3   4   5   6   7   8   9   10......
> 1   1   2   3   5   8  13   21  34  55......
> 
> 分析：求func(5)
> 第一步
> func(5) = func(4) + func(3) = 3 + 2 = 5
> 第二步：
> func(4) = func(3) + func(2) = 2 + 1 = 3
> func(3) = func(2) + func(1) = 1 + 1 = 2
> 第三步：
> func(3) = func(2) + func(1) = 1 + 1 = 2
> 
> func(n) = func(n - 1) + func(n - 2)
> """
> def func(n):
>     print('~~~~',n)
>     if n == 1 or n == 2:
>         return 1
>     else:  # n >= 3
>         return func(n - 1) + func(n - 2)
> 
> # r1 = func(2)
> # print(r1)  # 1
> # r1 = func(5)
> # print(r1)
> # r1 = func(20)
> # print(r1)  # 55
> # r1 = func(6)
> # print(r1)  # 8
> 
> # b.求1~某个数之间所有整数的和
> '''
> func(100)--->1~100 = func(99) + 100
> func(99) --->1~99 = func(98) + 99
> .....
> func(n)--->1~n = func(n - 1) + n
> '''
> 
> def func(n):
>     print('~~~~~',n)
>     if n == 1:
>         return 1
>     else:
>         return func(n - 1) + n
> 
> r2 = func(100)
> print(r2)  # 5050
> 
> # 注意：在实际应用中，不推荐使用递归，相比于循环，递归的效率较低
> ```

### 三、装饰器【掌握】

#### 1.概念

> 概念：已知一个函数，如果需要给该函数增加新的功能，但是不希望修改原函数，在Python中，这种在代码运行期间动态执行的机制被称为装饰器【Decorator】
>
> 装饰器的作用：为已经存在的函数或者类添加额外的功能
>
> 装饰器的本质：实际上就是一个闭包，概念：内部函数访问外部函数中的变量【一个已知的函数】

#### 2.基本语法

> ```Python
> # 1.闭包
> # a
> # def outer(n):
> #     m = 10
> #     def inner():
> #         print(m,n)
> #     inner()
> # outer(20)
> 
> # b.
> # def outer(n):
> #     m = 10
> #     def inner():
> #         print(m,n)
> #     return inner   # 切记：需要返回的是函数本身inner，所以不要写成inner()
> # f = outer(20)   # 调用的是外部函数
> # f()  # 相当于调用的是内部函数inner()
> 
> 
> # 2.装饰器的基本语法
> # 注意：自定义函数的过程中，函数名不要出现test,否则会自动调起系统的测试模块
> 
> # 已知函数：需要被装饰的函数
> def a():
>     print('春节快乐')
> 
> # 书写装饰器：给已知函数增加新的功能
> # 基本流程
> # a.书写一个闭包，给外部函数设置参数，该参数表示需要被装饰的函数，建议命名：f/fun/func
> def outter(func):
>     def inner():
>         # b.为了吻合闭包的概念，在内部函数中访问外部函数中的变量func
>         # func表示一个需要被装饰的函数，所以调用func
>         # 调用原函数
>         print('~~~',func)   # <function a at 0x0000010FB626F040>
>         func()
>         # 增加新的功能
>         print('new~~~~~~')
>     return inner
> # c.使用装饰器。将已知的函数作为参数传递给装饰器
> # f = inner   func = a
> f = outter(a)  # 注意：一个函数作为另一个函数的参数或返回值使用，只需要使用函数名即可
> print(f)   # <function outter.<locals>.inner at 0x0000022FD700C4C0>
> f()
> 
> '''
> 总结：
>     a.outter是装饰器的名称【外部函数的函数名】
>     b.inner是装饰器的核心部分【调用原函数，增加新的功能】
>     c.在inner中，调用原函数和新增功能没有先后顺序，可以根据具体的需求做出调整
> '''
> ```

#### 3.使用一

> 使用  @xxx  可以将一个装饰器作用于一个函数上，只需要将@xxx书写在一个函数的前面，则表示xxx装饰器装饰指定的函数
> @xxx:xxx表示装饰器的名称【外部函数的函数名】
> 注意：如果使用@xxx加载装饰器，则必须装饰器先存在，然后才能使用
>
> ```Python
> def outter(func):
>     print('外部函数~~~~~~start')
>     def inner():
>         # 调用原函数
>         print('inner~~~~~~~~~~')
>         func()
>         # 增加新的功能
>         print('new~~~~~~')
> 
>     print('外部函数~~~~~~end')
>     return inner
> 
> @outter    # 等价于f = outter(a)。调用了外部函数
> def a():
>     print('春节快乐')
> 
> print(a)   # <function outter.<locals>.inner at 0x000001AE54DCC430>
> a()    # 等价于 f()，调用了内部函数
> 
> 
> '''
> 总结：
>     a.使用@xxx装饰某个函数，则该装饰器一定要先存在，然后才能使用
>     b.@xxx本质上表示调用装饰器的外部函数，自动将已知的函数传参给了func，同时自动将返回值inner接出来
>     c.当原函数传参给func之后，此时原函数的函数名就会给重新赋值，赋值为inner,所以a()表示调用的是inner()
> '''
> ```

#### 4.使用二

> ```Python
> # 【面试题】需求：书写一个装饰器，同时装饰多个函数，给多个函数同时增加同一个新的功能
> def wrapper(func):
>     print('wrapper~~~~~~~~')
>     def inner(*args,**kwargs):     # 打包
>         print(args,kwargs)
>         func(*args,**kwargs)  # 调用原函数,拆包
>         print('new~~~~~')
>     return inner
> 
> @wrapper
> def a():
>     print('aaa')
> 
> @wrapper
> def b(m,n):
>     print('bbbbb',m,n)
> 
> @wrapper
> def c(num1,num2,num3):
>     print('cccc',num1,num2,num3)
> 
> a()  # 调用inner
> b(3,5)  # 调用inner
> c(23,5,7)
> 
> '''
> 注意：
>     a.一个装饰器装饰多个函数，则@xxx需要书写多次
>     b.如果一个装饰器装饰多个不同的函数，为了满足不同函数的参数需求，则给装饰器的内部函数设置不定长参数，格式为：*xxx,**xxx
> '''
> 
> # 案例/面试题：书写一个装饰器，可以统计任意一个函数的执行时间
> import time
> # print(time.time())  # 获取从1970.1.1 00：00：00到当前的时间戳【秒数】
> 
> def wrapper(func):
>     def get_time(*args,**kwargs):
>         start = time.time()
>         func()
>         end = time.time()
>         return round(end - start,3)   # 保留小数点后3位
>     return get_time
> 
> @wrapper
> def check():
>     for i in range(138232300):
>         pass
> 
> r = check()
> print(f'花费的时间为：{r}')
> ```

