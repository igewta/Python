# -*- coding:utf-8 -*-

"""
文件说明：
subporcess
- 完全跳过线程，使用进程
- 是派生进程的主要替代方案
- python 2.4 后引入

multiprocessiong
- 使用threading 接口派生，使用子进程
- 允许为多核或者多CPU 派生进程，接口跟threading 非常相似
- Python2.6

concurrent.futures
- 新的异步执行模块
- 任务级别的操作
- python3.2 后引入

# 多进程
- 进程间通讯（InterProcessCommunication,IPC）
- 进程之间无任何共享状态
- 进程的创建
"""
import multiprocessing
from time import sleep, ctime


def clock(interval):
    while True:
        print('The time is %s' % ctime())
        sleep(interval)


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))  # 报错，没有这个attribute
    p.start()
    while True:
        print('sleeping .....')
        sleep(1)