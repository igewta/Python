# -*- coding:utf-8 -*-

"""
文件说明：
生产者消费者问题：
- 一个模型，可以用来搭建消息队列
- queue 是一个用来你存放变量的数据结构，特点是先进先出,内部元素排队，可以理解为一个特殊的list

死锁问题：
- 锁的等待问题：timeout
- senphort :运行一个资源最多同时由几个线程使用

threading.Timer,几秒后启动函数

可重入锁
- 一个锁，可以被一个线程多次申请
- 主要解决递归调用的时候，需要申请锁的情况

"""
'''
# 生产者，消费者模型
import threading
import time
import queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # queue.qsize 返回queue 的内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    # put  往queue 中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            # queue.qsize 返回queue 的内容长度
            if queue.qsize() > 100:
                for i in range(3):
                    #get 是从queue 中取出一个值
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))

    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
'''
'''
# 死锁问题
import  threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print('fun_1 starting ......')
    lock_1.acquire()
    print('fun_1申请了 lock_1.....')
    time.sleep(2)
    print('func_1 等待 lock_2.....')
    lock_2.acquire()
    print('func_1 申请了 lock_2.....')

    lock_2.release()
    print('func_1 释放了lock_2.....')

    lock_1.release()
    print('func_1 释放了 lock_1')

    print('func_1 done.....')

def func_2():
    print('fun_2 starting ......')
    lock_2.acquire()
    print('fun_2申请了 lock_2.....')
    time.sleep(4)
    print('func_2 等待 lock_1.....')
    lock_1.acquire()
    print('func_2 申请了 lock_1.....')

    lock_1.release()
    print('func_2 释放了lock_1.....')

    lock_2.release()
    print('func_2释放了 lock_2')

    print('func_2 done.....')


if __name__ == '__main__':
    print('主程序启动。。。。。。')
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('主程序结束。。。。')
    
# 死锁问题,设置超时机制
import  threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print('fun_1 starting ......')
    lock_1.acquire(timeout=4)
    print('fun_1申请了 lock_1.....')
    time.sleep(2)
    print('func_1 等待 lock_2.....')
    rst = lock_2.acquire(timeout=2)
    if rst:
        print('func_1 已经申请到了锁2')
    else:
        print('func_1 没有申请到锁2')
    print('func_1 申请了 lock_2.....')

    lock_2.release()
    print('func_1 释放了lock_2.....')

    lock_1.release()
    print('func_1 释放了 lock_1')

    print('func_1 done.....')

def func_2():
    print('fun_2 starting ......')
    lock_2.acquire(timeout=4)
    print('fun_2申请了 lock_2.....')
    time.sleep(4)
    print('func_2 等待 lock_1.....')
    rst = lock_1.acquire(timeout=2)
    if rst:
        print('func_2 已经申请到了锁1')
    else:
        print('func_2 没有申请到锁1')
    print('func_2 申请了 lock_1.....')

    lock_1.release()
    print('func_2 释放了lock_1.....')

    lock_2.release()
    print('func_2释放了 lock_2')

    print('func_2 done.....')


if __name__ == '__main__':
    print('主程序启动。。。。。。')
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('主程序结束。。。。')
    


# semphore
import  threading
import time
# 参数定义最多几个县城同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + 'get semaphore')
        time.sleep(15)
        semaphore.release()
        print(threading.currentThread().getName() + 'release samaphore')

for i in range(8):
    t1 = threading.Thread(target=func, args=())
    t1.start()
'''
'''
import threading
import time

def func():
    print('I am runing ......')
    time.sleep(3)
    print('I am done .....')

if __name__ == '__main__':
    t = threading.Timer(6,func)
    t.start()
    i=0
    while True:
        print(f'{i}**************')
        time.sleep(3)
        i += 1

'''
import time
import threading


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num = num +1
            msg = self.name + 'set num to ' + str(num)
            print(msg)
            mutex.acquire()
            mutex.acquire()
            mutex.acquire()

num = 0
mutex = threading.RLock()

def testTh():
    for i in range(5):
        t = MyThread()
        t.start()