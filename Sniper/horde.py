import random, pygame, sys,os
from pygame import *
from random import *
from sys import *

def end():
  pygame.quit()
  sys.exit()

def start():
  pygame.init()
  global DISPLAY,maps,backs,scope,base,FPS,fpsClock,bul,Slow,frz,kll,Kill,fogs,fog,bomb,map4,Army
  FPS = 30
  fpsClock = pygame.time.Clock()
  DISPLAY = pygame.display.set_mode((1200,700),FULLSCREEN)
  scope = pygame.image.load("Scope1.png").convert_alpha()
  bomb2 = pygame.image.load("Bomb.png").convert_alpha()
  bomb = pygame.Surface((80,80))
  pygame.transform.scale(bomb2,(80,80),bomb).convert_alpha() 
  base = pygame.image.load("base.png").convert_alpha()
  map1 = [pygame.image.load(os.path.join("enemy.png")).convert_alpha(),pygame.image.load(os.path.join("Desert.png")).convert_alpha(),pygame.image.load(os.path.join("big.png")).convert_alpha(),base,pygame.image.load(os.path.join("mag.png")).convert_alpha()]
  map2 = [pygame.image.load(os.path.join("enemy.png")).convert_alpha(),pygame.image.load(os.path.join("Grass.png")).convert_alpha(),pygame.image.load(os.path.join("big.png")).convert_alpha(),base,pygame.image.load(os.path.join("mag.png")).convert_alpha()]
  map3 = [pygame.image.load(os.path.join("moonenemy.png")).convert_alpha(),pygame.image.load(os.path.join("Moon.png")).convert_alpha(),pygame.image.load(os.path.join("big.png")).convert_alpha(),base,pygame.image.load(os.path.join("mag.png")).convert_alpha()]
  map4 = [pygame.image.load(os.path.join("zombie.png")).convert_alpha(),pygame.image.load(os.path.join("Halloween.png")).convert_alpha()]
  maps = [map2,map1,map3]#,map4]
  Slow = pygame.image.load("Ice.png").convert_alpha()
  Kill = pygame.image.load("Kill.png").convert_alpha()
  bul = pygame.image.load("ammo.png").convert_alpha()
  frz = pygame.image.load("pwrup1.png").convert_alpha()
  kll = pygame.image.load("pwrup2.png").convert_alpha()
  fog = pygame.image.load("Fog.png").convert_alpha()
  Army = pygame.image.load("Army.png").convert_alpha()
  backs = []
  fogs = []
  x = -960
  y = -480
  for i in range(25):
    x += 480
    if y == -480:
      fogs.append((x,y))
    if x == 1920:
      x = -480
      y += 480
    backs.append((x,y))

    
