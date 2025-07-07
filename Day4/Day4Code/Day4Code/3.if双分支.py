# 1.基本语法
# a.双分支中条件的使用和单分支中完全相同
# b.if-else双分支的特点：实现二选一的操作
print('start~~~~~~')
num1 = 45
num2 = 45
if num1 == num2:
    print('yes~~~1111')
else:
    print('no~~~~~1111')
print('end~~~~~~~')

# 2.应用
# a.禁止未成年人进入网吧
# age = int(input('请输入你的年龄：'))
# if age < 18:
#     print('未成年禁止进入网吧')
# else:
#     print('欢迎光临，请多多充值')

# b.从控制台输入一个数，判断该数是否是偶数
# num = int(input('请输入一个数：'))
# # 偶数---》2的倍数----》能被2整除-----》%
# # 注意：=只使用在给变量赋值的语法中，==用于比较
# if num % 2 == 0:
#     print(f'{num}是偶数')
# else:
#     print(f'{num}是奇数')

# 3.随机数的获取
import random
# 方式一
n1 = random.randint(1,100)  # 在1~100之间获取一个整数随机数，是闭区间
print(n1)
# 方式二
n2 = random.choice(range(1,101,1))  # 在1~100之间获取一个整数随机数，前闭后开区间，等价于[1,2,3,4,5....100]
print(n2)

# 获取0~100之间的任意一个整数随机数
n3 = random.randint(0,100)
n3 = random.choice(range(0,101,1))
n3 = random.choice(range(101))
# 其他用法
n4 = random.choice(range(1,100)) #获取1~99之间的任意一个整数随机数,等价于[1,2,3....99]
n5 = random.choice(range(1,100,2)) #获取1~99之间的任意一个奇数随机数,等价于[1,3,5.....99]
n6 = random.choice(range(0,100,2)) #获取0~99之间的任意一个偶数随机数,等价于[0,2,4,6....98]

# 问题一：只省略start
print(list(range(101,2)))   # []，原因：101被识别为start,2被识别为end,省略了step,等价于range(101,2,1)
# print(random.choice(range(101,2)))  # 相当于要从一个空容器中取出一个数据，报错out of range

# 问题二：从start~end递增，则步长为正数，从start~end递减，则步长为负数
print(list(range(1,101,2)))
print(list(range(100,-1,-2)))   # 100~0

# 4.应用二
# 模拟彩票中奖
import random
# random_num = random.randint(1,99)
random_num = random.choice(range(1,100))
print(random_num)
input_num = int(input('请输入一个1~99之间的数字：'))
if input_num == random_num:
    print('恭喜你，中奖了！')
else:
    print('很遗憾，可以期待下次~~~~~')