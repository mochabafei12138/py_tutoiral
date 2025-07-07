### Day19作业讲解

> ```Python
> # 1.封装函数，给定一个文件夹路径，获取该路径下所有的文件，注意：要输出所有文件夹及子文件夹下面的文件
> import os
> def get_file(folder_path):
>     # 判断路径是否存在
>     if not os.path.exists(folder_path):
>         print('路径不存在')
>         return
> 
>     # 判断路径表示的是文件还是文件夹
>     if os.path.isfile(folder_path):
>         print(f'是文件：{folder_path}')
>         return
> 
>     # 说明folder_path是一个文件夹
>     # 获取该文件夹下的所有的内容的名称
>     names_list = os.listdir(folder_path)
>     # print(names_list)
>     # 遍历列表，获取其中的名称，然后拼接为路径
>     for name in names_list:
>         sub_path = os.path.join(folder_path,name)
>         # print(sub_path)
>         if os.path.isfile(sub_path):
>             # 文件
>             print(f'是文件：{sub_path}')
>         else:
>             # 文件夹,则就可以递归执行【因为子路径是文件夹的情况下，需要反复获取，遍历，拼接，判断】
>             get_file(sub_path)
> 
> folder_path = r'd:\Desktop\coding'
> # get_file(folder_path)
> 
> 
> # 2.获取当前时间，判断是否是元旦，如果不是，计算和元旦差了多少天
> import  datetime
> 
> # 获取当前时间
> now = datetime.datetime.now()
> print(now)
> # today = datetime.datetime.today()
> # print(today)
> 
> # 获取元旦日期
> new_year = datetime.datetime(now.year,1,1)
> 
> # 判断
> if now.month == 1 and now.day == 1:
>     print('今天是元旦！')
> else:
>     # 计算差值
>     days_diff = (now - new_year).days
>     print(f'今天不是元旦，距离元旦{days_diff}天')
> ```

### 一、面向对象基础

#### 1.概念

##### 1.1面向对象的设计思想

> 面向对象是基于万物皆对象这个哲学观点，在Python中，一切皆对象

> 举例说明：
>
> ​	案例一：我想要吃大盘鸡
>
> ​	面向过程 							面向对象
>
> ​	1.自己去买菜						    1.委托一个会砍价的人帮忙去买菜
>
> ​	2.自己择菜						    2.委托一个临时工帮忙择菜
>
> ​	3.自己做菜						    3.委托一个厨师帮忙做菜
>
> ​	4.自己开始吃						    4.自己开始吃
>
> ​	
>
> ​	案例二：小明是一个电脑小白，想要配一台电脑，买完零件后需要运到家里，组装完成后打开电脑玩游戏
>
> ​	面向过程 							面向对象
>
> ​	1.小明补充电脑知识				1.委托一个懂电脑的朋友(老王)去帮忙买零件
>
> ​	2.小明去买零件				    	2.委托一个能跑腿的人将零件运送到家里
>
> ​	3.小明把零件带回家里				3.委托一个会组装电脑的人帮小明组装电脑
>
> ​	4.小明组装电脑				    	4.小明自己打开电脑，开始玩游戏
>
> ​	5.小明开机玩电脑	
>

##### 1.2面向过程和面向对象的区别【面试题】

> 面向过程
>
> 在生活案例中：	
>
> ​	一种看待问题的思维方式，在思考问题的时候，着眼于问题是怎样一步一步解决的，然后亲力亲为的去解决问题	
>
> 在程序中：	
>
> ​	1》代码从上而下顺序执行
>
> ​	2》每一模块内部均是由顺序、选择和循环三种基本结构组成
>
> ​	3》程序流程在写程序时就已决定

