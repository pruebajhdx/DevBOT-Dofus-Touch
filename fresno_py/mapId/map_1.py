import pyautogui as auto


from movimiento import clickPosition, clickToCell


def map_1():

    loop = True
     # Fresno MOOB
     
    MOOB_ASHTREE1 = auto.locateOnScreen(
        './assets/fresno/moob/moob1.png', confidence=0.8)
    MOOB_ASHTREE2 = auto.locateOnScreen(
        './assets/fresno/moob/moob2.png', confidence=0.9)
    
    if MOOB_ASHTREE1 or MOOB_ASHTREE2:
        loop = False
    
    while loop:

        ASHTREE1_1 = auto.locateOnScreen(
            './assets/fresno/mapas/1/1.png',  confidence=0.9)
        ASHTREE1_2 = auto.locateOnScreen(
            './assets/fresno/mapas/1/2.png',  confidence=0.9)
        ASHTREE1_3 = auto.locateOnScreen(
            './assets/fresno/mapas/1/3.png',  confidence=0.9)
        ASHTREE1_4 = auto.locateOnScreen(
            './assets/fresno/mapas/1/5.png',  confidence=0.9)
        ASHTREE1_r5 = auto.locateOnScreen(
            './assets/fresno/mapas/1/4.png',  confidence=0.9)
        ASHTREE1_5 = auto.locateOnScreen(
            './assets/fresno/mapas/1/7.png',  confidence=0.9)
        ASHTREE1_6 = auto.locateOnScreen(
            './assets/fresno/mapas/1/9.png',  confidence=0.9)
        ASHTREE1_7 = auto.locateOnScreen(
            './assets/fresno/mapas/1/10.png',  confidence=0.9)
        ASHTREE1_8 = auto.locateOnScreen(
            './assets/fresno/mapas/1/11.png',  confidence=0.9)
        ASHTREE1_9 = auto.locateOnScreen(
            './assets/fresno/mapas/1/12.png',  confidence=0.9)
        ASHTREE1_10 = auto.locateOnScreen(
            './assets/fresno/mapas/1/13.png',  confidence=0.9)
        ASHTREE1_11 = auto.locateOnScreen(
            './assets/fresno/mapas/1/14.png',  confidence=0.9)
        ASHTREE1_v1 = auto.locateOnScreen(
            './assets/fresno/mapas/1/v1.png',  confidence=0.9)
        ASHTREE1_v2 = auto.locateOnScreen(
            './assets/fresno/mapas/1/v2.png',  confidence=0.9)
        ASHTREE1_v3 = auto.locateOnScreen(
            './assets/fresno/mapas/1/v3.png',  confidence=0.9)
 

        if ASHTREE1_1 or ASHTREE1_2:
            clickPosition(ASHTREE1_1 or ASHTREE1_2)

        elif ASHTREE1_3 or ASHTREE1_4:
            clickPosition(ASHTREE1_3 or ASHTREE1_4)

        elif ASHTREE1_5 or ASHTREE1_6:
            clickPosition(ASHTREE1_5 or ASHTREE1_6)

        elif ASHTREE1_7 or ASHTREE1_8:
            clickPosition(ASHTREE1_7 or ASHTREE1_8)

        elif ASHTREE1_9 or ASHTREE1_10:
            clickPosition(ASHTREE1_9 or ASHTREE1_10)

        elif ASHTREE1_11 or ASHTREE1_r5:
            clickPosition(ASHTREE1_11 or ASHTREE1_r5)
        
        elif ASHTREE1_v1 or ASHTREE1_v2:
            clickPosition(ASHTREE1_v1 or ASHTREE1_v2)
            
        elif ASHTREE1_v3:
            clickPosition(ASHTREE1_v3)

        else:
            clickToCell(163, 514, 1, 3)
            loop = False
