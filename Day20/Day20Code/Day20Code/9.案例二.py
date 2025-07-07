'''
1.定义一个Number类，其中定义加减乘除的函数，分别计算两个数的相关运算
'''
# 方式一：实例函数
class Number():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
num = Number(10,20)
print(num.add(),num.sub(),num.mul(),num.div())

# 方式二：类函数
class Number():
    @classmethod
    def add(cls,num1,num2):
        return num1 + num2
    @classmethod
    def sub(cls,num1,num2):
        return num1 - num2
    @classmethod
    def mul(cls,num1,num2):
        return num1 * num2
    @classmethod
    def div(cls,num1,num2):
        if num2 != 0:
            return num1 / num2
print(Number.add(10,20),Number.sub(10,20),Number.mul(10,20),Number.div(10,20))

# 方式三：静态函数
class Number():
    @staticmethod
    def add(num1,num2):
        return num1 + num2
    @staticmethod
    def sub(num1,num2):
        return num1 - num2
    @staticmethod
    def mul(num1,num2):
        return num1 * num2
    @staticmethod
    def div(num1,num2):
        if num2 != 0:
            return num1 / num2
print(Number.add(10,20),Number.sub(10,20),Number.mul(10,20),Number.div(10,20))


'''
2.构造一个圆，求该圆的面积和周长，最后判断一个点和该圆之间的关系
'''
'''
圆类
    特征：圆心【本质上就是一个点】和半径
    行为：该圆的面积
         该圆的周长
         判断一个点和该圆之间的关系
         
点类：
    特征：x  y
'''
import math
class Point():
    __slots__ = ('x','y')
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Circle():
    __slots__ = ('circle_center','radius')
    # circle_center:圆心，本质上就是一个点，所以此处传参Point类的对象
    def __init__(self,circle_center,radius):
        self.circle_center = circle_center
        self.radius = radius
    def length(self):
        return round(2 * math.pi * self.radius,3)
    def area(self):
        return round(math.pi * self.radius ** 2,3)
    def judge(self,point):
        # self:圆的对象   point:某点的对象
        '''
        判断某点和圆之间的关系：判断某点到圆心的距离和圆的半径之间的大小关系
        两点之间的距离：(x1,y1)  (x2,y2)    math.sqrt((x1 - x2) ** 2 + (y1- y2) ** 2)

        圆心的坐标：(self.circle_center.x,self.circle_center.y)
        某点的坐标：(point.x,point.y)
        '''
        distance = math.sqrt((self.circle_center.x - point.x) ** 2 + (self.circle_center.y - point.y) ** 2)
        if distance > self.radius:
            return '圆外'
        elif distance < self.radius:
            return '圆内'
        else:
            return '圆上'

# 创建圆心的对象
circle_center = Point(23,18)
# 创建圆的对象
circle = Circle(circle_center,10)
r1 = circle.length()
r2 = circle.area()
print(f'该圆的面积:{r2},周长:{r1}')

point = Point(56,19)
print(f'某点和该圆之间的关系为：{circle.judge(point)}')

'''
3.定义类，用来描述数字时钟

时钟类：
    特征:时分秒
    行为：走针
'''
import  time
class Clock():
    __slots__ =  ('hour','minutes','seconds')
    def __init__(self,hour=0,minutes=0,seconds=0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    def run(self):
        self.seconds += 1        # 17:20:59---->17:21:00
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1    # 17:59:59
            if self.minutes == 60:
                self.minutes = 0
                self.hour += 1   # 23:59:59
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        print('%.2d:%.2d:%.2d' % (self.hour,self.minutes,self.seconds))

# clock = Clock()
# clock = Clock(17,24,30)

# 获取当前时间
t1 = time.localtime()
# print(t1[3],t1[4],t1[5])
clock = Clock(t1[3],t1[4],t1[5])

while True:
    clock.show()
    time.sleep(1)
    clock.run()
