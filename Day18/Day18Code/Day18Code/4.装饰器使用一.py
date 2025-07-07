def outter(func):
    print('外部函数~~~~~~start')
    def inner():
        # 调用原函数
        print('inner~~~~~~~~~~')
        func()
        # 增加新的功能
        print('new~~~~~~')

    print('外部函数~~~~~~end')
    return inner

@outter    # 等价于f = outter(a)。调用了外部函数
def a():
    print('春节快乐')

print(a)   # <function outter.<locals>.inner at 0x000001AE54DCC430>
a()    # 等价于 f()，调用了内部函数


'''
总结：
    a.使用@xxx装饰某个函数，则该装饰器一定要先存在，然后才能使用
    b.@xxx本质上表示调用装饰器的外部函数，自动将已知的函数传参给了func，同时自动将返回值inner接出来
    c.当原函数传参给func之后，此时原函数的函数名就会给重新赋值，赋值为inner,所以a()表示调用的是inner()
'''