> 面向对象
>
> 在生活案例中：	
>
> ​	也是一种看待问题的思维方式，着眼于找到【一个具有特殊功能的具体个体，然后委托这个个体去做某件事情】，我们把这个个体就叫做对象，一切皆对象
>
> ​	是一种更符合人类思考习惯的思想【懒人思想】，可以将复杂的事情简单化，将程序员从执行者角度转换成了指挥者角度
>
> 在程序中：
>
> ​	把数据及对数据的操作方法放在一起，作为一个相互依存的整体——对象
>
> ​	1》对同类对象抽象出其共性，形成类
>
> ​	2》类中的大多数数据，只能用本类的方法进行处理
>
> ​	3》程序流程由用户在使用中决定
>
> ​	4》使用面向对象进行开发，先要去找具有所需功能的对象，如果该对象不存在，那么创建一个具有该功能的对象
>
> 注意：面向对象只是一种思想，不是一门编程语言，也不会绑定编程语言

> 面向过程和面向对象的优缺点【面试题】
>
> 面向过程：
>
> ​	优点：性能较高，比如单片机，嵌入式开发等一般采用的是面向过程的方式，因为性能是最重要的因素
>
> ​	缺点：没有面向对象易于维护，易于复用，易于扩展，开销比较大，比较消耗资源
>
> 面向对象：
>
> ​	优点：易于维护，易于复用，易于扩展，因为面向对象有封装、继承和多态的特征，可以涉及出低耦合的系统，使得系统更加灵活
>
> ​	缺点：性能较低
>
> 使用面向对象解决问题,其中的核心内容：类和对象

#### 2.类和对象【重点掌握】

##### 2.1概念

> 类：一个具有特殊功能的实体的集合【群体】，是抽象的概念
>
> 对象：在一个类中，一个具有特殊功能的实体，能够帮忙解决特定的问题【对象也被称为实例】，是具体的存在
>
> 两者之间的关系：类用于描述某一类对象的共同特征，而对象则是类的具体存在
>
> 问题：先有对象还是先有类？
>
> 先有对象，再有类-----》将多个具有共同特征的对象，抽取一个类出来
>
> 先有类，再有对象----》在代码中，一般都是先定义类，通过类创建对象，

> 举例：
>
> ​				类								对象
>
> ​				人							张三、李四、王麻子、杨阳。。。
>
> ​				SuperHero             			蝙蝠侠、蜘蛛侠、美国队长。。。
>
> ​				快递   						 顺丰、圆通、申通、韵达。。。
>
> 帮助理解：类也是一种数据类型，只不过是自定义的，用于描述生活中的一些事物，且Python中并没有提供这些类型，跟学过的intAct，float,str。。。。类似，用类创建对象则相当于定义一个类的变量

##### 2.2类的定义

> 格式：
>
> ```
> class  类名()：
> 	类体
> 	
> # ()可以省略
> ```
>
> 说明：
>
> ​	a.Python中使用class关键字定义类
>
> ​	b.类名只要是一个合法的标识符即可，但是要求：遵循大驼峰命名法【每个单词的首字母大写】 ，如：KeyError,ValueError,NameError,IndexError…….
>
> ​	c.尽量使用单个或多个有意义的单词连接而成，类名中一般不使用下划线
>
> ​	d.通过缩进来体现类体的存在
>
> ​	e.类体一般包含两部分内容：对类的特征描述和行为描述
>
> ​	f.类的包含两部分：类的声明和类的实现
>
> ```Python
> # 1.类是一种数据类型
> # a
> num = 10  # 定义一个变量
> print(type(num))  # <class 'int'>
> 
> # b.
> v = ValueError() # 创建一个对象
> print(type(v))   # <class 'ValueError'>
> 
> # 2.类的定义
> # a.函数的定义
> # def func():
> #     print('ok~~~~~func')
> 
> # b.类的定义
> class Check():
>     # 一般不会在类中print
>     print('ok~~~~class')
> class MyClass1():
>     pass
> class MyClass2:
>     pass
> 
> # 通过类创建对象，语法：变量 = 类名()
> m1 = MyClass1()
> print(m1)
> m2 = MyClass2()
> print(m2,id(m2))
> m22 = MyClass2()
> print(m22,id(m22))
> 
> '''
> 总结：
>     a.类和函数相比，函数必须调用才能执行其中的代码，但是类只要定义完毕，其中的内容就会被加载一遍
>     b.在同一个py文件中，可以定义多个类，但是，如果要实现的需求较为复杂，一般会结合模块使用，在一个模块中定义一个类
>     c.定义类的过程中，类名后面的()可以省略
>     d.创建对象：变量 = 类名()，此处的()不能省略
>     e.同一个类，默认情况下，可以创建无数个对象，每个对象都会被分配不同的地址
>     f.直接输出对象，默认的情况下，会得到一个地址
> '''
> ```

