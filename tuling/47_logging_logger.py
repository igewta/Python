# -*- coding:utf-8 -*-

"""
文件说明：
用loggging 的四大组件来实现日志的工鞥
- 打印出函数的执行时间，日志的等级，日志的消息
- 用装饰器
- 不同的日志，要记录不同的日志消息

一般情况下，我们在实际工作当中，我们经常把logging 封装成一个装饰器，按照自己的习惯，新建一个loggerTools 文件，
在需要保存日志的地方，把loggerTools 引入

"""
import logging

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# handler
# TimeRotalFilterHandlder 是用来按照日期去划分日志
# RotalFileHandlder 是按照日志的文件大小来划分日志
debug_handle = logging.FileHandler("1024debug.txt")
debug_handle.setLevel(logging.DEBUG)
debug_handle.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handle = logging.FileHandler("1024error.txt")
error_handle.setLevel(logging.ERROR)
error_handle.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(debug_handle)
logger.addHandler(error_handle)

def log(func):
    def wrpper(*arg, **kw):
        logger.debug("this is debugger message")
        logger.error("this is error message")
        return func(*arg, **kw)
    return wrpper

def loghiger(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            logger.debug(text)
            logger.error(text)
            return func(*arg, **kw)
        return wrapper
    return decorator

@loghiger("执行 test() 函数")
def test():
    print("test done")

@log
def mian():
    print("main done")

test()