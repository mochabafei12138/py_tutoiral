from multiprocessing import  Process
import  os,time

# 需求：在子进程中修改全局变量，查看父进程中访问到的全局变量的值
num  = 100

def task():
    print('子进程启动~~~~')
    global num
    num += 50
    time.sleep(2)
    print('子进程结束~~~~~')
    print(f'子进程，全局变量num={num}~~~~~')  # 150

if __name__ == '__main__':
    print('父进程启动')

    p = Process(target=task)
    p.start()

    # 合并进程
    p.join()

    print('主进程的任务执行了****')

    print('父进程结束')
    print(f'父进程，全局变量num={num}')   # 100

    '''
    总结：
        验证了进程之间是独立的，相互之间资源不共享
        
        工作原理：在创建子进程对象的时候，会将所有的全局变量数据进行备份
                每个进程都有自己的代码段，数据段和堆栈段，所以进程之间是独立的，资源不共享
    '''