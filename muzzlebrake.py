import win32api, win32con, win32gui
import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE,x,y,x,y)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,x,y)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)


while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
            x, y = win32api.GetCursorPos()
            y = y + 50
            click(x,y)

        else:
            print('Left Button Released')

    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            print('Right Button Pressed')

        else:
            print('Right Button Released')
    time.sleep(0.001)
