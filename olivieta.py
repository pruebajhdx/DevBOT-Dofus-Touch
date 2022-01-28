from ashtree import clickPosition, clickToCell
import pyautogui as auto
import time

farm = True
death = False

# Moverse en el camino sombrio

def moveToMapGhost(mapId):
    if mapId == 1:
        clickToCell(796, 63)
    elif mapId == 2:
        clickToCell(1648, 607)
    return


def moveToMapGloomyRoad(mapId):
    if mapId == 1:
        clickToCell(148, 514)
    elif mapId == 2:
        clickToCell(156, 526)
    elif mapId == 3:
        clickToCell(154, 568)
    elif mapId == 4:
        clickToCell(1157, 41)
    elif mapId == 5:
        clickToCell(1418, 73)
    elif mapId == 6:
        clickToCell(894, 48)
    elif mapId == 7:
        clickToCell(1157, 41)
    elif mapId == 8:
        clickToCell(1157, 41)
    elif mapId == 9:
        clickToCell(1182, 1058)
    elif mapId == 10:
        clickToCell(1182, 1058)
    elif mapId == 11:
        clickToCell(1182, 1058)
    elif mapId == 12:
        clickToCell(1182, 1058)
    elif mapId == 13:
        clickToCell(1182, 1058)
    elif mapId == 14:
        clickToCell(1182, 1058)
    elif mapId == 15:
        clickToCell(1182, 1058)
    return mapId

def mapGloomyRoad(mapId):


    """ MAPA1 = auto.locateOnScreen('assets/olivieta/mapa/mapa1.png',  confidence=0.7)
    MAPA2 = auto.locateOnScreen('assets/olivieta/mapa/mapa2.png',  confidence=0.5)
    MAPA3 = auto.locateOnScreen('assets/olivieta/mapa/mapa3.png',  confidence=0.9)
    MAPA4 = auto.locateOnScreen('assets/olivieta/mapa/mapa4.png',  confidence=0.6)
    MAPA5 = auto.locateOnScreen('assets/olivieta/mapa/mapa5.png',  confidence=0.5)
    MAPA6 = auto.locateOnScreen('assets/olivieta/mapa/mapa6.png',  confidence=0.6)
    MAPA7 = auto.locateOnScreen('assets/olivieta/mapa/mapa7.png',  confidence=0.4)
    MAPA8 = auto.locateOnScreen('assets/olivieta/mapa/mapa8.png',  confidence=0.7) """

    #MAPA2 = auto.locateOnScreen('assets/olivieta/mapa/mapatest3.png',  confidence=0.9)

    if mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm) 
    elif mapId:
        moveToMapGloomyRoad(mapId)
        moveToFarm(farm)     
   
    moveToFarm(farm) 

    return mapId
 


def toDead(death):

    mapNext = 0
    uniqueClick = 0
    
    while death:

        LEAVE = auto.locateOnScreen('assets/abandono/abandonar.png', confidence=0.9)
        LEAVE_YES = auto.locateOnScreen('assets/abandono/abandonarsi.png', confidence=0.9)
        MSG_OK = auto.locateOnScreen('assets/abandono/ok.png', confidence=0.8)
        INTERFACE_X = auto.locateOnScreen('assets/abandono/x.png', confidence=0.8)
        FENIX = auto.locateOnScreen('assets/olivieta/fenix.png', confidence=0.8)
        POTION = auto.locateOnScreen('assets/fresno/pocima.png', confidence=0.7)

        if LEAVE and uniqueClick <= 1:
            uniqueClick += 1
            clickPosition(LEAVE)
        elif LEAVE_YES:
            clickPosition(LEAVE_YES)
        elif MSG_OK or INTERFACE_X:
            clickPosition(MSG_OK or INTERFACE_X)
        elif FENIX:
            clickPosition(FENIX)
            time.sleep(7)
            if POTION:
                auto.doubleClick(POTION, duration=0.1)
                death = False
                farm = True
                moveToFarm(farm)
        else:
            mapNext += 1
            print('ghostID', mapNext)
            moveToMapGhost(mapNext)
            time.sleep(5)

    return death


def moveToFarm(farm):
    mapId = 0

    while farm:

        OLIVIETE1 = auto.locateOnScreen('assets/olivieta/olivieta1.png',  confidence=0.8)
        OLIVIETE2 = auto.locateOnScreen('assets/olivieta/olivieta2.png',  confidence=0.5)
        OLIVIETE3 = auto.locateOnScreen('assets/olivieta/olivieta3.png',  confidence=0.5)
        OLIVIETE4 = auto.locateOnScreen('assets/olivieta/olivieta4.png',  confidence=0.9)
        OLIVIETE5 = auto.locateOnScreen('assets/olivieta/olivieta5.png',  confidence=0.9)
        OLIVIETE6 = auto.locateOnScreen('assets/olivieta/olivieta6.png',  confidence=0.9)
        OLIVIETE7 = auto.locateOnScreen('assets/olivieta/olivieta7.png',  confidence=0.9)
        OLIVIETE8 = auto.locateOnScreen('assets/olivieta/olivieta8.png',  confidence=0.9)
        OLIVIETE9 = auto.locateOnScreen('assets/olivieta/olivieta9.png',  confidence=0.9)
        OLIVIETE10 = auto.locateOnScreen('assets/olivieta/olivieta10.png',  confidence=0.5)
        OLIVIETE11 = auto.locateOnScreen('assets/olivieta/olivieta10.png',  confidence=0.9)

        MOOB1 = auto.locateOnScreen('assets/olivieta/moob1.png',  confidence=0.9)
        MOOB2 = auto.locateOnScreen('assets/olivieta/moob2.png',  confidence=0.9)

        
        if OLIVIETE1 or OLIVIETE2:
            clickPosition(OLIVIETE1 or OLIVIETE2)
        
        elif OLIVIETE3 or OLIVIETE4:
            clickPosition(OLIVIETE3 or OLIVIETE4)
        
        elif OLIVIETE5 or OLIVIETE6:
            clickPosition(OLIVIETE5 or OLIVIETE6)
       
        elif OLIVIETE7 or OLIVIETE8:
            clickPosition(OLIVIETE7 or OLIVIETE8)
       
        elif OLIVIETE9 or OLIVIETE10:
            clickPosition(OLIVIETE9 or OLIVIETE10)    
        
        elif OLIVIETE11 or OLIVIETE10:
            clickPosition(OLIVIETE11 or OLIVIETE10)   
        
        elif MOOB1 or MOOB2:
            farm = False
            death = True
            toDead(death)

        else:
            mapId = mapId + 1
            if mapId >= 15:
                mapId = 0
            else:
                print('Farm mapID: ', mapId)
                mapGloomyRoad(mapId)
        time.sleep(15)

        #print(auto.position())

        

if __name__ == "__main__":
    moveToFarm(farm)
    #print(auto.getAllWindows())
