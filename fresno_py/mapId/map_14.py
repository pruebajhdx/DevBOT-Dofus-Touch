import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_14():

    loop = True

    
    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/14/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE14_1 = auto.locateOnScreen(
                './assets/fresno/mapas/14/1.png',  confidence=0.9)
            ASHTREE14_1 = auto.locateOnScreen(
                './assets/fresno/mapas/14/1.png',  confidence=0.9)
            ASHTREE14_2 = auto.locateOnScreen(
                './assets/fresno/mapas/14/2.png',  confidence=0.9)
            ASHTREE14_3 = auto.locateOnScreen(
                './assets/fresno/mapas/14/3.png',  confidence=0.9)
            ASHTREE14_4 = auto.locateOnScreen(
                './assets/fresno/mapas/14/4.png',  confidence=0.9)
            ASHTREE14_5 = auto.locateOnScreen(
                './assets/fresno/mapas/14/5.png',  confidence=0.9)
            ASHTREE14_6 = auto.locateOnScreen(
                './assets/fresno/mapas/14/6.png',  confidence=0.9)
            ASHTREE14_7 = auto.locateOnScreen(
                './assets/fresno/mapas/14/7.png',  confidence=0.9)
            ASHTREE14_8 = auto.locateOnScreen(
                './assets/fresno/mapas/14/8.png',  confidence=0.9)
            ASHTREE14_9 = auto.locateOnScreen(
                './assets/fresno/mapas/14/9.png',  confidence=0.9)
            
            # Variantes fresnos
            ASHTREE14_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/14/v1.png',  confidence=0.9)
            ASHTREE14_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/14/v2.png',  confidence=0.9) 

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

            else:
                clickToCell(1376, 46, 1, 3)
                loop = False
