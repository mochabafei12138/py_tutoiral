'''
编写小学生算术能力测试系统
设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以下功能：
a.提供10道加、减、乘或除四种基本算术运算的题目；
b.练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确并显示出相应的信息。
'''
import  random

print('欢迎进入天才儿童答题系统'.center(40,'*'))

# 定义用来记录总的题目数和回答正确的数量
count = 0
right = 0

# 10道题目，循环10次
while count < 10:
    # 定义列表，表示加减乘除的符号
    options = ['+','-','*','/']
    # 随机产生运算符
    op = random.choice(options)
    # 随机产生0~100以内的运算数
    num1 = random.randint(0,99)
    num2 = random.randint(1,99)   # 除数不能为0
    # 出题
    print(f'{num1} {op} {num2} =')
    # 等待用户输入答案
    answer = input('请输入你的答案【输入q退出】：')
    if answer.lower() == 'q':
        break

    # 判断随机生成的运算符，并计算正确结果
    if op == options[0]:
        r = num1 + num2
    elif op == options[1]:
        r = num1 - num2
    elif op == options[2]:
        r = num1 * num2
    else:
        r = num1 / num2

    # 判断用户输入的结果是否正确，为了保持类型的一致，转换类型
    if answer == str(r):
        print('回答正确')
        right += 1
    else:
        print('回答错误')
    count += 1

# 计算正确率
if count == 0:
    percent = 0
else:
    percent = right / count
print('答题结束，共回答%d道题,正确%d道题，正确率为%.2f%%' % (count,right,percent * 100))