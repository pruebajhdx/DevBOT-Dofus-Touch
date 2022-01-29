import pyautogui as auto


from movimiento import clickPosition, clickToCell



def map_2():

    loop = True

    
    
    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/8/pos.png',  confidence=0.9)

        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE8_1 = auto.locateOnScreen(
                './assets/fresno/mapas/8/1.png',  confidence=0.9)
            ASHTREE8_2 = auto.locateOnScreen(
                './assets/fresno/mapas/8/2.png',  confidence=0.9)
            ASHTREE8_3 = auto.locateOnScreen(
                './assets/fresno/mapas/8/3.png',  confidence=0.9)
            ASHTREE8_4 = auto.locateOnScreen(
                './assets/fresno/mapas/8/4.png',  confidence=0.9)
            ASHTREE8_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/8/v1.png',  confidence=0.9)
            ASHTREE8_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/8/v2.png',  confidence=0.9)

            if ASHTREE8_1 or ASHTREE8_2:
                clickPosition(ASHTREE8_1 or ASHTREE8_2)
                
            elif ASHTREE8_3 or ASHTREE8_4:
                clickPosition(ASHTREE8_3 or ASHTREE8_4)

            elif ASHTREE8_v1 or ASHTREE8_v2:
                clickPosition(ASHTREE8_v1 or ASHTREE8_v2)
            
            else:
                clickToCell(1582, 498, 1, 3)
                loop = False
