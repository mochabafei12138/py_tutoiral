### 一、多态

> 多态的前提：继承
>
> 体现1：同一种事物的多种体现形式，如：动物有很多种
>
> 体现2：在定义的过程无法确定变量的类型，只有当程序正常运行的时候才会确定该变量是什么类型，调用哪个函数
>
> ```Python
> # 体现1：同一种事物的多种体现形式，如：动物有很多种
> class Animal():
>     pass
> class Cat(Animal):
>     pass
> class SmallCat(Cat):
>     pass
> 
> sc = SmallCat()
> # isinstance(对象,类型):判断一个对象是否是指定的类型
> print(isinstance(sc,SmallCat))
> print(isinstance(sc,Cat))
> print(isinstance(sc,Animal))
> print(isinstance(sc,object))
> 
> # 体现2：在定义的过程中无法确定变量的类型和调用的函数，只有当程序正常运行的时候才会确定该变量是什么类型，调用哪个函数
> class Animal():
>     def style(self):
>         print('walking')
> class Cat(Animal):
>     pass
> class Dog(Animal):
>     pass
> class Pig(Animal):
>     pass
> class Bird(Animal):
>     def style(self):
>         print('flying')
> class Fish(Animal):
>     def style(self):
>         print('swimming')
> 
> def func(ani):   # ani有多种类型的体现形式，所以此处是多态的体现
>     ani.style()
> 
> cat = Cat()
> func(cat)
> 
> bird = Bird()
> func(bird)
> 
> fish = Fish()
> func(fish)
> ```

### 二、函数重写【重点掌握】

> 重写：override,在继承的前提下，如果在子类中重新实现了父类中的函数

> ```Python
> """
> 注意：
>     1.什么时候需要重写函数
>         如果一个类有很多子类，大多数子类可以直接使用父类中实现的功能
>         但是，如果父类中实现的需求满足不了部分子类的使用，则需要在子类中重写函数
>     2.重写需要注意的事项
>         保留函数的声明部分：def  xxx(self,形参列表)
>         重新实现函数的实现部分【函数体】
> """
> ```

> ```Python
> # 1.自定义函数的重写
> # class Animal():
> #     def style(self):
> #         print('walking')
> # class Cat(Animal):
> #     pass
> # class Dog(Animal):
> #     pass
> # class Pig(Animal):
> #     pass
> # class Bird(Animal):
> #     def style(self):
> #         print('flying')
> # class Fish(Animal):
> #     def style(self):
> #         print('swimming')
> 
> # 2.系统函数的重写
> # a.
> class Person(object):
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> 
>     def show(self):
>         print(f'name:{self.name},age:{self.age}')
> 
> p = Person('小明',10)
> # 注意1：当输出对象时，默认会调用魔术函数__str__,__str__是object中的函数，该函数默认返回当前对象在计算机中的地址
> print(p)    # <__main__.Person object at 0x0000026DE30C5FD0>
> print(p.__str__())  # <__main__.Person object at 0x0000026DE30C5FD0>
> 
> # b
> class Person(object):
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> 
>     def show(self):
>         print(f'name:{self.name},age:{self.age}')
> 
>     # 注意2：当重写__str__时，返回值必须是一个字符串，表示一个对象的字符串描述信息，一般是和当前对象相关的属性信息
>     def __str__(self):
>         # TypeError: __str__ returned non-string (type NoneType)
>         return f'name:{self.name},age:{self.age}'
> 
> p = Person('小明',10)
> print(p)
> print(p.__str__())
> 
> # c.
> class Person(object):
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> 
>     def show(self):
>         print(f'name:{self.name},age:{self.age}')
> 
>     # 方式一：只重写__repr__
>     # def __repr__(self):
>     #     return f'name:{self.name},age:{self.age}'
>     # 方式二：
>     def __str__(self):
>         return f'name:{self.name},age:{self.age}'
>     __repr__ = __str__
> 
> p = Person('小明',10)
> print(p)  # 输出对象的时候，调用子类中重写之后的__str__
> print(p.__str__())
> # 注意3：当将对象作为作为存储在列表等容器中时，输出列表，元素仍然以地址的形式呈现，则重写__repr__
> lst = [p]
> print(lst)   # 前：[<__main__.Person object at 0x000001A553037FD0>]  后：[name:小明,age:10]
> 
> # 3.注意4：当子类中重写了父类中的函数，创建子类对象调用函数，优先调用的是子类中的函数
> # a.如果在子类的构造函数中需要用到父类中绑定的属性，则可以在子类的构造函数中调用父类中的构造函数
> class A():
>     def __init__(self,a):
>         self.a = a
> class B(A):
>     def __init__(self,a,b):
>         super().__init__(a)
>         self.b = b
> b = B(23,4)
> 
> # b.当在子类重写之后的函数中需要用到父类中对应函数中的功能，则可以在子类函数中调用父类中的函数
> class Animal():
>     def style(self):
>         print('walking')
> class Bird(Animal):
>     def style(self):
>         # super(Bird,self).style()
>         # super().style()
>         Animal.style(self)
>         print('flying')
> bird = Bird()
> bird.style()
> ```

