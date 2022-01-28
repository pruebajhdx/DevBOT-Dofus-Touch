from xmlrpc.client import boolean
import pyautogui as auto
import time


# Variables
position = []
count = 0
mapIdDeath = 0
death = False
farm = True


""" d = auto.locateOnScreen("assets/fresno/fresno4.png", confidence=0.4)
e = auto.locateOnScreen("assets/fresno/fresno5.png", confidence=0.4)
f = auto.locateOnScreen("assets/fresno/fresno6.png", confidence=0.4)
g = auto.locateOnScreen("assets/fresno/fresno7.png", confidence=0.4) """


def clickPosition(option):
    auto.click(option, duration=0.1, clicks=1)
    x, y = auto.position()
    position.append(
        {
         'x': int(str(x).rjust(4)), 
         'y': int(str(y).rjust(4))
        })
    return position

def clickToCell(x, y):
    auto.click(x, y, clicks=1, duration=0.1)
    return x, y

def noneClick(box):
    auto.click(box, click=0, duration=0.1)
    return box


def moveToMap(count):
    if count == 1:
        clickToCell(163, 514)
    elif count == 2:
        clickToCell(748, 1073)
    elif count == 3:
        clickToCell(167, 167)
    elif count == 4:
        clickToCell(173, 537)
    elif count == 5:
        clickToCell(165, 584)
    elif count == 6:
        clickToCell(163, 557)
    elif count == 7:
        clickToCell(1086, 1074)
    elif count == 8:
        clickToCell(1582, 498)
    elif count == 9:
        clickToCell(1593, 501)
    elif count == 10:
        clickToCell(1591, 405)
    elif count == 11:
        clickToCell(1587, 538)
    elif count == 12:
        clickToCell(1598, 452)
    elif count == 13:
        clickToCell(1163, 49)
    elif count == 14:
        clickToCell(1376, 46)

def moveToDead(mapId):
    if mapId == 1:
        clickToCell(1670, 668)
    elif mapId == 2:
        clickToCell(1669, 751)
    elif mapId == 3:
        clickToCell(1666, 650)
    elif mapId == 4:
        clickToCell(1672, 498)
    elif mapId == 5:
        clickToCell(975, 38)
    elif mapId == 6:
        clickToCell(1130, 48)
    elif mapId == 7:
        clickToCell(955, 37)
    elif mapId == 8:
        clickToCell(655, 38)
    elif mapId == 9:
        clickToCell(155, 868)


def toDead(death):

    mapNext = 0
    uniqueClick = 0
    
    while death:

        LEAVE = auto.locateOnScreen('assets/abandono/abandonar.png', confidence=0.9)
        LEAVE_YES = auto.locateOnScreen('assets/abandono/abandonarsi.png', confidence=0.9)
        MSG_OK = auto.locateOnScreen('assets/abandono/ok.png', confidence=0.8)
        INTERFACE_X = auto.locateOnScreen('assets/abandono/x.png', confidence=0.8)
        FENIX = auto.locateOnScreen('assets/fresno/fenix/fenix.png', confidence=0.8)
        POTION = auto.locateOnScreen('assets/otros/pocima.png', confidence=0.7)

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
                moveToFarm(farm)
        else:
            mapNext += 1
            print('ghostID', mapNext)
            moveToDead(mapNext)
            time.sleep(5)

    return death

def moveToFarm(farm):
    
    count = 0

    while farm:

        """ ASHTREE1 = auto.locateOnScreen('assets/fresno/fresno1.png',  confidence=0.9)
        ASHTREE2 = auto.locateOnScreen('assets/fresno/fresno2.png',  confidence=0.9)
        ASHTREE3 = auto.locateOnScreen('assets/fresno/fresno3.png',  confidence=0.9)
        ASHTREE4 = auto.locateOnScreen('assets/fresno/fresno4.png',  confidence=0.9)
        ASHTREE5 = auto.locateOnScreen('assets/fresno/fresno5.png',  confidence=0.9)
        ASHTREE6 = auto.locateOnScreen('assets/fresno/fresno6.png',  confidence=0.9)
        ASHTREE7 = auto.locateOnScreen('assets/fresno/fresno7.png',  confidence=0.9)
        ASHTREE8 = auto.locateOnScreen('assets/fresno/fresno8.png',  confidence=0.9)
        ASHTREE9 = auto.locateOnScreen('assets/fresno/fresno9.png',  confidence=0.9)
        ASHTREE10 = auto.locateOnScreen('assets/fresno/fresno10.png',  confidence=0.7)
        ASHTREE11 = auto.locateOnScreen('assets/fresno/fresno11.png',  confidence=0.7) """

        #MapaId 13

        
        #MapaId 14

        ASHTREE14_1 = auto.locateOnScreen('assets/fresno/mapas/14/1.png',  confidence=0.9)
        ASHTREE14_2 = auto.locateOnScreen('assets/fresno/mapas/14/2.png',  confidence=0.9)
        ASHTREE14_3 = auto.locateOnScreen('assets/fresno/mapas/14/3.png',  confidence=0.9)
        ASHTREE14_4 = auto.locateOnScreen('assets/fresno/mapas/14/4.png',  confidence=0.9)
        ASHTREE14_5 = auto.locateOnScreen('assets/fresno/mapas/14/5.png',  confidence=0.9)
        ASHTREE14_6 = auto.locateOnScreen('assets/fresno/mapas/14/6.png',  confidence=0.9)
        ASHTREE14_7 = auto.locateOnScreen('assets/fresno/mapas/14/7.png',  confidence=0.9)
        ASHTREE14_8 = auto.locateOnScreen('assets/fresno/mapas/14/8.png',  confidence=0.9)
        ASHTREE14_9 = auto.locateOnScreen('assets/fresno/mapas/14/9.png',  confidence=0.9)

        # Variantes fresnos
        ASHTREE14_v1 = auto.locateOnScreen('assets/fresno/mapas/14/v1.png',  confidence=0.7)
        ASHTREE14_v2  = auto.locateOnScreen('assets/fresno/mapas/14/v2.png',  confidence=0.9)
   
        # Fresno MOOB
        MOOB_ASHTREE1 = auto.locateOnScreen('assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen('assets/fresno/moob/moob2.png', confidence=0.9)

        # Inventario

        INVENTARY_FULL = auto.locateOnScreen("assets/otros/inventario.png", confidence=0.9)

        if ASHTREE14_1 or ASHTREE14_2:
            clickPosition(ASHTREE14_1 or ASHTREE14_2)
        elif ASHTREE14_3 or ASHTREE14_4:
            clickPosition(ASHTREE14_3 or ASHTREE14_4)
        elif ASHTREE14_5 or ASHTREE14_6:
            clickPosition(ASHTREE14_5 or ASHTREE14_6)
        elif ASHTREE14_7 or ASHTREE14_8:
            clickPosition(ASHTREE14_7 or ASHTREE14_8) 
        elif ASHTREE14_9 or ASHTREE14_v1:
            clickPosition(ASHTREE14_9 or ASHTREE14_v1)
        elif ASHTREE14_v2:
            clickPosition(ASHTREE14_v2)
                 
        elif MOOB_ASHTREE1 or MOOB_ASHTREE2:
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
        #print(position)


if __name__ == "__main__":
    moveToFarm(farm)
    auto.FAILSAFE
    #print(auto.getAllWindows())
