# -*- coding:utf-8 -*-

"""
文件说明：
- 共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题
解决方法：锁，信号灯
- 锁（Lock）
 - 是一个标志，表示一个线程在占用一些资源
 - 使用方法：
  - 上锁
  - 使用共享资源，放心的用
  - 取消锁，释放锁
- 锁谁：哪个资源需要多个线程共享，锁哪个
- 理解锁：锁其实并不是锁住谁，而是一个令牌

- 线程安全问题
 - 如果一个资源/变量，他对于多线程莱多，不用加锁也不会引起任何问题，则成为线程安全
 - 线程不安全变量类型： list ,set, dict
 - 线程安全类型：queue

 - 生产者消费者问题
  - 一个模型
"""
'''
import threading

sum = 0
loopsum = 100

def myadd():
    global sum, loopsum
    for i in range(1, loopsum):
        sum = sum +1

def myminu():
    global sum, loopsum
    for i in range(1, loopsum):
        sum -= 1


if __name__ == '__main__':
    print('start :',sum)
    #
    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myminu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('sum:', sum, 'loopsum:', loopsum)
'''

# 锁的用法
import threading

sum = 0
loopsum = 10000

lock = threading.Lock()

def myAdd():
    global sum, loopsum
    for i in range(1, loopsum):
        # 上锁，申请锁
        # lock.acquire()
        sum +=1
        # 释放锁
        # lock.release()

def mymium():
    global sum, loopsum
    for i in range(1, loopsum):
        #上锁，申请锁
        # lock.acquire()

        sum -= 1
        # 释放锁
        # lock.release()


if __name__ == '__main__':
    print('start:', sum)
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=mymium, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('end ,sum is :', sum)
