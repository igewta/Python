# -*- coding:utf-8 -*-

"""
文件说明：
固定步骤：
1. 创建总面板： base = tkinter.Tk()
2. 创建面板上的各种组件
    1. 指定组件的父组件，即依附关系
    2.利用相应的属性对组件进行设置
    3. 给组件安排布局
3. 同步骤2相似，创建多个组件
4. 最后启动总面板的消息循环 ： base.mainloop()

"""
import tkinter

# tkinter._test()
base = tkinter.Tk()

# 消息循环
# base.mainloop()

# 负责标题
base.wm_title('Label Test')
lb = tkinter.Label(base, text='Python Label')
# 给对应组件指定布局
lb.pack()# 布局方式
base.mainloop()


'''
- 按钮
    Button 按钮组件
    RadioButton 单选框组件
    CheckButton 复选框组件
    Listbox 列表框组件
- 文本输入组件
    Entry 单行文本框组件
    Text 多行文本框组件
- 标签组件
    Label 标签组件，可以显示图片和文字
    Message 标签组件，可以根据内容将文字换行
- 菜单
    Menu 菜单组件
    MenuButton 菜单按钮组件，可以使用Menu 代替
- 滚动条
    Scale 滑块组件
    Scrollbar 滚动条组件
- 其他组件
    Canvas 画布组件
    Frame 框架组件，将多个组件编组
    Toplevel 创建子窗口容器组件  
'''