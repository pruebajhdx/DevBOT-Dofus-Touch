import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_3():

    ASHTREE3_1  =  auto.locateOnScreen('./assets/fresno/mapas/3/2-2v.png',  confidence=0.9)
    ASHTREE3_2  =  auto.locateOnScreen('./assets/fresno/mapas/3/3.png',  confidence=0.9)
    ASHTREE3_3  =  auto.locateOnScreen('./assets/fresno/mapas/3/4.png',  confidence=0.9)
    ASHTREE3_4  =  auto.locateOnScreen('./assets/fresno/mapas/3/6.png',  confidence=0.9)
    ASHTREE3_5  =  auto.locateOnScreen('./assets/fresno/mapas/3/7-v6.png',  confidence=0.9)
    ASHTREE3_6  =  auto.locateOnScreen('./assets/fresno/mapas/3/7.png',  confidence=0.9)
    ASHTREE3_7  =  auto.locateOnScreen('./assets/fresno/mapas/3/8.png',  confidence=0.9)
    ASHTREE3_8  =  auto.locateOnScreen('./assets/fresno/mapas/3/9.png',  confidence=0.9)
    ASHTREE3_10 =  auto.locateOnScreen('./assets/fresno/mapas/3/10.png',  confidence=0.9)
    ASHTREE3_11 =  auto.locateOnScreen('./assets/fresno/mapas/3/11.png',  confidence=0.9)
    ASHTREE3_12 =  auto.locateOnScreen('./assets/fresno/mapas/3/12.png',  confidence=0.9)
    ASHTREE3_13 =  auto.locateOnScreen('./assets/fresno/mapas/3/13-v12.png',  confidence=0.9)
    ASHTREE3_14 =  auto.locateOnScreen('./assets/fresno/mapas/3/13.png',  confidence=0.9)
    ASHTREE3_15 =  auto.locateOnScreen('./assets/fresno/mapas/3/14.png',  confidence=0.9)
    ASHTREE3_16 =  auto.locateOnScreen('./assets/fresno/mapas/3/15.png',  confidence=0.9)
    ASHTREE3_17 =  auto.locateOnScreen('./assets/fresno/mapas/3/16-v15.png',  confidence=0.9)
    ASHTREE3_18 =  auto.locateOnScreen('./assets/fresno/mapas/3/17.png',  confidence=0.9)
    ASHTREE3_19 =  auto.locateOnScreen('./assets/fresno/mapas/3/18.png',  confidence=0.9)
    ASHTREE3_20 =  auto.locateOnScreen('./assets/fresno/mapas/3/19.png',  confidence=0.9)
    ASHTREE3_21 =  auto.locateOnScreen('./assets/fresno/mapas/3/20.png',  confidence=0.9)

    if ASHTREE3_1 or ASHTREE3_2:
        clickPosition(ASHTREE3_1 or ASHTREE3_2)

    elif ASHTREE3_3 or ASHTREE3_4:
        clickPosition(ASHTREE3_3 or ASHTREE3_4)

    elif ASHTREE3_5 or ASHTREE3_6:
        clickPosition(ASHTREE3_5 or ASHTREE3_6)

    elif ASHTREE3_7 or ASHTREE3_8:
        clickPosition(ASHTREE3_7 or ASHTREE3_8) 

    elif ASHTREE3_10 or ASHTREE3_11:
        clickPosition(ASHTREE3_10 or ASHTREE3_11)

    elif ASHTREE3_12 or ASHTREE3_13:
        clickPosition(ASHTREE3_12 or ASHTREE3_13)

    elif ASHTREE3_14 or ASHTREE3_15:
        clickPosition(ASHTREE3_14 or ASHTREE3_15)

    elif ASHTREE3_16 or ASHTREE3_17:
        clickPosition(ASHTREE3_16 or ASHTREE3_17)

    elif ASHTREE3_18 or ASHTREE3_19:
        clickPosition(ASHTREE3_18 or ASHTREE3_19)

    elif ASHTREE3_20 or ASHTREE3_21:
        clickPosition(ASHTREE3_20 or ASHTREE3_21)

    else:
        clickToCell(167, 167)