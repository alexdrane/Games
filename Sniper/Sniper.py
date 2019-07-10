import pygame, sys
from pygame.locals import *
import random
from random import *

pygame.init()

class enemy(object):
  pos_x = 0
  pos_y = 0
  clock = 150
  def __init__(self,pos_x,pos_y):
    self.pos_x = pos_x
    self.pos_y = pos_y
      
    
enemy_list = []
timers = []
myfont = pygame.font.SysFont('Comic Sans MS', 10)
clock = 0
FPS = 30
d = 15
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1200,600))
pygame.display.set_caption("SAS Dude")
die = False
t = 150
timer = 0
pygame.mouse.set_visible( False )
while True:
  DISPLAYSURF.fill((240,240,240))
  mx,my = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  c = 0
  g = None
  for enemy in enemy_list:
    if click[0] == 1:
      if enemy[0]<=mx<=enemy[0]+enemy[3] and enemy[1]<=my<=enemy[1]+enemy[3]:
        enemy_list.pop(c)
    c+=1

    
  clock +=1
  if timer < 0:
    timer = 0
  if clock == 100:
    for i in enemy_list:
      i[2] -= 1
      if i[2] == 0:
        die == True
  if clock == t:
    for i in range(randint(1,2)):
      n = [randint(10,1170),randint(10,570),randint(8,25)]
      if n[0] <  260 and n[1] < 140:
        n[0] += 260
        n[1] += 140
      enemy_list.append(n)
    clock = 0
    d -= 1
    if d < 6:
      d = 6
    t -= 5
    if t < 60:
      t = 60

  
  if die == False:
    for enemy in enemy_list:
      pygame.draw.rect(DISPLAYSURF,(255,0,0),(enemy[0],enemy[1],enemy[3],enemy[3]))
      pygame.draw.line(DISPLAYSURF, (255,0,0), (enemy[0]+int(enemy[3]/2),enemy[1]+enemy[3]), (enemy[0]+int(enemy[3]/2),enemy[1]+enemy[3]*1.3), 2)
      pygame.draw.line(DISPLAYSURF, (255,0,0), (enemy[0]+int(enemy[3]/2),enemy[1]+enemy[3]*1.3), (enemy[0]+int(enemy[3]*0.8),enemy[1]+enemy[3]*2), 2)
      pygame.draw.line(DISPLAYSURF, (255,0,0), (enemy[0]+int(enemy[3]/2),enemy[1]+enemy[3]*1.3), (enemy[0]+int(enemy[3]*0.2),enemy[1]+enemy[3]*2), 2)
      pygame.draw.line(DISPLAYSURF, (0,0,0), (enemy[0]+int(enemy[3]*0.9),enemy[1]+enemy[3]), (enemy[0],enemy[1]+enemy[3]*1.3), 4)
      textsurface = myfont.render(str(enemy[2]), False, (0, 0, 0))
      DISPLAYSURF.blit(textsurface,(enemy[0]+enemy[3],enemy[1]+enemy[3]))
         
    if timer > 0:
      pygame.draw.circle(DISPLAYSURF, (100,100,100,100), (mx,my), 53)
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx,my-100,1,200))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-100,my,200,1))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-3,my+10,6,1))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-3,my+20,6,1))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-3,my+40,6,1))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-3,my+30,6,1))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-10,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-30,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-20,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx-40,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx+30,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx+20,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx+40,my-3,1,6))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(mx+10,my-3,1,6))
    pygame.draw.circle(DISPLAYSURF, (0,0,0), (mx,my), 300,203)
    pygame.draw.rect(DISPLAYSURF,(0,0,0),(mx-1200,my-1200,2400,2400),2200)
    
    pygame.draw.rect(DISPLAYSURF,(0,0,0),(8,8,244,124),4)
    pygame.draw.rect(DISPLAYSURF,(255,255,255),(10,10,240,120))
    for enemy in enemy_list:
      pygame.draw.rect(DISPLAYSURF,(255,0,0),(10+int(enemy[0]/5),10+int(enemy[1]/5),4,4))
    pygame.draw.circle(DISPLAYSURF, (0,0,0), (10+int(mx/5),10+int(my/5)),23,1)
    

  

    
  pygame.display.update()
  
  fpsClock.tick(FPS)
