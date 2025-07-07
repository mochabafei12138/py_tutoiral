# 1.【面试题】交换两个变量的值
# 方式一:借助于第三个变量
num1 = 10
num2 = 20
num3 = num1
num1 = num2
num2 = num3
print(num1,num2)  # 20 10

# 方式二：Python特有的语法【推荐】
num1 = 10
num2 = 20
num1,num2 = num2,num1
print(num1,num2)

# 方式三：加减法【只适用于数据是数字的情况下】
num1 = 10
num2 = 20
num2 = num1 + num2   # num2 = 30
num1 = num2 - num1   # num1 = 20
num2 = num2 - num1   # num2 = 10
print(num1,num2)

num1 = 10
num2 = 20
num3 = num1 + num2    # num3 = 30
num2 = num3 - num2    # num2 = 10
num1 = num3 - num1    # num1 = 20
print(num1,num2)

# 2.【面试题】打包和拆包
# 打包
# m1,m2,m3,m4 = 45,19,3   # ValueError: not enough values to unpack (expected 4, got 3)
m1,m2,m3,*m4 = 45,19,3,45,7,9,123,6,8,90,32
print(m1,m2,m3,m4)   # 45 19 3 [45, 7, 9, 123, 6, 8, 90, 32]
m1,m2,*m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
print(m1,m2,m3,m4)
m1,*m2,m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
print(m1,m2,m3,m4)
*m1,m2,m3,m4 = 45,19,3,45,7,9,123,6,8,90,32
print(m1,m2,m3,m4)

# 问题：在同一个赋值中，*只能出现一次
# m1,m2,*m3,*m4 = 45,19,3,45,7,9,123,6,8,90,32   # SyntaxError: multiple starred expressions in assignment
# print(m1,m2,m3,m4)

# 拆包
a1,a2,a3 = (45,7,8)
print(a1,a2,a3)
a1,a2,a3 = [45,7,8]
print(a1,a2,a3)

# 3.重要扩展：
# num1 = input('first num:')
# num2 = input('second num:')
# num3 = input('third num:')
# print(num1,num2,num3)   # str

# eval(x):识别并转换字符串x,x一定得是Python中一个有效的语法，才能识别
# r = input('请输入三个数据，用逗号隔开:')
# print(type(r))   # <class 'str'>
# r1 = eval(r)
# print(r1)
# print(type(r1))   # <class 'tuple'>

# 简化:拆包
num1,num2,num3 = eval(input('请输入三个数据，用逗号隔开:'))
print(num1,num2,num3)   # int



