import pyautogui as gui
import time

refresh_btn = './sauce/refresh_btn.png'
confirm_refresh_btn = './sauce/confirm_refresh.png'

mystic = './sauce/mystic.png'
confirm_btn_my = './sauce/confirm_btn_my.png'

bookmark = './sauce/bookmark.png'
confirm_btn_bm = './sauce/confirm_btn_bm.png'

confirm_offset = 800
list_offset = 600

def find_bookmark():
    try:
        x, y = gui.locateCenterOnScreen(bookmark, confidence=0.8)
        return x, y
    except:
        return 0, 0

def find_mystic():
    try:
        x, y = gui.locateCenterOnScreen(mystic, confidence=0.8)
        return x, y
    except:
        return 0, 0

def find_refresh():
    x, y = gui.locateCenterOnScreen(refresh_btn, confidence=0.8)
    return x, y

def find_confirm_refresh():
    x, y = gui.locateCenterOnScreen(confirm_refresh_btn, confidence=0.8)
    return x, y

def find_confirm_bm():
    x, y = gui.locateCenterOnScreen(confirm_btn_bm, confidence=0.8)
    return x, y

def find_confirm_my():
    x, y = gui.locateCenterOnScreen(confirm_btn_my, confidence=0.8)
    return x, y

def scroll():
    x, y = find_refresh()

    gui.moveTo(x + list_offset, y)
    gui.click(x + list_offset, y)
    gui.scroll(-10)

def click(x, y):
    gui.click(x, y)

def refresh():
    x, y = find_refresh()

    gui.click(x, y)
    time.sleep(500)

    x, y = find_confirm_refresh()

    gui.click(x, y)
    time.sleep(500)

def purchase(x, y):
    gui.click(x + confirm_offset, y)

def purchase_bm():
    x, y = find_bookmark()

    if x != 0:
        purchase(x, y)
        time.sleep(500)

        x, y = find_confirm_bm()
        click(x, y)

def purchase_my():
    x, y = find_mystic()

    if x != 0:
        purchase(x, y)
        time.sleep(500)

        x, y = find_confirm_my()
        click(x, y)

print("[INFO] Starting in 5 seconds, focus the application")
time.sleep(5000)

counter = 0
limit = 2

while True:
    try:
        counter++

        if counter > limit:
            break

        purchase_bm() 
        purchase_my() 

        scroll()

        purchase_bm() 
        purchase_my()

        refresh()

        print("[INFO] Round:", counter + 1)

    except:
        print("[WARN] Image not found, retrying...")
        pass

