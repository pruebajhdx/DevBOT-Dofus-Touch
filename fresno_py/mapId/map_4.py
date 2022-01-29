import pyautogui as auto

from movimiento import clickPosition, clickToCell


def map_4(timeClick):

    loop = True

    while loop:

        IDENTIFIED = auto.locateOnScreen(
            './assets/fresno/mapas/4/pos.png',  confidence=0.9)
        
        MOOB_ASHTREE1 = auto.locateOnScreen(
            './assets/fresno/moob/moob1.png', confidence=0.8)
        MOOB_ASHTREE2 = auto.locateOnScreen(
            './assets/fresno/moob/moob2.png', confidence=0.9)
        INVENTARY_FULL = auto.locateOnScreen(
            "./assets/otros/inventario.png", confidence=0.9)
        
        if MOOB_ASHTREE1 or MOOB_ASHTREE2:
            loop = False

        elif IDENTIFIED:

            ASHTREE3_1 = auto.locateOnScreen(
                './assets/fresno/mapas/4/2-2v.png',  confidence=0.9)
            ASHTREE3_2 = auto.locateOnScreen(
                './assets/fresno/mapas/4/3.png',  confidence=0.9)
            ASHTREE3_3 = auto.locateOnScreen(
                './assets/fresno/mapas/4/4.png',  confidence=0.9)
            ASHTREE3_4 = auto.locateOnScreen(
                './assets/fresno/mapas/4/6.png',  confidence=0.9)
            ASHTREE3_5 = auto.locateOnScreen(
                './assets/fresno/mapas/4/7-v6.png',  confidence=0.9)
            ASHTREE3_6 = auto.locateOnScreen(
                './assets/fresno/mapas/4/7.png',  confidence=0.9)
            ASHTREE3_7 = auto.locateOnScreen(
                './assets/fresno/mapas/4/8.png',  confidence=0.9)
            ASHTREE3_8 = auto.locateOnScreen(
                './assets/fresno/mapas/4/9.png',  confidence=0.9)
            ASHTREE3_10 = auto.locateOnScreen(
                './assets/fresno/mapas/4/10.png',  confidence=0.9)
            ASHTREE3_11 = auto.locateOnScreen(
                './assets/fresno/mapas/4/11.png',  confidence=0.9)
            ASHTREE3_12 = auto.locateOnScreen(
                './assets/fresno/mapas/4/12.png',  confidence=0.9)
            ASHTREE3_13 = auto.locateOnScreen(
                './assets/fresno/mapas/4/13-v12.png',  confidence=0.9)
            ASHTREE3_14 = auto.locateOnScreen(
                './assets/fresno/mapas/4/13.png',  confidence=0.9)
            ASHTREE3_15 = auto.locateOnScreen(
                './assets/fresno/mapas/4/14.png',  confidence=0.9)
            ASHTREE3_16 = auto.locateOnScreen(
                './assets/fresno/mapas/4/15.png',  confidence=0.9)
            ASHTREE3_17 = auto.locateOnScreen(
                './assets/fresno/mapas/4/16-v15.png',  confidence=0.9)
            ASHTREE3_18 = auto.locateOnScreen(
                './assets/fresno/mapas/4/17.png',  confidence=0.9)
            ASHTREE3_19 = auto.locateOnScreen(
                './assets/fresno/mapas/4/18.png',  confidence=0.9)
            ASHTREE3_20 = auto.locateOnScreen(
                './assets/fresno/mapas/4/19.png',  confidence=0.9)
            ASHTREE3_21 = auto.locateOnScreen(
                './assets/fresno/mapas/4/20.png',  confidence=0.9)
            ASHTREE3_v1 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v1.png',  confidence=0.9)
            ASHTREE3_v2 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v2.png',  confidence=0.9)
            ASHTREE3_v3 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v3.png',  confidence=0.9)
            ASHTREE3_v4 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v4.png',  confidence=0.9)
            ASHTREE3_v5 = auto.locateOnScreen(
                './assets/fresno/mapas/4/v5.png',  confidence=0.9)

            INVENTARY_FULL = auto.locateOnScreen(
            "./assets/otros/inventario.png", confidence=0.9)

            if ASHTREE3_1 or ASHTREE3_2:
                clickPosition(ASHTREE3_1 or ASHTREE3_2)

            elif ASHTREE3_3 or ASHTREE3_4:
                clickPosition(ASHTREE3_3 or ASHTREE3_4)

            elif ASHTREE3_5 or ASHTREE3_6:
                clickPosition(ASHTREE3_5 or ASHTREE3_6)

            elif ASHTREE3_7 or ASHTREE3_8:
                clickPosition(ASHTREE3_7 or ASHTREE3_8)

            elif ASHTREE3_10 or ASHTREE3_11:
                clickPosition(ASHTREE3_10 or ASHTREE3_11)

            elif ASHTREE3_12 or ASHTREE3_13:
                clickPosition(ASHTREE3_12 or ASHTREE3_13)

            elif ASHTREE3_14 or ASHTREE3_15:
                clickPosition(ASHTREE3_14 or ASHTREE3_15)

            elif ASHTREE3_16 or ASHTREE3_17:
                clickPosition(ASHTREE3_16 or ASHTREE3_17)

            elif ASHTREE3_18 or ASHTREE3_19:
                clickPosition(ASHTREE3_18 or ASHTREE3_19)

            elif ASHTREE3_20 or ASHTREE3_21:
                clickPosition(ASHTREE3_20 or ASHTREE3_21)
            
            elif ASHTREE3_v1 or ASHTREE3_v2:
                clickPosition(ASHTREE3_v1 or ASHTREE3_v2)

            elif ASHTREE3_v3 or ASHTREE3_v4 :
                clickPosition(ASHTREE3_v3 or ASHTREE3_v4)
            
            elif ASHTREE3_v5 :
                clickPosition(ASHTREE3_v5)
            
            elif INVENTARY_FULL:
                auto.click(INVENTARY_FULL, duration=0.1, clicks=0)
                auto.alert(text='Inventario, lleno. Pararé vacía tu inventario.', title='Ups Mensaje de Botus', button='OK')
                break
        
            else:
                clickToCell(167, 167, 1, timeClick)
                loop = False
