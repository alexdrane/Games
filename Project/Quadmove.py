import random, pygame, sys,os
import math
from math import *
from pygame import *
from random import *
from sys import *

def start():
  global FPS,fpsClock,DISPLAY,line
  pygame.init()
  pygame.mixer.pre_init(44100, 16, 4, 4096)
  pygame.mixer.init()
  FPS = 30
  fpsClock = pygame.time.Clock()
  DISPLAY = pygame.display.set_mode((1000,1000))
  line = pygame.Surface((10,40))
  main()
  

def moveto(mx,my,x,y,speed):
  mx -= x
  my -= y
  if mx == 0:
    mx = 1
  grad = my/mx
  vx = sqrt((speed*speed)/(1+(grad*grad)))
  if mx < 0:
    vx = -vx
  vy = sqrt((speed*speed)-(vx*vx))
  if my < 0:
    vy = - vy
  return(vx,vy)

def anglecalc(mx,my):
  adjacant = my
  hyp = sqrt((mx*mx)+(my*my))
  return(acos(adjacant/hyp))

def main():
  x = 500
  y = 500
  vx = 0
  vy = 0
  speed = 6
  angle = 0
  while True:
    DISPLAY.fill((100,100,100))


    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        mx,my = pygame.mouse.get_pos()
        if event.button == 1:
          vx,vy = moveto(mx,my,x,y,speed)
        elif event.button == 3:
          vx,vy = moveto(mx,my,x,y,speed)
          vx = -vx
          vy = -vy
        angle = anglecalc(mx,my)

        

    x+= vx
    y+= vy
    DISPLAY.blit(pygame.transform.rotate(line,angle),(x,y))
    pygame.display.update()
    fpsClock.tick(FPS)

start()
    
          
        
        
