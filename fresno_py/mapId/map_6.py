import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_6():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/6/pos.png',  confidence=0.9)

        if IDENTIFIED:

            ASHTREE6_1 = auto.locateOnScreen(
                './assets/fresno/mapas/6/1.png',  confidence=0.9)
            ASHTREE6_2 = auto.locateOnScreen(
                './assets/fresno/mapas/6/3.png',  confidence=0.9)
            ASHTREE6_3 = auto.locateOnScreen(
                './assets/fresno/mapas/6/4.png',  confidence=0.9)
            ASHTREE6_4 = auto.locateOnScreen(
                './assets/fresno/mapas/6/5.png',  confidence=0.9)
            ASHTREE6_5 = auto.locateOnScreen(
                './assets/fresno/mapas/6/6.png',  confidence=0.9)
            ASHTREE6_6 = auto.locateOnScreen(
                './assets/fresno/mapas/6/7.png',  confidence=0.9)
            ASHTREE6_7 = auto.locateOnScreen(
                './assets/fresno/mapas/6/8.png',  confidence=0.9)
            ASHTREE6_8 = auto.locateOnScreen(
                './assets/fresno/mapas/6/9.png',  confidence=0.9)
            ASHTREE6_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/6/v1.png',  confidence=0.9)
        

            if ASHTREE6_1 or ASHTREE6_2:
                clickPosition(ASHTREE6_1 or ASHTREE6_2)

            elif ASHTREE6_3 or ASHTREE6_4:
                clickPosition(ASHTREE6_3 or ASHTREE6_4)

            elif ASHTREE6_5 or ASHTREE6_6:
                clickPosition(ASHTREE6_5 or ASHTREE6_6)

            elif ASHTREE6_7 or ASHTREE6_8:
                clickPosition(ASHTREE6_7 or ASHTREE6_8)

            elif ASHTREE6_v1:
                clickPosition(ASHTREE6_v1)

            else:
                clickToCell(163, 557)
                loop = False