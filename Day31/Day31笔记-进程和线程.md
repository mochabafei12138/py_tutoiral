### 一、进程和线程简介

#### 1.概念

##### 1.1多任务

> 程序的运行是CPU和内存协同工作的结果
>
> 操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统
>
> 问题1：什么是多任务？
>
> ​	就是操作系统可以同时运行多个任务。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已
>
> 问题2：多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？
>
> ​	答案：操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。实际上，每个任务都是交替执行的，但是，表面上看，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样【现在的电脑最起码都4核起】
>
> 并行：真正一起执行，任务数量小于cpu的核心数量【理想型】
>
> 并发：看上去一起执行，任务数量大于cpu的核心数量【现实型】
>
> ​	多核cpu实现多任务的原理：真正的并行执行多任务只能在多核cpu上实现，但是由于任务数量远远远多于cpu的核心数量，所以操作系统也会自动把很多任务轮流调度到每个核心上执行
>
> ​	对于操作系统而言，一个任务就是一个进程【process】,一个操作系统可以开启多个进程；有的进程启动之后，有可能又需要处理多个子任务，这些子若任务被称为线程【thread】

##### 1.2进程

> 是一个程序的运行状态和资源占用（内存，CPU）的描述
>
> 进程是程序的一个动态过程,它指的是从代码加载到执行完毕的一个完整过程
>
> 【面试题】进程的特点：
>
> ​	a.独立性：不同的进程之间是独立的，相互之间资源不共享（举例：两个正在上课的教室有各自的财产，相互之间不共享）
>
> ​	b.动态性：进程在系统中不是静止不动的，而是在系统中一直活动的（举例：教室里一直在讲课）
>
> ​	c.并发性：多个进程可以在单个处理器上同时进行，且互不影响（举例：一栋教学楼是处理器，多个教室同时上课就相当于多个进程，相互之间不影响）
>

##### 1.3线程

> ​	线程是进程的组成部分，一个进程可以有多个线程，每个线程去处理一个特定的子任务
>
> ​	线程的执行是抢占式的，多个线程在同一个进程中可以并发执行，其实就是CPU快速的在不同的线程之间切换，也就是说，当前运行的线程在任何时候都有可能被挂起，以便另外一个线程可以运行	
>
> ​	多线程：
>
> ​	在一个进程中，多个线程可以同时进行
>
> ​	多线程是实现了并发机制的一种有效手段,一个进程中可以包含多个线程，不同线程之间是可以资源共享的,同时运行可以提高程序的执行效率,可以同时完成多个工作
>
> 【面试题】简述进程和线程之间的区别和联系
>
> ​	a.一个程序启动之后，肯定会启动一个进程
>
> ​	b.一个进程启动之后，可能会启动多个线程，但是，该进程至少需要一个线程，否则进程是没有意义的
>
> ​	c.多个进程之间资源不共享，多个线程之间资源共享
>
> ​	d.系统创建进程需要为进程重新分配系统资源，而创建线程则容易的多，所以在实际开发中，使用多线程多于多进程

### 二、进程

#### 1.单任务现象

> ```Python
> def func():
>     while True:
>         print('222222')
> 
> if __name__ == '__main__':
>     # 任务一
>     while True:
>         print('111111')
> 
>     # 任务二
>     func()
> 
>     '''
>     在上述代码中，任务二必须等待任务一执行完毕，才有执行的机会
>     多个任务必须按照顺序执行，当一个任务执行时，其他任务必须处于等待状态，这种现象被称为单任务现象
>     '''
> ```

#### 2.多进程实现多任务

##### 2.1启动进程实现多任务

> Unix/Linux操作系统提供了一个`fork()`系统调用，fork()存在于os模块下【os.fork()】，但是，Windows没有`fork`调用
>
> 由于Python是跨平台的，提供了一个跨平台的多进程支持。`multiprocessing`模块就是跨平台版本的多进程模块
>
> `multiprocessing`模块提供了一个`Process`类来代表一个进程对象
>
> ```Python
> # 1.导入模块
> from multiprocessing import  Process
> import os,time
> 
> # 子进程需要处理的任务
> def func():
>     print(f'子进程启动，进程号：{os.getpid()},对应的父进程：{os.getppid()}')
>     while True:
>         print('222222')
>         time.sleep(0.5)
> 
> def func1(a,b,c):
>     print(a,b,c,a + b + c)
>     print(f'子进程启动，进程号：{os.getpid()},对应的父进程：{os.getppid()}')
>     while True:
>         print('222222')
>         time.sleep(0.5)
> 
> if __name__ == '__main__':
>     # 2.
>     # 只要运行程序，则默认表示启动了一个进程，该进程被称为主进程/父进程
>     # 注意：系统会自动给启动的进程分配一个进程号，通过od.getpid可以获取
>     print(f'父进程启动，进程号：{os.getpid()}')
> 
>     # 3.在父进程中创建一个子进程
>     # 注意：进程对象创建之后，一定要手动启动
>     '''
>     Process(target,args)
>         target:当前进程需要执行的任务的函数名
>         args:表示任务函数的参数。值一定是一个元组
>     '''
>     # a.任务函数没有参数
>     # p = Process(target=func)
>     # p.start()
> 
>     # b.任务函数有参数
>     p = Process(target=func1,args=(34,6,7))
>     p.start()
> 
>     # 父进程需要处理的任务
>     while True:
>         print('111111')
>         time.sleep(1)
> ```

