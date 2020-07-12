# -*- coding:utf-8 -*-

"""
文件说明：
多线程，利用time函数，生成两个函数，顺序调用，计算总的运行时间
threading Python3 使用的线程包
_thread python2 中的线程，基本已经不使用
案例01： 顺序执行，耗时较长
案例02：使用_thread,
案例03：使用_thread ,传参数
案例04： 使用threading
案例05： 使用t.join()
- 守护线程：damon
- 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
一般认为，守护线程不重要或者不允许离开主线程独立运行
守护线程案例能否有效跟环境有关
## threading 的使用
- 直接利用threading.Thread 生成Thread 实例
1.t =  threading.Thread(target=xxx, args=(xxx, ))
2.t.start(): 启动多线程
3.t.join(): 等待多线程执行完成

- 直接继承自threading.Thread
 - 必须要重写run() 函数，run 函数代表的是真正执行的功能



### 线程常用属性
- threading.currentThread: 返回当前线程变量
- threading.enumerate: 返回一个包含正在运行的线程的list,正在运行的线程启动后，结束前
- threading.activeCount: 返回正在运行的线程的数量
- t.setName(): 给线程设置名称
- t.getName(): 获取线程名称

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
    t1.join()
    t2.join()
    print('ALL DONE AT: ', time.ctime())


if __name__ == '__main__':
    main()
    # while True:# 死循环
    #     time.sleep(10)

# 主线程结束了，但子线程仍然在运行，所以子线程中的程序仍然会运行
import time
import threading

def fun():
    print('start fun')
    time.sleep(2)
    print('end fun')

print('Main thread')

t1 = threading.Thread(target=fun, args=())
t1.start()
time.sleep(1)
print('Main thread end')

# 添加守护线程，不会输出’End fun‘
import time
import threading

def fun():
    print('start fun')
    time.sleep(2)
    print('end fun')

print('Main thread')

t1 = threading.Thread(target=fun, args=())
t1.setDaemon(True)# 设置为守护线程，必须在start 前设置
# t1.daemon =TRUE
t1.start()

time.sleep(1)
print('Main thread end')
'''
# 使用线程的各个属性