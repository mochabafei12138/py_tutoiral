# 1.从控制台输入一个数，判断该数是否是偶数，且是3的倍数
# num = int(input('请输入一个数：'))
# if num % 2 == 0 and num % 3 == 0:
#     print(f"{num}是偶数，同时是3的倍数")
# else:
#     print('不符合')

# 2.模拟猜拳游戏
import random
player = int(input('请输入(0)剪刀，(1)石头，(2)布：'))
print('玩家出的是:',player)
computer = random.randint(0,2)   # random.choice(range(3))
print('电脑出的是:',computer)
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('玩家胜利！')
elif player == computer:
    print('平局')
else:
    print('玩家失败')

