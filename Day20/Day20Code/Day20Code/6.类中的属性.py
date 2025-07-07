class Person():
    # 1.定义位置不同：类属性直接定义在类中，只要是动态绑定的属性都是实例属性【在__init__中或在类的外面直接动态绑定定义】
    # 注意：只要是  对象.属性 = 值  这样的语法，其实都是实例属性
    # 类属性
    place = '地球'
    num = 66

    def __init__(self,name,age):
        # 实例属性/对象属性
        self.name = name
        self.age = age
p1 = Person('赵四',34)
# 实例属性/对象属性
p1.height = 170
p1.num = 100

# 2.访问方式不同
# 类属性可以通过类名或对象访问
print(Person.place)
print(p1.place)

# 而实例属性只能通过对象访问
print(p1.name,p1.age,p1.height)

# 3.访问优先级不同
# 当类属性和实例属性重名时，通过对象访问，优先访问的是实例属性
print(p1.num)   # 100  实例属性

del p1.num     # 实例属性优先被访问，所以此处被删除的是实例属性
print(p1.num)  # 66   类属性

# 4.内存中的类属性和实例属性
p2 = Person('小王',18)

print(p1.name is p2.name)  # False
print(p1.place is p2.place)  # True

# 问题:p1.name和p2.name是否共享同一份内存地址？----》是不同的地址
p1.name = 'Jack'
print(p2.name)

# 问题:p1.palce和p2.place是否共享同一份内存地址？----》是同一份地址
# p1.place = '火星'   # 并不是在修改类属性的值，而是给p1动态绑定了一个place的实例属性

# 如果要修改类属性的值，则格式:类名.类属性  = 值
Person.place = '火星'
print(p1.place,p2.place)

# 5.使用场景不同：类属性用于表示多个对象共享的数据，实例属性表示每个对象特有的数据
class Student():
    # 类属性：多个对象公共的数据
    school_name = '千锋'
    def __init__(self,name,city):
        self.name = name
        self.city = city
stu1 = Student('小明','北京')
stu2 = Student('小王','成都')
print(stu1.name,stu1.city,stu1.school_name)
print(stu2.name,stu2.city,stu2.school_name)

Student.school_name = '万锋'
print(stu1.name,stu1.city,stu1.school_name)
print(stu2.name,stu2.city,stu2.school_name)

