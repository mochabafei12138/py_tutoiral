
# 2.猜数字游戏
'''
从控制台输入一个数，和程序产生的随机数进行比较
控制台输入的数  > 随机数 ，提示：你猜大了，往小了猜
控制台输入的数  < 随机数 ，提示：你猜小了，往大了猜
控制台输入的数  == 随机数 ，提示：恭喜你，猜对了
如果猜对，则游戏结束
'''
import  random
'''
注意：
    如果不确定循环的次数，则使用while,常用死循环while True结合break使用
    如果确定循环的次数，则使用for【range()】,常用for
'''
random_num = random.randint(1,100)
print(random_num)
guess_count = 0
while True:
    input_num = input('请输入一个1~100之间的整数：')
    if input_num.isdigit():
        input_num = int(input_num)
        if input_num in range(1,101):  # 成员运算符
            guess_count += 1
            if input_num > random_num:
                print('你猜大了，往小了猜')
            elif input_num < random_num:
                print("猜小了，往大了猜")
            else:
                print('恭喜你，猜对了')
                # 如果猜对，则游戏结束,使用break打断死循环
                break
        else:
            print('范围有误')
    else:
        print('输入有误')

print(f'总共猜了{guess_count}次')
if guess_count > 7:
    print('智商有点捉急啊，怪不得彩票中不了奖')