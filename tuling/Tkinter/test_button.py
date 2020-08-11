# -*- coding:utf-8 -*-

"""
文件说明：
设置Button 例子,设置一个button ,点击后显示label

"""
import tkinter

def showlabel():
    global baseFrame
    # 在函数中定义了一个label
    # label 的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text='显示Label')
    lb.pack()

baseFrame = tkinter.Tk()
baseFrame.wm_title('test button')
# 生成一个按钮
# command 参数指示：当按钮被按下的时候，执行哪个函数

btn = tkinter.Button(baseFrame, text='SHOW LABEL', command=showlabel)
btn.pack()

baseFrame.mainloop()