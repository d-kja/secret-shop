import pyautogui as gui
import msvcrt
import time

refresh_btn = './sauce/refresh_btn.png'
confirm_refresh_btn = './sauce/confirm_refresh.png'

mystic = './sauce/mystic.png'
confirm_btn_my = './sauce/confirm_btn_my.png'

bookmark = './sauce/bookmark.png'
confirm_btn_bm = './sauce/confirm_btn_bm.png'

confirm_offset = 800
list_offset = 650

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
    time.sleep(.35)

def click(x, y):
    gui.click(x, y)

def refresh():
    x, y = find_refresh()

    gui.click(x, y)
    time.sleep(.5)

    x, y = find_confirm_refresh()

    gui.click(x, y)
    time.sleep(.25)

def purchase(x, y):
    time.sleep(.25)
    gui.click(x + confirm_offset, y)

def purchase_bm():
    time.sleep(.25)
    x, y = find_bookmark()

    if x != 0:
        purchase(x, y)
        time.sleep(.25)

        x, y = find_confirm_bm()
        click(x, y)
        time.sleep(.25)

def purchase_my():
    time.sleep(.25)
    x, y = find_mystic()

    if x != 0:
        purchase(x, y)
        time.sleep(.25)

        x, y = find_confirm_my()
        click(x, y)
        time.sleep(.25)

print("[INFO] Starting in 5 seconds, focus the application")
time.sleep(5)

counter = 0
image_not_found_count = 0
limit = 200

while True:
    try:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode()
            if key == 'q':
                break

        if counter > limit:
            break

        purchase_bm() 
        purchase_my() 

        scroll()

        purchase_bm() 
        purchase_my()

        refresh()

        counter+=1
        image_not_found_count = 0
        print("[INFO] Round:", counter)

    except:
        print("[WARN] Image not found, retrying...")
        image_not_found_count += 1

        if image_not_found_count > 5:
            raise 

        pass

