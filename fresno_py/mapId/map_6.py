import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_6(timeClick):

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/6/pos.png',  confidence=0.9)
        IDENTIFIED1 = auto.locateOnScreen(
            './assets/fresno/mapas/6/pos1.png',  confidence=0.9)
        
        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False  

        elif IDENTIFIED or IDENTIFIED1:

            ASHTREE6_1 = auto.locateOnScreen(
                './assets/fresno/mapas/6/1.png',  confidence=0.9)
            ASHTREE6_2 = auto.locateOnScreen(
                './assets/fresno/mapas/6/2.png',  confidence=0.9)
            ASHTREE6_3 = auto.locateOnScreen(
                './assets/fresno/mapas/6/3.png',  confidence=0.9)
            ASHTREE6_4 = auto.locateOnScreen(
                './assets/fresno/mapas/6/4.png',  confidence=0.9)
            ASHTREE6_5 = auto.locateOnScreen(
                './assets/fresno/mapas/6/5.png',  confidence=0.9)
            ASHTREE6_6 = auto.locateOnScreen(
                './assets/fresno/mapas/6/6.png',  confidence=0.9)
            ASHTREE6_7 = auto.locateOnScreen(
                './assets/fresno/mapas/6/7.png',  confidence=0.9)
            ASHTREE6_8 = auto.locateOnScreen(
                './assets/fresno/mapas/6/8.png',  confidence=0.9)
            ASHTREE6_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/6/v1.png',  confidence=0.9)
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)

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
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break

            else:
                clickToCell(163, 557, 1, timeClick)
                loop = False