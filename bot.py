import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import win32gui

# ekran çözünürlüğünü otomatik almaya çalış
ekranGenişliği, ekranYüksekliği= pyautogui.size()

# veya el ile çözünürlük gir
ekranGenişliği = 1920
ekranYüksekliği = 1080

# değişkenler
tamirEt = True
durum = "çekildi"
sayaç = 1
süre = 0

# oltayı atan fonksiyon. çalışabilmesi için oyunun önplanda olması gerekir..
def oltayıAt(sefer):
    print(strftime("%H:%M:%S", gmtime()), f"Olta atılıyor. sayaç: {sefer}")

    # haydi bakiyim rastgele......
    pyautogui.keyDown('e')
    time.sleep( random.uniform( 0.25, 0.55 ))
    pyautogui.keyUp('e')
    time.sleep( random.uniform(4.5, 6.5))

# premium pet özelliği ile oltayı otomatik tamir ettirmece sistemi
def oltayıTamirEt(ekranGenişliği, ekranYüksekliği):

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
    xOffset = 0.2
    yOffset = random.uniform(0.2, 0.5)
    gitX3 = round(ekranGenişliği * xOffset)
    gitY3 = round(ekranYüksekliği * yOffset)
    pyautogui.click(x=gitX3, y=gitY3, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=gitX3, y=gitY3, clicks=1, button='left')

# yapay zeka eğitim resimleri
template = cv2.imread(f"resources/{ekranYüksekliği}/template.png", 0)
poplavok = cv2.imread(f"resources/{ekranYüksekliği}/poplavok.png", 0)

print("Los Tarık Deli Balıklısı gms10ur gururla sunar.... 2C'ye selamlarla.")
print(strftime("%H:%M:%S", gmtime()), "5 Saniye sonra bot çalışacaktır. Olta 'E' tuşunda olmalıdır.")

if tamirEt:
    print("Otomatik tamir etkin, her 50 toplayışta bir tamir edilecek. Premiumun etkin olduğundan emin olunuz.")
else:
    print("Otomatik tamir devre dışı")

time.sleep(5)

while(1):
    süre = süre + 1
    if durum == "çekildi":
        oltayıAt(sayaç)
        durum = "atıldı"
        sayaç = sayaç + 1
        
    # ss almaca
    görsel = pyautogui.screenshot(region=(ekranGenişliği/2 - 100, ekranYüksekliği/2 - 150, 200, 200))
    görsel = cv2.cvtColor(numpy.array(görsel), 0)
    görsel = cv2.cvtColor(görsel, cv2.COLOR_BGR2GRAY)

    # şablon aramaca
    temp_kordinatları = cv2.matchTemplate(görsel, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(temp_kordinatları >= 0.7)

    # taramaya göre oltayı geri çek veya bekle
    if len(loc[0]) > 0 and durum == "atıldı":
        print(strftime("%H:%M:%S", gmtime()), "ha burya buni yakalayrum")
        süre = 0
        time.sleep(random.uniform(0.25, 1.0))

        # Balık yakalandı, hemen oltayı geri çek
        pyautogui.keyDown('e')
        time.sleep( random.uniform( 0.25, 0.55 ))
        pyautogui.keyUp('e')

        durum = "çekildi"
        time.sleep(random.uniform(5.5, 7.5))

    # 50 de 1 tamir sekansını başlat
    if (sayaç % 50 == 0) and (süre == 500 or durum == "çekildi") and tamirEt:
        print(strftime("%H:%M:%S", gmtime()), f"sayaç: {sayaç}. Tamir vakti geldi. Tamire başlanıyor.. durum: {durum}")
        oltayıTamirEt(ekranGenişliği, ekranYüksekliği)
        sayaç = sayaç + 1

    # search pattern on screen for buoy
    poplavok_coordinates = cv2.matchTemplate(görsel, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where(poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and durum == "çekildi":
        oltayıAt(sayaç)
        durum = "atıldı"
        sayaç = sayaç + 1

    print(strftime("%H:%M:%S", gmtime()), f"balug bekleyrum. geçen zaman: {süre}. ha bu 500 olursa saburım taşay daa. durum: {durum}")

    if süre == 500:
        print(f"ahanda saburım taşdi. oltayı yeniden atayrum.")
        süre = 0

        # Recast
        oltayıAt(sayaç)
        durum = "atıldı"
        sayaç = sayaç + 1