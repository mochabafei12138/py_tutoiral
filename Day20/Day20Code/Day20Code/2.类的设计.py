# 类的定义
class Person():
    # 行为描述：函数
    '''
    关于self
        a.self不是关键字，本质上可以是一个任意的标识符，但是使用self表示自己【self在Java中是关键字】
        b.类中的函数，默认的情况下，形参列表的第一个参数都是self
        c.self表示当前对象，哪个对象调用该函数，则self表示哪个对象
        d.当调用函数的时候，self无需手动传参，会自动将当前对象传参给self,只需要注意自己定义的参数的传参即可
    '''
    def eat(self,food):
        print(f'eating {food}',f'self:{id(self)}')
    def run(self):
        print('running')
    def show(self):
        print(f'姓名:{self.name},年龄：{self.age}')  # 哪个对象调用show函数，则输出的就是该对象对应的属性

# 创建对象
p1 = Person()
print(p1)

p2 = Person()
print(p2)

# 特征描述：变量，语法：对象.属性  = 值
# 对一个对象进行某个特征的描述，可以借助于变量表示，此时的变量也可以被称为属性
p1.name = '张三'
p1.age = 20
# print(p1.name,p1.age)

p2.name = '李四'
p2.age = 18
p2.height = 180
# print(p2.name,p2.age,p2.height)

# 对象能且只能执行当前类中的行为【对象调用当前类中的函数】，语法：对象.函数(实参)
print('p1:',id(p1))
p1.eat('apple')
# p1.run()
p1.show()

print('p2:',id(p2))
p2.eat('banana')
# p2.run()
p2.show()


