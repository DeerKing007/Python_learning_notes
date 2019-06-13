# 进程和线程

~~~
1. 安全性
2. 高并发
~~~

~~~markdown
任务调度
1. 大部分操作系统的任务调度是采用时间片轮转的抢占式调用
		时间片：某一小段时间---操作系统 
				任务执行的一小段时间
				是由操作系统进行分配的（每次的时间片不一定相等）
		程序执行的状态：运行状态
		程序不执行的状态：
				1. 结束：终止状态
				2. 不结束：阻塞状态（input()）
2. 任务执行一段时间后，强制暂停，执行下一个任务
3. cpu的计算速度很快，上下文切换较快，时间片很短，人无法感知，人误以为是同时执行的多个任务
4. 宏观并行，微观串行
		从宏观角度：人认为是同时执行多个任务
		从微观角度：任何时刻只有一个任务在执行（仅限于单核）
5. 在多核模式下可以达到真正的并行
~~~

* 进程和线程的区别

~~~markdown
进程：
	计算机的核心：cpu ---计算
	计算机的管理者：操作系统---负责任务调度，资源分配，资源的管理，统计整个计算机硬件
	所有的程序运行在操作系统中的
1. 进程是一个具有一定独立功能的程序，是在一个数据集合上的一次动态执行过程，是操作系统进行资源分配的一个独立单位，是应用程序运行的载体
2. 进程是一种抽象的概念，从来没有一个标准定义，进程的结构：
		1. 程序：用于描述进程要完成的功能，是控制进程的指令集
		2. 数据集合：是程序在执行时所需要的数据和工作区
		3. 程序控制块：包含进程的描述信息和控制信息，是进程存在的唯一标志
3. 进程的特点：
		1. 动态性
		2. 并发性
		3. 独立性
		4. 结构性
4. 进程和进程之间资源相互独立，互不干扰
		
线程：
是轻量级的进程（进程中包含线程）
1. 进程太重，上下文切换消耗太大，出现了线程的概念，线程的调度方式同进程
		时间片轮转抢占式调度
		线程资源分配的最小单位
		线程和线程之间资源共享（共享进程的资源）
2. 线程的结构：
		1. 线程ID
		2. 指令指针
		3. 寄存器
		4. 堆栈
3. 线程的上下文切换，远快于进程上下文的切换
4. 一个进程是由多个线程组成，线程是一个进程中代码的不同执行路线


单线程和多线程
1. 单线程：在一个进程中，只有一个线程，程序的所有资源只提供给一个线程使用
2. 多线程：在一个进程中有多个线程，多个线程之间会并发执行（宏观并行，微观串行），相互抢占进程的资源
~~~

---

### 多线程模块：threading

~~~markdown
Python： CPython
GIL：全局解释锁：保证每次只有一个线程可以执行
GIL导致CPython中的多核模式下的多线程几乎等同于单线程，单核几乎不影响
只有CPython有GIL
~~~

