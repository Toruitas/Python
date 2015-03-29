__author__ = 'Stuart'

import win32gui, win32ui, win32con, win32api
import datetime
from time import sleep
from PIL import Image
import os

hwin = win32gui.GetDesktopWindow()
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
hwindc = win32gui.GetWindowDC(hwin)
srcdc = win32ui.CreateDCFromHandle(hwindc)
memdc = srcdc.CreateCompatibleDC()
bmp = win32ui.CreateBitmap()
bmp.CreateCompatibleBitmap(srcdc, width, height)
memdc.SelectObject(bmp)
memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
# bmp.SaveBitmapFile(memdc, 'screenshot.bmp')
time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
outfile = "{}_{}".format("me", time)
bmp.SaveBitmapFile(memdc, outfile+'.bmp')
sleep(3)
Image.open(outfile+'.bmp').save(outfile+'.jpg')
sleep(3)
os.remove(outfile+'.bmp')


# hwnd = win32gui.FindWindow(None, windowname)
# wDC = win32gui.GetWindowDC(hwnd)
# dcObj=win32ui.CreateDCFromHandle(wDC)
# cDC=dcObj.CreateCompatibleDC()
# dataBitMap = win32ui.CreateBitmap()
# dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
# cDC.SelectObject(dataBitMap)
# cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
# dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
# # Free Resources
# dcObj.DeleteDC()
# cDC.DeleteDC()
# win32gui.ReleaseDC(hwnd, wDC)
# win32gui.DeleteObject(dataBitMap.GetHandle())
# dcObj.DeleteDC()
# cDC.DeleteDC()
# win32gui.ReleaseDC(hwnd, wDC)