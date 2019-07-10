import random, pygame, sys,os
from pygame import *
from random import *
from sys import *

def end():
  pygame.quit()
  sys.exit()

def spawn(you,location):
  you[0],you[1] = location


def level_up():
  global level,blocks
  if level < len(blocks)-1:
    level += 1
  spawn(you)

def start():
  global FPS,fpsClock,DISPLAY,you,stone,char1,char2,bounce,bounce2,you2
  pygame.init()
  FPS = 30
  fpsClock = pygame.time.Clock()
  DISPLAY = pygame.display.set_mode((1200,700),FULLSCREEN)
  you,you2 = [0,0],[0,0]
  stone = pygame.image.load("Block.png").convert_alpha()
  char1 = pygame.image.load("your.png").convert_alpha()
  char2 = pygame.image.load("youb.png").convert_alpha()
  bounce = pygame.image.load("bounce.png").convert_alpha()
  bounce2 = pygame.image.load("bounce2.png").convert_alpha()

def run():
  global FPS,fpsClock,DISPLAY,you,you2,blocks,level
  velocity_x = 0
  velocity_y = 0
  col1 = (0,0,255)
  col2 = (255,0,0)
  velocity_x2 = 0
  velocity_y2 = 0
  spawn(you,(100,350))
  spawn(you2,(990,350))
  shots = []
  gravity = True
  jump = False
  ap,dp = False,False
  ap2,dp2 = False,False
  floored = False
  floored2 = False
  level = 0
  blocks = [[[0,600,1200,40,0],[0,590,50,10,2],[1150,590,50,10,2],[300,350,60,20,2],[900,350,60,20,2],[590,540,20,60,2],[400,400,150,20,1],[650,400,150,20,1],[0,220,150,20,0],[1050,220,150,20,0],[500,200,200,10,0]]]

  while True:
    DISPLAY.fill((0,0,0))

    you[1] += velocity_y
    you[0] += velocity_x

    you2[1] += velocity_y2
    you2[0] += velocity_x2

    if you[1] > 850:
      velocity_y = 0
      velocity_x = 0
      spawn(you,(100,350))
    if you2[1] > 850:
      velocity_y2 = 0
      velocity_x2 = 0
      spawn(you2,(1100,350))
    
    if gravity and not floored:
      velocity_y += 0.4
    floored = False
    for floor in blocks[level]:
      if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x > 0 and floor[0]+7>you[0]+15>floor[0]:
        velocity_x = -velocity_x
        you[0] -= 7
        if floor[4] == 1 or floor[4] == 2:
          velocity_y -= 9
      if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x < 0 and floor[0]+floor[2]-7<you[0]<floor[0]+floor[2]:
        velocity_x = -velocity_x
        you[0] += 7
        if floor[4] == 1 or floor[4] ==  2:
          velocity_y -= 9
      if floor[1]<you[1]<floor[1]+floor[3] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2] and velocity_y > 0:
        you[1] = floor[1]
        if floor[4] == 1:
          velocity_y = -0.9*velocity_y
        elif floor[4] == 2:
          velocity_y = -16
      if floor[1]<you[1]-15<floor[1]+floor[3] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2] and velocity_y < 0:
        you[1] = floor[1]+floor[3]+15
        velocity_y = 0
      if you[1] == floor[1] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2]:
        if floor[4]!=1 and floor[4]!= 2:
          velocity_y = 0
          floored = True
          
    if gravity and not floored2:
      velocity_y2 += 0.4
      
    floored2 = False
    for floor in blocks[level]:
      if floor[1]<you2[1]-1<floor[1]+floor[3] and velocity_x2 > 0 and floor[0]+7>you2[0]+15>floor[0]:
        velocity_x2 = -velocity_x2
        you2[0] -= 7
        if floor[4] == 1 or floor[4] == 2:
          velocity_y2 -= 9
      if floor[1]<you2[1]-1<floor[1]+floor[3] and velocity_x2 < 0 and floor[0]+floor[2]-7<you2[0]<floor[0]+floor[2]:
        velocity_x2 = -velocity_x2
        you2[0] += 7
        if floor[4] == 1 or floor[4] ==  2:
          velocity_y2 -= 9
      if floor[1]<you2[1]<floor[1]+floor[3] and floor[0]<you2[0]+15 and you2[0]<floor[0]+floor[2] and velocity_y2 > 0:
        you2[1] = floor[1]
        if floor[4] == 1:
          velocity_y2 = -0.9*velocity_y2
        elif floor[4] == 2:
          velocity_y2 = -16
      if floor[1]<you2[1]-15<floor[1]+floor[3] and floor[0]<you2[0]+15 and you2[0]<floor[0]+floor[2] and velocity_y2 < 0:
        you2[1] = floor[1]+floor[3]+15
        velocity_y2 = 0
      if you2[1] == floor[1] and floor[0]<you2[0]+15 and you2[0]<floor[0]+floor[2]:
        if floor[4]!=1 and floor[4]!= 2:
          velocity_y2 = 0
          floored2 = True
          
    for shot in shots:
      shot[0] += shot[2]*7
      pygame.draw.circle(DISPLAY,shot[3],(int(shot[0]),int(shot[1])),3)
      for floor in blocks[level]:
        if floor[0]<shot[0]<floor[0]+floor[2] and floor[1]<shot[1]<floor[1]+floor[3]:
          shots.pop(shots.index(shot))
      if you[0]<shot[0]<you[0]+15 and you[1]-15<shot[1]<you[1]:
        if shot[3] == col1:
          spawn(you,(100,350))
      if you2[0]<shot[0]<you2[0]+15 and you2[1]-15<shot[1]<you2[1]:
        if shot[3] == col2:
          spawn(you2,(1100,350))
      

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          end()
        if event.key == K_a:
          ap = True
        if event.key == K_d:
          dp = True
        if event.key == K_s:
          if you[0] - you2[0] < 0:
            d = 1
          else:
            d = -1
          shots.append([you[0],you[1]-7,d,col2])
        if event.key == K_DOWN:
          if you2[0] - you[0] < 0:
            d = 1
          else:
            d = -1
          shots.append([you2[0],you2[1]-7,d,col1])
        if event.key == K_w and floored:
          velocity_y -= 7
        if event.key == K_LEFT:
          ap2 = True
        if event.key == K_RIGHT:
          dp2 = True
        if event.key == K_UP and floored2:
          velocity_y2 -= 7
      if event.type == KEYUP:
        if event.key == K_a:
          ap = False
        if event.key == K_d:
          dp = False
        if event.key == K_LEFT:
          ap2 = False
        if event.key == K_RIGHT:
          dp2 = False
      
    if ap:
      velocity_x -= 0.2
    elif velocity_x < 0:
      velocity_x += 0.2
    if dp:
      velocity_x += 0.2
    elif velocity_x > 0:
      velocity_x -= 0.2

    if velocity_x > 5:
      velocity_x = 5
    if velocity_x < -5:
      velocity_x = -5

    if ap2:
      velocity_x2 -= 0.2
    elif velocity_x2 < 0:
      velocity_x2 += 0.2
    if dp2:
      velocity_x2 += 0.2
    elif velocity_x2 > 0:
      velocity_x2 -= 0.2

    if velocity_x2 > 5:
      velocity_x2 = 5
    if velocity_x2 < -5:
      velocity_x2 = -5

    for floor in blocks[level]:
      y = 0
      x = 0
      for i in range((int(floor[2]/10))*(int(floor[3]/10))):
        if floor[4] == 0:
          DISPLAY.blit(stone,(floor[0]+x,floor[1]+y))
        elif floor[4] == 1:
           DISPLAY.blit(bounce,(floor[0]+x,floor[1]+y))
        elif floor[4] == 2:
          DISPLAY.blit(bounce2,(floor[0]+x,floor[1]+y))
        x+=10
        if x == floor[2]:
          y+=10
          x = 0

    
    
    if not 1170>you[0]>0:
      velocity_x = -velocity_x
    if not 1170>you2[0]>0:
      velocity_x2 = -velocity_x2
    DISPLAY.blit(char1,(int(you[0]),int(you[1])-15))
    DISPLAY.blit(char2,(int(you2[0]),int(you2[1])-15))

         
    pygame.display.update()
    fpsClock.tick(FPS) 

start()
run()
