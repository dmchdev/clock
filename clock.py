#!/usr/bin/env Python
"""This is a program that displays time on screen by drawing a mechanical clock.
Pygame module must be installed in order for it to work."""
import sys, time, pygame, math
#-------DEFINITIONS
bg = pygame.image.load('clock.jpg')
Rs = 220 #Radius of seconds hand
Rm = 220
Rh = 180
hourPos = [] #all possible tip positions for clock hands are preloaded into lists
minPos = []
secPos = []
def getHour():
    curHour = time.strftime("%I") #this extracts hours from system time
    return curHour
def getMin():
    curMin = time.strftime("%M")
    return curMin
def getSec():
    curSec = time.strftime("%S")
    return curSec

#----------LOADING
#using trigonometric functions and degree to radian conversions to load proper coordinates into
#lists. Each list position is itself a list of x and y coordinates.
for s in range (0,60):
    pos = [int(math.cos(math.radians(s*6+270))*Rs+330),int(math.sin(math.radians(s*6+270))*Rs+330)]
    secPos.append(pos)
for m in range (0,60):
    pos = [math.cos(math.radians(m*6+270))*Rm+330,math.sin(math.radians(m*6+270))*Rm+330]
    minPos.append(pos)
for h in range (0,60):
    pos = [math.cos(math.radians(h*6+270))*Rh+330,math.sin(math.radians(h*6+270))*Rh+330]
    hourPos.append(pos)
#----------EXECUTION
pygame.init()
screen = pygame.display.set_mode([660, 660])

#print datetime.datetime.today()
while True:
    if int(getHour())==12: #hour hand setting from system time
        hourX = hourPos[0*5 + int(int(getMin())/12)][0]
        hourY = hourPos[0*5 + int(int(getMin())/12)][1]
    else:
        hourX = hourPos[int(getHour())*5 + int(int(getMin())/12)][0] #because list indices must be integers and
        hourY = hourPos[int(getHour())*5 + int(int(getMin())/12)][1] #and getMin method returns a string which needs to be converted to integer first
    
    minX = minPos[int(getMin())][0] #minute and seconds setting from system time
    minY = minPos[int(getMin())][1]
    secX = secPos[int(getSec())][0]
    secY = secPos[int(getSec())][1]
#doube-buffering the screen before displaying
    screen.blit(bg, [0,0])
    pygame.draw.line(screen,[0,0,0],(330,330),(hourX,hourY),15)
    pygame.draw.line(screen,[0,0,0],(330,330),(minX,minY),10)
    
    #print secX, secY
    pygame.draw.circle(screen,[0,0,0],(330,330),30,0)
    pygame.draw.circle(screen,[255,0,0],(330,330),20,0)
    pygame.draw.line(screen,[255,0,0],(330,330),(secX,secY),10)
    #pygame.draw.circle(screen,[255,0,0],(secX,secY),4,0)
    font = pygame.font.Font(None, 30)
    dateStamp = font.render(getHour()+':'+getMin()+':'+getSec(), 1, (255,255,255))
    pygame.draw.rect(screen, [0,0,50],(20,20,90,30),0)
    screen.blit(dateStamp, [22,22])
#displaying screen
    pygame.display.flip()
    time.sleep(1) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()