import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_10(timeClick):

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/10/pos.png',  confidence=0.9)

        MOOB_ASHTREE10 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE11 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE10 or MOOB_ASHTREE11:
            loop = False    

        elif IDENTIFIED:
            
            ASHTREE10_1 = auto.locateOnScreen(
                './assets/fresno/mapas/10/1.png',  confidence=0.9)
            ASHTREE10_2 = auto.locateOnScreen(
                './assets/fresno/mapas/10/2.png',  confidence=0.9)
            ASHTREE10_3 = auto.locateOnScreen(
                './assets/fresno/mapas/10/3.png',  confidence=0.9)
            ASHTREE10_4 = auto.locateOnScreen(
                './assets/fresno/mapas/10/4.png',  confidence=0.9)
            ASHTREE10_5 = auto.locateOnScreen(
                './assets/fresno/mapas/10/5.png',  confidence=0.9)
            ASHTREE10_6 = auto.locateOnScreen(
                './assets/fresno/mapas/10/6.png',  confidence=0.9)
            ASHTREE10_7 = auto.locateOnScreen(
                './assets/fresno/mapas/10/7.png',  confidence=0.9)
            ASHTREE10_8 = auto.locateOnScreen(
                './assets/fresno/mapas/10/8.png',  confidence=0.9)
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)
       
            if ASHTREE10_2 or ASHTREE10_1 :
                clickPosition(ASHTREE10_2 or ASHTREE10_1 )

            elif ASHTREE10_4 or ASHTREE10_3:
                clickPosition(ASHTREE10_4 or ASHTREE10_3)

            elif ASHTREE10_5 or ASHTREE10_6:
                clickPosition(ASHTREE10_5 or ASHTREE10_6)

            elif ASHTREE10_7 or ASHTREE10_8:
                clickPosition(ASHTREE10_7 or ASHTREE10_8)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break
                
            else:
                clickToCell(1591, 405, 1, timeClick)
                loop = False