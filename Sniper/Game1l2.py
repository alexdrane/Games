import pygame, sys
from pygame.locals import *
import random
from random import *

class wall(object):
  pos = (0,0,0,0)
  col = (140,140,140)
  def __init__(self,pos1,pos2):
    self.pos = (pos1,pos2,20,20)
class en(object):
  d = "r"
  px = 0
  py = 0
  ppx = 0
  ppy = 0
  def __init__(self,px,py):
    self.px = px
    self.py = py

enemies = []

walls = []
for i in range(90):
  walls.append(wall(20*i,0))
  walls.append(wall(20*i,580))
for i in range(30):
  walls.append(wall(0,20*i))
  walls.append(wall(880,20*i))
walls.append(wall(60,20))
walls.append(wall(60,40))
walls.append(wall(60,60))
walls.append(wall(20,60))
walls.append(wall(20,80))
walls.append(wall(60,80))
walls.append(wall(60,100))
walls.append(wall(60,120))
walls.append(wall(40,120))
walls.append(wall(20,160))
walls.append(wall(40,160))
walls.append(wall(60,160))
walls.append(wall(60,180))
walls.append(wall(80,180))
walls.append(wall(100,180))
walls.append(wall(120,180))
walls.append(wall(140,180))
walls.append(wall(160,180))
walls.append(wall(180,180))
walls.append(wall(100,140))
walls.append(wall(120,140))
walls.append(wall(140,140))
walls.append(wall(160,140))
walls.append(wall(100,120))
walls.append(wall(100,100))
walls.append(wall(100,80))
walls.append(wall(100,60))
walls.append(wall(100,20))
walls.append(wall(160,120))
walls.append(wall(160,100))
walls.append(wall(140,100))
walls.append(wall(140,80))
walls.append(wall(120,20))
walls.append(wall(140,20))
walls.append(wall(140,40))
walls.append(wall(140,60))
walls.append(wall(200,180))
walls.append(wall(200,160))
walls.append(wall(200,140))
walls.append(wall(200,120))
walls.append(wall(200,100))
walls.append(wall(180,60))
walls.append(wall(180,40))
walls.append(wall(200,40))
walls.append(wall(220,40))
walls.append(wall(240,40))
walls.append(wall(260,40))
walls.append(wall(200,60))
walls.append(wall(220,60))
walls.append(wall(240,60))
walls.append(wall(240,80))
walls.append(wall(240,100))
walls.append(wall(240,120))
walls.append(wall(260,120))
walls.append(wall(280,120))
walls.append(wall(300,120))
walls.append(wall(320,120))
walls.append(wall(340,120))
walls.append(wall(220,180))
walls.append(wall(240,180))
walls.append(wall(240,160))
walls.append(wall(260,160))
walls.append(wall(280,160))
walls.append(wall(300,160))
walls.append(wall(320,160))
walls.append(wall(340,160))
walls.append(wall(360,160))
walls.append(wall(380,160))
walls.append(wall(380,140))
walls.append(wall(380,120))
walls.append(wall(380,100))
walls.append(wall(380,80))
walls.append(wall(360,80))
walls.append(wall(340,80))
walls.append(wall(320,80))
walls.append(wall(300,80))
walls.append(wall(280,80))
walls.append(wall(280,40))
walls.append(wall(300,40))
walls.append(wall(320,40))
walls.append(wall(340,40))
walls.append(wall(360,40))
walls.append(wall(380,40))
walls.append(wall(420,20))
walls.append(wall(420,40))
walls.append(wall(420,60))
walls.append(wall(420,80))
walls.append(wall(420,100))
walls.append(wall(420,120))
walls.append(wall(420,140))
walls.append(wall(420,160))
walls.append(wall(420,180))
walls.append(wall(420,200))
walls.append(wall(400,200))
walls.append(wall(380,200))
walls.append(wall(360,200))
walls.append(wall(340,200))
walls.append(wall(320,200))
walls.append(wall(300,200))
walls.append(wall(280,200))
walls.append(wall(280,220))
walls.append(wall(280,240))
walls.append(wall(280,260))
walls.append(wall(280,280))
walls.append(wall(280,300))
walls.append(wall(280,320))
walls.append(wall(280,340))
walls.append(wall(280,360))
walls.append(wall(260,340))
walls.append(wall(260,380))
walls.append(wall(280,380))
walls.append(wall(260,300))
walls.append(wall(260,260))
walls.append(wall(260,220))
walls.append(wall(20,220))
walls.append(wall(20,260))
walls.append(wall(20,300))
walls.append(wall(20,340))
walls.append(wall(20,380))
walls.append(wall(20,420))
walls.append(wall(40,420))
walls.append(wall(60,420))
walls.append(wall(80,420))
walls.append(wall(100,420))
walls.append(wall(120,420))
walls.append(wall(140,420))
walls.append(wall(160,420))
walls.append(wall(180,420))
walls.append(wall(200,420))
walls.append(wall(220,420))
walls.append(wall(240,420))
walls.append(wall(260,420))
walls.append(wall(280,420))
walls.append(wall(300,420))
walls.append(wall(200,400))
walls.append(wall(160,400))
walls.append(wall(160,200))
walls.append(wall(200,200))
walls.append(wall(320,420))
walls.append(wall(320,400))
walls.append(wall(320,380))
walls.append(wall(320,360))
walls.append(wall(320,340))
walls.append(wall(320,320))
walls.append(wall(320,300))
walls.append(wall(320,280))
walls.append(wall(320,260))
walls.append(wall(320,240))
walls.append(wall(340,240))
walls.append(wall(360,240))
walls.append(wall(380,240))
walls.append(wall(400,240))
walls.append(wall(420,240))
walls.append(wall(440,240))
walls.append(wall(460,240))
walls.append(wall(460,220))
walls.append(wall(460,200))
walls.append(wall(460,180))
walls.append(wall(460,160))
walls.append(wall(460,140))
walls.append(wall(460,120))
walls.append(wall(460,100))
walls.append(wall(460,80))
walls.append(wall(460,60))
walls.append(wall(460,20))
walls.append(wall(480,240))
walls.append(wall(500,240))
walls.append(wall(520,240))
walls.append(wall(540,240))
walls.append(wall(560,240))
walls.append(wall(580,240))
walls.append(wall(600,240))
walls.append(wall(620,240))
walls.append(wall(640,240))
walls.append(wall(660,240))
walls.append(wall(680,240))
walls.append(wall(700,240))
walls.append(wall(720,220))
walls.append(wall(720,240))
walls.append(wall(720,200))
walls.append(wall(720,180))
walls.append(wall(720,160))
walls.append(wall(720,140))
walls.append(wall(720,120))
walls.append(wall(720,100))
walls.append(wall(720,80))
walls.append(wall(720,60))
walls.append(wall(720,40))
walls.append(wall(700,40))
walls.append(wall(500,40))
walls.append(wall(500,60))
walls.append(wall(500,20))
walls.append(wall(520,20))
walls.append(wall(500,200))
walls.append(wall(500,220))
walls.append(wall(520,220))
walls.append(wall(680,220))
walls.append(wall(700,220))
walls.append(wall(700,200))
walls.append(wall(540,20))
walls.append(wall(760,20))
walls.append(wall(760,40))
walls.append(wall(760,60))
walls.append(wall(760,80))
walls.append(wall(760,100))
walls.append(wall(760,120))
walls.append(wall(760,140))
walls.append(wall(760,160))
walls.append(wall(660,80))
walls.append(wall(680,80))
walls.append(wall(700,80))
walls.append(wall(480,200))
walls.append(wall(480,220))
walls.append(wall(760,180))
walls.append(wall(760,200))
walls.append(wall(760,220))
walls.append(wall(760,240))
walls.append(wall(780,240))
walls.append(wall(780,260))
walls.append(wall(780,280))
walls.append(wall(780,300))
walls.append(wall(780,320))
walls.append(wall(780,340))
walls.append(wall(780,360))
walls.append(wall(780,380))
walls.append(wall(780,400))
walls.append(wall(780,420))
walls.append(wall(760,420))
walls.append(wall(760,380))
walls.append(wall(760,340))
walls.append(wall(760,300))
walls.append(wall(760,260))
walls.append(wall(340,260))
walls.append(wall(340,300))
walls.append(wall(340,340))
walls.append(wall(340,380))
walls.append(wall(340,420))
walls.append(wall(440,320))
walls.append(wall(420,340))
walls.append(wall(440,340))
walls.append(wall(440,300))
walls.append(wall(420,300))
walls.append(wall(460,300))
walls.append(wall(460,340))
walls.append(wall(560,360))
walls.append(wall(600,360))
walls.append(wall(560,380))
walls.append(wall(580,380))
walls.append(wall(600,380))
walls.append(wall(620,340))
walls.append(wall(620,380))
walls.append(wall(540,340))
walls.append(wall(540,380))
walls.append(wall(560,260))
walls.append(wall(600,260))
walls.append(wall(320,440))
walls.append(wall(340,440))
walls.append(wall(360,440))
walls.append(wall(380,440))
walls.append(wall(400,440))
walls.append(wall(420,440))
walls.append(wall(440,440))
walls.append(wall(440,440))
walls.append(wall(460,440))
walls.append(wall(500,440))
walls.append(wall(520,440))
walls.append(wall(540,440))
walls.append(wall(560,440))
walls.append(wall(580,440))
walls.append(wall(600,440))
walls.append(wall(620,440))
walls.append(wall(640,440))
walls.append(wall(660,440))
walls.append(wall(700,440))
walls.append(wall(680,440))
walls.append(wall(720,440))
walls.append(wall(740,440))
walls.append(wall(760,440))
walls.append(wall(780,440))
walls.append(wall(460,460))
walls.append(wall(460,480))
walls.append(wall(440,480))
walls.append(wall(420,480))
walls.append(wall(400,480))
walls.append(wall(380,480))
walls.append(wall(360,480))
walls.append(wall(340,480))
walls.append(wall(320,480))
walls.append(wall(300,480))
walls.append(wall(280,480))
walls.append(wall(280,460))
walls.append(wall(240,440))
walls.append(wall(240,460))
walls.append(wall(240,480))
walls.append(wall(240,500))
walls.append(wall(240,520))
walls.append(wall(260,520))
walls.append(wall(280,520))
walls.append(wall(300,520))
walls.append(wall(320,520))
walls.append(wall(340,520))
walls.append(wall(360,520))
walls.append(wall(380,520))
walls.append(wall(400,520))
walls.append(wall(420,520))
walls.append(wall(440,520))
walls.append(wall(460,520))
walls.append(wall(480,520))
walls.append(wall(500,520))
walls.append(wall(520,520))
walls.append(wall(540,520))
walls.append(wall(560,520))
walls.append(wall(580,520))
walls.append(wall(600,520))
walls.append(wall(600,500))
walls.append(wall(600,480))
walls.append(wall(600,460))
enemies.append(en(140,120))
enemies.append(en(360,140))
enemies.append(en(260,240))
enemies.append(en(260,320))
enemies.append(en(20,360))
enemies.append(en(20,280))
enemies.append(en(180,400))
enemies.append(en(520,40))
enemies.append(en(540,40))
enemies.append(en(560,40))
enemies.append(en(580,40))
enemies.append(en(600,40))
enemies.append(en(620,40))
enemies.append(en(620,40))
enemies.append(en(640,40))
enemies.append(en(520,200))
enemies.append(en(540,200))
enemies.append(en(560,200))
enemies.append(en(580,200))
enemies.append(en(600,200))
enemies.append(en(620,200))
enemies.append(en(640,200))
enemies.append(en(660,200))
enemies.append(en(680,200))
enemies.append(en(660,40))
enemies.append(en(680,40))
enemies.append(en(580,160))
enemies.append(en(620,140))
enemies.append(en(640,100))
enemies.append(en(680,140))
enemies.append(en(340,280))
enemies.append(en(360,280))
enemies.append(en(380,280))
enemies.append(en(420,280))
enemies.append(en(440,280))
enemies.append(en(460,280))
enemies.append(en(500,280))
enemies.append(en(520,280))
enemies.append(en(540,280))
enemies.append(en(420,320))
enemies.append(en(460,320))
enemies.append(en(580,360))
enemies.append(en(620,360))
enemies.append(en(540,360))
enemies.append(en(660,400))
enemies.append(en(700,400))
enemies.append(en(620,400))
enemies.append(en(580,400))
enemies.append(en(540,400))
enemies.append(en(500,400))
enemies.append(en(460,400))
enemies.append(en(420,400))
enemies.append(en(440,460))


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('You died!', False, (255, 0, 0))
DISPLAYSURF = pygame.display.set_mode((900,700))
pygame.display.set_caption("Game")
direction = 1
rectx = 20
recty = 20
rectxv = 0
rectyv = 0
d = 1
t = 0
FPS = 30
fpsClock = pygame.time.Clock()
px = 860
py = 560
die = None
while True:
  DISPLAYSURF.fill((0,0,0))
  prectx = rectx
  precty = recty
  for en in enemies:
    en.ppx,en.ppy = (en.px,en.py)

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
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_w:
        rectyv = -5
      if event.key == K_a:
        rectxv = -5
      if event.key == K_s:
        rectyv = 5
      if event.key == K_d:
        rectxv = 5
    if event.type == KEYUP:
      if event.key == K_w:
        rectyv = 0
      if event.key == K_a:
        rectxv = 0
      if event.key == K_s:
        rectyv = 0
      if event.key == K_d:
        rectxv = 0
  for en in enemies:
    if en.d == "r":
      en.px += 4
    if en.d == "d":
      en.py += 4
    if en.d == "l":
      en.px -= 4
    if en.d == "u":
      en.py -= 4
    for wall in walls:
      wallr = pygame.Rect(wall.pos)
      if en.px > wallr.left - 18 and en.px < wallr.right and en.py < wallr.bottom  and en.py > wallr.top - 18:
        en.px,en.py = (en.ppx,en.ppy)
        if en.d == "r":
          en.d = "u"
        elif en.d == "u":
          en.d = "l"
        elif en.d == "l":
          en.d = "d"
        elif en.d == "d":
          en.d = "r"
        
  rectx += rectxv
  recty += rectyv
  for wall in walls:
    save = (prectx,precty)
    wallr = pygame.Rect(wall.pos)
    if rectx > wallr.left - 18 and rectx < wallr.right and recty < wallr.bottom  and recty > wallr.top - 18:
      rectx,recty = save
  zns = []
  for i in enemies:
    zn = Rect(i.px-20,i.py-20,60,60)
    zns.append(zn)
    if rectx >= zn.left and rectx <= zn.right - 20 and recty <= zn.bottom -20 and recty >= zn.top:
      die = True
      t = 400
  pygame.draw.rect(DISPLAYSURF,(0,200,100),(20,20,40,40))
  for zn in zns:
    pygame.draw.rect(DISPLAYSURF,(100,0,0),zn)
  for wall in walls:
    pygame.draw.rect(DISPLAYSURF,wall.col,wall.pos)
  for en in enemies:
    pygame.draw.rect(DISPLAYSURF,(200,100,100),(en.px+1,en.py+1,16,16))

  pygame.draw.rect(DISPLAYSURF,(255,255,255),(rectx+1,recty+1,16,16))
      
  pygame.display.update()
  
  fpsClock.tick(FPS)