### 三、运算符重载

> 重载：overload
>
> ```Python
> # 1.+
> '''
> 除了数字之外，其他数据类型但凡支持+的运算，底层都是调用了__add__
> '''
> # a
> print('abc' + '123')   # str + str ---- >str
> print('abc'.__add__('123'))
> 
> print([2,3] + [5,6])  # list + list --->list
> print([2,3].__add__([5,6]))
> 
> # __dict__
> # print(str.__dict__)
> # print(list.__dict__)
> 
> # b
> # class Person():
> #     def __init__(self,age):
> #         self.age = age
> # p1 = Person(10)
> # p2 = Person(23)
> # print(p1 + p2)  # TypeError: unsupported operand type(s) for +: 'Person' and 'Person'
> # print(Person.__dict__)
> 
> # c,如果一个类不支持+，则可以在类中重载__add__
> class Person():
>     def __init__(self,age):
>         self.age = age
>     # 重写：函数存在但是实现的需求不满足使用
>     # 重载：不支持指定的运算，通过重载让支持运算
>     def __add__(self, other):
>         return Person(self.age + other.age)
> 
>     # 重写
>     def __str__(self):
>         return str(self.age)
> 
> p1 = Person(10)
> p2 = Person(23)
> # 问题1:Person + Person ----》int ,解决：Person + Person ----》Person
> # 问题2：当__add__返回 Person(self.age + other.age)，输出p1 + p2结果为对象的地址， 解决：重写__str__
> p = p1 + p2
> print(p)   # 本质上相加两个人的属性【年龄】
> # print(p.__str__())   # 33
> # print(p1.__add__(p2))  # 33
> 
> 
> # 2.
> '''
> > ---->__gt__   greater than
> < ----> __lt__  less than
> == ---> __eq__  equal
> != ---> __ne__  not equal
> >= ---> __ge__
> <= --->__le__
> 比较的结果都是布尔值，重载上述运算符时，返回值都设置为布尔值
> '''
> class Person():
>     def __init__(self,age):
>         self.age = age
>     def __gt__(self, other):
>         return self.age > other.age
> 
> p1 = Person(10)
> p2 = Person(23)
> print(p1 > p2)
> print(p1.__gt__(p2))
> print(Person.__dict__)
> 
> ```

### 四、对象的内置内容

#### 1.内置对象

> ```Python
> # 1.__slots__:限制对象属性的动态绑定
> 
> # 2.__dict__:获取类或对象的所有信息【属性和函数】，返回一个字典   ****
> # print(str.__dict__)
> 
> # 3.__module__;获取指定对象属于哪个模块，如果时当前模块，则结果为__main__,如果是其他模块，则结果为模块名
> print(str.__module__)  # builtins
> 
> class Person():
>     def __init__(self,age):
>         self.age = age
> p = Person(45)
> # print(p.__module__)  # __main__
> 
> # 4. __name__:可以用来判断正在执行的是否是当前文件    ******
> # 如果结果为__main__则说明运行的是当前文件，如果是模块名则表示运行的是其他文件
> # print(__name__)
> import t1
> 
> # 适用的场景:当作代码的规范，认为是程序执行的入口
> if __name__ == '__main__':
>     # 函数的调用
>     pass
> 
> # 5.__class__：类似于type(),获取指定对象的数据类型
> print(type(p))
> print(p.__class__)
> 
> ```

#### 2.内置函数

> ```Python
> # 1.id():获取一个对象的内存地址
> 
> # 2.type():获取一个对象的数据类型
> 
> # 3.isinstance():判断一个对象的数据类型是否是指定类型   ******
> print(isinstance(45,str))
> print(type(45) == str)
> 
> # 练习
> lst = ['faf',24,6,False,34,True,'535',18]
> l1 = [ele for ele in lst if isinstance(ele,int)]  # 涉及到继承，继承自int或int都会挑选
> print(l1)  # [24, 6, False, 34, True, 18]
> l2 = [ele for ele in lst if type(ele) == int]  # 精确匹配，只挑选int
> print(l2)  # [24, 6, 34, 18]
> 
> # 4.issubclass(类1，类2)：判断类1和类2直接是否具有继承关系
> class Animal():
>     pass
> class Cat(Animal):
>     pass
> class SmallCat(Cat):
>     pass
> print(issubclass(Cat,Animal))
> ```