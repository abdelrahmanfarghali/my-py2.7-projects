from inputs import devices
from inputs import get_gamepad
import time
import threading
from pynput.mouse import Button,Controller
import sys
from win32api import GetSystemMetrics
delay = 0.300
button = Button.left
running = False
program_running = True
x,y = 0,0
mouse = Controller()
def exits():
    program_running = False
    exit()
def click(delay,button,x,y):
    mouse.position = (x,y)
    mouse.click(button)
    time.sleep(delay)
def booleanString(device,substring):
    if str(device).find(substring) > -1:
        return True
def main():
    print("Devices detected...\n")
    for device in devices:
        print(device)
        if(booleanString(device,"Mouse")):
            for device in devices:
                if(booleanString(device,"360")):
                    print(device)
                    while 1:
                        try:
                            events = get_gamepad()
                            for event in events:
                                #print(event.ev_type, event.code, event.state)
                                print(event.code,event.state)
                            if event.state > 0 and event.code.find("ABS_Y")>=0:
                                mouse.move(0,-3)
                            if event.state < 0 and event.code.find("ABS_Y")>=0:
                                mouse.move(0,3)
                            if event.state < 0 and event.code.find("ABS_X")>=0:
                                mouse.move(-3,0)
                            if event.state > 0 and event.code.find("ABS_X")>=0:
                                mouse.move(3,0)
                            if event.state > 0 and event.code.find("ABS_RY")>=0:
                                mouse.move(0,-50)
                            if event.state < 0 and event.code.find("ABS_RY")>=0:
                                mouse.move(0,50)
                            if event.state < 0 and event.code.find("ABS_RX")>=0:
                                mouse.move(-50,0)
                            if event.state > 0 and event.code.find("ABS_RX")>=0:
                                mouse.move(50,0)
                            if event.state == 1 and event.code.find("BTN_WEST")>=0:
                                exits()
                            if event.state == 1 and event.code.find("BTN_EAST")>=0:
                                mouse.click(button)
                            if event.state == 1 and event.code.find("BTN_NORTH")>=0:
                                mouse.move(0,-50)
                            if event.state == 1 and event.code.find("BTN_SOUTH")>=0:
                                mouse.move(0,50)
                            if event.state == 1 and event.code.find("ABS_HAT0Y")>=0:
                                click(delay,button,(GetSystemMetrics(0)/2),(GetSystemMetrics(1)/2)+50)
                            if event.state == -1 and event.code.find("ABS_HAT0Y")>=0:
                                click(delay,button,(GetSystemMetrics(0)/2),(GetSystemMetrics(1)/2)-50)
                            if event.state == 1 and event.code.find("ABS_HAT0X")>=0:
                                click(delay,button,(GetSystemMetrics(0)/2)+50,(GetSystemMetrics(1)/2))
                            if event.state == -1 and event.code.find("ABS_HAT0X")>=0:
                                click(delay,button,(GetSystemMetrics(0)/2)-50,(GetSystemMetrics(1)/2))
                                

                        except IndexError:
                            raise inputs.UnpluggedError("No controller detected!!")
                else:
                    pass
    print("Couldn't detect 360 Controller...")
print (GetSystemMetrics(0)/2)
main()
