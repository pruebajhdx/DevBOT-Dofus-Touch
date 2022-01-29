import pyautogui as auto


def clickPosition(option):
    auto.click(option, clicks=1, duration=0.1)
    

def clickToCell(x, y, num, time):
    auto.click(x, y, clicks= num, duration= time)


def clickToCellMove(x, y):
    auto.click(x, y, clicks=1, duration=0.1)

   

def noneClick(box):
    auto.click(box, click=0, duration=0.1)

