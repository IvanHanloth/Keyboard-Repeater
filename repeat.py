import keyboard as kb
from time import sleep
lock=0
num=0
version="V1.0.1"
def a():
    global lock
    if lock==0:
        kb.hook(c)
        lock=1
        print("按键重复已启动")
    else:
        print("按键重复已在运行")
def b():
    global lock
    if lock==1:
        kb.unhook(c)
        lock=0
        print("按键重复已暂停")
    else:
        print("按键重复未在运行")
def c(x):
    if x.event_type=="up":
        for i in range(0,num):
            kb.press_and_release(x.name)
def d(x=-1):
    global num
    global lock
    kb.remove_all_hotkeys()
    if lock==1:
        kb.unhook(c)
        lock=0
    while x<0:
        x = input("请输入单次按键重复次数：")
        if x.isdigit():
            x = int(x)
            break
        else:
            x=-1
            print("请输入大于0的数字")
    s()
    num=x
    a()
    print("设置成功，单次按键将重复{}次".format(num))
def e():
    d(0)
def f():
    d(1)
def g():
    d(2)
def h():
    d(3)
def i():
    d(4)
def j():
    d(5)
def k():
    d(6)
def l():
    d(7)
def m():
    d(8)
def n():
    d(9)
def o():
    print('''按键重复器 {}
    作者：Ivan Hanloth
    博客：https://ivan.hanloth.cn/
    邮箱：ivan@hanloth.com
    开源协议：MIT License
    开源地址：https://github.com/IvanHanloth/Keyboard-Repeater/
    https://gitee.com/IvanHanloth/Keyboard-Repeater/
    ©2023 Ivan Hanloth All Rights Reserved
    '''.format(version))
def p():
    print('''MIT License

Copyright (c) 2023 Ivan Hanloth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
    ''')
def q():
    print('''快捷键列表：
    Ctrl+Alt+B 启用按键重复
    Ctrl+Alt+S 停用按键重复
    Ctrl+Alt+C 修改按键重复次数
    Ctrl+Alt+E+0~9 快速修改按键重复次数
    Ctrl+Alt+H 查看帮助
    Ctrl+Alt+I 查看版本信息
    Ctrl+Alt+L 查看开源协议
    Ctrl+Esc
    ''')
def r(x,y):
    kb.add_hotkey(x,y)
def s():
    r("ctrl+alt+b",a)
    r("ctrl+alt+s",b)
    r("ctrl+alt+c",d)
    r("ctrl+alt+h",q)
    r("ctrl+alt+i",o)
    r("ctrl+alt+l",p)
    r("ctrl+alt+e+0",e)
    r("ctrl+alt+e+1",f)
    r("ctrl+alt+e+2",g)
    r("ctrl+alt+e+3",h)
    r("ctrl+alt+e+4",i)
    r("ctrl+alt+e+5",j)
    r("ctrl+alt+e+6",k)
    r("ctrl+alt+e+7",l)
    r("ctrl+alt+e+8",m)
    r("ctrl+alt+e+9",n)
def t():
    pass
def u():
    pass
def v():
    pass
def w():
    pass
def x():
    pass
def y():
    try:
        z()
    except:
        print("程序出现异常")
        if input("输入r重启，输入其他值关闭程序")=="r":
            y()
        else:
            exit()
def z():
    s()
    print('''按键重复器 {}
    按Ctrl+Alt+H查看帮助
    '''.format(version))
    d()
    kb.wait()
y()