##### 2.3对象的创建

> ```Python
> # 通过类创建对象，语法：变量 = 类名()
> m1 = MyClass1()
> print(m1)
> m2 = MyClass2()
> print(m2,id(m2))
> m22 = MyClass2()
> print(m22,id(m22))
> ```

##### 2.4类的设计

> 只需要关心3个要素
>
> ​	事物名称（类名）：人类（Person）
>
> ​	特征：身高（height）、年龄（age）—————》名词———》变量
>
> ​	行为：跑（run）、打架（fight）———————》动词————》函数
>
> ​	初期学习，通过提炼动名词进行类的提取
>
> ```Python
> # 类的定义
> class Person():
>     # 行为描述：函数
>     '''
>     关于self
>         a.self不是关键字，本质上可以是一个任意的标识符，但是使用self表示自己【self在Java中是关键字】
>         b.类中的函数，默认的情况下，形参列表的第一个参数都是self
>         c.self表示当前对象，哪个对象调用该函数，则self表示哪个对象
>         d.当调用函数的时候，self无需手动传参，会自动将当前对象传参给self,只需要注意自己定义的参数的传参即可
>     '''
>     def eat(self,food):
>         print(f'eating {food}',f'self:{id(self)}')
>     def run(self):
>         print('running')
>     def show(self):
>         print(f'姓名:{self.name},年龄：{self.age}')  # 哪个对象调用show函数，则输出的就是该对象对应的属性
> 
> # 创建对象
> p1 = Person()
> print(p1)
> 
> p2 = Person()
> print(p2)
> 
> # 特征描述：变量，语法：对象.属性  = 值
> # 对一个对象进行某个特征的描述，可以借助于变量表示，此时的变量也可以被称为属性
> p1.name = '张三'
> p1.age = 20
> # print(p1.name,p1.age)
> 
> p2.name = '李四'
> p2.age = 18
> p2.height = 180
> # print(p2.name,p2.age,p2.height)
> 
> # 对象能且只能执行当前类中的行为【对象调用当前类中的函数】，语法：对象.函数(实参)
> print('p1:',id(p1))
> p1.eat('apple')
> # p1.run()
> p1.show()
> 
> print('p2:',id(p2))
> p2.eat('banana')
> # p2.run()
> p2.show()
> ```

##### 2.5案例一

> ```Python
> '''
> 需求：开学了，王老师让小明，小花，小丽做自我介绍
>     介绍内容包括：姓名，年龄，爱好
>     展示一段才艺
> '''
> 
> '''
> 分析：
>     a.定义教师类和学生类
>     b.教师类
>         特征：姓名
>         行为：让 学生 做自我介绍
>     c.学生类
>         特征：姓名，年龄，爱好
>         行为：做 自我介绍
>              才艺展示
> '''
> # 第一步：定义类
> class Teacher():
>     # self表示老师对象，stu是一个学生对象,只要一个变量表示的是某个对象，则该变量作为对象使用，可以访问对象的属性或类中的函数
>     def let_stu_introduce(self,stu):
>         print(stu)
>         print(f'{self.name}让{stu.name}做自我介绍')
>         # 学生开始执行自己的行为：做自我介绍和才艺战术
>         stu.introduce()
>         stu.show_talent()
> 
> class Student():
>     def introduce(self):
>         print(f'大家好，我是{self.name},今年{self.age},爱好{self.hobby}')
>     def show_talent(self):
>         if self.name == '小明':
>             print(f'接下来给大家展示一段{self.hobby},我家里有几百头牛，几百头🐏~~~~')
>         elif self.name == '小花':
>             print(f'接下来给大家展示一段{self.hobby},一起来摇摆~~~~')
>         elif self.name == '小丽':
>             print(f'接下来给大家展示一段{self.hobby},看谁在唱歌~~~~')
> 
> # 第二步：创建对象并描述特征
> tea = Teacher()
> tea.name = '王老师'
> 
> stu1 = Student()
> stu1.name = '小明'
> stu1.age = 18
> stu1.hobby = '吹牛逼'
> 
> stu2 = Student()
> stu2.name = '小花'
> stu2.age = 17
> stu2.hobby = '跳舞'
> 
> stu3 = Student()
> stu3.name = '小丽'
> stu3.age = 19
> stu3.hobby = '唱歌'
> 
> # 第三步：在类中定义函数并调用函数
> tea.let_stu_introduce(stu2)
> tea.let_stu_introduce(stu1)
> tea.let_stu_introduce(stu3)
> ```

