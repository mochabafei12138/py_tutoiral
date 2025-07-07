# 1.对象属性的动态绑定
# 只要是 对象.属性 = 值 类似这样的语法，都是给对象动态绑定属性，在默认情况下，对于属性的绑定没有任何限制
# class Doctor():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# doc = Doctor('张大夫',40)
# doc.kind = '外科'
# print(doc.name,doc.age,doc.kind)
# doc.a = 234
# doc.eggw= 45

# 2.限制对象属性的动态绑定
class Doctor():
    # 用__slots__限制对象属性的动态绑定，定义一个元组，将属性名以字符串的形式书写在元组中,一般是结合实际需求或实际情况确定
    __slots__ = ('name','age','kind')
    # 注意：当元组中只有一个元素的时候，要添加逗号
    # __slots__ =  ('name',)
    def __init__(self,name,age):
        self.name = name
        self.age = age

doc = Doctor('张大夫',40)
doc.kind = '外科'
print(doc.name,doc.age,doc.kind)
# doc.a = 234   # AttributeError: 'Doctor' object has no attribute 'a'
# doc.eggw= 45