![多线程](https://github.com/DeerKing007/Python_learning_notes/blob/master/Python_learning_notes/picture/多线程.png)

一般情况：多个线程争抢进程中的资源

CPython中：多个线程争抢GIL资源

~~~markdown
threading模块：是python并发库的模块
Python2： thead  threading
python3： threading
~~~

* threading

~~~markdown
创建线程的两种方式：
1. 继承Thread类，并覆盖run方法
2. 直接使用Thread的构造方法
		Thread.__init__(self, group=None, target=None, name=None,args=(), kwargs=None, daemon=None)
			self:当前对象
			group:预留参数
			target:目标（要做的事--函数对象）
			name:设置线程的名字
			args:必须是元组，是target的参数
			kwargs:必须是字典，是target的参数
			daemon：设置守护线程
3. 任何程序都至少有一个线程：主线程
注意：Thread类是threading模块中的一个类
		threading.Thread 
~~~

~~~python
# 单线程
def music(name,count):
    for i in range(count):
        print('list to music%s  %d times'%(name,i+1))

def movie(name,count):
    for i in range(count):
        print('list to movie %s %d times'%(name,i+1))


if __name__=='__main__':
    music('凉凉',3)
    movie('我不是药神',3)
    
# 多线程
class Music(threading.Thread):  # 继承Thread类
    def __init__(self,name,count):
        super().__init__()
        self.name=name
        self.count=count

    def run(self):  # 覆盖run方法
        for i in range(self.count):
            print('list to music%s  %d times' % (self.name, i + 1))
            time.sleep(0.5)

#####################################################
def movieFunc(name,count):
    for i in range(count):
        print('list to movie %s %d times'%(name,i+1))
        time.sleep(0.5)


if __name__ == '__main__':
    music=Music('凉凉',3) #创建线程对象
    movie=threading.Thread(target=movieFunc,args=('我不是药神',3))  # target：目标，要执行的内容
    music.start()  #启动线程
    movie.start()
~~~

---

* Thread类中的其他方法

~~~markdown
1. getName()/name:
		获得线程的名字
		默认是Thread-N
2. setName(newName)/直接在构造方法中修改:
		设置线程名称
3. ident:
		线程的id
		线程id只有在start之后才会被分配
4. is_alive()/isAlive:
		判断线程是否存活（激活状态）
5. join([timeout]):
		timeout:设置超时时间
		会阻塞调用该方法的线程（当前线程），执行被调用的线程，直到被调用的线程执行完毕或到达超时时长时，才继续执行当前线程
		如果timeout不设置：不限制超时时间
6. setDaemon（bool）：
		设置该线程为守护线程（精灵线程）
		主线程中的子线程如果设置为守护线程，当主线程结束时，会杀死所有守护线程（不论守护线程是否结束）
		典型的守护线程：GC—-垃圾回收机制
		
		
主线程和子线程
主线程：不通过Thread创建的线程
子线程：通过Thread创建的线程
~~~

~~~python
import threading,time

def music(name,n):
    for i in range(n):
        print('listen to the music %s  %s times'%(name,i+1))
        time.sleep(0.5)

def movie(name,n):
    for i in range(n):
        print('watch the movie %s  %s times'%(name,i+1))
        time.sleep(1)

if __name__ == '__main__':
    t1=threading.Thread(target=music,args=('凉凉',3),daemon=False)
    t2=threading.Thread(target=movie,kwargs={'name':'我不是药神','n':3},name='hehe3')
    t1.setDaemon(True)
    t2.setDaemon(True)
    # t1.setName('hehe')
    # t1.name='hehe2'
    # print(t1.getName(),t2.getName())
    # print(t1.name,t2.name)

    # print(t1.is_alive())
    t1.start()

    t2.start()
    # print(t1.ident, t2.ident)
    # time.sleep(4)
    # print(t1.is_alive())
    # print(t1.isAlive)
    # t1.join()
    # t2.join()
    # print('end')
    print('end')
~~~

* 线程的状态

~~~markdown
Python 有5个状态
~~~



![线程状态](https://github.com/DeerKing007/Python_learning_notes/blob/master/Python_learning_notes/picture/线程状态.png)

### GIL锁

~~~markdown
GIL：Global Interpreter Lock
1. GIL并不是Python的特性，Python完全可以不用GIL
		CPython使用GIL
		Jython，PyPy，IronPython
2. 对于多核，GIL锁将多核性质几乎限制为单核性质
3. 多进程和多线程使用的时机：
		1. CPU密集型程序宜用多进程
		2. I/O密集型程序宜用多线程
4. CPython中GIL锁的弊端：
		1. GIL锁管理的线程之间，挣钱的不是时间片，而是锁标记
		2. 在单核模式下，和没有GIL锁的程序没有太大区别
		3. GIL锁标记的从释放到再获取的时间间隔极短，导致在多核模式下，其他核被激活但无法获得锁标记，导致CPU使用效率大打折扣
5. GIL优化：
		1. GIL短时间内不可能取消
		2. 延长GIL所标记从释放到再获取的时间（最后手段）
		3. 增加其他线程的权重
		4. 控制每个线程执行数据集合的总量（字节）
~~~

---

### 线程同步

~~~markdown
同步：数据安全
原子操作：从业务角度，是不可分割的的操作
		一个流程中，不可被分割的整体
临界资源：任何线程都可以访问的资源

同步：保证原子操作不被破坏的操作
		原子操作如果被破坏则会导致数据读取不一致（脏读）
		方案：加锁
加锁：同步锁，线程锁，互斥锁，排他锁
		效率降低，换来数据的安全
~~~

~~~python
import time,threading

class MyList(list):
    def __init__(self):
        self.l=['A','B','','','','','']
        self.index=2

    def add(self,value):
        self.l[self.index]=value
        time.sleep(0.0001)
        self.index+=1

    def getList(self):
        return self.l

m=MyList()
def fun(char):
    m.add(char)

if __name__ == '__main__':
    t1=threading.Thread(target=fun,args=('C',))
    t2=threading.Thread(target=fun,args=('D',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(m.getList())
~~~

~~~python
# 加锁
import time,threading
lock=threading.Lock()  # 创建锁对象

class MyList(list):
    def __init__(self):
        self.l=['A','B','','','','','']
        self.index=2

    def add(self,value):
        lock.acquire()  # 获取所标记
        self.l[self.index]=value
        time.sleep(3)
        self.index+=1
        lock.release() # 释放所标记

    def getList(self):
        return self.l

m=MyList()
def fun(char):
    m.add(char)

if __name__ == '__main__':
    t1=threading.Thread(target=fun,args=('C',))
    t2=threading.Thread(target=fun,args=('D',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(m.getList())
~~~

* 死锁问题

~~~markdown
如果一个原子操作，被重复加锁，会导致死锁问题
解决方案：
RLock类：可重入锁
		可以重复的对资源进行加锁和释放
~~~

* 补充ThreadLocal

~~~markdown
1. 全局变量不安全，可以使用局部变量
2. 局部变量占用空间，使用麻烦，作用域小
3. 全局变量，为了安全，可以加锁，加锁又会导致效率低

4. 刚需：既有全局的使用便利性，又有局部的安全性，且效率高的一种变量
		ThreadLocal：线程绑定对象
注意：
ThreadLocal对象是并发库中的高级对象
		同时拥有全局变量和局部变量的性质
~~~

~~~python
import threading,time

l=threading.local()

def fun1():
    l.a=20
    time.sleep(1)
    print(l.a)


def fun2():
    l.a=30
    print(l.a)

if __name__ == '__main__':
    t1=threading.Thread(target=fun1)
    t2=threading.Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
~~~

---

### 多进程模块multiprocessing

~~~markdown
1. 用于创建进程，替换了threading模块（将threading中的方法名移植过来）
2. CPython下多线程是由GIL管理，导致多核模式下效率降低，GIL在进程之中的（不同的进程拥有不同的GIL），进程就不会受到GIL的影响，多核模式下CPU密集型程序可以使用多进程
~~~

* multiprocessing

~~~Markdown
1. 主要用于多进程管理
2. 该模块中的方法和多线程管理模块类似
3. 包含Lock等类似于线程中的类
4. 包含特殊类：Pipe，Queue进程通信相关的类（IPC）
~~~

* Process

~~~Markdown
Process:进程类
1. Process.__init__(self, group=None, target=None, name=None, args=(), kwargs={}, daemon=None)
		self:指代当前进程对象
		group:预留参数
		target：目标
		name:进程名称
		args:目标的参数（必须是元组）
		kwargs:目标的参数（必须是字典）
		daemon：是否是守护进程
2. terminate（）
		结束当前进程
~~~

~~~python
import multiprocessing,time

def music(name,n):
    for i in range(n):
        print('listen to the music %s %s times'%(name,i+1))
        time.sleep(0.5)


def movie(name,n):
    for i in range(n):
        print('watch movie  %s %s times'%(name,i+1))
        time.sleep(0.5)

if __name__ == '__main__':
    p1=multiprocessing.Process(target=music,args=('凉凉',3))
    p2=multiprocessing.Process(target=movie,args=('我不是药神',3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('end')
~~~

* 多进程模块的其他类：

~~~Markdown
1. Lock:同步锁
2. Pool:进程池
3. Queue：多进程安全队列
4. Pipe：管道
~~~

* Lock

~~~markdown
同步和异步：
		1. 同步：原子操作不被破坏，多个进程同一时间只能有一个进程可以访问临界资源（或原子操作）
		2. 异步：多个进程同一只时间可以同时访问临界资源（或原子操作）
~~~

~~~python
进程之间相互独立，互不干扰
# 进程同步
import multiprocessing as m,time
lock=m.Lock()

class MyList(list):
    def __init__(self):
        self.l=['A','B','','','']
        self.index=2

    def add(self,value):
        lock.acquire()
        self.l[self.index]=value
        time.sleep(0.001)
        self.index+=1
        lock.release()

    def getList(self):
        return self.l

mylist=MyList()

def func(char):
    mylist.add(char)

if __name__ == '__main__':
    p1=m.Process(target=func,args=('C',))
    p2=m.Process(target=func,args=('D',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(mylist.getList()) # 进程间各自独立，所以子进程修改全局变量不会影响当前主进程
~~~

---

* Pool

~~~Markdown
Pool：进程池
1. 进程池可以提供指定数量的进程，用于调用
		1. 当有新的进程请求提交到Pool中是，如果池没满，就会创建一个新的进程
		2. 如果满了，则新的进程的请求就会等待
		3. 如果Pool结束，则不会创建任何进程，也不会处理任何请求
2. 进程池的方法：
		1. apply（func,[args,[kwargs]]):
				阻塞执行，进程池中的进程，每次只能执行一个
				Python3弃用该方法
		2. apply_async（func,[args,[kwargs，[callback]]]）
				非阻塞执行，进程池中的进程，异步执行
		3. close():
				关闭pool，不再接收新的任务，池中的任务继续执行
		4. terminate（）：
				结束工作进程，不再处理未完成的进程任务
		5. join()：
				阻塞当前进程，等待子进程的退出（join必须在close或terminate之后使用）
3. 进程池批量创建进程
~~~

~~~python
import multiprocessing as m,time

def work(n):
    print('Hello world: %s'%n)
    time.sleep(1)

if __name__ == '__main__':
    pool=m.Pool(3) # 设置进程池的容量
    for i in range(10):
        pool.apply_async(func=work,args=(i,))

    pool.close()
    pool.join()  # 必须调用：如果主进程执行完毕，进程池还没执行完，主进程结束，控制台不再接收打印任务
~~~

---

* Queue

~~~Markdown
1. Queue：队列
		进程安全队列
2. 进程之间是相互独立的，互不干扰
		1. 让进程之间可以进行通信的一种数据结构
3. 队列的创建
		Queue([maxsize]) 
			maxsize:设置队列的容量，不设置表示无限大（不限制大小）
4. 队列对象的方法：
		1. put(value): 
				向队列中传入值
				blocked参数：bool类型 
				timeout参数：超时时长
				如果blocked为True，并且timeout为正值，如果队列已满，到达超时时间则抛出异常：Queue.Full异常；如果为blocked为False如果队列已满，直接抛出异常
				
		2. get()：从队列中读取，并删除一个元素
				blocked参数：bool类型 
				timeout参数：超时时长
				如果blocked为True，并且timeout为正值，如果队列已空，到达超时时间则抛出异常：Queue.Full异常；如果为blocked为False如果队列已空，直接抛出异常
				
		3. get_nowait():get(False)
		4. put_nowait():put(False)
		5. empty():
				判断队列是否为空，该方法不可靠
		6. full（）：
				判断队列是否满了，该方法不可靠
		7. qsize():
				返回队列中的元素个数，该方法不可靠
~~~

~~~python
import multiprocessing as m ,time

def putValues(q): # 向一个队列中插入数据 q:队列对象
    for i in ['A','B','C']:  # i:A  B  C
        print('发送%s到queue'%i)
        q.put(i)
        time.sleep(1)

def getValues(q):
    while True:
        value=q.get()
        print('从queue中获取到数据%s'%value)

if __name__ == '__main__':
    queue=m.Queue() # 创建队列对象
    process1=m.Process(target=putValues,args=(queue,)) # 向队列中放入数据
    process2=m.Process(target=getValues,args=(queue,)) # 从队列取出数据

    process1.start()
    process2.start()

    process1.join()
    process2.terminate()
    print('end')
~~~

* Pipe

~~~markdown
Pipe：管道
1. 用于进程之间的通信
		Pipe的底层实现是队列
2. Pipe(duplex):
		duplex:双向的，通过的，设置管道对象的运行模式
		返回一个元组，(conn1,conn2)代表了管道的两端
		duplex：True:全双工模式（conn1和conn2都可以接收也可以发送）
				Flase:半双工模式（conn1只负责接收，conn2只负责发送）
3. send(mesg): 管道两端的方法
		mesg：消息（对象，元素）
		发送消息
4. recv(): 管道两端的方法
		接收消息
		接收消息提前做好准备：消息接收会让处于阻塞状态，用于等待消息的到来
		如果管道关闭，调用recv方法，抛出EOFError（异常终止）
~~~

~~~python
import multiprocessing as m,time

def putValues(p): # p此时为管道对象
    for i in ['A','B','C']:
        print('发送%s到pipe' % i)
        p[1].send(i)
        time.sleep(1)

def getValues(p):
    while 1:
        value=p[0].recv()
        print('从pipe中获取到数据%s'%value)

if __name__ == '__main__':
    # 创建管道对象
    pipe=m.Pipe(duplex=False)
    process_in=m.Process(target=putValues,args=(pipe,))
    process_out=m.Process(target=getValues,args=(pipe,))
    process_in.start()
    process_out.start()
    process_in.join()
    process_out.terminate()
    print('end')

~~~

---

* 生产者消费者模型

~~~Markdown
对于一块内存空间，有任务向该空间存储数据，同时也会有任务从该空间获取数据---生产者消费者模型（业务模型）
举例：
队列：
1. 跨进程通信队列
		multiprocessing.Queue
		用于进程通信
2. 队列模块
		queue.Queue
		不属于线程
~~~

~~~python
import threading,time,queue

queue=queue.Queue()

def producer(name):# 生产者
    count=1
    while 1:
        queue.put('第%s根香烟'%count)
        print('%s 生产了第%s根香烟'%(name,count))
        count+=1
        time.sleep(1)

def consumer(name): # 消费者
    while 1:
        print('%s 拿到了 %s'%(name,queue.get()))
        time.sleep(2)

if __name__ == '__main__':
    l=[]
    l.append(threading.Thread(target=producer,args=('老王',)))
    l.append(threading.Thread(target=consumer,args=('张三',)))
    l.append(threading.Thread(target=consumer,args=('李四',)))

    for i in l:
        i.start()
~~~

---

