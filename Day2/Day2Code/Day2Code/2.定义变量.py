# 1.定义变量
# 注意1：书写规范：遇到符号，如：=，+，- 等，在符号的前后添加空格
'''
name :变量名,是一个标识符【规则和规范】
=：赋值运算符
'张三':值/数据

含义：将'张三'数据赋值给name变量，name中存储了'张三'
'''
# Python中的代码是从上往下依次执行的，所以后期代码中使用name，相当于使用‘张三’
name = '张三'
print(name)

# 2.在定义变量的同时，可以声明变量的类型，后期才会用到【好处：后期会用到某些数据类型中的功能，有了类型的声明之后，系统功能可以自动提示】
num:int = 10
hobby:str = '唱歌'

# 3.定义多个变量
# a.多个变量具有相同的值
# num1 = 10
# num2 = 10
# num3 = 10

# 简化
num1 = num2 = num3 = 10
print(num1,num2,num3)

# b.多个变量具有不同的值
# score1 = 10
# score2 = 34
# score3 = 69

# 工作原理：数据和变量是从左往右一一对应的关系
score1,score2,score3 = 10,34,69
print(score1,score2,score3)

# 问题1：
# score1,score2,score3,score4 = 10,34,69  # ValueError: not enough values to unpack (expected 4, got 3)
# score1,score2,score3 = 10,34,69,878     # ValueError: too many values to unpack (expected 3)
# 注意：默认情况下，定义多个不同值的变量，则变量的数量和数据的数量一定要保持一致

# 问题2：
num1,num2 = 45,66
print(num1,num2)

num3,num3 = 19,38
print(num3)

# 等价于
num3 = 19
num3 = 38
print(num3)