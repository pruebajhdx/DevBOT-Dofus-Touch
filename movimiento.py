import pyautogui as auto

position = []

def clickPosition(option):
    auto.click(option, clicks=1, duration=1)
    x, y = auto.position()
    position.append(
        {
         'x': int(str(x).rjust(4)), 
         'y': int(str(y).rjust(4))
        })
    return position

def clickToCell(x, y):
    auto.click(x, y, clicks=1, duration=3.5)
    return x, y

def noneClick(box):
    auto.click(box, click=0, duration=0.1)
    return box