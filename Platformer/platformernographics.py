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
  spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))

def start():
  global FPS,fpsClock,DISPLAY,you,stone,char,bounce,bounce2,level,cannon_png,back,warp
  level = 0
  pygame.init()
  pygame.mixer.pre_init(44100, 16, 4, 4096)
  pygame.mixer.init()
  def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)
  FPS = 30
  fpsClock = pygame.time.Clock()
  DISPLAY = pygame.display.set_mode((1200,700),FULLSCREEN)
  you = [0,0]





def game_menu():
  global DISPLAY
  pygame.mouse.set_visible(True)
  while True:
    escape = False
    mx,my = pygame.mouse.get_pos()
    myfont = pygame.font.SysFont('Cambria', 20)
    sizemssg = myfont.render('Exit Fullscreen', False, (255, 255, 255))
    sizemssg2 = myfont.render('Fullscreen', False, (255, 255, 255))
    quitmssg = myfont.render('Quit', False, (255, 255, 255))
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          escape = True
      if event.type == MOUSEBUTTONDOWN:
        if 500<=mx<=700 and 100<=my<=200:
          end()
        if 100<=mx<=300 and 100<=my<=200:
          DISPLAY= pygame.display.set_mode((1200,700))
        if 100<=mx<=300 and 220<=my<=320:
          DISPLAY= pygame.display.set_mode((1200,700),FULLSCREEN)
        if 800<=mx<=1000 and 220<=my<=320:
          run()
        if 800<=mx<=1000 and 100<=my<=320:
          level_menu()
      if event.type == QUIT:
        end()
    DISPLAY.fill((0,0,0,250))
    pygame.draw.rect(DISPLAY,(200,200,200),(100,100,200,100))
    pygame.draw.rect(DISPLAY,(200,200,200),(500,220,200,100))
    pygame.draw.rect(DISPLAY,(200,200,200),(100,220,200,100))
    pygame.draw.rect(DISPLAY,(200,200,200),(500,100,200,100))
    pygame.draw.rect(DISPLAY,(200,200,200),(800,220,200,100))
    pygame.draw.rect(DISPLAY,(200,200,200),(800,100,200,100))
    DISPLAY.blit(sizemssg,(140,140))
    DISPLAY.blit(sizemssg2,(140,260))
    DISPLAY.blit(quitmssg,(540,130))
    pygame.display.update()
    if escape:
      break

def level_menu():
  global DISPLAY,level,shots
  pygame.mouse.set_visible(True)
  levels = []
  x = 100
  y = 100
  l = -1
  for i in range(len(blocks)):
    levels.append([x,y,l])
    x += 200
    l += 1
    if x > 1000:
      x = 100
      y += 200
  while True:
    escape = False
    mx,my = pygame.mouse.get_pos()
    myfont = pygame.font.SysFont('Cambria', 20)
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          escape = True
      if event.type == MOUSEBUTTONDOWN:
        for click in levels:
          if click[0]<mx<click[0]+100 and click[1]<my<click[1]+100:
            level = click[2]
            shots = []
            level_up()
            run()
      if event.type == QUIT:
        end()
    DISPLAY.fill((0,0,0,250))
    for click in levels:
      pygame.draw.rect(DISPLAY,(230,230,230),(click[0],click[1],100,100))
      DISPLAY.blit(myfont.render(str(click[2]+2), False, (255, 255, 255)),(click[0]+40,click[1]+20))
    pygame.display.update()
    if escape:
      break

