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
        # 进入with代码块，则表示获取锁，当with代码块执行完毕，会自动释放锁
        with lock:
            # 共享资源
            change(m)

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