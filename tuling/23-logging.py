# -*- coding:utf-8 -*-

"""
文件说明：

"""
'''
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="test.log")
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.critical("this is critical")

'''
'''
##装饰器
- 使用装饰器，打印函数执行时间
'''
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

def log(func):
    def wrapper(*arg, **kw):
        logging.info("this is info message")
        return func(*arg, **kw)
    return wrapper

@log("TEST DONME")
def test():
    print("test demo")

if __name__ == '__main__':
    test()