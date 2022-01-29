import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_3():

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/3/pos.png',  confidence=0.9)

        if IDENTIFIED:

            ASHTREE3_1 = auto.locateOnScreen(
                './assets/fresno/mapas/3/1.png',  confidence=0.9)
            ASHTREE3_2 = auto.locateOnScreen(
                './assets/fresno/mapas/3/2.png',  confidence=0.9)

            if ASHTREE3_1 or ASHTREE3_2:
                clickPosition(ASHTREE3_1 or ASHTREE3_2)
            else:
                clickToCell(190, 698)
                loop = False
