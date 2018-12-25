#reflex test using datetime class
import turtle
import datetime
import time
#import win32api, win32con
sec = datetime.datetime.now().second
msec = datetime.datetime.now().microsecond
print sec,msec
def overrun():
    i = 1
    for e in range(0,i):
        time.sleep(1)
        if win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0):
            turtle.Turtle(forward(100))
            print sec,msec
overrun()
