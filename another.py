import pygame as pgame
import random
import time

aaa = pgame.init()
clock = pgame.time.Clock()
mainW = 600
mainH = 500
white = (255,255,255)
red = (255,20,0)
blue = (0,0,255)

redBall = (218,62,62)
blueBall = (95,117,211)

darkredBall = (123,18,18)
darkblueBall = (4,10,38)

green = (0,200,0)
black = (0,0,0)
mainCol = (221,234,171)
fps = 20
carW = 30
carH = 30
ballW = 20
ballH = 20
contW = 180
contH = 300
blockW =  32
blockH = 10

#Container position definition
contPosX = mainW/2-contW/2
contPosY = mainH/2-contH/2

#initial positions of cars
aIniPosX = contPosX + 10
aIniPosY = contPosY + contH - (carH + 10)
bIniPosX = mainW/2+ 20

redBlock0 = contPosX+5
redBlock1 = contPosX+blockW+15
blueBlock0 = mainW/2+15
blueBlock1 = mainW/2+blockW+25

mainSr = pgame.display.set_mode((mainW,mainH))
pgame.display.set_caption("Blocking Blocks")

font = pgame.font.SysFont(None,25)
largeFont = pgame.font.SysFont(None,45)

def showMsg(text,col,placing = [ mainW/2,mainH/2 ],size = font):
    msg = size.render(text,True,col)
    msgBox = msg.get_rect()
    msgBox.center = placing[0],placing[1]
    mainSr.blit(msg,msgBox)

def checkThis(block,xCo,yCo):
    if xCo >= block[1] and xCo <= block[1] + blockW:
       if yCo >= block[2] and yCo < block[2] + blockH:
           return True
    return False
    
def pause():
    paused = True
    showMsg("Paused",black,size = largeFont)
    showMsg("'C' to continue or 'Q' to quit",black,[mainW/2,mainH/2+25])
    pgame.display.update()
    while paused:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            elif event.type == pgame.KEYDOWN:
                if event.key == pgame.K_c:
                    paused = False
                    break
                elif event.key == pgame.K_q:
                    main()

