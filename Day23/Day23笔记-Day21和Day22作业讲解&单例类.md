### Day21作业讲解

> ```Python
> '''
> 1.有一个银行账户类 Account, 包括名字 , 余额等属性，方法有存钱、取钱、查询余额的操作。要求：
> 	a.在存钱时，注意存款数据的格式
> 	b.取钱时，要判断余额是否充足，余额不够的时候要提示余额不足
> '''
> class Account():
>     __slots__ = ('name','__balance')
>     def __init__(self,name,balance):
>         self.name = name
>         # 结合实际情况，银行卡余额不是随便可以访问的
>         self.__balance = balance
>     def save_money(self,money):
>         if money < 0:
>             money = -money
>         self.__balance += money
>         print(f'存了{money}元')
>         self.show_balance()
> 
>     def get_money(self,money):
>         if money > self.__balance:
>             print('余额不足')
>         else:
>             self.__balance -= money
>             print(f'取走{money}元')
>             self.show_balance()
> 
>     def show_balance(self):
>         print(f'当前余额为：{self.__balance}')
> 
> def main():
>     a = Account('xxxx', 1000)
>     print(f'欢迎进入{a.name}的账户操作界面'.center(40, '*'))
>     while True:
>         print('''可以进行如下功能：
>             0.存钱
>             1.取钱
>             2.查询余额
>             3.退出''')
>         select = input('请输入需要进行的操作：')
>         if select == '0':
>             num = int(input('请输入需要存的钱数：'))
>             a.save_money(num)
>         elif select == '1':
>             num = int(input('请输入需要取的钱数：'))
>             a.get_money(num)
>         elif select == '2':
>             a.show_balance()
>         elif select == '3':
>             break
> 
> # if __name__ == '__main__':
> #     main()
> 
> 
> '''
> 2.家具类(HouseItem) 有 名字 和 占地面积属性，其中
>     - 席梦思(bed) 占地 4 平米
>     - 衣柜(chest) 占地 2 平米
>     - 餐桌(table) 占地 1.5 平米
> 
> 房子类(House) 有 户型、总面积 、剩余面积 和 家具名称列表 属性
>     - 新房子没有任何的家具
>     - 将 家具的名称 追加到 家具名称列表 中
>     - 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具
> 
> a.将以上三件 家具对象 添加 到 房子对象 中
> b.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
> 使用面向对象思想，编码完成上述功能。
> '''
> class HouseItem():
>     __slots__ =  ('name','area')
>     def __init__(self,name,area):
>         self.name = name
>         self.area = area
>     def __repr__(self):
>         return f'家具名称：{self.name}'
> class House():
>     __slots__ = ('kind','total_area','free_area','houseitem_list')
>     def __init__(self,kind,total_area,free_area):
>         self.kind = kind
>         self.total_area = total_area
>         self.free_area = free_area
>         self.houseitem_list = []
>     def add_item(self,item):
>         if item.area > self.free_area:
>             print('剩余面积不足，无法添加')
>         else:
>             # self.houseitem_list.append(item.name)  # 添加的是家具的名称
>             self.houseitem_list.append(item)   # 添加的是家具的对象
>             self.free_area -= item.area
>     def __repr__(self):
>         return f'{self.houseitem_list}'
> 
> if __name__ == '__main__':
>     bed = HouseItem('席梦思',4)
>     chest = HouseItem('沙发',3)
>     table = HouseItem('餐桌',1.5)
> 
>     house = House('四室两厅两卫',160,120)
>     house.add_item(bed)
>     house.add_item(chest)
>     house.add_item(table)
>     print(house)
> 
> # 刷题：牛客网  leetcode
> ```

### Day22作业讲解

> ```Python
> '''
> 学生类Student:
> 		属性:学号，姓名，年龄，性别，成绩
> 
> 班级类 Grade:
>  		属性:班级名称，班级中的学生 【使用列表存储学生】
> 
> 		方法:
> 			1.查看该班级中的所有学生的信息
> 			2.查看指定学号的学生信息
> 			3.查看班级中成绩不及格的学生信息
> 			4.将班级中的学生按照成绩降序排序
> '''
> 
> class Student():
>     __slots__ = ('sid','name','age','score')
>     def __init__(self,sid,name,age,score):
>         self.sid = sid
>         self.name = name
>         self.age = age
>         self.score = score
>     def __repr__(self):
>         return f'{self.sid}-{self.name}-{self.score}'
> 
> class Grade():
>     __slots__ = ('grade_name','stus_list')
>     def __init__(self,grade_name,stus_list):
>         self.grade_name = grade_name
>         self.stus_list = stus_list   # 将学生的对象添加到列表中
>     def show_all(self):
>         print('所有学生的信息如下：')
>         for stu in self.stus_list:
>             print(stu)  # 调用__init__或__repr__
>     def show_single(self,sid):
>         print(f'学号为{sid}的学生的信息如下：')
>         for stu in self.stus_list:
>             if stu.sid == sid:
>                 print(stu)
>                 break
>         else:
>             print('不存在')
>     def show_low(self):
>         print('不及格学生的信息如下：')
>         for stu in self.stus_list:
>             if stu.score < 60:
>                 print(stu)
>     def sort_by_score(self):
>         print('降序排序之后的信息如下：')
>         self.stus_list.sort(reverse=True,key=lambda stu:stu.score)
>         self.show_all()
> 
> if __name__ == '__main__':
>     s1 = Student('1003','小明',19,88)
>     s2 = Student('1001', '小王', 17, 100)
>     s3 = Student('1005', '小李', 19, 56)
>     s4 = Student('1006', '小张', 20, 99)
>     s5 = Student('1002', '小赵', 18, 60)
> 
>     grade = Grade('千锋2401',[s1,s2,s3,s4,s5])
>     grade.show_all()
>     grade.show_single('1006')
>     grade.show_low()
>     grade.sort_by_score()
> ```

