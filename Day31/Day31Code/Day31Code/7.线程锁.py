from threading import  *

# 创建一个锁对象
lock = Lock()

num = 0

def change(n):
    global  num
    num += n
    num -= n      # 0

def task(m):
    for _ in range(10000000):
        # 获取锁
        lock.acquire()
        try:
            # 共享资源
            change(m)
        finally:
            # 释放锁
            lock.release()

if __name__ == '__main__':
    print('主线程启动~~~~')
    t1 = Thread(target=task,args=(5,))
    t2 = Thread(target=task, args=(8,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('主线程结束~~~~~')
    print(f'全局变量num={num}')