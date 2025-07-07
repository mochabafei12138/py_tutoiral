# 1.导入模块
from multiprocessing import  Process
import os,time

# 子进程需要处理的任务
def func():
    print(f'子进程启动，进程号：{os.getpid()},对应的父进程：{os.getppid()}')
    while True:
        print('222222')
        time.sleep(0.5)

def func1(a,b,c):
    print(a,b,c,a + b + c)
    print(f'子进程启动，进程号：{os.getpid()},对应的父进程：{os.getppid()}')
    while True:
        print('222222')
        time.sleep(0.5)

if __name__ == '__main__':
    # 2.
    # 只要运行程序，则默认表示启动了一个进程，该进程被称为主进程/父进程
    # 注意：系统会自动给启动的进程分配一个进程号，通过od.getpid可以获取
    print(f'父进程启动，进程号：{os.getpid()}')

    # 3.在父进程中创建一个子进程
    # 注意：进程对象创建之后，一定要手动启动
    '''
    Process(target,args)
        target:当前进程需要执行的任务的函数名
        args:表示任务函数的参数。值一定是一个元组
    '''
    # a.任务函数没有参数
    # p = Process(target=func)
    # p.start()

    # b.任务函数有参数
    p = Process(target=func1,args=(34,6,7))
    p.start()

    # 父进程需要处理的任务
    while True:
        print('111111')
        time.sleep(1)