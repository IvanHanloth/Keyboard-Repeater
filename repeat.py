import keyboard
print('''欢迎使用按键重复器 V1.0.0
作者:Ivan Hanloth
博客:https://ivan.hanloth.cn/''')
num=int(input("输入单次按键重复次数："))
print('''正在执行键盘按键重复,单次按键重复{}次。请勿关闭此窗口。
快捷键：
Ctrl+Alt+Shift+E  退出此程序
Ctrl+Alt+Shift+C  更改重复次数'''.format(num))
def a(x):
    global num
    if x.event_type=="up":
        for i in range(0,num):
            keyboard.send(x.name)
def b():
    global num
    num=int(input("输入单次按键重复次数："))
    keyboard.unhook(a)
    print(num)
    keyboard.hook(a)
    print('修改成功！单次按键将重复{}次'.format(num))
keyboard.hook(a)
keyboard.add_hotkey('ctrl+alt+shift+c',b)
keyboard.wait('ctrl+alt+shift+e')