##### 2.2合并进程

> ```Python
> from multiprocessing import  Process
> import  os,time
> 
> def task():
>     print(f'子进程启动，进程号:{os.getpid()}')
>     print(3536523)
>     time.sleep(5)
>     print(f'子进程结束~~~~，进程号:{os.getpid()}')
> 
> if __name__ == '__main__':
>     print(f'父进程启动，进程号:{os.getpid()}')
> 
>     # 创建子进程
>     p = Process(target=task)
>     p.start()
> 
>     '''
>     默认情况下，根据系统的调度，主进程可能会早于子进程结束
>     但是将子进程进行合并【join】之后，主进程等待子进程执行完毕之后才结束，子进程相当于做了插队操作
>     '''
>     # join一定要在start之后，否则报错：AssertionError: can only join a started process
>     p.join()
> 
>     print('main~~~~~')
>     time.sleep(1)
> 
>     print(f'父进程结束~~~~~，进程号:{os.getpid()}')
> '''
> join之前
> 父进程启动，进程号:7792
> main~~~~~
> 子进程启动，进程号:13904
> 3536523
> 父进程结束~~~~~，进程号:7792
> 子进程结束~~~~，进程号:13904
> 
> join之后
> 父进程启动，进程号:3772
> 子进程启动，进程号:12468
> 3536523
> 子进程结束~~~~，进程号:12468
> main~~~~~
> 父进程结束~~~~~，进程号:3772
> '''
> ```

##### 2.3多个进程中的全局变量

> ```Python
> from multiprocessing import  Process
> import  os,time
> 
> # 需求：在子进程中修改全局变量，查看父进程中访问到的全局变量的值
> num  = 100
> 
> def task():
>     print('子进程启动~~~~')
>     global num
>     num += 50
>     time.sleep(2)
>     print('子进程结束~~~~~')
>     print(f'子进程，全局变量num={num}~~~~~')  # 150
> 
> if __name__ == '__main__':
>     print('父进程启动')
> 
>     p = Process(target=task)
>     p.start()
> 
>     # 合并进程
>     p.join()
> 
>     print('主进程的任务执行了****')
> 
>     print('父进程结束')
>     print(f'父进程，全局变量num={num}')   # 100
> 
>     '''
>     总结：
>         验证了进程之间是独立的，相互之间资源不共享
>         
>         工作原理：在创建子进程对象的时候，会将所有的全局变量数据进行备份
>                 每个进程都有自己的代码段，数据段和堆栈段，所以进程之间是独立的，资源不共享
>     '''
> ```

### 三、线程

> 多任务可以由多进程完成，也可以由一个进程内的多线程完成
>
> 在一个进程的内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”叫做线程
>
> 线程通常叫做轻型的进程。线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程中的资源
>
> 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，也不能决定执行多长时间
>
> 而且线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程
>
> 模块
>
> ```
> 1、_thread模块：提供了低级别的、原始的线程【低级并不是不好，只是功能比较有限,底层采用的是c语言封装的】
>
> 2、threading模块：高级模块，对_thre
> ad进行了封装，并提供了_thread中没有的功能
>
> 绝大多数情况下，我们只需要使用threading这个高级模块
> ```

#### 1.创建线程

