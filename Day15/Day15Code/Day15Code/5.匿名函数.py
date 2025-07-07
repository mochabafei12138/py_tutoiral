# 1.
# 标准函数的定义
def f1(n):
    print('函数被调用了~~~')
    return n + 1
print(f1)   # <function f1 at 0x00000228F1D7F040>
r1 = f1(6)  # 函数的调用
print(r1)   # 函数的返回值

# 匿名函数/lambda表达式，语法：lambda  形参列表:返回值
f2 = lambda n: n + 1
print(f2)   # <function <lambda> at 0x000002860924C3A0>
r2 = f2(8)  # 调用函数
print(r2)   # 函数的返回值

# 2.注意：在匿名函数中，返回值涉及到判断，可以借助于三目运算符实现
def is_even(num):
    if num % 2 == 0:
        return True
    return False
r21 = is_even(10)
print(r21)

is_even2 = lambda  num: True if num % 2 == 0 else False
r22 = is_even2(13)
print(r22)

# 3.在匿名函数中，同样可以使用默认参数，关键字参数和不定长参数
f31 = lambda x,y=0:x ** 2 + y ** 2
print(f31(2))
print(f31(2,3))
print(f31(x=4,y=5))

f32 = lambda *x:sum(x)
print(f32(34,65,7,8))

f33 = lambda **x:x['a']
print(f33(a=23,b=45,c=67))

# 4.匿名函数定义完之后可以直接调用
print((lambda *x:sum(x))(456,7,8,9))

# 使用场景：匿名函数常用于作为其他函数的参数使用，max()/sort()/高阶函数

# 思考题【面试题】
def func():
    lst = []
    for x in range(5):
        lst.append(lambda n:x * n)
    return lst
r = func()
# 下面代码输出的结果，并说明原因
print(r[0](2))
print(r[1](2))
print(r[2](2))
print(r[3](2))
print(r[4](2))