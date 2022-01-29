import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_11(timeClick):

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/11/pos.png',  confidence=0.9)

        MOOB_ASHTREE11 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE12 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE11 or MOOB_ASHTREE12:
            loop = False

        elif IDENTIFIED:

            ASHTREE11_1 = auto.locateOnScreen(
                './assets/fresno/mapas/11/1.png',  confidence=0.9)
            ASHTREE11_2 = auto.locateOnScreen(
                './assets/fresno/mapas/11/2.png',  confidence=0.9)
            ASHTREE11_3 = auto.locateOnScreen(
                './assets/fresno/mapas/11/3.png',  confidence=0.9)
            ASHTREE11_4 = auto.locateOnScreen(
                './assets/fresno/mapas/11/4.png',  confidence=0.9)
            ASHTREE11_5 = auto.locateOnScreen(
                './assets/fresno/mapas/11/5.png',  confidence=0.9)
            ASHTREE11_6 = auto.locateOnScreen(
                './assets/fresno/mapas/11/6.png',  confidence=0.9)
            ASHTREE11_7 = auto.locateOnScreen(
                './assets/fresno/mapas/11/7.png',  confidence=0.9)
            ASHTREE11_8 = auto.locateOnScreen(
                './assets/fresno/mapas/11/8.png',  confidence=0.9)
            ASHTREE11_9 = auto.locateOnScreen(
                './assets/fresno/mapas/11/9.png',  confidence=0.9)
            ASHTREE11_10 = auto.locateOnScreen(
                './assets/fresno/mapas/11/10.png',  confidence=0.9)
            ASHTREE11_11 = auto.locateOnScreen(
                './assets/fresno/mapas/11/11.png',  confidence=0.9)
            
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)

            if ASHTREE11_1 or ASHTREE11_2:
                clickPosition(ASHTREE11_1 or ASHTREE11_2)

            elif ASHTREE11_4 or ASHTREE11_3:
                clickPosition(ASHTREE11_4 or ASHTREE11_3)

            elif ASHTREE11_5 or ASHTREE11_6:
                clickPosition(ASHTREE11_5 or ASHTREE11_6)

            elif ASHTREE11_7 or ASHTREE11_8:
                clickPosition(ASHTREE11_7 or ASHTREE11_8)

            elif ASHTREE11_9 or ASHTREE11_10:
                clickPosition(ASHTREE11_9 or ASHTREE11_10)

            elif ASHTREE11_11:
                clickPosition(ASHTREE11_11)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break 
      
            else:
                clickToCell(1655, 761, 1, timeClick)
                loop = False