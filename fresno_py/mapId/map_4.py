import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_4():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/4/pos.png',  confidence=0.9)

        if IDENTIFIED:

            ASHTREE3_1 = auto.locateOnScreen(
                './assets/fresno/mapas/4/2-2v.png',  confidence=0.9)
            ASHTREE3_2 = auto.locateOnScreen(
                './assets/fresno/mapas/4/3.png',  confidence=0.9)
            ASHTREE3_3 = auto.locateOnScreen(
                './assets/fresno/mapas/4/4.png',  confidence=0.9)
            ASHTREE3_4 = auto.locateOnScreen(
                './assets/fresno/mapas/4/6.png',  confidence=0.9)
            ASHTREE3_5 = auto.locateOnScreen(
                './assets/fresno/mapas/4/7-v6.png',  confidence=0.9)
            ASHTREE3_6 = auto.locateOnScreen(
                './assets/fresno/mapas/4/7.png',  confidence=0.9)
            ASHTREE3_7 = auto.locateOnScreen(
                './assets/fresno/mapas/4/8.png',  confidence=0.9)
            ASHTREE3_8 = auto.locateOnScreen(
                './assets/fresno/mapas/4/9.png',  confidence=0.9)
            ASHTREE3_10 = auto.locateOnScreen(
                './assets/fresno/mapas/4/10.png',  confidence=0.9)
            ASHTREE3_11 = auto.locateOnScreen(
                './assets/fresno/mapas/4/11.png',  confidence=0.9)
            ASHTREE3_12 = auto.locateOnScreen(
                './assets/fresno/mapas/4/12.png',  confidence=0.9)
            ASHTREE3_13 = auto.locateOnScreen(
                './assets/fresno/mapas/4/13-v12.png',  confidence=0.9)
            ASHTREE3_14 = auto.locateOnScreen(
                './assets/fresno/mapas/4/13.png',  confidence=0.9)
            ASHTREE3_15 = auto.locateOnScreen(
                './assets/fresno/mapas/4/14.png',  confidence=0.9)
            ASHTREE3_16 = auto.locateOnScreen(
                './assets/fresno/mapas/4/15.png',  confidence=0.9)
            ASHTREE3_17 = auto.locateOnScreen(
                './assets/fresno/mapas/4/16-v15.png',  confidence=0.9)
            ASHTREE3_18 = auto.locateOnScreen(
                './assets/fresno/mapas/4/17.png',  confidence=0.9)
            ASHTREE3_19 = auto.locateOnScreen(
                './assets/fresno/mapas/4/18.png',  confidence=0.9)
            ASHTREE3_20 = auto.locateOnScreen(
                './assets/fresno/mapas/4/19.png',  confidence=0.9)
            ASHTREE3_21 = auto.locateOnScreen(
                './assets/fresno/mapas/4/20.png',  confidence=0.9)
            ASHTREE3_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v1.png',  confidence=0.9)
            ASHTREE3_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v2.png',  confidence=0.9)

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
            
            elif ASHTREE3_v1 or ASHTREE3_v2:
                clickPosition(ASHTREE3_v1 or ASHTREE3_v2)

            else:
                clickToCell(167, 167)
                loop = False