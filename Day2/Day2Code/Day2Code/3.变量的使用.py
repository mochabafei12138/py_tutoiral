# 1.变量的重新赋值
name = '张三'     # 如果一个变量在代码中第一次出现，则称为定义，‘张三’被称为初始值
print(name)

name = '李四'     # 如果一个变量在代码中不是第一次出现，则表示重新赋值，'李四'被称为重新赋的值
print(name)

# 2.常量
# 变量命名法：所有字母全部小写，不同单词之间使用下划线连接
# 常量命名法：所有字母全部大写，不同单词之间使用下划线连接
stu_name = '尼古拉斯.赵四'

# 众所周知，圆周率是一个典型的常量，所以在Python中也用常量的方式表示
PI = 3.14
print(PI)

# 注意：Python中没有任何的机制阻止你干坏事，全凭自觉,常量的本质还是一个变量，只是一个标记
PI = 'abc'
print(PI)   # abc

# 3.type(x):获取数据x的数据类型
num1 = 12
print(type(num1))   # <class 'int'>

data1 = 'abc'
print(type(data1))  # <class 'str'>

list1 = [4,5,7]
print(type(list1))  # <class 'list'>

# 注意1：
a1 = 88
a2 = '88'
print(a1,a2)  # 88 88
print(type(a1),type(a2))  # <class 'int'> <class 'str'>

# 注意2：但凡通过input从控制台输入的内容，不管你输入了什么，全部都是字符串
# age = input('请输入你的年龄：')   # 18
# print(age,type(age))   # 18 <class 'str'>

# 注意3：类型可以直接比较，比较运算符：==
print(type(a1) == int)
print(type(a1) == str)
print(type(a1) == type(a2))