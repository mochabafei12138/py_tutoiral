# 所谓函数的返回值，本质上是return的使用，return只能使用在函数中

# 1.一个函数没有设置返回值，默认返回None
def f1():
    print('11111')
r1 = f1()
print(r1)   # None

# 2.return可以单独作为一条语句，表示结束函数,所以在return的后面且和return对齐的情况下，不书写任何语句
# a
def f2():
    print('2222')
    return
    # print('over')    # 永远没有机会执行
    # print('over')
    # print('over')
f2()

# b.书写在return的后面但是和return没有对齐的语句，有执行的可能性，但是，一旦return被执行了，则后面的语句全都没有执行的机会，哪怕书写在循环中
def f2(n):
    print('222222')
    if n:
        print('yes')
    else:
        print('no')
        return
    print('over')       # 可能会执行
f2(0)

# 3.break/return/exit()三者的区别    *****
# a.break:结束当前循环
def f3():
    print('start~~~~~')
    for n in range(5):
        for m in range(3):
            if n == 2:
                break
            print(n,m)
    print('end~~~~~~~')
f3()
print('over~~~~')

print('*' * 50)

# b.retutn:结束当前函数
def f3():
    print('start~~~~~')
    for n in range(5):
        for m in range(3):
            if n == 2:
                return
            print(n,m)
    print('end~~~~~~~')
f3()
print('over~~~~')

print('*' * 50)

# 扩展c.exit(): 结束程序
def f3():
    print('start~~~~~')
    for n in range(5):
        for m in range(3):
            if n == 2:
                exit()
            print(n,m)
    print('end~~~~~~~')
f3()
print('over~~~~')
