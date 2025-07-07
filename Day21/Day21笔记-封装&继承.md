### 复习面向对象基础语法

> ```Python
> # 定义类
> class Person():
>     # 类属性
>     num = 10
>     # 限制对象属性的动态绑定
>     __slots__ = ('name','age','hobby')
>     # 定义实例属性
>     def __init__(self,name,age,hobby):
>         self.name = name
>         self.age = age
>         self.hobby = hobby
>     # 类中的函数
>     # 实例函数
>     def func1(self,a,b):
>         print('1111',a,b)
>     # 类函数
>     @classmethod
>     def func2(cls,a):
>         print('22222',a)
>     # 静态函数
>     @staticmethod
>     def func3(num1,num2):
>         print('333333',num1,num2)
> 
> # 创建对象/实例化对象/类的实例化
> p = Person('aaa',10,'dance')
> # 访问属性
> print(Person.num)
> print(p.num)
> print(p.name,p.age,p.hobby)
> # 调用函数
> p.func1(5,8)
> 
> Person.func2(34)
> p.func2(34)
> 
> Person.func3(45,7)
> p.func3(45,8)
> ```

### Day20作业

> ```Python
> '''
> 1.设计两个类：
> 	a. 一个点Pointer类，属性包括x，y坐标。
> 	b. 一个Rectangle类（矩形）,属性有左上角坐标，宽，高
> 		方法：1. 计算矩形的面积；2. 判断点是否在矩形内
>  	c.实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形
> '''
> class Pointer():
>     __slots__ = ('x','y')
>     def __init__(self,x,y):
>         self.x = x
>         self.y = y
> class Rectangle():
>     __slots__ =  ('left_top_point','width','height')
>     # left_top_point:表示一个点Pointer的对象
>     def __init__(self,left_top_point,width,height):
>         self.left_top_point = left_top_point
>         self.width = width
>         self.height = height
>     def area(self):
>         return self.width * self.height
>     def judge(self,point):
>         # self:矩形对象  point:点的对象
>         # x轴
>         r0 = self.left_top_point.x < point.x < self.left_top_point.x + self.width
>         # y轴
>         r1 = self.left_top_point.y - self.height < point.y < self.left_top_point.y
>         return r0 and r1
> 
> # 创建表示左上角点的对象
> left_top_point = Pointer(2,19)
> # 创建矩形对象
> rect = Rectangle(left_top_point,10,10)
> print(f'矩形的面积为：{rect.area()}')
> 
> # 创建一个某点的对象
> point = Pointer(54,10)
> print(rect.judge(point))
> ```

### 一、面向对象三大特征

#### 1.封装

> 面向对象的三大特征：封装，继承和多态

> 广义的封装：函数的定义和类的定义
>
> 狭义的封装：一个类中的某些属性，如果不希望被外界直接访问，则可以将该属性私有化，该属性只能在当前类中被直接访问，如果在类的外面需要访问【获取或修改】，则可以通过暴露给外界的函数间接访问
>
> 封装的本质：将类中的属性进行私有化
>
> ```
> 【面试题】解释下面不同形式的变量出现在类中的意义
> a:普通属性，也被称为公开属性，在类的外面可以直接访问             ****
> _a:在类的外面可以直接访问,但是不建议使用，容易和私有属性混淆
> __a:私有属性，只能在类的内部被直接访问。类的外面可以通过暴露给外界的函数访问    *****
> __a__:在类的外面可以直接访问,但是不建议使用，因为系统属性和魔术方法都是这种形式的命名，
>     如：__slots__  __init__  __new__  __del__，__name__,__add__,__sub__,__mul__等
> ```

> ```Python
> # 封装的本质：将类中的属性进行私有化
> '''
> 公开属性：可以在当前类之外的任何地方直接访问的属性
> 私有属性：只能在当前类中被直接访问的属性
> '''
> 
> # 1.属性未被私有化
> class Animal1():
>     __slots__ = ('name','age')
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
>     def show(self):
>         print(self.name,self.age)
> 
> a1 = Animal1('大黄',3)
> print(a1.name,a1.age)
> a1.show()
> 
> a1.name = '小白'
> 
> print('*' * 30)
> 
> # 2.属性私有化     ******
> # 作用：为了数据的安全性，不希望当前类以外的其他地方访问该属性
> class Animal2():
>     __slots__ = ('__name','__age')
>     def __init__(self,name,age):
>         # 当给对象动态绑定属性的时候，如果在属性名的前面添加两个下划线，则表示该属性被私有化了
>         self.__name = name
>         self.__age = age
>     def show(self):
>         print(self.__name,self.__age)
> 
> a2 = Animal2('大黄',3)
> a2.show()
> # print(a2.__name,a2.__age)  # AttributeError: 'Animal2' object has no attribute '__name'
> 
> print('*' * 30)
> 
> # 3.暴露给外界访问的函数
> # a.
> class Animal3():
>     __slots__ = ('__name','__age')
>     def __init__(self,name,age):
>         self.__name = name
>         self.__age = age
>     def show(self):
>         print(self.__name,self.__age)
> 
>     # 获取值
>     def func1(self):
>         return self.__name
>     # 修改值
>     def func2(self,a):
>         self.__name = a
> 
>     def func3(self):
>         return self.__age
>     def func4(self,b):
>         if b < 0:
>             b = -b
>         self.__age = b
> 
> a3 = Animal3('大黄',3)
> a3.show()
> print(a3.func1())
> a3.func2('旺财')
> print(a3.func1())
> 
> print(a3.func3())
> a3.func4(-45)
> print(a3.func3())
> 
> print('*' * 30)
> 
> # b.装饰器实现
> class Animal3():
>     __slots__ = ('__name','__age')
>     def __init__(self,name,age):
>         self.__name = name
>         self.__age = age
>     def show(self):
>         print(self.__name,self.__age)
> 
>     # 获取值
>     '''
>     @property用来装饰获取私有化属性的函数，将该函数处理成属性使用
>     '''
>     @property
>     def name(self):
>         return self.__name
>     # 修改值
>     '''
>      @xxx.setter用来装饰修改私有化属性的函数，将该函数处理成属性使用
>      xxx:一定得是被@property装饰的函数名
>      
>      一般情况下，func1和func2这两处的函数名不会随意命名，建议命名为被私有化的属性的属性名
>     '''
>     @name.setter
>     def name(self,name):
>         self.__name = name
> 
>     @property
>     def age(self):
>         return self.__age
>     @age.setter
>     def age(self,age):
>         if age < 0:
>             age = -age
>         self.age  = age
> 
> a3 = Animal3('大黄',3)
> a3.show()
> print(a3.name)  # 大黄，调用的是被@property装饰的函数，a3.func1获取的是原func1函数的返回值
> # print(a3.func1())   # TypeError: 'str' object is not callable
> 
> # print(a3.func2)
> a3.name = '旺财'   # 调用的是被@xxx.setter装饰的函数
> # a3.func2('旺财')     # TypeError: 'str' object is not callable
> print(a3.name)
> ```

