
import time
import win32gui
import win32con
import win32api


test = 0
start = 1


time.sleep(3)
while start:
    try:

        handle = win32gui.FindWindow("StandardWindow", None)
        left, top, right, bottom = win32gui.GetWindowRect(handle)
        print(left, top, right, bottom)
        pos = (int((left + right) / 2), int((top + bottom) / 2))
        client_pos = win32gui.ScreenToClient(handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
        time.sleep(1)
    except:
        time.sleep(10)

