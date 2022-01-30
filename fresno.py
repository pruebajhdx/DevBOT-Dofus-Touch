from re import I
import time
import pyautogui as auto
from bcolor import bcolors

from fresno_py.mapId.map_1 import map_1
from fresno_py.mapId.map_2 import map_2
from fresno_py.mapId.map_3 import map_3
from fresno_py.mapId.map_4 import map_4
from fresno_py.mapId.map_5 import map_5
from fresno_py.mapId.map_6 import map_6
from fresno_py.mapId.map_7 import map_7
from fresno_py.mapId.map_8 import map_8
from fresno_py.mapId.map_9 import map_9
from fresno_py.mapId.map_10 import map_10
from fresno_py.mapId.map_11 import map_11
from fresno_py.mapId.map_12 import map_12
from fresno_py.mapId.map_13 import map_13
from fresno_py.mapId.map_14 import map_14

from movimiento import clickPosition, clickToCell


# Variables
# mapIdDeath = 0

death = False
farm = True


def moveToMap(count):

    move = True
    timeClick = 1

    if count == 1:
        map_1(timeClick)
        moveToFarm(move, count)
    elif count == 2:
        map_2(timeClick)
        moveToFarm(move, count)
    elif count == 3:
        map_3(timeClick)
        moveToFarm(move, count)
    elif count == 4:
        map_4(timeClick)
        moveToFarm(move, count)
    elif count == 5:
        map_5(timeClick)
        moveToFarm(move, count)
    elif count == 6:
        map_6(timeClick)
        moveToFarm(move, count)
    elif count == 7:
        map_7(timeClick)
        moveToFarm(move, count)
    elif count == 8:
        map_8(timeClick)
        moveToFarm(move, count)
    elif count == 9:
        map_9(timeClick)
        moveToFarm(move, count)
    elif count == 10:
        map_10(timeClick)
        moveToFarm(move, count)
    elif count == 11:
        map_11(timeClick)
        moveToFarm(move, count)
    elif count == 12:
        map_12(timeClick)
        moveToFarm(move, count)
    elif count == 13:
        map_13(timeClick)
        moveToFarm(move, count)
    elif count == 14:
        map_14(timeClick)
        moveToFarm(move, count)


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

    cycle = 0

    while farm:

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)

        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            farm = False
            death = True
            toDead(death)

        count = count + 1

        if count >= 15:
            count = 0
            cycle += 1
        else:
            print(bcolors.OK + 'Farmeando mapID Rincón del Jalato: ' +
                  bcolors.RESET, bcolors.COUNT + str(count) + bcolors.RESET)
            print(bcolors.WHITE_N +
                  'Capturando objetos interactivos...' + bcolors.RESET)
            moveToMap(count)
            farm = False

        print('Rondas terminadas: ', cycle)


if __name__ == "__main__":
    count = 0
    print(bcolors.YELLOW_N + 'Botus Dofus Touch' + bcolors.RESET)
    print(bcolors.YELLOW_N + 'Analizando mapas ...' + bcolors.RESET)
    moveToFarm(farm, count)
    # auto.FAILSAFEc
    # print(auto.getAllWindows())