#### 2.继承

> 如果两个或者两个以上的类具有相同的属性和方法，我们可以抽取一个类出来，在抽取出来的类中声明各个类公共的部分
>
> ​	被抽取出来的类——父类【father class】  超类【super class】  基类【base class】
>
> ​	两个或两个以上的类——子类  派生类
>
> ​	他们之间的关系——子类 继承自 父类   或者   父类  派生了 子类

> 简单来说，
>
> 一个子类只有一个父类，被称为单继承
>
> 一个子类有多个父类，被称为多继承
>
> ```
> 语法：
> class 子类类名(父类类名):
> 	类体
> class 子类类名(父类类名1,父类类名2.......):
> 	类体
> ```
>
> 注意：object是Python中所有类的根类
>
> ```Python
> 
> # 1.单继承
> # 在Python中，object是所有类的根类
> # 父类
> class Person():  # 在此处的()中什么都不写，默认的父类仍然是object
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
>     def show(self):
>         print('showing')
> 
> # 子类
> class Worker(Person):
>     pass
> # a.当子类中未定义__init__，则创建子类对象，默认会调用父类中的构造函数，所以要注意和父类中的__init__的参数匹配【子类继承了父类中的__init__】
> # w = Worker()  # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
> w = Worker('小王',20)
> print(w.name,w.age)
> w.show()
> 
> class Student(Person):
>     def study(self):
>         print('study~~~~')
> stu = Student('小明',19)
> print(stu.name,stu.age)
> stu.show()
> stu.study()
> 
> # b.如果子类中定义了__init__函数，则创建子类对象，优先会调用子类中的__init__
> class Doctor(Person):
>     def __init__(self,name,age,kind):
>         # 在子类的__init__中调用父类的__init__
>         # 方式一：super(当前类，self).__init__(参数列表)
>         # super(Doctor,self).__init__(name,age)
>         # 方式二：super().__init__(参数列表)
>         # super().__init__(name,age)
>         # 方式三：父类类名.__init__(self,参数列表)
>         Person.__init__(self,name,age)
> 
>         self.kind = kind
>     def assist(self):
>         print('assist~~~~')
> 
> # d = Doctor() # TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'kind'
> d = Doctor('王大夫',45,'外科')
> print(d.kind)
> # 当子类对象需要访问父类中提取出来的属性时，无法访问，解决方案：在子类的__init__中调用父类中的__init__
> print(d.name,d.age)  # AttributeError: 'Doctor' object has no attribute 'name'
> d.show()
> d.assist()
> 
> # 2.多继承
> # a
> class Flyable():
>     def fly(self):
>         print('flying')
> class Runable():
>     def run(self):
>         print('running')
> class Bird(Flyable,Runable):
>     pass
> 
> bird = Bird()
> bird.fly()
> bird.run()
> 
> # b.
> # class FatherClass1():
> #     def __init__(self,num):
> #         self.num = num
> #     def func(self):
> #         print('11111')
> #
> # class FatherClass2():
> #     def __init__(self,value):
> #         self.value = value
> #     def func(self):
> #         print('2222')
> #
> # class SubClass(FatherClass1,FatherClass2):
> #     pass
> 
> # 当一个类有多个父类，且子类中未定义构造函数，则创建子类对象，默认情况下调用的时父类列表中第一个父类中的__init__,多个父类中出现重名的函数也是这种原理
> # sc = SubClass(45)
> # sc.func()
> 
> # c
> class FatherClass1():
>     def __init__(self,num):
>         self.num = num
>     def func(self):
>         print('11111')
> 
> class FatherClass2():
>     def __init__(self,value):
>         self.value = value
>     def func(self):
>         print('2222')
> 
> class SubClass(FatherClass1,FatherClass2):
>     def __init__(self,num,value,a,b):
>         # 在多继承中，在子类的__init__中调用父类的__init__,只能使用方式三，可以区分父类
>         FatherClass1.__init__(self, num)
>         FatherClass2.__init__(self, value)
>         self.a = a
>         self.b = b
> 
> sc = SubClass(34,6,7,8)
> print(sc.a,sc.b)
> print(sc.num,sc.value)
> ```

