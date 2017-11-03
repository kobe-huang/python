#coding=utf-8
#This's a sample of operate the clipboard
 
import win32clipboard as wincb
import win32con
 
for i in range(2,2):
    print(str(i))

wincb.OpenClipboard()
wincb.EmptyClipboard()
wincb.SetClipboardData(win32con.CF_TEXT, "Hello World!")  #复制文本内容到剪贴板，系统后台会返回内存地址
print (wincb.GetClipboardData(win32con.CF_TEXT))  #'Hello World!'
wincb.CloseClipboard() 