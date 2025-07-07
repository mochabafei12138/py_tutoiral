# 1.基本语法
print('start~~~~~')
# a.if语句中的条件是常量，变量或表达式
# b.Python中表示假的数据：0  0.0   False "" []  ()  {}  None等,在if语句中作为条件，都表示条件不成立
if 'twt':
    print('yes')

num = 0
if num:
    print('yes~~~1111')

num1 = 45
num2 = 99
if num1 == num2:
    print('yes~~~2222')

print('end~~~~~~')

# 在Python中，是通过缩进区分代码块的，在编写程序的过程中，要注意缩进对齐问题,
#  一个缩进一般是4个空格或一个tab键
if 34:
    print('wgwhwh')

print('=' * 50)

# 2.工作原理：代码块要么执行，要么不执行
num1 = 45
num2 = 90
if num1 == num2:
    print('yes~~~2222')

print('over')

# 3.应用
# a.禁止未成年人进入网吧
# age = int(input('请输入你的年龄：'))
# if age < 18:
#     print('未成年禁止进入网吧')

# b.从控制台输入一个数，判断该数是否是偶数
num = int(input('请输入一个数：'))
# 偶数---》2的倍数----》能被2整除-----》%

# 注意：=只使用在给变量赋值的语法中，==用于比较
if num % 2 == 0:
    print(f'{num}是偶数')