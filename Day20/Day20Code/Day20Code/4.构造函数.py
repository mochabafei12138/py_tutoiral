# 一、构造函数的工作原理
'''
构造函数：包括__new__和__init__
在Python中，以__xxx__方式命名的函数，被称为魔术函数/魔术方法，该类函数都是在特定的场景下被自动调用的，无需手动调用
    __new__:从无到有的过程，表示真正意义上创建对象
    __init__:初始化的过程，表示将__new__创建出来的对象进行初始化

代码执行顺序：当x = 类名()创建对象的时候，首先会自动调用__new__,创建出来一个对象，且将该对象返回，
           同时自动将该对象传递给__init__,对该对象完成初始化
'''
class Person():
    def __new__(cls, *args, **kwargs):
        print('new~~~~')
        return super().__new__(cls)   # 返回一个对象
    def __init__(self):
        print('init~~~~~')
p = Person()

# 二、构造函数常用的形式  ******
# 1.基本语法
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'name：{self.name},age:{self.age}')

# 一般在创建对象的时候，倾向于将对象创建完有初始状态的【初始状态：创建对象的同时进行特征的描述，或者定义属性】
# 注意：当类中定义了__init__,创建对象的时候，一定要注意参数保持一致
p1 = Person('aaa',10)
# p1.name = 'aaa'
# p1.age = 10
print(p1.name,p1.age)

p2 = Person('bbb',10)
# p2.name = 'bbb'
# p2.age = 10
print(p2.name,p2.age)

p3 = Person('ccc',20)
print(p3.name,p3.age)

p1.show()
p2.show()
p3.show()

# 2.应用
# 第一步：定义类
class Teacher():
    def __init__(self,name):
        self.name = name
    # self表示老师对象，stu是一个学生对象,只要一个变量表示的是某个对象，则该变量作为对象使用，可以访问对象的属性或类中的函数
    def let_stu_introduce(self,stu):
        print(stu)
        print(f'{self.name}让{stu.name}做自我介绍')
        # 学生开始执行自己的行为：做自我介绍和才艺战术
        stu.introduce()
        stu.show_talent()

class Student():
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def introduce(self):
        print(f'大家好，我是{self.name},今年{self.age},爱好{self.hobby}')
    def show_talent(self):
        if self.name == '小明':
            print(f'接下来给大家展示一段{self.hobby},我家里有几百头牛，几百头🐏~~~~')
        elif self.name == '小花':
            print(f'接下来给大家展示一段{self.hobby},一起来摇摆~~~~')
        elif self.name == '小丽':
            print(f'接下来给大家展示一段{self.hobby},看谁在唱歌~~~~')

# 第二步：创建对象并描述特征
tea = Teacher('王老师')

stu1 = Student('小明',18,'吹牛逼')
stu2 = Student('小花',17,'跳舞')
stu3 = Student('小丽',19,'唱歌')

# 第三步：在类中定义函数并调用函数
tea.let_stu_introduce(stu2)
tea.let_stu_introduce(stu1)
tea.let_stu_introduce(stu3)