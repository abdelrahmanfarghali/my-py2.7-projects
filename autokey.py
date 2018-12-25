from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
keys = Controller()
from pynput.mouse import Button, Controller

def onclick(x, y, button, pressed):
    if pressed:
        keys.press('1')
        keys.press('3')
        Controller().press(Button.left)
def onscroll(x, y, dx, dy):
    pass
def onmove(x,y):
    pass
with mouse.Listener(on_move=onmove,on_click=onclick,on_scroll=onscroll) as listener:
    listener.join()
def onpressed(key):
    pass
def onreleased(key):
    pass
with keys.Listener(on_press=onpressed, on_release=onreleased) as listener:
    listener.join()
