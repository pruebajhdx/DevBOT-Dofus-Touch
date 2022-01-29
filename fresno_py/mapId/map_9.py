import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_9():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/7/pos.png',  confidence=0.9)

        MOOB_ASHTREE9 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE9 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE9 or MOOB_ASHTREE9:
            loop = False

        elif IDENTIFIED:

            ASHTREE9_1 = auto.locateOnScreen(
                './assets/fresno/mapas/7/1.png',  confidence=0.9)
            ASHTREE9_2 = auto.locateOnScreen(
                './assets/fresno/mapas/7/2.png',  confidence=0.9)
            ASHTREE9_3 = auto.locateOnScreen(
                './assets/fresno/mapas/7/3.png',  confidence=0.9)
            ASHTREE9_4 = auto.locateOnScreen(
                './assets/fresno/mapas/7/4.png',  confidence=0.9)
            ASHTREE9_5 = auto.locateOnScreen(
                './assets/fresno/mapas/7/5.png',  confidence=0.9)
            ASHTREE9_6 = auto.locateOnScreen(
                './assets/fresno/mapas/7/6.png',  confidence=0.9)
            ASHTREE9_7 = auto.locateOnScreen(
                './assets/fresno/mapas/7/7.png',  confidence=0.9)
            ASHTREE9_8 = auto.locateOnScreen(
                './assets/fresno/mapas/7/8.png',  confidence=0.9)
            ASHTREE9_9 = auto.locateOnScreen(
                './assets/fresno/mapas/7/9.png',  confidence=0.9)
            ASHTREE9_10 = auto.locateOnScreen(
                './assets/fresno/mapas/7/10.png',  confidence=0.9)
            ASHTREE9_11 = auto.locateOnScreen(
                './assets/fresno/mapas/7/v1.png',  confidence=0.9)

            if ASHTREE9_1 or ASHTREE9_2:
                clickPosition(ASHTREE9_1 or ASHTREE9_2)

            elif ASHTREE9_4 or ASHTREE9_3:
                clickPosition(ASHTREE9_4 or ASHTREE9_3)

            elif ASHTREE9_5 or ASHTREE9_6:
                clickPosition(ASHTREE9_5 or ASHTREE9_6)

            elif ASHTREE9_7 or ASHTREE9_8:
                clickPosition(ASHTREE9_7 or ASHTREE9_8)

            elif ASHTREE9_9 or ASHTREE9_10:
                clickPosition(ASHTREE9_9 or ASHTREE9_10)

            elif ASHTREE9_11:
                clickPosition(ASHTREE9_11)
      

            else:
                clickToCell(1086, 1074, 1, 3)
                loop = False