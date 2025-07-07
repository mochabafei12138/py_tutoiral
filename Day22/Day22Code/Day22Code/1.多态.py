# 体现1：同一种事物的多种体现形式，如：动物有很多种
class Animal():
    pass
class Cat(Animal):
    pass
class SmallCat(Cat):
    pass

sc = SmallCat()
# isinstance(对象,类型):判断一个对象是否是指定的类型
print(isinstance(sc,SmallCat))
print(isinstance(sc,Cat))
print(isinstance(sc,Animal))
print(isinstance(sc,object))

# 体现2：在定义的过程中无法确定变量的类型和调用的函数，只有当程序正常运行的时候才会确定该变量是什么类型，调用哪个函数
class Animal():
    def style(self):
        print('walking')
class Cat(Animal):
    pass
class Dog(Animal):
    pass
class Pig(Animal):
    pass
class Bird(Animal):
    def style(self):
        print('flying')
class Fish(Animal):
    def style(self):
        print('swimming')

def func(ani):   # ani有多种类型的体现形式，所以此处是多态的体现
    ani.style()

cat = Cat()
func(cat)

bird = Bird()
func(bird)

fish = Fish()
func(fish)


