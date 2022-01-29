import pyautogui as auto


from movimiento import clickPosition, clickToCell



def map_13(timeClick):

    loop = True
    
    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/13/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE13 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE13:
            loop = False

        elif IDENTIFIED:

            ASHTREE13_1 = auto.locateOnScreen(
                './assets/fresno/mapas/13/1.png',  confidence=0.9)
            ASHTREE13_2 = auto.locateOnScreen(
                './assets/fresno/mapas/13/2.png',  confidence=0.9)
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)
           
            if ASHTREE13_1 or ASHTREE13_2:
                clickPosition(ASHTREE13_1 or ASHTREE13_2)

            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break

            else:
                clickToCell(1407, 49, 1, timeClick)
                loop = False
