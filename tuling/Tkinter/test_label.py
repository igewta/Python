# -*- coding:utf-8 -*-

"""
文件说明：
设置Label 的例子

"""
import tkinter

base = tkinter.Tk()
base.wm_title('Label Test')
# 支持属性很多，background ,font ,underline等
# 第一个参数，指定所属
lb1 = tkinter.Label(base, text='Python AI')
lb1.pack()

lb2 = tkinter.Label(base, text='第二个Ppython Label')
lb2.pack()

base.mainloop()
