# 1.导入模块
from  threading import *
import  os,time

def task1():
    print(f'子线程启动~~~~~~：{current_thread().name}')
    time.sleep(5)
    print(f'子线程结束~~~~~~：{current_thread().name}')

def task2(a,b):
    print(f'子线程启动~~~~~~：{current_thread().name}')
    print(a,b)
    time.sleep(5)
    print(f'子线程结束~~~~~~：{current_thread().name}')

if __name__ == '__main__':
    # 2.任何一个程序启动之后，会启动一个进程，该进程被称为父进程，同时，该进程会默认启动一个线程，该线程被称为主线程
    # current_thread().name获取的是当前正在执行的线程的名称，主线程的默认名称为MainThread
    print(f'主进程{os.getpid()}中的主线程启动:{current_thread().name}')

    # 3.创建子线程
    '''
    Thread(target,args,name)
        target:当前线程需要执行的任务的函数名
        args:表示任务函数的参数。值一定是一个元组
        name:给线程命名
    '''
    # 注意：子线程默认的名称为Thread-1,Thread-2.....
    # a.任务函数无参
    # t = Thread(target=task1)
    # t.start()

    # t = Thread(target=task1,name='hello')
    # t.start()

    # b.任务函数有参
    t = Thread(target=task2,args=(34,19),name='abc')
    t.start()

    # 和进程的用法类似，也可以合并线程，则该线程优先执行
    t.join()

    time.sleep(1)

    print(f'主进程{os.getpid()}中的主线程结束:{current_thread().name}')
