'''
1.设计两个类：
	a. 一个点Pointer类，属性包括x，y坐标。
	b. 一个Rectangle类（矩形）,属性有左上角坐标，宽，高
		方法：1. 计算矩形的面积；2. 判断点是否在矩形内
 	c.实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形
'''
class Pointer():
    __slots__ = ('x','y')
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rectangle():
    __slots__ =  ('left_top_point','width','height')
    # left_top_point:表示一个点Pointer的对象
    def __init__(self,left_top_point,width,height):
        self.left_top_point = left_top_point
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def judge(self,point):
        # self:矩形对象  point:点的对象
        # x轴
        r0 = self.left_top_point.x < point.x < self.left_top_point.x + self.width
        # y轴
        r1 = self.left_top_point.y - self.height < point.y < self.left_top_point.y
        return r0 and r1

# 创建表示左上角点的对象
left_top_point = Pointer(2,19)
# 创建矩形对象
rect = Rectangle(left_top_point,10,10)
print(f'矩形的面积为：{rect.area()}')

# 创建一个某点的对象
point = Pointer(54,10)
print(rect.judge(point))