def gameLoop():
    gameExit = False
    gameOver = False
    aCarPosX = aIniPosX
    aCarPosY = aIniPosY
    bCarPosX = bIniPosX
    bCarPosY = aCarPosY
    flagA = True
    flagB = True
    totalBall = 0
    level = 1
    totalCol = 0
    countSec = 0
    blockList = []
    while not gameExit:
        while gameOver == True:
            showMsg("Game Over, you!! Press 'P' to play again or 'Q' to quit",red,[mainW/2,mainH-50])
            pgame.display.update()
            
            for event in pgame.event.get():
                if event.type == pgame.QUIT:
                        gameExit = True
                        gameOver = False
                        break
                if event.type == pgame.KEYDOWN:
                    if event.key == pgame.K_q:
                        main()
                    elif event.key == pgame.K_p:
                        gameLoop()
        if gameExit:
            continue
        
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                gameExit = True
                break
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_LEFT:
                    if flagA:
                        aCarPosX += carW
                        flagA = False
                    else:
                        aCarPosX -= carW
                        flagA = True
                if event.key == pgame.K_RIGHT:
                    if flagB:
                        bCarPosX += carW
                        flagB = False
                    else:
                        bCarPosX -= carW
                        flagB = True
                if event.key == pgame.K_p:
                    pause()
                
        mainSr.fill(white)
        
        #A kind of legend
        showMsg("To be Avoided: ",green,[mainW-100,mainH/2 - 50])  
        mainSr.fill(darkredBall,rect = [mainW-130,mainH/2-25,ballW,ballH])
        mainSr.fill(darkblueBall,rect = [mainW-100,mainH/2-25,ballW,ballH])

        
        mainSr.fill(mainCol,rect = [contPosX,contPosY,contW,contH])
        mainSr.fill(black,rect = [mainW/2-10,contPosY,20,contH])
        
        thisBlock = []
        if countSec == 3*fps/4:
            countSec = 0
            ran = int(random.randrange(0,4))
            #to give the block or not
            if ran != 0:
                #to give in blue or red or both
                ran = int(random.randrange(0,3))
                if ran == 0:
                    thisBlock.append(darkredBall)
                    ran = int(random.randrange(0,2))
                    #to give in which track
                    if ran == 0:
                        thisBlock.append(redBlock0)
                    else:
                        thisBlock.append(redBlock1)
                    thisBlock.append(contPosY-blockH)
                    blockList.append(thisBlock)
                elif ran == 1:
                    thisBlock.append(darkblueBall)
                    ran = int(random.randrange(0,2))
                    #to give in which track
                    if ran == 0:
                        thisBlock.append(blueBlock0)
                    else:
                        thisBlock.append(blueBlock1)
                    thisBlock.append(contPosY-blockH)
                    blockList.append(thisBlock)    
                else:
                    thisBlock.append(darkredBall)
                    ran = int(random.randrange(0,2))
                    #to give in which track
                    if ran == 0:
                        thisBlock.append(redBlock0)
                    else:
                        thisBlock.append(redBlock1)
                    thisBlock.append(contPosY-blockH)
                    blockList.append(thisBlock)

                    
                    thisBlock = []
                    thisBlock.append(darkblueBall)
                    ran = int(random.randrange(0,2))
                    #to give in which track
                    if ran == 0:
                        thisBlock.append(blueBlock0)
                    else:
                        thisBlock.append(blueBlock1)
                    thisBlock.append(contPosY-blockH)
                    blockList.append(thisBlock)

        count = 0
        for block in reversed(blockList):
            if block[2] >= contPosY + contH :
                break
            mainSr.fill(block[0],rect = [block[1],block[2],blockW,blockH])
            block[2] += 5 
            count += 1

        score = len(blockList) - count
        level = int(score/20) + 1
        showMsg("Be Honest, Play Alone !!",green,[mainW/2,50])
        #msgShow("Level : " + str(level),green,[100,mainH/2 - 50])
        showMsg("Score : " + str(score),green,[100,mainH/2])
                
        for block in reversed(blockList):
            if block[2] > contPosY + contH :
                break
            
            if block[0] == darkredBall:
                if checkThis(block,aCarPosX,aCarPosY):
                    gameOver = True
                    break
                elif checkThis(block,aCarPosX+carW,aCarPosY):
                    gameOver = True
                    break
                elif checkThis(block,aCarPosX,aCarPosY+carH):
                    gameOver = True
                    break
                elif checkThis(block,aCarPosX+carW,aCarPosY+carH):
                    gameOver = True
                    break
            else:
                if checkThis(block,bCarPosX,bCarPosY):
                    gameOver = True
                    break
                elif checkThis(block,bCarPosX+carW,bCarPosY):
                    gameOver = True
                    break
                elif checkThis(block,bCarPosX,bCarPosY+carH):
                    gameOver = True
                    break
                elif checkThis(block,bCarPosX+carW,bCarPosY+carH):
                    gameOver = True
                    break
        
        countSec += 1
        mainSr.fill(red,rect = [aCarPosX,aCarPosY,carW,carH])
        mainSr.fill(blue,rect = [bCarPosX,bCarPosY,carW,carH])
        pgame.display.update()
        clock.tick(fps)
    pgame.quit()
    quit()

def main():
    mainSr.fill(white)
    showMsg("Go Thru !!",green,[mainW/2,mainH/2-150])
    showMsg("Press 'P' to begin gameplay or 'E' to Exit.",green,[mainW/2,mainH/2-125])
    showMsg("During gameplay press 'P' to pause",green,[mainW/2,mainH/2-100])
    
    #Controls
    showMsg("Controls",black)
    showMsg("Press 'Left' to control red and 'Right' for blue",black,[mainW/2,mainH/2+100])
    showMsg("by kishanp",red,[mainW/2,mainH-75])
    pgame.display.update()
    
    while True:
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                pgame.quit()
                quit()
            if event.type == pgame.KEYDOWN:
                if event.key == pgame.K_p:
                    gameLoop()
                elif event.key == pgame.K_e:
                    mainSr.fill(white)
                    showMsg("Good Bye",red)
                    pgame.display.update()
                    pgame.quit()
                    quit()

if __name__ == "__main__": main()


