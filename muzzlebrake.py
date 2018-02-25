import win32api, win32con, win32gui
import time
import threading

mode_enabled = False
muzzlebrake_enabled = False

def compensate():
    global mode_enabled
    global muzzlebrake_enabled
    while True:
        if mode_enabled and muzzlebrake_enabled:
            x, y = win32api.GetCursorPos()
            y = y + 35
            print(y)
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, x, y)
        time.sleep(0.1)

def caps_watch():
    global mode_enabled
    state_caps = win32api.GetAsyncKeyState(win32con.VK_CAPITAL)
    while True:
        current_state_caps = win32api.GetAsyncKeyState(win32con.VK_CAPITAL)
        if current_state_caps != state_caps:
            state_caps = current_state_caps
            if current_state_caps < 0:
                mode_enabled = not mode_enabled
        time.sleep(0.1)

def left_watch():
    global muzzlebrake_enabled
    state_left = win32api.GetKeyState(0x01)
    while True:
        x, y = win32api.GetCursorPos()
        print (x, y)
        current_state_left = win32api.GetKeyState(0x01)
        if current_state_left != state_left:
            state_left = current_state_left
            if current_state_left < 0:
                muzzlebrake_enabled = True
            else:
                muzzlebrake_enabled = False
        time.sleep(0.001)

def main():
    t1 = threading.Thread(target=compensate)
    t2 = threading.Thread(target=caps_watch)
    t3 = threading.Thread(target=left_watch)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    input()

main()    