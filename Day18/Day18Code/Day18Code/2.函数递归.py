# 1.恶意递归调用
# def a():
#     print('aaaa')
#     a()
# a()

# 2.
# a.斐波那契数列
# 需求：报一个数，返回斐波那契数列中该位置的数字
"""
1   2   3   4   5   6   7   8   9   10......
1   1   2   3   5   8  13   21  34  55......

分析：求func(5)
第一步
func(5) = func(4) + func(3) = 3 + 2 = 5
第二步：
func(4) = func(3) + func(2) = 2 + 1 = 3
func(3) = func(2) + func(1) = 1 + 1 = 2
第三步：
func(3) = func(2) + func(1) = 1 + 1 = 2

func(n) = func(n - 1) + func(n - 2)
"""
def func(n):
    print('~~~~',n)
    if n == 1 or n == 2:
        return 1
    else:  # n >= 3
        return func(n - 1) + func(n - 2)

# r1 = func(2)
# print(r1)  # 1
# r1 = func(5)
# print(r1)
# r1 = func(20)
# print(r1)  # 55
# r1 = func(6)
# print(r1)  # 8

# b.求1~某个数之间所有整数的和
'''
func(100)--->1~100 = func(99) + 100
func(99) --->1~99 = func(98) + 99
.....
func(n)--->1~n = func(n - 1) + n
'''

def func(n):
    print('~~~~~',n)
    if n == 1:
        return 1
    else:
        return func(n - 1) + n

r2 = func(100)
print(r2)  # 5050

# 注意：在实际应用中，不推荐使用递归，相比于循环，递归的效率较低