#### 3.构造函数

> ```Python
> # 一、构造函数的工作原理
> '''
> 构造函数：包括__new__和__init__
> 在Python中，以__xxx__方式命名的函数，被称为魔术函数/魔术方法，该类函数都是在特定的场景下被自动调用的，无需手动调用
>     __new__:从无到有的过程，表示真正意义上创建对象
>     __init__:初始化的过程，表示将__new__创建出来的对象进行初始化
> 
> 代码执行顺序：当x = 类名()创建对象的时候，首先会自动调用__new__,创建出来一个对象，且将该对象返回，
>            同时自动将该对象传递给__init__,对该对象完成初始化
> '''
> class Person():
>     def __new__(cls, *args, **kwargs):
>         print('new~~~~')
>         return super().__new__(cls)   # 返回一个对象
>     def __init__(self):
>         print('init~~~~~')
> p = Person()
> 
> # 二、构造函数常用的形式  ******
> # 1.基本语法
> class Person():
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
>     def show(self):
>         print(f'name：{self.name},age:{self.age}')
> 
> # 一般在创建对象的时候，倾向于将对象创建完有初始状态的【初始状态：创建对象的同时进行特征的描述，或者定义属性】
> # 注意：当类中定义了__init__,创建对象的时候，一定要注意参数保持一致
> p1 = Person('aaa',10)
> # p1.name = 'aaa'
> # p1.age = 10
> print(p1.name,p1.age)
> 
> p2 = Person('bbb',10)
> # p2.name = 'bbb'
> # p2.age = 10
> print(p2.name,p2.age)
> 
> p3 = Person('ccc',20)
> print(p3.name,p3.age)
> 
> p1.show()
> p2.show()
> p3.show()
> 
> # 2.应用
> # 第一步：定义类
> class Teacher():
>     def __init__(self,name):
>         self.name = name
>     # self表示老师对象，stu是一个学生对象,只要一个变量表示的是某个对象，则该变量作为对象使用，可以访问对象的属性或类中的函数
>     def let_stu_introduce(self,stu):
>         print(stu)
>         print(f'{self.name}让{stu.name}做自我介绍')
>         # 学生开始执行自己的行为：做自我介绍和才艺战术
>         stu.introduce()
>         stu.show_talent()
> 
> class Student():
>     def __init__(self,name,age,hobby):
>         self.name = name
>         self.age = age
>         self.hobby = hobby
> 
>     def introduce(self):
>         print(f'大家好，我是{self.name},今年{self.age},爱好{self.hobby}')
>     def show_talent(self):
>         if self.name == '小明':
>             print(f'接下来给大家展示一段{self.hobby},我家里有几百头牛，几百头🐏~~~~')
>         elif self.name == '小花':
>             print(f'接下来给大家展示一段{self.hobby},一起来摇摆~~~~')
>         elif self.name == '小丽':
>             print(f'接下来给大家展示一段{self.hobby},看谁在唱歌~~~~')
> 
> # 第二步：创建对象并描述特征
> tea = Teacher('王老师')
> 
> stu1 = Student('小明',18,'吹牛逼')
> stu2 = Student('小花',17,'跳舞')
> stu3 = Student('小丽',19,'唱歌')
> 
> # 第三步：在类中定义函数并调用函数
> tea.let_stu_introduce(stu2)
> tea.let_stu_introduce(stu1)
> tea.let_stu_introduce(stu3)
> ```

#### 4.属性的动态绑定和限制绑定

