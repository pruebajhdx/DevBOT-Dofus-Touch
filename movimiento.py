import pyautogui as auto


def clickPosition(option):
    auto.click(option, clicks=1, duration=0.1)
    

def clickToCell(x, y):
    auto.click(x, y, clicks=1, duration=3)
   

def noneClick(box):
    auto.click(box, click=0, duration=0.1)