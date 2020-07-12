# -*- coding:utf-8 -*-

"""
文件说明：
生产者消费者问题：
- 一个模型，可以用来搭建消息队列
- queue 是一个用来你存放变量的数据结构，特点是先进先出,内部元素排队，可以理解为一个特殊的list

死锁问题：

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
