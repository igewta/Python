# -*- coding:utf-8 -*-

"""
文件说明：
用来学习logging模块
"""
import logging
'''
四大组件：
- 日志器：Logger：产生日志的一个接口
- 处理器：Handler：把产生的日志发送到那些相应的目的地
- 过滤器：Filter:更精细的控制那些日志输出
- 格式器：Formatter:对输出的内容进行格式化

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.critical("this is critical message")
logging.log("debug","this is test debug message")
logging.basicConfig("")
print("071101")

format 语句中的内容：
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名，python如：login.py
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号,在第几行打印的日志
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息


- Logger:
    - Logger.setLevel()
    - Logger.addHandler()
    - Logger.addFilter()
    - Logger.debug
- 实例化：logging.getLogger()

系统默认的日志级别是warning ,所以必须要设置下，否则下列中的debug 和info 信息是不嫌的。
'''
#设置日志输入格式
log_format = "%(asctime)s====%(levelname)s++++++%(message)s  pid=%(process)s"
# 设置日志默认格式
logging.basicConfig(level=logging.DEBUG, filename="testlog.txt", format=log_format)

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.critical("this is critical message")
# logging.log(logging.DEBUG, "this is test debug message")