def horde():
  global DISPLAY,maps,backs,scope,FPS,bul,basehealth,total_kills,score,mids,score,Slow,frz,kll,Kill,fogs,fog,game,pgame,bomb,map4,Army
  pygame.mouse.set_visible(False)
  enemy,back2 = map4
  back = pygame.Surface((480,480))
  pygame.transform.scale(back2,(480,480),back).convert_alpha()
  enemies = []
  myfont = pygame.font.SysFont('Cambria', 20)
  passed = 0
  c_ens = 0
  clock = 0
  wave_enemies = 8
  basehealth = 3000
  kills = 0
  total_kills = kills
  ammo = 6
  live = True
  ammo_timer = 0
  shots = 0
  score = 0
  hits = 0
  save = []
  for i in range(10):
    save.append([randint(10,50)*20,randint(10,20)*20])
  
  s = False
  rushing = False
  speedsave = 1.1
  spwnsave = 100
  rl = 100
  rl2 = 100
  rush = 0
  rushtimer = 0
  spwn = 300
  while len(save) > 0:
    if clock == 0:
      for i in range(10):
        save.append([randint(10,50)*20,randint(10,20)*20])
    if ammo == 0:
      ammo_timer -= 1
      if ammo_timer == 0:
        ammo = 5
    mx,my = pygame.mouse.get_pos()
    mx,my = mx-600,my-350
    DISPLAY.fill((0,0,0))
    for event in pygame.event.get():
      if event.type == QUIT:
        end()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          DISPLAY= pygame.display.set_mode((1200,700),RESIZABLE)
      if event.type == MOUSEBUTTONDOWN and ammo > 0:
        shots += 1
        c = 0
        ammo -= 1
        hit = False
        for bad in enemies:
          if bad[0]<=mx+600<=bad[0]+20 and bad[1]<=my+350<=bad[1]+20:
            enemies.pop(c)
            kills += 1
            total_kills += 1
            hit = True
            hits += 1
            score += 10
          c += 1
        if ammo == 0:
          ammo_timer = 90

    for bad in enemies:
      nearest = 10000000
      for good in save:
        near = good[0]- bad[0]+good[1]-bad[1]
        if near * near < nearest * nearest:
          nearest = near
          hunt = good
      difx,dify = hunt[0]-bad[0],hunt[1]-bad[1]
      if -20<difx<20 and -40<dify<40:
        if len(save) > 1:
          enemies.append([hunt[0],hunt[1]])
          save.pop(save.index([hunt[0],hunt[1]]))
        else:
          save = []
      if difx > 1:
        difx = 1
      if difx < -1:
        difx = -1
      if dify > 1:
        dify = 1
      if dify < -1:
        dify = -1
      x,y = None,None
      for block in enemies:
        if bad != block:
          while block[0]- 20 < bad[0] + difx < block[0]+ 20 and block[1]-40 < bad[1] + difx < block[1]+ 40:
            x = False
            y = False
            bad[0] -= difx
            bad[1] -= dify
      if y == None:
        y = True
      if x == None:
        x = True
      if x:
        bad[0] += difx
      if y:
        bad[1] += dify

    for good in save:
      safe = [0,0]
      for bad in enemies:
        safe[0],safe[1] = safe[0]+(good[0]-bad[0]),safe[1]+(good[1]-bad[1])
      difx,dify,x,y = 0,0,True,True
      if safe[0] > 0:
        difx = 0.5
      if safe[0] < 0:
        difx = -0.5
      if safe[1] > 0:
        dify = 0.5
      if safe[1] < 0:
        dify = -0.5
      for block in save:
        if good != block:
          while block[0]- 20 < good[0] + difx < block[0]+ 20 and block[1]-40 < good[1] + difx < block[1]+ 40:
            good[0] -= difx
            good[1] -= dify
      if x:
        good[0] += difx
      if y:
        good[1] += dify
        
      for check in save:
        if check[0] > 1110:
          check[0] = 1110
        if check[0] < 10:
          check[0] = 10
        if check[1] > 510:
          check[1] = 510
        if check[1] < 10:
          check[1] = 10
        
    
    if clock % spwn == 0 or len(enemies) == 0 and  clock > 50:
      if spwn > 60:
        spwn -= 1
      pushx = 0
      pushy = 0
      for good in save:
        pushx += good[0]-600
        pushy += good[1]-300
      l = [randint(-50,0),randint(0,600)]
      r = [randint(1200,1250),randint(0,600)]
      t = [randint(0,1200),randint(-50,0)]
      b = [randint(0,1200),randint(600,650)]
      if pushx > 0:
        a = r
      else:
        a = l
      if pushy > 0:
        c = b
      else:
        c = t
      posx,posy = choice([[a[0],a[1]],[c[0],c[1]]])
      enemies.append([posx,posy])
    
    for i in backs:
      DISPLAY.blit(back,(i[0]-mx,i[1]-my))
    
    for bad in enemies:
      DISPLAY.blit(enemy,(bad[0]-mx,bad[1]-my))

    for good in save:
      DISPLAY.blit(Army,(good[0]-mx,good[1]-my))
    
    DISPLAY.blit(scope,(0,-100))
      
    pygame.draw.rect(DISPLAY,(255,255,255),(30,30,240,120))
    textsurface = myfont.render('Score: '+str(score), False, (255, 255, 255))
    DISPLAY.blit(textsurface,(850,120))
    textsurface = myfont.render(str(len(save))+'/20', False, (255, 255, 255))
    DISPLAY.blit(textsurface,(850,160))

    if ammo > 0:
      for i in range(ammo):
        DISPLAY.blit(bul,(860+3*i*14,270))
    else:
      pygame.draw.rect(DISPLAY,(255,0,0),(860,285,(ammo_timer*1.6),30))
    p = 0
    for good in save:
      pygame.draw.rect(DISPLAY,(0,255,0),((good[0]/5)+30,(good[1]/5)+30,3,3))
    pygame.draw.circle(DISPLAY, (0,0,0), (30+int((mx+600)/5),30+int((my+350)/5)),40,1)
    pygame.display.update()
    fpsClock.tick(FPS)
    clock += 1
  myfont = pygame.font.SysFont('Cambria', 100)
  diemssg = myfont.render('You died!', False, (255, 0, 0))
  myfont2 = pygame.font.SysFont('Cambria', 40)
  scoremssg = myfont2.render('Your score: '+str(score), False, (255, 255, 255))
  leavemssg = myfont2.render('Menu', False, (255, 255, 255))
  killsmssg = myfont2.render('Kills: '+str(total_kills), False, (255, 255, 255))
  if shots > 0:
    accmssg = myfont2.render('Accuracy: '+str(round((hits/shots)*100))+'%', False, (255, 255, 255))
  else:
    accmssg = myfont2.render('Accuracy: '+str(0)+'%', False, (255, 255, 255))
  pygame.mouse.set_visible(True)
  while True:
    DISPLAY.fill((0,0,0))
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == QUIT:
        end()
      if event.type == MOUSEBUTTONDOWN:
        if 100<=mx<=300 and 470<=my<=530:
          menu()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          DISPLAY= pygame.display.set_mode((1200,700),RESIZABLE)
    DISPLAY.fill((0,0,0))
    pygame.draw.rect(DISPLAY,(200,200,200),(160,470,200,100))
    DISPLAY.blit(diemssg,(420,150))
    DISPLAY.blit(scoremssg,(420,270))
    DISPLAY.blit(leavemssg,(200,500))
    DISPLAY.blit(killsmssg,(420,370))
    DISPLAY.blit(accmssg,(420,420))
    pygame.display.update()
    fpsClock.tick(FPS)

start()
horde()
