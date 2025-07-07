# 1.函数本质是一个变量，函数名其实就是一个变量名
# a.系统函数，如：abs()
print(abs)   # 函数本身，<built-in内置/内建 function abs>
print(abs(-23))  # 函数调用，获取返回值

f1 = abs    # 将abs作为数据赋值给f1变量,f1中存储的是可以求绝对值的函数
print(f1)   # <built-in function abs>
print(f1(-18))

# b.自定义函数
def func():
    print('1111111')
print(func)   # 函数本身，<function func at 0x0000020280F4F040>
func()   # 函数的调用

f11 = func
print(f11)    # <function func at 0x0000020280F4F040>
f11()

# c.注意：既然函数名相当于一个变量名，所以可以给该变量重新赋值,但是会导致系统的功能失效
# 所以自定义变量的时候，除了要避开关键字之外，还要避开系统函数名
# print(abs,type(abs))
# abs = 'abc'
# print(abs,type(abs))
# print(abs(-50))  # TypeError: 'str' object is not callable可调用的，注意：只有function或method才能被调用，其他类型都无法调用

# 尽量不要使用list/tuple/dict/set等命名变量,一般给这些系统的函数名添加前缀或后缀区分
print(list('abc'))
list = [23,5,56,8,9]
# print(list('fea'))  # TypeError: 'list' object is not callable


# 2.一个函数可以作为另一个函数的参数或返回值使用,只需要传递或返回函数名即可
# a.作为参数使用
def func(a,b,f):
    print(a,b,f)
    # 在函数体中，f是当作函数被调用的，所以传参的时候一定要给f传一个函数，且该函数必须有一个参数
    total = f(a) + f(b)   # 等价于abs(a) + abs(b)
    return total

print(func(34,-67,abs))  # a = 34   b = -67   f = abs

# b.
def func():
    return sum   # 返回函数本身
r = func()  # r = sum
print(r)  # <built-in function sum>

def func():
    return sum([1,2])   # 返回函数调用的返回值
r = func()  # r = 3
print(r)   # 3



