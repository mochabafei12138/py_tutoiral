'''
构造函数：__new__和__init__,创建对象并给对象初始化【对象从无到有】
析构函数：__del__,对象被销毁的时候会自动调用的函数，

对象被销毁的时机
    a.程序执行完毕，对象的声明周期完成
    b.程序还未执行执行完毕，但是手动销毁对象，语法：del  xxx
'''
class Animal():
    def __init__(self):
        print('init被调用了')
    def __del__(self):
        print('del被调用了~~~~~')

# 1.程序执行完毕，对象自动被销毁：全局变量
# print('start')
# a = Animal()
# print('end')
'''
start
init被调用了
end
del被调用了~~~~~
'''

# 2.程序执行完毕，对象自动被销毁：局部变量
# print('start')
# def func():
#     print('func函数被调用了')
#     a = Animal()
# func()
# print('end')
'''
start
func函数被调用了
init被调用了
del被调用了~~~~~
end
'''

# 3.程序未执行完毕，对象被手动销毁
print('start')
a = Animal()
print('end')
del a
print('over')
'''
start
init被调用了
end
del被调用了~~~~~
over
'''