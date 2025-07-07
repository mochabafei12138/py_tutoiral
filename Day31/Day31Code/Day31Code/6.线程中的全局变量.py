from threading import  Thread

num = 0

def change(n):
    global  num
    num += n
    num -= n      # 0

def task(m):
    for _ in range(10000000):
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

    '''
    原因：多个线程之间资源是共享的，所以当多个线程同时访问一个全局变量的时候，会导致全局变量的结果和理论不一致
    
    分析：
        num += n-----》第一步：x = num + n   第二步：num = x
        
        t1:x1 = num + n       x1 = 5
        
        t2:x2 = num + n       x2 = 8
        t2:num = x2          num = 8
        
        t1:num = x1         num = 5
        t1:x1 = num - n     x1 = 0
        t1:num = x1         num = 0
        
        t2:x2 = num - n    x2 = -8
        t2:num = x2         num = -8
        
    解决：
        只需要保证一个线程抢到时间片之后，能够将所有的代码执行完毕，其他线程处于等待状态
    实现：
        给共享资源加锁，哪个线程抢到时间片，则该线程持有锁，当共享资源对应的代码执行完毕，则释放锁
    '''