> ```Python
> # 1.对象属性的动态绑定
> # 只要是 对象.属性 = 值 类似这样的语法，都是给对象动态绑定属性，在默认情况下，对于属性的绑定没有任何限制
> # class Doctor():
> #     def __init__(self,name,age):
> #         self.name = name
> #         self.age = age
> #
> # doc = Doctor('张大夫',40)
> # doc.kind = '外科'
> # print(doc.name,doc.age,doc.kind)
> # doc.a = 234
> # doc.eggw= 45
> 
> # 2.限制对象属性的动态绑定
> class Doctor():
>     # 用__slots__限制对象属性的动态绑定，定义一个元组，将属性名以字符串的形式书写在元组中,一般是结合实际需求或实际情况确定
>     __slots__ = ('name','age','kind')
>     # 注意：当元组中只有一个元素的时候，要添加逗号
>     # __slots__ =  ('name',)
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> 
> doc = Doctor('张大夫',40)
> doc.kind = '外科'
> print(doc.name,doc.age,doc.kind)
> # doc.a = 234   # AttributeError: 'Doctor' object has no attribute 'a'
> # doc.eggw= 45
> ```

#### 5.类中的属性【重点掌握】

> 【面试题】简述类属性【类的字段】和实例属性【对象属性，对象的字段】的区别
> 1.定义位置不同：类属性直接定义在类中，只要是动态绑定的属性都是实例属性【在__init__中或在类的外面直接动态绑定定义】
> 2.访问方式不同：类属性可以通过类名或对象访问，而实例属性只能通过对象访问
> 3.访问优先级不同：当类属性和实例属性重名时，通过对象访问，优先访问的是实例属性
> 4.在内存中出现的时机不同：类属性优先于实例属性出现在内存中，类属性随着类的加载而出现，实例属性是对象创建完毕之后才会出现
> 5.使用场景不同：类属性用于表示多个对象共享的数据，实例属性表示每个对象特有的数据
>
> ```Python
> class Person():
>     # 1.定义位置不同：类属性直接定义在类中，只要是动态绑定的属性都是实例属性【在__init__中或在类的外面直接动态绑定定义】
>     # 注意：只要是  对象.属性 = 值  这样的语法，其实都是实例属性
>     # 类属性
>     place = '地球'
>     num = 66
> 
>     def __init__(self,name,age):
>         # 实例属性/对象属性
>         self.name = name
>         self.age = age
> p1 = Person('赵四',34)
> # 实例属性/对象属性
> p1.height = 170
> p1.num = 100
> 
> # 2.访问方式不同
> # 类属性可以通过类名或对象访问
> print(Person.place)
> print(p1.place)
> 
> # 而实例属性只能通过对象访问
> print(p1.name,p1.age,p1.height)
> 
> # 3.访问优先级不同
> # 当类属性和实例属性重名时，通过对象访问，优先访问的是实例属性
> print(p1.num)   # 100  实例属性
> 
> del p1.num     # 实例属性优先被访问，所以此处被删除的是实例属性
> print(p1.num)  # 66   类属性
> 
> # 4.内存中的类属性和实例属性
> p2 = Person('小王',18)
> 
> print(p1.name is p2.name)  # False
> print(p1.place is p2.place)  # True
> 
> # 问题:p1.name和p2.name是否共享同一份内存地址？----》是不同的地址
> p1.name = 'Jack'
> print(p2.name)
> 
> # 问题:p1.palce和p2.place是否共享同一份内存地址？----》是同一份地址
> # p1.place = '火星'   # 并不是在修改类属性的值，而是给p1动态绑定了一个place的实例属性
> 
> # 如果要修改类属性的值，则格式:类名.类属性  = 值
> Person.place = '火星'
> print(p1.place,p2.place)
> 
> # 5.使用场景不同：类属性用于表示多个对象共享的数据，实例属性表示每个对象特有的数据
> class Student():
>     # 类属性：多个对象公共的数据
>     school_name = '千锋'
>     def __init__(self,name,city):
>         self.name = name
>         self.city = city
> stu1 = Student('小明','北京')
> stu2 = Student('小王','成都')
> print(stu1.name,stu1.city,stu1.school_name)
> print(stu2.name,stu2.city,stu2.school_name)
> 
> Student.school_name = '万锋'
> print(stu1.name,stu1.city,stu1.school_name)
> print(stu2.name,stu2.city,stu2.school_name)
> 
> ```

