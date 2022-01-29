import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_5():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/5/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE5_1 = auto.locateOnScreen(
                './assets/fresno/mapas/5/1.png',  confidence=0.9)
            ASHTREE5_2 = auto.locateOnScreen(
                './assets/fresno/mapas/5/2.png',  confidence=0.9)
            ASHTREE5_3 = auto.locateOnScreen(
                './assets/fresno/mapas/5/3.png',  confidence=0.9)
            ASHTREE5_4 = auto.locateOnScreen(
                './assets/fresno/mapas/5/4.png',  confidence=0.9)
            ASHTREE5_5 = auto.locateOnScreen(
                './assets/fresno/mapas/5/5.png',  confidence=0.9)
            ASHTREE5_6 = auto.locateOnScreen(
                './assets/fresno/mapas/5/6.png',  confidence=0.9)
            ASHTREE5_7 = auto.locateOnScreen(
                './assets/fresno/mapas/5/7.png',  confidence=0.9)
            ASHTREE5_8 = auto.locateOnScreen(
                './assets/fresno/mapas/5/8.png',  confidence=0.9)
            ASHTREE5_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/5/v1.png',  confidence=0.9)
            ASHTREE5_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/5/v2.png',  confidence=0.9)

            if ASHTREE5_1 or ASHTREE5_2:
                clickPosition(ASHTREE5_1 or ASHTREE5_2)

            elif ASHTREE5_3 or ASHTREE5_4:
                clickPosition(ASHTREE5_3 or ASHTREE5_4)

            elif ASHTREE5_5 or ASHTREE5_6:
                clickPosition(ASHTREE5_5 or ASHTREE5_6)

            elif ASHTREE5_7 or ASHTREE5_8:
                clickPosition(ASHTREE5_7 or ASHTREE5_8)

            elif ASHTREE5_v1 or ASHTREE5_v2:
                clickPosition(ASHTREE5_v1 or ASHTREE5_v2)         

            else:
                clickToCell(165, 584, 1, 3)
                loop = False