> 创建并启动一个线程就是把一个函数传入并创建`Thread`实例，然后调用`start()`开始执行
>
> ```Python
> # 1.导入模块
> from  threading import *
> import  os,time
> 
> def task1():
>     print(f'子线程启动~~~~~~：{current_thread().name}')
>     time.sleep(5)
>     print(f'子线程结束~~~~~~：{current_thread().name}')
> 
> def task2(a,b):
>     print(f'子线程启动~~~~~~：{current_thread().name}')
>     print(a,b)
>     time.sleep(5)
>     print(f'子线程结束~~~~~~：{current_thread().name}')
> 
> if __name__ == '__main__':
>     # 2.任何一个程序启动之后，会启动一个进程，该进程被称为父进程，同时，该进程会默认启动一个线程，该线程被称为主线程
>     # current_thread().name获取的是当前正在执行的线程的名称，主线程的默认名称为MainThread
>     print(f'主进程{os.getpid()}中的主线程启动:{current_thread().name}')
> 
>     # 3.创建子线程
>     '''
>     Thread(target,args,name)
>         target:当前线程需要执行的任务的函数名
>         args:表示任务函数的参数。值一定是一个元组
>         name:给线程命名
>     '''
>     # 注意：子线程默认的名称为Thread-1,Thread-2.....
>     # a.任务函数无参
>     # t = Thread(target=task1)
>     # t.start()
> 
>     # t = Thread(target=task1,name='hello')
>     # t.start()
> 
>     # b.任务函数有参
>     t = Thread(target=task2,args=(34,19),name='abc')
>     t.start()
> 
>     # 和进程的用法类似，也可以合并线程，则该线程优先执行
>     t.join()
> 
>     time.sleep(1)
> 
>     print(f'主进程{os.getpid()}中的主线程结束:{current_thread().name}')
> 
> ```

#### 2.线程中的全局变量

> ```Python
> from threading import  Thread
> 
> num = 0
> 
> def change(n):
>     global  num
>     num += n
>     num -= n      # 0
> 
> def task(m):
>     for _ in range(10000000):
>         # 共享资源
>         change(m)
> 
> if __name__ == '__main__':
>     print('主线程启动~~~~')
>     t1 = Thread(target=task,args=(5,))
>     t2 = Thread(target=task, args=(8,))
>     t1.start()
>     t2.start()
> 
>     t1.join()
>     t2.join()
> 
>     print('主线程结束~~~~~')
>     print(f'全局变量num={num}')
> 
>     '''
>     原因：多个线程之间资源是共享的，所以当多个线程同时访问一个全局变量的时候，会导致全局变量的结果和理论不一致
>     
>     分析：
>         num += n-----》第一步：x = num + n   第二步：num = x
>         
>         t1:x1 = num + n       x1 = 5
>         
>         t2:x2 = num + n       x2 = 8
>         t2:num = x2          num = 8
>         
>         t1:num = x1         num = 5
>         t1:x1 = num - n     x1 = 0
>         t1:num = x1         num = 0
>         
>         t2:x2 = num - n    x2 = -8
>         t2:num = x2         num = -8
>         
>     解决：
>         只需要保证一个线程抢到时间片之后，能够将所有的代码执行完毕，其他线程处于等待状态
>     实现：
>         给共享资源加锁，哪个线程抢到时间片，则该线程持有锁，当共享资源对应的代码执行完毕，则释放锁
>     '''
> ```

#### 3.线程锁

> ```Python
> from threading import  *
> 
> # 创建一个锁对象
> lock = Lock()
> 
> num = 0
> 
> def change(n):
>     global  num
>     num += n
>     num -= n      # 0
> 
> def task(m):
>     for _ in range(10000000):
>         # 获取锁
>         lock.acquire()
>         try:
>             # 共享资源
>             change(m)
>         finally:
>             # 释放锁
>             lock.release()
> 
> if __name__ == '__main__':
>     print('主线程启动~~~~')
>     t1 = Thread(target=task,args=(5,))
>     t2 = Thread(target=task, args=(8,))
>     t1.start()
>     t2.start()
> 
>     t1.join()
>     t2.join()
> 
>     print('主线程结束~~~~~')
>     print(f'全局变量num={num}')
> ```
>
> ```Python
> from threading import  *
> 
> # 创建一个锁对象
> lock = Lock()
> 
> num = 0
> 
> def change(n):
>     global  num
>     num += n
>     num -= n      # 0
> 
> def task(m):
>     for _ in range(10000000):
>         # 进入with代码块，则表示获取锁，当with代码块执行完毕，会自动释放锁
>         with lock:
>             # 共享资源
>             change(m)
> 
> if __name__ == '__main__':
>     print('主线程启动~~~~')
>     t1 = Thread(target=task,args=(5,))
>     t2 = Thread(target=task, args=(8,))
>     t1.start()
>     t2.start()
> 
>     t1.join()
>     t2.join()
> 
>     print('主线程结束~~~~~')
>     print(f'全局变量num={num}')
> ```