def run():
  global FPS,fpsClock,DISPLAY,you,blocks,level,shots
  velocity_x = 0
  velocity_y = 0
  b = 0
  acc_x,acc_y = 0,0
  gravity = 0.4
  jump = False
  ap,dp = False,False
  floored = False
  clock = 1
  blocks = [
            [[0,550,300,200,0],[400,500,300,300,0],[720,440,30,10,0],[750,250,10,500,0],[360,390,330,10,0],[280,300,10,50,0],[290,340,20,10,0],[320,240,440,10,0]],
            [[0,550,120,200,0],[260,530,30,10,0],[400,500,100,200,0],[600,440,30,10,0],[420,390,70,30,0],[600,330,20,10,0],[800,400,100,400,0]],
            [[90,500,30,400,0],[330,670,200,50,0],[590,620,20,10,0],[530,570,20,10,0],[590,520,20,10,0],[530,470,20,10,0],[450,460,40,10,0],[390,440,40,10,0],[370,300,10,120,1],[450,250,100,10,1],[700,400,80,40,0],[900,200,10,500,1]],
            [[90,350,30,400,0],[330,600,50,40,1],[580,350,30,400,0],[650,0,20,600,0],[610,640,50,40,0],[660,640,50,40,2],[710,390,30,390,0],[710,330,30,60,1],[710,160,30,170,0],[840,710,400,10,2]],[[350,200,70,30,0],[350,270,40,440,0],
              [500,660,30,50,1],[0,650,30,10,2],[100,650,250,20,0],[300,220,50,10,0],[350,100,10,100,0],[300,230,10,340,0],[100,400,30,20,1],[200,350,50,10,2],[260,100,100,10,0],[600,140,50,660,0],[650,600,40,20,0],[780,600,20,20,1],[870,300,20,400,1],[870,200,20,100,0],[750,320,50,10,0],[700,270,50,10,0],[680,200,20,60,1],[850,200,60,20,0],[680,0,10,500,0],[750,170,70,10,1]],
            [[0,600,1200,10,0],[100,540,10,60,0],[1000,590,50,10,2],[900,280,10,50,1],[700,330,200,10,0],[500,330,100,10,0],[40,330,360,10,0],[0,330,40,10,2],[-10,100,10,200,0],[100,100,980,10,0],[1300,0,10,300,0]],
            [[0,420,10,10,0],[-10,0,10,400,0],[0,390,1100,330,0],[1150,350,50,350,0],[0,380,60,10,0],[60,380,50,10,2],[100,350,100,40,0],[200,380,60,10,0],[260,380,40,10,2],[300,350,100,40,0],[400,380,60,10,0],[460,380,40,10,2],[500,350,100,40,0],[500,265,10,40,0],[600,380,150,10,1],[750,350,100,40,0], [880,350,200,10,0]],
            [[0,200,50,10,0],[200,300,50,10,3,100,False,0],[400,350,50,10,3,100,True,10],[570,340,50,10,3,50,False,0],[750,00,10,260,0],[750,350,70,20,0],[750,260,10,90,3,20,True,0],[960,200,10,150,3,40,False,0],[960,350,10,350,0],[860,400,30,20,1]],
            [[0, 100, 100, 10, 0], [100, 100, 100, 10, 3, 10, True, 0], [200, 100, 1000, 10, 0], [260, 110, 10, 110, 3, 40, False, 0], [260, 220, 10, 490, 0], [110, 650, 100, 40, 1], [110, 620, 100, 30, 3, 40, True, 0],
             [200, 690, 10, 10, 0], [270, 620, 100, 90, 0], [360, 110, 10, 480, 0], [370, 620, 40, 80, 2], [110, 690, 90, 10, 0], [450, 350, 30, 20, 0], [490, 350, 60, 20, 0],
             [370, 270, 10, 100, 0], [560, 350, 70, 20, 0], [480, 280, 10, 90, 3, 60, True, 0], [550, 280, 10, 90, 3, 45, True, 0], [640, 350, 110, 20, 2], [380, 270, 260, 10, 0],
             [760, 270, 70, 10, 0], [830, 270, 10, 440, 0], [630, 280, 10, 90, 3, 30, True, 0]],
            [[0, 100, 100, 10, 3, 100, False, 0], [100, 100, 10, 370, 0], [110, 460, 660, 10, 0], [0, 200, 100, 10, 3, 100, True, 0], [0, 330, 100, 10, 3, 100, False, 0], [0, 460, 100, 10, 3, 100, True, 0], [0, 620, 1270, 90, 0], [160, 470, 240, 150, 3, 90, True, 0],
             [400, 470, 260, 150, 3, 90, False, 20], [660, 470, 110, 150, 3, 90, True, 0], [770, 460, 110, 160, 3, 90, False, 20], [970, 610, 60, 10, 2]],
            [[0, 530, 80, 10, 0], [0, 630, 780, 200, 0], [780, 630, 170, 100, 3, 100, True, 30], [790, 650, 140, 30, 2], [140, 400, 30, 260, 3, 20, True, 0], [250, 400, 30, 260, 3, 10, False, 0], [360, 400, 30, 260, 3, 20, True, 0],
             [470, 400, 30, 260, 3, 10, False, 0], [570, 400, 30, 260, 3, 30, True, 0], [670, 400, 30, 260, 3, 10, False, 0], [760, 400, 30, 260, 3, 60, False, 0], [0, 640, 780, 70, 0], [0, 430, 10, 100, 0], [0, 540, 10, 50, 0],
             [950, 630, 50, 70, 1],[940, 640, 10, 60, 0], [930, 360, 20, 90, 1], [750, 360, 30, 30, 1], [630, 260, 40, 20, 2], [0, 360, 10, 30, 0], [10, 350, 10, 10, 0], [330, 380, 80, 10, 2], [0, 410, 10, 10, 0], [0, 390, 780, 40, 0]]
            ]
  endzones = [[920,600,150,50],[920,600,150,50],[800,200,100,100],[970,600,50,20],[970,600,50,20],[1100,100,50,50],[1100,500,50,50],[1100,500,50,50],[920, 600, 150, 50],[920, 240, 150, 50],[70, 130, 150, 50]]
  spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
  cannons = [[],[],[],[],[],[[0,90,0.5,30,0],[0,70,0.5,30,5],[900,590,-1,25,0],[930,540,-2,50,0],[100,300,1,20,0],[100,200,-1,60,0],[100,200,-1,60,0],[100,180,-1,60,0],[100,160,-1,60,0],[100,140,-1,60,0],[100,120,-1,60,0]],
             [[1000,340,-1.5,20,0],[1000,310,-1.5,20,0],[1100,295,-0.6,15,0,0],[1100,280,-2,20,0]],[],[[810, 340, -0.5, 20, 0]],[],
             [[0, 590, 2.5, 30, 0], [0, 600, 2.5, 30, 0], [0, 620, 2.5, 30, 0], [0, 610, 2.5, 30, 0], [270, 620, 2.0, 30, 0], [990, 620, -3.0, 30, 10], [990, 610, -3.0, 30, 10], [600, 620, 1, 30, 0], [10, 360, -1.5, 30, 10], [10, 370, 1.5, 30, 0], [10, 380, 1.5, 30, 10], [740, 370,-2.0, 30, 0], [740, 370, -2.0, 30, 0], [740, 360, -2.0, 30, 10], [740, 380, 2.0, 30, 10]]]
  shots = []
  while True:
    DISPLAY.fill((40,40,40))
    x = 0
    y = 0
    you[1] += velocity_y
    you[0] += velocity_x

    if you[1] > 850:
      velocity_y = 0
      velocity_x = 0
      spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
    
    if not floored:
      velocity_y += gravity
    floored = False
    for floor in blocks[level]:
      if ((you[0]-floor[0]*you[0]-floor[0]) < 100 or (you[0]-floor[0]+floor[2]*you[0]-floor[0]+floor[2]) < 100) or ((you[1]-floor[1]*you[1]-floor[1]) < 100 or (you[1]-floor[1]+floor[3]*you[1]-floor[1]+floor[3]) < 100):
        if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x >= 0 and floor[0]+7>you[0]+15>floor[0]:
          if floor[4] != 3:
            velocity_x = -velocity_x
            you[0] -= 7
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] -= 7
          if floor[4] == 1 or floor[4] == 2:
            velocity_y -= 9
        if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x < 0 and floor[0]+floor[2]-7<you[0]<floor[0]+floor[2]:
          if floor[4] != 3:
            velocity_x = -velocity_x
            you[0] += 7
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] += 7
          if floor[4] == 1 or floor[4] ==  2:
            velocity_y -= 9
        if floor[1]<you[1]<floor[1]+floor[3] and floor[0]<you[0]+13 and you[0]+2<floor[0]+floor[2] and velocity_y > 0:
          if floor[4] != 3:
            you[1] = floor[1]
          elif floor[4] == 3 and floor[6]:
            you[1] = floor[1]
          elif floor[4] == 3 and not floor[6]:
            floored = False
          if floor[4] == 1:
            velocity_y = -0.9*velocity_y
          elif floor[4] == 2:
            velocity_y = -16
        if floor[1]<you[1]-15<floor[1]+floor[3] and floor[0]<you[0]+13 and you[0]+2<floor[0]+floor[2] and velocity_y < 0:
          if floor[4] != 3:
            you[1] = floor[1]+floor[3]+15
            velocity_y = 0
          elif floor[4] == 3 and floor[6]:
            you[1] = floor[1]+floor[3]+15
            velocity_y = 0
        if you[1] == floor[1] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2]:
          if floor[4]!=3:
            if floor[4]!=1 and floor[4]!= 2:
              velocity_y = 0
              floored = True
          elif floor[4] == 3 and floor[6]:
            velocity_y = 0
            floored = True

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          game_menu()
        if event.key == K_a:
          ap = True
        if event.key == K_d:
          dp = True
        if event.key == K_SPACE and floored:
          velocity_y -= 7
      if event.type == KEYUP:
        if event.key == K_a:
          ap = False
        if event.key == K_d:
          dp = False


    for shot in shots:
      shot[0] += shot[2]*7
      pygame.draw.circle(DISPLAY,shot[3],(int(shot[0]),int(shot[1])),3)
      for floor in blocks[level]:
        if (floor[0]<shot[0]<floor[0]+floor[2] and floor[1]<shot[1]<floor[1]+floor[3]) and (floor[4] != 3 or floor[6]):
          shots.pop(shots.index(shot))
          break
      if you[0]<shot[0]<you[0]+15 and you[1]-15<shot[1]<you[1]:
        velocity_y = 0
        velocity_x = 0
        spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        
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

    for floor in blocks[level]:
      y = 0
      x = 0
      for i in range((int(floor[2]/10))*(int(floor[3]/10))):
        if floor[4] == 0:
          pygame.draw.rect(DISPLAY,(220,220,220),(floor[0]+x,floor[1]+y,10,10))
        elif floor[4] == 1:
           pygame.draw.rect(DISPLAY,(220,160,0),(floor[0]+x,floor[1]+y,10,10))
        elif floor[4] == 2:
          pygame.draw.rect(DISPLAY,(0,220,0),(floor[0]+x,floor[1]+y,10,10))
        elif floor[4] == 3 and floor[6]:
          pygame.draw.rect(DISPLAY,(0,0,220),(floor[0]+x,floor[1]+y,10,10))
        x+=10
        if x == floor[2]:
          y+=10
          x = 0
      if floor[4] == 3 and (clock+floor[7]) % floor[5] == 0:
        if floor[6]:
          floor[6] = False
        else:
          floor[6] = True
          if ((floor[0]<you[0]<floor[0]+floor[2])or(floor[0]<you[0]+15<floor[0]+floor[2])) and ((floor[1]<you[1]<floor[1]+floor[3])or(floor[1]<you[1]+15<floor[1]+floor[3])):
            velocity_y = 0
            velocity_x = 0
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
    pygame.draw.rect(DISPLAY,(0,255,255),(endzones[level]))

    for cannon in cannons[level]:
      pygame.draw.rect(DISPLAY,(220,0,0),(cannon[0],cannon[1],10,10))
      if (clock+cannon[4]) % cannon[3] == 0:
        shots.append([cannon[0]+5,cannon[1]+5,cannon[2],(255,0,0)])
                
    if endzones[level][0]<you[0]<endzones[level][0]+endzones[level][2] and endzones[level][1]<you[1]<endzones[level][1]+endzones[level][3]:
      velocity_y = 0
      velocity_x = 0
      shots = []
      level_up()
    
    
    if not 1170>you[0]>0:
      velocity_x = -velocity_x
      ch = you[0] - 600
      if ch > 3:
        ch = 3
      elif ch < -3:
        ch = -3
      you[0] -= ch
    pygame.draw.rect(DISPLAY,(255,255,255),(int(you[0]),int(you[1])-15,15,15))     
    pygame.display.update()
    fpsClock.tick(FPS)
    clock+=1

start()
run()
