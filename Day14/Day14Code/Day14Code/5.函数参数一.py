# 1. 必需参数/必须参数
# 注意：必须参数，实参必须传参，实参和形参的数量保持一致
def func1(num1,num2):
    print(num1,num2,num1 + num2)
func1(34,3)

# 注意：调用函数传参的过程中，要注意需要的数据类型
def func2(name,age):
    print('姓名:%s,年龄：%d' % (name,age))
# func2('张三','18')  # TypeError: %d format: a number is required, not str
func2('张三',18)

# 注意：name:str表示给name参数声明类型
# ->int表示返回值类型为int
def func3(name:str) -> str:
    print('333333')
func3('fafgqg4')

# 2. 默认参数
def func1(num1=0,num2=0):
    print(num1,num2,num1 + num2)
# 如果形参有默认值，则调用函数的时候根据需要可以不传参
func1()
func1(10)
func1(10,20)

# 注意
def func1(num1,num2=0):
    print(num1,num2,num1 + num2)
func1(7)
func1(7,10)

# 多个参数，部分为必须参数，部分为默认参数，一定要将必须参数书写在默认参数的前面non-default argument follows default argument
# 错误写法
# def func1(num1=0,num2):
#     print(num1,num2,num1 + num2)