# 1.int(x):将x转换为整型
# x是float
print(int(45.843))  # 45

# x是字符串，使用最多
# 要求：字符串只能由正负号和数字组成，且正负号只能出现在字符串的开头的情况下，才能正确转化为整型
s1 = '34641'
print(s1,type(s1))
n1 = int(s1)
print(n1,type(n1))

s1 = '+34641'
print(s1,type(s1))
n1 = int(s1)
print(n1,type(n1))

s1 = '-34641'
print(s1,type(s1))
n1 = int(s1)
print(n1,type(n1))

# print(int('354+56')) # ValueError: invalid literal for int() with base 10: '354+56'
# print(int('35ag456'))  # ValueError: invalid literal for int() with base 10: '35ag456'
# print(int('35.456'))   # ValueError: invalid literal for int() with base 10: '35.456'

# 2.float(x):将x转换为浮点型
# x可以是int
print(float(45))  # 45.0

# x是字符串，使用较多
# 要求：字符串只能由正负号、数字和小数点组成，且正负号只能出现在字符串的开头的情况下，才能正确转化为浮点型
s1 = '34641'
print(s1,type(s1))
f1 = float(s1)
print(f1,type(f1))

s1 = '346.41'
print(s1,type(s1))
f1 = float(s1)
print(f1,type(f1))

s1 = '.34641'
print(s1,type(s1))
f1 = float(s1)
print(f1,type(f1))   # 0.34641

s1 = '-34641.'
print(s1,type(s1))
f1 = float(s1)
print(f1,type(f1))   # 34641.0

# 3.str(x):将x转换为字符串,x可以是任意类型
num1 = 89
print(type(num1))
s1 = str(num1)
print(type(s1))

# 4.bool(x):将x转换为布尔型,x可以是任意类型
# 注意1：在Python中，所有的数据类型都可以转换为布尔
# 注意2:表示空的数据转换完之后结果都是False,非空的数据转换完之后都是True
# 注意3：常用的数据类型中，表示空的数据有：False,0,0.0,'',[],(),{},None，b''
print(bool(0))     # int
print(bool(0.0))   # float
print(bool(''))    # 空str
print(bool([]))    # 空list
print(bool(()))    # 空tuple
print(bool({}))    # 空字典
print(bool(None))  # 空值

print(bool(45))
print(bool(23.6))
print(bool('faga'))
print(bool([45,67,89]))
print(bool((45,7,8)))
print(bool({'a':19}))

# 5.应用
# 需求1：假设高考数学总分为150分，请输入你的分数，计算还有多少分才能满分？
# 错误写法，原因：但凡从控制台输入进来的数据，都是字符串
# TOTAL_SCORE = 150
# score = input('请输入你的高考数学成绩：')
# print(TOTAL_SCORE - score)  # TypeError: unsupported operand type(s) for -: 'int' and 'str'

# 正确写法
# a.
# TOTAL_SCORE = 150
# score = input('请输入你的高考数学成绩：')
# print(TOTAL_SCORE - int(score))

# b.
# TOTAL_SCORE = 150
# score = input('请输入你的高考数学成绩：')
# score = int(score)
# print(TOTAL_SCORE - score)

# c.
# TOTAL_SCORE = 150
# score = int(input('请输入你的高考数学成绩：'))
# print(TOTAL_SCORE - score)

# 需求2：从控制台分别输入两个数字，求该两个数字的和
# num1 = input('请输入第一个数字：')
# num2 = input('请输入第二个数字：')
# print(num1 + num2)   # str + str---->str，+表示字符串的拼接

# a
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')
print(int(num1) + int(num2))

# b
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

# c
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
print(num1 + num2)

# d
num1,num2 = eval(input('请输入两个数字，用逗号隔开：'))
print(num1 + num2)