### 一、单例设计模式【重点掌握】

#### 1.概念

> 什么是设计模式？
>
> ​	设计模式是经过总结、优化的，对我们经常会碰到的一些编程问题的可重用解决方案
>
> ​	设计模式更为高级，它是一种必须在特定情形下实现的一种方法模板。设计模式不会绑定具体的编程语言
>
> ​	 23种设计模式，其中比较常用的是单例设计模式，工厂设计模式，代理模式，装饰者模式等等
>
> 什么是单例设计模式？	
>
> ​	单例：单个实例/单个对象，一个类只能创建一个对象，只能创建出一个对象的类被称为单例类
>
> ​	程序运行过程中，确保某一个类只有一个实例【对象】，不管在哪个模块获取这个类的对象，获取到的都是同一个对象。例如：一个国家只有一个主席，不管他在哪
>
> 单例设计模式的核心：一个类有且仅有一个实例，并且这个实例需要应用于整个程序中，该类被称为单例类
>
> 问题：验证两个变量中是否存储的是同一个对象
>
> 解决：地址
>
> ​	方式一：x1   is  x2
>
> ​	方式二：id(x1)  == id(x2)

#### 2.应用场景

> 应用程序中描述当前使用用户对应的类 ———> 当前用户对于该应用程序的操作而言是唯一的——> 所以一般将该对象设计为单例
>
> 实际应用：数据库连接池操作 ——> 应用程序中多处地方连接到数据库 ———> 连接数据库时的连接池只需一个就行，没有必要在每个地方都创建一个新的连接池，这种也是浪费资源 ————> 解决方案也是单例

#### 3.实现

##### 3.1实现单例类方式一

> ```Python
> # 1.普通类
> class Person():
>     pass
> p1 = Person()
> p2 = Person()
> print(p1 is p2)  # False
> print(id(p1) == id(p2))  # Flase
> 
> print('*' * 50)
> 
> # 2.单例类
> '''
> __new__
> __init__
> '''
> class Person():
>     # 定义一个类属性，用于表示当前类可以创建的唯一的对象
>     # 因为此类属性无需在类的外面被访问修改，则设置为私有属性
>     __instance = None
>     def __new__(cls, *args, **kwargs):
>         print('new~~~')
>         # 只要super().__new__(cls)被执行一次，则会创建出一个新的对象
>         # 判断__instance的值，如果为None，则重新赋值为对象并返回，如果非空则直接返回
>         if not cls.__instance:
>             print('if~~~~')
>             cls.__instance = super().__new__(cls)
>         return cls.__instance
> 
>     def __init__(self,name,age):
>         print('init~~~~',name,age)
>         self.name = name
>         self.age = age
> p1 = Person('张三',10)  # 创建对象
> p2 = Person('李四',20)   # 获取第一次创建的对象，此处的李四和20相当于给对象的name和age属性重新赋值
> print(p1 is p2)  # True
> print(id(p1) == id(p2))   # True
> 
> print(p1.name,p2.name)   # 李四
> 
> p1.name = 'Jack'
> print(p1.name,p2.name)
> ```

##### 3.2装饰器装饰类

> ```Python
> .装饰器装饰类
> def wrapper(cls):  # cls表示需要被装饰的类
>     def inner(*args,**kwargs):
>         c = cls(*args,**kwargs)      # 类(),创建对象：调用类中的构造函数__new__,__init__,所以此处的参数需要和__init__中的参数保持一致
>         print('new~~~')  # 新增的功能
>         return c
>     return inner
> 
> @wrapper            # 调用外部函数wrapper
> class A():
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> print(A)   # <function wrapper.<locals>.inner at 0x000001DF7EDCC430>
> a1 = A('111',10)        # 调用inner,a1中存储的是inner的返回值，为了符合最初创建对象的语法，则给inner设置返回值
> print(a1)
> ```

##### 3.3实现单例类方式二

> ```Python
> def singleton(cls):
>     # 定义一个函数作用域的变量，用于存储被装饰的类可以创建的唯一的对象
>     instance = None
>     def get_instance(*args,**kwargs):
>         nonlocal instance
>         if not instance:
>             instance = cls(*args, **kwargs)  # 调用__init__
>         return instance
>     return get_instance
> 
> @singleton
> class Person():
>     def __init__(self,name,age):
>         print('init~~~~~',name,age)
>         self.name = name
>         self.age = age
> 
> p1 = Person('张三',10)   # 调用get_instance
> p2 = Person('李四',20)   # 调用get_instance
> print(p1 is p2)  # True
> print(id(p1) == id(p2))  # True
> 
> print(p1.name,p2.name)   # 张三
> 
> p1.name = 'Jack'
> print(p1.name,p2.name)
> ```

##### 3.4实现单例类方式三

> ```Python
> def singleton(cls):
>     # 定义一个函数作用域的字典变量，key:被装饰的类，value:唯一的对象
>     instance = {}
>     def get_instance(*args,**kwargs):
>         if not instance:
>             # 向字典中添加键值对
>             instance[cls] = cls(*args, **kwargs)  # 调用__init__
>         return instance[cls]
>     return get_instance
> 
> @singleton
> class Person():
>     def __init__(self,name,age):
>         print('init~~~~~',name,age)
>         self.name = name
>         self.age = age
> 
> p1 = Person('张三',10)   # 调用get_instance
> p2 = Person('李四',20)   # 调用get_instance
> print(p1 is p2)  # True
> print(id(p1) == id(p2))  # True
> 
> print(p1.name,p2.name)   # 张三
> 
> p1.name = 'Jack'
> print(p1.name,p2.name)
> ```