#### 5.类中的函数【重点掌握】

> ```Python
> class Book():
>     __slots__ =  ('name','author')
>     # 1.定义
>     # 1_a.实例函数，特点：第一个形参是self，self表示当前对象
>     def __init__(self,name,author):
>         self.name = name
>         self.author = author
> 
>     # 3.函数之间相互调用
>     # 3_a.实例函数之间相互调用，格式：self.xxx()
>     def show1(self):
>         print('实例函数~~~~~~')
>         print(f'书名:{self.name},作者:{self.author}')
>         # 在show1中调用show2
>         self.show2()
>     def show2(self):
>         print('show~~~2222')
> 
>     # 1_b.类函数,特点：用@classmethod装饰器装饰，第一个形参是cls，cls是class的缩写，表示当前类
>     @classmethod
>     def func1(cls):
>         print('类函数~~~~',cls)
>         # 3_b.类函数之间相互调用，格式:cls.xxx()
>         cls.func2()
> 
>         # 3_c.类函数中调用实例函数,格式：先通过cls创建对象，然后再调用
>         # 创建对象，同样会调用__init__，注意参数
>         b = cls('Python机器学习入门与精通','tom')
>         b.show2()
> 
>     @classmethod
>     def func2(cls):
>         print('func~~~~22222')
> 
>     # 1_c.静态函数,特点：用@staticmethod装饰器装饰，参数没有特别之处
>     @staticmethod
>     def check1():
>         print('静态函数~~~~~')
> 
> book = Book("Python疯狂讲义",'jack')
> 
> # 2.调用
> # a.实例函数：只能通过对象调用
> book.show1()
> 
> # b.静态函数和类函数：可以通过类名或对象调用
> Book.func1()
> Book.check1()
> 
> # book.func1()
> # book.check1()
> ```

#### 6.析构函数

> ```Python
> '''
> 构造函数：__new__和__init__,创建对象并给对象初始化【对象从无到有】
> 析构函数：__del__,对象被销毁的时候会自动调用的函数，
> 
> 对象被销毁的时机
>     a.程序执行完毕，对象的声明周期完成
>     b.程序还未执行执行完毕，但是手动销毁对象，语法：del  xxx
> '''
> class Animal():
>     def __init__(self):
>         print('init被调用了')
>     def __del__(self):
>         print('del被调用了~~~~~')
> 
> # 1.程序执行完毕，对象自动被销毁：全局变量
> # print('start')
> # a = Animal()
> # print('end')
> '''
> start
> init被调用了
> end
> del被调用了~~~~~
> '''
> 
> # 2.程序执行完毕，对象自动被销毁：局部变量
> # print('start')
> # def func():
> #     print('func函数被调用了')
> #     a = Animal()
> # func()
> # print('end')
> '''
> start
> func函数被调用了
> init被调用了
> del被调用了~~~~~
> end
> '''
> 
> # 3.程序未执行完毕，对象被手动销毁
> print('start')
> a = Animal()
> print('end')
> del a
> print('over')
> '''
> start
> init被调用了
> end
> del被调用了~~~~~
> over
> '''
> ```

#### 7.案例二

