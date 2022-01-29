import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_7():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/7/pos.png',  confidence=0.9)

        if IDENTIFIED:

            ASHTREE7_1 = auto.locateOnScreen(
                './assets/fresno/mapas/7/1.png',  confidence=0.9)
            ASHTREE7_2 = auto.locateOnScreen(
                './assets/fresno/mapas/7/3.png',  confidence=0.9)
            ASHTREE7_3 = auto.locateOnScreen(
                './assets/fresno/mapas/7/4.png',  confidence=0.9)
            ASHTREE7_4 = auto.locateOnScreen(
                './assets/fresno/mapas/7/5.png',  confidence=0.9)
            ASHTREE7_5 = auto.locateOnScreen(
                './assets/fresno/mapas/7/6.png',  confidence=0.9)
            ASHTREE7_6 = auto.locateOnScreen(
                './assets/fresno/mapas/7/7.png',  confidence=0.9)
            ASHTREE7_7 = auto.locateOnScreen(
                './assets/fresno/mapas/7/8.png',  confidence=0.9)
            ASHTREE7_8 = auto.locateOnScreen(
                './assets/fresno/mapas/7/9.png',  confidence=0.9)
            ASHTREE7_10 = auto.locateOnScreen(
                './assets/fresno/mapas/7/10.png',  confidence=0.9)
            ASHTREE7_11 = auto.locateOnScreen(
                './assets/fresno/mapas/7/11.png',  confidence=0.9)
            ASHTREE7_12 = auto.locateOnScreen(
                './assets/fresno/mapas/7/12.png',  confidence=0.9)
            ASHTREE7_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/7/v1.png',  confidence=0.9)
        

            if ASHTREE7_1 or ASHTREE7_2:
                clickPosition(ASHTREE7_1 or ASHTREE7_2)

            elif ASHTREE7_3 or ASHTREE7_4:
                clickPosition(ASHTREE7_3 or ASHTREE7_4)

            elif ASHTREE7_5 or ASHTREE7_6:
                clickPosition(ASHTREE7_5 or ASHTREE7_6)

            elif ASHTREE7_7 or ASHTREE7_8:
                clickPosition(ASHTREE7_7 or ASHTREE7_8)

            elif ASHTREE7_10 or ASHTREE7_11:
                clickPosition(ASHTREE7_10 or ASHTREE7_11)

            elif ASHTREE7_12 or ASHTREE7_v1:
                clickPosition(ASHTREE7_12 or ASHTREE7_v1)

            else:
                clickToCell(1086, 1074)
                loop = False