import pyautogui as auto


from movimiento import clickPosition, clickToCell



def map_12(timeClick):

    loop = True
    
    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/12/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE12 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE12:
            loop = False

        elif IDENTIFIED:

            ASHTREE12_1 = auto.locateOnScreen(
                './assets/fresno/mapas/12/1.png',  confidence=0.9)
            ASHTREE12_2 = auto.locateOnScreen(
                './assets/fresno/mapas/12/2.png',  confidence=0.9)
            ASHTREE12_4 = auto.locateOnScreen(
                './assets/fresno/mapas/12/4.png',  confidence=0.9)
            ASHTREE12_5 = auto.locateOnScreen(
                './assets/fresno/mapas/12/5.png',  confidence=0.9)
            ASHTREE12_6 = auto.locateOnScreen(
                './assets/fresno/mapas/12/6.png',  confidence=0.9)
            INVENTARY_FULL = auto.locateOnScreen(
                "./assets/otros/inventario.png", confidence=0.9)
        

            if ASHTREE12_1 or ASHTREE12_2:
                clickPosition(ASHTREE12_1 or ASHTREE12_2)
                
            elif ASHTREE12_4:
                clickPosition(ASHTREE12_4)

            elif ASHTREE12_5 or ASHTREE12_6:
                clickPosition(ASHTREE12_5 or ASHTREE12_6)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break
                    
            else:
                clickToCell(1598, 452, 1, timeClick)
                loop = False