> ```Python
> '''
> 1.定义一个Number类，其中定义加减乘除的函数，分别计算两个数的相关运算
> '''
> # 方式一：实例函数
> class Number():
>     def __init__(self,num1,num2):
>         self.num1 = num1
>         self.num2 = num2
>     def add(self):
>         return self.num1 + self.num2
>     def sub(self):
>         return self.num1 - self.num2
>     def mul(self):
>         return self.num1 * self.num2
>     def div(self):
>         if self.num2 != 0:
>             return self.num1 / self.num2
> num = Number(10,20)
> print(num.add(),num.sub(),num.mul(),num.div())
> 
> # 方式二：类函数
> class Number():
>     @classmethod
>     def add(cls,num1,num2):
>         return num1 + num2
>     @classmethod
>     def sub(cls,num1,num2):
>         return num1 - num2
>     @classmethod
>     def mul(cls,num1,num2):
>         return num1 * num2
>     @classmethod
>     def div(cls,num1,num2):
>         if num2 != 0:
>             return num1 / num2
> print(Number.add(10,20),Number.sub(10,20),Number.mul(10,20),Number.div(10,20))
> 
> # 方式三：静态函数
> class Number():
>     @staticmethod
>     def add(num1,num2):
>         return num1 + num2
>     @staticmethod
>     def sub(num1,num2):
>         return num1 - num2
>     @staticmethod
>     def mul(num1,num2):
>         return num1 * num2
>     @staticmethod
>     def div(num1,num2):
>         if num2 != 0:
>             return num1 / num2
> print(Number.add(10,20),Number.sub(10,20),Number.mul(10,20),Number.div(10,20))
> 
> 
> '''
> 2.构造一个圆，求该圆的面积和周长，最后判断一个点和该圆之间的关系
> '''
> '''
> 圆类
>     特征：圆心【本质上就是一个点】和半径
>     行为：该圆的面积
>          该圆的周长
>          判断一个点和该圆之间的关系
>          
> 点类：
>     特征：x  y
> '''
> import math
> class Point():
>     __slots__ = ('x','y')
>     def __init__(self,x,y):
>         self.x = x
>         self.y = y
> class Circle():
>     __slots__ = ('circle_center','radius')
>     # circle_center:圆心，本质上就是一个点，所以此处传参Point类的对象
>     def __init__(self,circle_center,radius):
>         self.circle_center = circle_center
>         self.radius = radius
>     def length(self):
>         return round(2 * math.pi * self.radius,3)
>     def area(self):
>         return round(math.pi * self.radius ** 2,3)
>     def judge(self,point):
>         # self:圆的对象   point:某点的对象
>         '''
>         判断某点和圆之间的关系：判断某点到圆心的距离和圆的半径之间的大小关系
>         两点之间的距离：(x1,y1)  (x2,y2)    math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2)
> 
>         圆心的坐标：(self.circle_center.x,self.circle_center.y)
>         某点的坐标：(point.x,point.y)
>         '''
>         distance = math.sqrt((self.circle_center.x - point.x) ** 2 + (self.circle_center.y - point.y) ** 2)
>         if distance > self.radius:
>             return '圆外'
>         elif distance < self.radius:
>             return '圆内'
>         else:
>             return '圆上'
> 
> # 创建圆心的对象
> circle_center = Point(23,18)
> # 创建圆的对象
> circle = Circle(circle_center,10)
> r1 = circle.length()
> r2 = circle.area()
> print(f'该圆的面积:{r2},周长:{r1}')
> 
> point = Point(56,19)
> print(f'某点和该圆之间的关系为：{circle.judge(point)}')
> 
> '''
> 3.定义类，用来描述数字时钟
> 
> 时钟类：
>     特征:时分秒
>     行为：走针
> '''
> import  time
> class Clock():
>     __slots__ =  ('hour','minutes','seconds')
>     def __init__(self,hour=0,minutes=0,seconds=0):
>         self.hour = hour
>         self.minutes = minutes
>         self.seconds = seconds
>     def run(self):
>         self.seconds += 1        # 17:20:59---->17:21:00
>         if self.seconds == 60:
>             self.seconds = 0
>             self.minutes += 1    # 17:59:59
>             if self.minutes == 60:
>                 self.minutes = 0
>                 self.hour += 1   # 23:59:59
>                 if self.hour == 24:
>                     self.hour = 0
> 
>     def show(self):
>         print('%.2d:%.2d:%.2d' % (self.hour,self.minutes,self.seconds))
> 
> # clock = Clock()
> # clock = Clock(17,24,30)
> 
> # 获取当前时间
> t1 = time.localtime()
> # print(t1[3],t1[4],t1[5])
> clock = Clock(t1[3],t1[4],t1[5])
> 
> while True:
>     clock.show()
>     time.sleep(1)
>     clock.run()
> ```