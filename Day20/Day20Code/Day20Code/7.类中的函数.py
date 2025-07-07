class Book():
    __slots__ =  ('name','author')
    # 1.定义
    # 1_a.实例函数，特点：第一个形参是self，self表示当前对象
    def __init__(self,name,author):
        self.name = name
        self.author = author

    # 3.函数之间相互调用
    # 3_a.实例函数之间相互调用，格式：self.xxx()
    def show1(self):
        print('实例函数~~~~~~')
        print(f'书名:{self.name},作者:{self.author}')
        # 在show1中调用show2
        self.show2()
    def show2(self):
        print('show~~~2222')

    # 1_b.类函数,特点：用@classmethod装饰器装饰，第一个形参是cls，cls是class的缩写，表示当前类
    @classmethod
    def func1(cls):
        print('类函数~~~~',cls)
        # 3_b.类函数之间相互调用，格式:cls.xxx()
        cls.func2()

        # 3_c.类函数中调用实例函数,格式：先通过cls创建对象，然后再调用
        # 创建对象，同样会调用__init__，注意参数
        b = cls('Python机器学习入门与精通','tom')
        b.show2()

    @classmethod
    def func2(cls):
        print('func~~~~22222')

    # 1_c.静态函数,特点：用@staticmethod装饰器装饰，参数没有特别之处
    @staticmethod
    def check1():
        print('静态函数~~~~~')

book = Book("Python疯狂讲义",'jack')

# 2.调用
# a.实例函数：只能通过对象调用
book.show1()

# b.静态函数和类函数：可以通过类名或对象调用
Book.func1()
Book.check1()

# book.func1()
# book.check1()