# 1.基本语法
# a.不加else
# day = input('请输入一个表示星期的数字：')
# if day == '1':
#     print('星期一')
# elif day == '2':
#     print('星期二')
# elif day == '3':
#     print('星期三')
# elif day == '4':
#     print('星期四')
# elif day == '5':
#     print('星期五')
# elif day == '6':
#     print('星期六')
# elif day == '7':
#     print('星期日')

# b.加else
# 注意1：在多分支中，else的作用:当if和elif后面的条件全都不成立时，才会执行else，else的后面一定不要添加条件
# 注意2：多分支的特点：实现了多选一的操作，哪怕有多个条件成立，都只会执行其中的一个分支
day = input('请输入一个表示星期的数字：')
if day == '1':
    print('星期一')
elif day == '1':
    print('星期二')
elif day == '1':
    print('星期三')
elif day == '1':
    print('星期四')
elif day == '5':
    print('星期五')
elif day == '6':
    print('星期六')
elif day == '7':
    print('星期日')
else:
    print('else~~~~~')

# 2.应用
# 从控制台输入两个数，判断两个数的大小，输出较大的数，如果相等，则输出'相等'
num1,num2 = eval(input('输入两个数，用逗号隔开：'))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('相等')