import pygame, sys
from pygame.locals import *
import random
from random import *
pygame.init()
class wall(object):
  pos = (0,0,0,0)
  col = (140,140,140)
  def __init__(self,pos1,pos2):
    self.pos = (pos1,pos2,20,20)


walls = []
ens = []


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('You died!', False, (255, 0, 0))
DISPLAYSURF = pygame.display.set_mode((900,700))
pygame.display.set_caption("Game")
direction = 1
rectx = 20
recty = 20
d = 1
FPS = 100
t = 0
fpsClock = pygame.time.Clock()
px = 860
py = 560
die = None
while True:
  DISPLAYSURF.fill((0,0,0))
  prectx = rectx
  precty = recty

  if die == True:
      DISPLAYSURF.blit(textsurface,(350,620))
      rectx,recty = -30,-30
      t -= 1
      if t == 0:
        die = False
  if die == False:
    rectx,recty = 20,20
    die = None
  
  for event in pygame.event.get():
    if event.type == QUIT:
      for i in walls:
        print("walls.append(wall("+str(i[0])+","+str(i[1])+"))")
      for i in ens:
        print("enemies.append(en("+str(i[0])+","+str(i[1])+"))")
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_w:
        recty -= 20
      if event.key == K_a:
        rectx -= 20
      if event.key == K_s:
        recty += 20
      if event.key == K_d:
        rectx += 20
      if event.key == K_SPACE:
        walls.append(Rect((rectx,recty,20,20)))
      if event.key == K_e:
        ens.append(Rect((rectx,recty,20,20)))
        

  pygame.draw.rect(DISPLAYSURF,(0,200,100),(20,20,40,40))
  for en in ens:
    pygame.draw.rect(DISPLAYSURF,(200,0,0),en)
  for wall in walls:
    pygame.draw.rect(DISPLAYSURF,(140,140,140),wall)
  pygame.draw.rect(DISPLAYSURF,(255,255,255),(rectx+1,recty+1,16,16))
      
  pygame.display.update()
  
  fpsClock.tick(FPS)
  
  fpsClock.tick(FPS)
