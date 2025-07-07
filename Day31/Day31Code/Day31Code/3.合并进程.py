from multiprocessing import  Process
import  os,time

def task():
    print(f'子进程启动，进程号:{os.getpid()}')
    print(3536523)
    time.sleep(5)
    print(f'子进程结束~~~~，进程号:{os.getpid()}')

if __name__ == '__main__':
    print(f'父进程启动，进程号:{os.getpid()}')

    # 创建子进程
    p = Process(target=task)
    p.start()

    '''
    默认情况下，根据系统的调度，主进程可能会早于子进程结束
    但是将子进程进行合并【join】之后，主进程等待子进程执行完毕之后才结束，子进程相当于做了插队操作
    '''
    # join一定要在start之后，否则报错：AssertionError: can only join a started process
    p.join()

    print('main~~~~~')
    time.sleep(1)

    print(f'父进程结束~~~~~，进程号:{os.getpid()}')
'''
join之前
父进程启动，进程号:7792
main~~~~~
子进程启动，进程号:13904
3536523
父进程结束~~~~~，进程号:7792
子进程结束~~~~，进程号:13904

join之后
父进程启动，进程号:3772
子进程启动，进程号:12468
3536523
子进程结束~~~~，进程号:12468
main~~~~~
父进程结束~~~~~，进程号:3772
'''