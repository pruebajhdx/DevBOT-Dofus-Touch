import time
import pyautogui as auto

from fresno_py.mapId.map_1 import map_1
from fresno_py.mapId.map_2 import map_2
from fresno_py.mapId.map_3 import map_3
from fresno_py.mapId.map_4 import map_4
from fresno_py.mapId.map_14 import map_14
from fresno_py.mapId.map_5 import map_5
from fresno_py.mapId.map_6 import map_6
from fresno_py.mapId.map_7 import map_7

from movimiento import clickPosition, clickToCell


# Variables
# mapIdDeath = 0

death = False
farm = True


def moveToMap(count):

    move = True

    if count == 1:
        map_1()
        moveToFarm(move, count)
    elif count == 2:
        map_2()
        moveToFarm(move, count)
    elif count == 3:
        map_3()
        moveToFarm(move, count)
    elif count == 4:
        map_4()
        moveToFarm(move, count)
    elif count == 5:
        map_5()
        moveToFarm(move, count)
    elif count == 6:
        map_6()
        moveToFarm(move, count)
    elif count == 7:
        map_7()
        moveToFarm(move, count)
    elif count == 8:
        clickToCell(1582, 498, 1, 3)
    elif count == 9:
        clickToCell(1593, 501, 1, 3)
    elif count == 10:
        clickToCell(1591, 405, 1, 3)
    elif count == 11:
        clickToCell(1587, 538, 1, 3)
    elif count == 12:
        clickToCell(1598, 452, 1, 3)
    elif count == 13:
        clickToCell(1163, 49, 1, 3)
    elif count == 14:
        map_14()


def moveToDead(mapId):
    if mapId == 1:
        clickToCell(1670, 668, 1, 0.1)
    elif mapId == 2:
        clickToCell(1669, 751, 1, 0.1)
    elif mapId == 3:
        clickToCell(1666, 650, 1, 0.1)
    elif mapId == 4:
        clickToCell(1672, 498, 1, 0.1)
    elif mapId == 5:
        clickToCell(975, 38, 1, 0.1)
    elif mapId == 6:
        clickToCell(1130, 48, 1, 0.1)
    elif mapId == 7:
        clickToCell(955, 37, 1, 0.1)
    elif mapId == 8:
        clickToCell(655, 38, 1, 0.1)
    elif mapId == 9:
        clickToCell(155, 868, 1, 0.1)


def toDead(death):

    mapNext = 0
    uniqueClick = 0

    while death:

        LEAVE = auto.locateOnScreen(
            './assets/abandono/abandonar.png', confidence=0.9)
        LEAVE_YES = auto.locateOnScreen(
            './assets/abandono/abandonarsi.png', confidence=0.9)
        MSG_OK = auto.locateOnScreen(
            './assets/abandono/ok.png', confidence=0.8)
        INTERFACE_X = auto.locateOnScreen(
            './assets/abandono/x.png', confidence=0.8)
        FENIX = auto.locateOnScreen(
            './assets/fresno/fenix/fenix.png', confidence=0.8)
        POTION = auto.locateOnScreen(
            './assets/otros/pocima.png', confidence=0.7)

        if LEAVE and uniqueClick <= 1:
            uniqueClick += 1
            clickPosition(LEAVE)
        elif LEAVE_YES:
            clickPosition(LEAVE_YES)
        elif MSG_OK or INTERFACE_X:
            clickPosition(MSG_OK or INTERFACE_X)
        elif FENIX:
            clickPosition(FENIX)
            time.sleep(7)
            if POTION:
                auto.doubleClick(POTION, duration=0.1)
                death = False
                farm = True
                moveToFarm(farm, 0)
        else:
            mapNext += 1
            print('ghostID', mapNext)
            moveToDead(mapNext)
            time.sleep(5)


def moveToFarm(farm, count):

    while farm:
        # MapaId 13

        # Fresno MOOB
        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)

        # Inventario

        INVENTARY_FULL = auto.locateOnScreen(
            "./assets/otros/inventario.png", confidence=0.9)

        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            farm = False
            death = True
            toDead(death)

        elif INVENTARY_FULL:
            auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
            auto.alert(text='Inventario lleno', title='Alerta', button='OK')
            break

        else:
            count = count + 1
            if count >= 15:
                count = 0
            else:
                print('Farm mapID: ', count)
                moveToMap(count)
                farm = False
        # print(position)


if __name__ == "__main__":
    count = 0
    moveToFarm(farm, count)
    # auto.FAILSAFE
    # print(auto.getAllWindows())
