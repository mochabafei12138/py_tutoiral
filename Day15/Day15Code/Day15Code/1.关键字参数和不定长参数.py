# 1.关键字参数
# 注意：默认参数主要体现在函数的定义中【声明】，关键字参数主要体现在函数的调用中
def func1(a,b,c):
    print('11111',a,b,c)
# 必须参数的缺点：必须按照顺序传参，否则可能会匹配不上
func1(10,20,30)
# 关键字的优点：可以不按照形参的顺序传参。根据关键字就可以识别,关键字一定要和形参保持一致
func1(b=20,c=30,a=10)
func1(10,20,c=30)

# 默认参数和关键字参数常用于系统函数
print(45,67,7)  # 默认参数sep
print(34,7,23,sep='=')
list1 = [23,5,5]
list1.sort(reverse=True)

print("*" * 30)

# 2.不定长参数/可变参数
# a.*x:x会被当作元组处理
def f1(*n):
    print(n,type(n))  # <class 'tuple'>
# 在调用函数的时候，不定长参数可以处理任意数量的参数
f1()   # ()
f1(10)
f1('abc')   # ('abc',)
f1(34,56,8,9,34,6,7,'faf','fag',True)  # (34, 56, 8, 9, 34, 6, 7, 'faf', 'fag', True)

# 练习：求任意多个数字的和
def get_total(*n):
    total = sum(n)
    print(total)
get_total(34,6,87)
get_total(2,6,8,90)

# b.**x:x会被当作字典处理
def f2(**n):
    print(n,type(n))   # <class 'dict'>
    for k,v in n.items():
        print(k,v)

f2()   # {}
# 在调用函数的过程中，给**x进行传参，要按照key=value的形式传参，而且key必须是以变量的形式存在，最终该变量会被识别为字符串
f2(x=10,y=20,z=30)  # {'x': 10, 'y': 20, 'z': 30}

# c.
# 注意：在同一个函数中，*只能出现一次，**也只能出现一次
# 错误写法
# def f3(*n1,*n2):
#     print(n1,n2)
# def f3(**n1,**n2):
#     print(n1,n2)
# *和**可以同时出现
def f3(*n1,**n2):
    print(n1,n2)
f3()
f3(435,6,67)
f3(a=45,b=123)
f3(34,6,7,8,name='张三',age=18)

# 如果*和**同时出现，经常会使用*args,**kwargs
def f3(*args,**kwargs):
    pass






