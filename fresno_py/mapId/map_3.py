import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_3(timeClick):

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/3/pos.png',  confidence=0.9)
        
        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9) 
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE3_1 = auto.locateOnScreen(
                './assets/fresno/mapas/3/1.png',  confidence=0.9)
            ASHTREE3_2 = auto.locateOnScreen(
                './assets/fresno/mapas/3/2.png',  confidence=0.9)
            
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)

            if ASHTREE3_1 or ASHTREE3_2:
                clickPosition(ASHTREE3_1 or ASHTREE3_2)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break

            else:
                clickToCell(190, 698, 1, timeClick)
                loop = False
