import pyautogui as auto


from movimiento import clickPosition, clickToCell



def map_2(timeClick):

    loop = True
    
    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/2/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE2_1 = auto.locateOnScreen(
                './assets/fresno/mapas/2/1.png',  confidence=0.9)
            ASHTREE2_2 = auto.locateOnScreen(
                './assets/fresno/mapas/2/2.png',  confidence=0.9)
            ASHTREE2_3 = auto.locateOnScreen(
                './assets/fresno/mapas/2/3.png',  confidence=0.9)
            ASHTREE2_4 = auto.locateOnScreen(
                './assets/fresno/mapas/2/4.png',  confidence=0.9)
            ASHTREE2_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/2/v1.png',  confidence=0.9)
            ASHTREE2_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/2/v2.png',  confidence=0.9)
            ASHTREE2_v3 = auto.locateOnScreen(
                './assets/fresno/mapas/2/v3.png',  confidence=0.9)

            INVENTARY_FULL = auto.locateOnScreen(
            "./assets/otros/inventario.png", confidence=0.9)    

            if ASHTREE2_1 or ASHTREE2_2:
                clickPosition(ASHTREE2_1 or ASHTREE2_2)
                
            elif ASHTREE2_3 or ASHTREE2_4:
                clickPosition(ASHTREE2_3 or ASHTREE2_4)

            elif ASHTREE2_v1 or ASHTREE2_v2:
                clickPosition(ASHTREE2_v1 or ASHTREE2_v2)

            elif ASHTREE2_v3:
                clickPosition(ASHTREE2_v3)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario lleno', title='Alerta', button='OK')
                break
                
            else:
                clickToCell(760, 1065, 1, timeClick)
                loop = False
