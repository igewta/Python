# -*- coding:utf-8 -*-

"""
文件说明：
多线程，利用time函数，生成两个函数，顺序调用，计算总的运行时间
threading Python3 使用的线程包
_thread python2 中的线程，基本已经不使用
案例01： 顺序执行，耗时较长
案例02：使用_thread,
案例03：使用_thread ,传参数


## threading 的使用
- 直接利用threading.Thread 生成Thread 实例
1.t =  threading.Thread(target=xxx, args=(xxx, ))
2.t.start(): 启动多线程
3.t.join(): 等待多线程执行完成
"""
'''
import time
import _thread as thread


def loop1():
    print("start loop 1 at: ",time.ctime())
    time.sleep(4)
    print('end loop 1 at :', time.ctime())


def loop2():
    print('start loop 2 at :', time.ctime())
    time.sleep(2)
    print('end loop 2 at : ', time.ctime())


def main():
    print('start at :', time.ctime())
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print('All done at : ', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)


import time
import _thread as thread

def loop1(in1):
    print('start loop 1 at : ', time.ctime())
    print('我是参数，',in1)
    time.sleep(4)
    print('end loop 1 at : ', time.ctime())

def loop2(in1, in2):
    print('start loop 2 at :', time.ctime())
'''
import time
import threading as thread

def loop1(in1):
    print('start loop 1 at : ', time.ctime())
    print('我是参数，',in1)
    time.sleep(4)
    print('end loop 1 at : ', time.ctime())

def loop2(in1, in2):
    print('start loop 2 at :', time.ctime())
    print('我是参数，', in1, '和参数', in2)
    time.sleep(2)
    print('end loop 2 at :', time.ctime())

def main():
    print('starting at :', time.ctime())
    t1 = thread.Thread(target=loop1, args=('王老大',))
    t1.start()
    t2 = thread.Thread(target=loop2,args=('张三', '李四'))
    t2.start()
    print('ALL DONE AT: ', time.ctime())


if __name__ == '__main__':
    main()
    while True:# 死循环
        time.sleep(10)


