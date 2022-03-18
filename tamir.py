import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

print(strftime("%H:%M:%S", gmtime()), "5 Sn içinde tamir işlemi başlayacaktır.")
time.sleep(5)

screenWidth, screenHeight= pyautogui.size()
pyautogui.position()

 # pet ekranını açıver
print(strftime("%H:%M:%S", gmtime()), "Pet ekranı açılıyor --> (ALT + P).")
pyautogui.keyDown('alt')
pyautogui.keyDown('p')
pyautogui.keyUp('p')
pyautogui.keyUp('alt')

# minik bi beklemece
time.sleep(random.uniform(2.0, 3.0))

# remote tamir tuşunu snipelamaca
print(strftime("%H:%M:%S", gmtime()), "Remote repair tuşuna gidiliyor..")
xOffset = 0.674
yOffset = 0.641
gitX1 = round(ekranGenişliği * xOffset)
gitY1 = round(ekranYüksekliği * yOffset)
pyautogui.click(x=gitX1, y=gitY1, clicks=0, button='left')
time.sleep(random.uniform(1.0, 1.5))
pyautogui.click(x=gitX1, y=gitY1, clicks=1, button='left')

# minik bi beklemece
time.sleep(random.uniform(2.0, 3.0))

# hepsini tamir et tuşuna bas
print(strftime("%H:%M:%S", gmtime()), "Hepsini tamir et tuşuna basılıyor..")
xOffset = 0.384
yOffset = 0.688
gitX2 = round(ekranGenişliği * xOffset)
gitY2 = round(ekranYüksekliği * yOffset)
pyautogui.click(x=gitX2, y=gitY2, clicks=0, button='left')
time.sleep(random.uniform(1.0, 1.5))
pyautogui.click(x=gitX2, y=gitY2, clicks=1, button='left')

# minik bi beklemece
time.sleep(random.uniform(2.0, 3.0))

# onayla tuşuna bas
print(strftime("%H:%M:%S", gmtime()), "OK tuşuna basılıyor..")
xOffset = 0.457
yOffset = 0.578
gitX3 = round(ekranGenişliği * xOffset)
gitY3 = round(ekranYüksekliği * yOffset)
pyautogui.click(x=gitX3, y=gitY3, clicks=0, button='left')
time.sleep(random.uniform(1.0, 1.5))
pyautogui.click(x=gitX3, y=gitY3, clicks=1, button='left')

# minik bi beklemece
time.sleep(random.uniform(4.0, 5.0))

# ESC
print(strftime("%H:%M:%S", gmtime()), "ESCye basılıyor, tamir ekranı kapatılıyor..")
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')

# minik bi beklemece
time.sleep(random.uniform(2.0, 3.0))

# ESC
print(strftime("%H:%M:%S", gmtime()), "SCye basılıyor, pet ekranı kapatılıyor.")
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')

# minik bi beklemece
time.sleep(random.uniform(2.0, 5.0))

# Mouse re-locate
print(strftime("%H:%M:%S", gmtime()), "Mouse yeni bi lokasyona çekiliyor.")
xOffset = random.uniform(0.2, 0.8)
yOffset = 0.1
gitX3 = round(ekranGenişliği * xOffset)
gitY3 = round(ekranYüksekliği * yOffset)
pyautogui.click(x=gitX3, y=gitY3, clicks=0, button='left')
time.sleep(random.uniform(1.0, 1.5))
pyautogui.click(x=gitX3, y=gitY3, clicks=1, button='left')