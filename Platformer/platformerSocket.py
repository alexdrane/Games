import random, pygame, sys,os
from pygame import *
from random import *
from sys import *

import socket,random

HOST = '192.168.0.11'  
PORT = 65432       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

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
  global FPS,fpsClock,DISPLAY,you,stone,char,bounce,bounce2,bounce1,bounce21,bounce11,bounce211,level,cannon_png,back,warp,char1,char2,char3,endp,fire,double,kill
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
  DISPLAY = pygame.display.set_mode((1200,700))
  you = [0,0]
  cannon_png = pygame.image.load("cannon.png").convert_alpha()
  stone = pygame.image.load("Block.png").convert_alpha()
  char = pygame.image.load("you.png").convert_alpha()
  char1 = pygame.image.load("yourrun.png").convert_alpha()
  char2 = pygame.image.load("yourrun2.png").convert_alpha()
  char3 = pygame.image.load("youjump.png").convert_alpha()
  bounce = pygame.image.load("bounce.png").convert_alpha()
  bounce2 = pygame.image.load("bounce2.png").convert_alpha()
  bounce1 = pygame.image.load("2bounce.png").convert_alpha()
  bounce21 = pygame.image.load("2bounce2.png").convert_alpha()
  bounce11 = pygame.image.load("3bounce.png").convert_alpha()
  bounce211 = pygame.image.load("3bounce2.png").convert_alpha()
  fire = pygame.image.load("fire.png").convert_alpha()
  endp = pygame.image.load("portal.png").convert_alpha()
  back = pygame.image.load("Back.png")
  warp = pygame.image.load("warp.png")
  double = pygame.image.load("doublejump.png").convert_alpha()
  kill = pygame.image.load("die.png").convert_alpha()


def leveldesign():
  velocity_x = 0
  velocity_y = 0
  acc_x,acc_y = 0,0
  gravity = 0.4
  jump = False
  ap,dp = False,False
  floored = False
  clock = 1
  blocks = [[0,100,100,10,0]]
  spawn(you,(blocks[0][0]+10,blocks[0][1]-50))
  endzones = [920,600,150,50]
  cannons = []
  shots = []
  start = False
  while True:
    DISPLAY.fill((0,0,0))

    you[1] += velocity_y
    you[0] += velocity_x

    if you[1] > 850:
      velocity_y = 0
      velocity_x = 0
      spawn(you,(blocks[0][0]+10,blocks[0][1]-50))
    
    if not floored:
      velocity_y += gravity
    floored = False
    for floor in blocks:
      if ((you[0]-floor[0]*you[0]-floor[0]) < 100 or (you[0]-floor[0]+floor[2]*you[0]-floor[0]+floor[2]) < 100) or ((you[1]-floor[1]*you[1]-floor[1]) < 100 or (you[1]-floor[1]+floor[3]*you[1]-floor[1]+floor[3]) < 100):
        if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x > 0 and floor[0]+7>you[0]+15>floor[0]:
          if floor[4] != 3:
            velocity_x = -velocity_x
            you[0] -= 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] -= 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          if floor[4] == 1 or floor[4] == 2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y -= 9
        if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x < 0 and floor[0]+floor[2]-7<you[0]<floor[0]+floor[2]:
          if floor[4] != 3:
            velocity_x = -velocity_x
            you[0] += 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] += 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          if floor[4] == 1 or floor[4] ==  2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y -= 9
        if floor[1]<you[1]<floor[1]+floor[3] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2] and velocity_y > 0:
          if floor[4] != 3:
            you[1] = floor[1]
          elif floor[4] == 3 and floor[6]:
            you[1] = floor[1]
          elif floor[4] == 3 and not floor[6]:
            floored = False
          if floor[4] == 1:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y = -0.9*velocity_y
          elif floor[4] == 2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y = -16
        if floor[1]<you[1]-15<floor[1]+floor[3] and floor[0]<you[0]+15 and you[0]<floor[0]+floor[2] and velocity_y < 0:
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
      if event.type == MOUSEBUTTONDOWN:
        if start:
          start = False
          fx,fy = pygame.mouse.get_pos()
          fx = fx - (fx%10)
          fy = fy - (fy%10)
          if fx < sx:
            fx,sx = sx,fx
          if fy < sy:
            fy,sy = sy,fy
          if fx == sx:
            fx = sx + 10
          if fy == sy:
            fy = sy + 10
          blocks.append([sx,sy,fx-sx,fy-sy,0])
        else:
          mx,my = pygame.mouse.get_pos()
          c = False
          for floor in blocks:
            if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
              floor[4]+=1
              if floor[4] > 3:
                floor[4] = 0
              c = True
              if floor[4] == 3 and len(floor) < 6:
                floor.append(100)
                floor.append(True)
                floor.append(0)
          for floor in cannons:
            if floor[0]<mx<floor[0]+10 and floor[1]<my<floor[1]+10:
              floor[2] = - floor[2]
              c = True
          if not c:
            start = True
            sx,sy = pygame.mouse.get_pos()
            sx = sx - (sx%10)
            sy = sy - (sy%10)
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          game_menu()
        if event.key == K_a:
          ap = True
        if event.key == K_d:
          dp = True
        if event.key == K_c:
          blocks = [[0,100,100,10,0]]
        if event.key == K_l:
          print(blocks)
          print(cannons)
          print(endzones)
        if event.key == K_e:
          mx,my = pygame.mouse.get_pos()
          endzones[0] = mx - (mx%10)
          endzones[1]= my - (my%10)
        if event.key == K_t:
          mx,my = pygame.mouse.get_pos()
          for floor in blocks:
            if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
              if floor[4] == 3:
                floor[5] += 10
                if floor[5] > 240:
                  floor[5] = 10
          for floor in cannons:
            if floor[0]<mx<floor[0]+10 and floor[1]<my<floor[1]+10:
              floor[3]+= 10
              if floor[3] > 200:
                floor[3] = 10
        if event.key == K_o:
          mx,my = pygame.mouse.get_pos()
          for floor in blocks:
            if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
              if floor[4] == 3:
                floor[7] += 10
                if floor[7] > 240:
                  floor[7] = 10
          for floor in cannons:
            if floor[0]<mx<floor[0]+10 and floor[1]<my<floor[1]+10:
              floor[4]+= 10
              if floor[4] > 200:
                floor[4] = 0
        if event.key == K_p:
          for floor in cannons:
            if floor[0]<mx<floor[0]+10 and floor[1]<my<floor[1]+10:
              floor[2]+= 0.5
              if floor[2] > 3:
                floor[2] = 0.5
        if event.key == K_i:
          mx,my = pygame.mouse.get_pos()
          for floor in blocks:
            if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
              if floor[4] == 3:
                floor[6] = not floor[6]
        if event.key == K_v:
          mx,my = pygame.mouse.get_pos()
          for floor in blocks:
            if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
              if len(blocks) > 1:
                blocks.pop(blocks.index(floor))
          for floor in cannons:
            if floor[0]<mx<floor[0]+10 and floor[1]<my<floor[1]+10:
              cannons.pop(cannons.index(floor))
        if event.key == K_f:
          mx,my = pygame.mouse.get_pos()
          cannons.append([mx-(mx%10),my-(my%10),1,30,0])
        if event.key == K_SPACE and floored:
          pygame.mixer.music.load("jump.mp3")
          pygame.mixer.music.play()
          velocity_y -= 7
      if event.type == KEYUP:
        if event.key == K_a:
          ap = False
        if event.key == K_d:
          dp = False
    
    for shot in shots:
      shot[0] += shot[2]*7
      pygame.draw.circle(DISPLAY,shot[3],(int(shot[0]),int(shot[1])),3)
      for floor in blocks:
        if (floor[0]<shot[0]<floor[0]+floor[2] and floor[1]<shot[1]<floor[1]+floor[3]) and (floor[4] != 3 or floor[6]):
          shots.pop(shots.index(shot))
          break
      if you[0]<shot[0]<you[0]+15 and you[1]-15<shot[1]<you[1]:
        velocity_y = 0
        velocity_x = 0
        spawn(you,(blocks[0][0]+10,blocks[0][1]-50))
        
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

    for floor in blocks:
      y = 0
      x = 0
      for i in range((int(floor[2]/10))*(int(floor[3]/10))):
        if floor[4] == 0:
          DISPLAY.blit(stone,(floor[0]+x,floor[1]+y))
        elif floor[4] == 1:
           DISPLAY.blit(bounce,(floor[0]+x,floor[1]+y))
        elif floor[4] == 2:
          DISPLAY.blit(bounce2,(floor[0]+x,floor[1]+y))
        elif floor[4] == 3:
          if floor[6]:
            DISPLAY.blit(stone,(floor[0]+x,floor[1]+y))
          myfont = pygame.font.SysFont('Cambria', 10)
          DISPLAY.blit(myfont.render(str(floor[5]), False, (255, 255, 255)),(floor[0],floor[1]))
          DISPLAY.blit(myfont.render(str(floor[7]), False, (255, 255, 255)),(floor[0],floor[1]+11))
        x+=10
        if x == floor[2]:
          y+=10
          x = 0
      if floor[4] == 3 and (clock+floor[7]) % floor[5] == 0:
        if floor[6]:
          floor[6] = False
        else:
          floor[6] = True
    pygame.draw.rect(DISPLAY,(0,255,255),(endzones))

    for floor in cannons:
      pygame.draw.rect(DISPLAY,(255,0,0),(floor[0],floor[1],10,10))
      if (clock+floor[4]) % floor[3] == 0:
        shots.append([floor[0]+5,floor[1]+5,floor[2],(255,0,0)])
      myfont = pygame.font.SysFont('Cambria', 10)
      DISPLAY.blit(myfont.render(str(floor[2]), False, (255, 255, 255)),(floor[0],floor[1]))
      DISPLAY.blit(myfont.render(str(floor[3]), False, (255, 255, 255)),(floor[0],floor[1]+11))
      DISPLAY.blit(myfont.render(str(floor[4]), False, (255, 255, 255)),(floor[0]+ 11,floor[1]+5))
                
    if endzones[0]<you[0]<endzones[0]+endzones[2] and endzones[1]<you[1]<endzones[1]+endzones[3]:
      velocity_y = 0
      velocity_x = 0
      spawn(you,(blocks[0][0]+10,blocks[0][1]-50))
    if start:
      mx,my = pygame.mouse.get_pos()
      w = (mx-(mx%10)-sx)
      h = (my-(my%10)-sy)
      if w == 0:
        w = 10
      if h == 0:
        h = 10
      pygame.draw.rect(DISPLAY,(255,255,255),(sx,sy,w,h))
    else:
      mx,my = pygame.mouse.get_pos()
      col = (255,255,255)
      for floor in blocks:
        if floor[0]<mx<floor[0]+floor[2] and floor[1]<my<floor[1]+floor[3]:
          col = (255,130,0)
      mx,my = pygame.mouse.get_pos()
      pygame.draw.rect(DISPLAY,col,(mx-(mx%10),my-(my%10),10,10))
    pygame.mouse.set_visible(False)
    if not 1170>you[0]>0:
      velocity_x = -velocity_x
      ch = you[0] - 600
      if ch > 3:
        ch = 3
      elif ch < -3:
        ch = -3
      you[0] -= ch
    DISPLAY.blit(char,(int(you[0]),int(you[1])-15))     
    pygame.display.update()
    fpsClock.tick(FPS)
    clock+=1


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
        if 500<=mx<=700 and 220<=my<=320:
          leveldesign()
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
      pygame.draw.rect(DISPLAY,(170,170,170),(click[0],click[1],100,100))
      DISPLAY.blit(myfont.render(str(click[2]+2), False, (255, 255, 255)),(click[0]+40,click[1]+20))
    pygame.display.update()
    if escape:
      break

def run():
  global FPS,fpsClock,DISPLAY,you,blocks,level,shots
  velocity_x = 0
  velocity_y = 0
  dt = False
  if level == 0:
    ttimer = 0
  else:
    ttimer = None
  acc_x,acc_y = 0,0
  gravity = 0.4
  jump = False
  ap,dp = False,False
  floored = False
  clock = 1
  dj = False
  trail = []
  timer = 0
  blocks = [
            [[0,550,300,200,0],[400,500,300,300,0],[720,440,30,10,0],[750,250,10,500,0],[360,390,330,10,0],[280,300,10,50,0],[290,340,20,10,0],[320,240,440,10,0]],
            [[0,550,120,200,0],[260,530,30,10,0],[400,500,100,200,0],[600,440,30,10,0],[420,390,70,30,0],[600,330,20,10,0],[801,407,100,400,0]],
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
          #  [[0, 100, 100, 10, 3, 30, False, 10], [100, 100, 10, 370, 0], [110, 460, 660, 10, 0], [0, 200, 100, 10, 3, 30, True, 10], [0, 330, 100, 10, 3, 30, False, 10], [0, 460, 100, 10, 3, 30, True, 10], [0, 620, 1270, 90, 0], [160, 470, 240, 150, 3, 90, False, 0],
          #   [400, 470, 260, 150, 3, 90, True, 30], [660, 470, 110, 150, 3, 90, False, 50], [770, 460, 110, 160, 3, 90, True, 70], [970, 610, 60, 10, 2]],
            [[0,400,50,10,0],[100, 500,100,10,4,-2,[100,500]],[500,450,40,10,0],[500, 400,50,10,4,-2,[400,700]],[500, 330,60,20,4,-5,[200,600]],[500, 290,100,10,4,-2,[400,900]]],
              [[0, 100, 100, 10, 0], [310, 10, 10, 480, 0], [120, 650, 190, 50, 0], [310, 650, 110, 10, 6], [470, 520, 130, 10, 6], [670, 400, 150, 10, 6], [110, 260, 50, 30, 5],[130,430,50,20,5], [220, 370, 50, 30, 5], [190, 480, 50, 30, 5],
               [210, 140, 40, 90, 5], [830, 300, 140, 10, 2], [970, 60, 10, 650, 0]],
            [[1100,100,100,10,0],[900,0,10,200,5],[900,300,10,400,5],[930,600,30,10,2],[401,300,60,10,4,3,[200,800]],[830,300,70,10,0],[450,240,20,60,5],[250,240,20,60,5],[650,290,40,10,5],[240,380,660,10,5],[100,300,80,10,0],[201,600,60,10,4,3,[0,600]],[190,500,50,200,3,200,True,600],[350,550,30,50,3,200,False,570],[600,600,50,10,6]]
            ]
  endzones = [[920,600,150,50],[920,600,150,50],[800,200,100,100],[970,600,50,20],[970,600,50,20],[1100,100,50,50],[1100,500,50,50],[1100,500,50,50],[920, 600, 150, 50],
              #[920, 240, 150, 50],
              [920, 240, 150, 50],[1030, 510, 150, 50],[800,400,100,70]]
  spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
  cannons = [[],[],[],[],[],[[0,90,0.4,30,0],[0,70,0.4,30,0],[900,590,-1,25,0],[930,540,-2,50,0],[100,300,1,20,0],[100,200,-1,60,0],
                             [100,200,-1,60,0],[100,180,-1,60,0],[100,160,-1,60,0],[100,140,-1,60,0],[100,120,-1,60,0]],
             [[1000,340,-1.5,20,0],[1000,310,-1.5,20,0],[1100,295,-0.6,30,0,0],[1100,280,-2,40,0]],[],[[810, 340, -0.5, 40, 0]],
             #[],
             [],[],[]
             ]
  shots = []
  if level == 0:
    streak = 0
  else:
    streak = None
  while True:
    if not floored:
      trail.append([you[0]+7,you[1]-7])
    if (len(trail) > 6 or floored) and len(trail) > 0:
      trail.pop(0)
    mom = 0
    DISPLAY.fill((0,0,0))
    x = 0
    y = 0
    for i in range(12):
      DISPLAY.blit(back,(x,y))
      x+=300
      if x == 1200:
        x = 0
        y += 300
    you[1] += velocity_y
    you[0] += velocity_x

    if you[1] > 850:
      velocity_y = 0
      velocity_x = 0
      pygame.mixer.music.load("die.mp3")
      pygame.mixer.music.play()
      timer = 0
      if level != 0:
        streak = None
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
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] -= 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          if floor[4] == 1 or floor[4] == 2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y -= 9
          if floor[4] == 5:
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        if floor[1]<you[1]-1<floor[1]+floor[3] and velocity_x < 0 and floor[0]+floor[2]-7<you[0]<floor[0]+floor[2]:
          if floor[4] != 3:
            velocity_x = -velocity_x
            you[0] += 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          elif floor[4] == 3 and floor[6]:
            velocity_x = -velocity_x
            you[0] += 7
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()
          if floor[4] == 1 or floor[4] ==  2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y -= 9
          if floor[4] == 5:
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        if floor[1]-velocity_y<you[1]<floor[1]+floor[3] and floor[0]<you[0]+13 and you[0]+2<floor[0]+floor[2] and velocity_y > 0:
          if floor[4] != 3:
            you[1] = floor[1]
          elif floor[4] == 3 and floor[6]:
            you[1] = floor[1]
          elif floor[4] == 3 and not floor[6]:
            floored = False
          if floor[4] == 1:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y = -0.9*velocity_y
          elif floor[4] == 2:
            pygame.mixer.music.load("bounce2.mp3")
            pygame.mixer.music.play()
            velocity_y = -16
          if floor[4] == 5:
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        if floor[1]<you[1]-15<floor[1]+floor[3]-velocity_y and floor[0]<you[0]+13 and you[0]+2<floor[0]+floor[2] and velocity_y < 0:
          if floor[4] != 3:
            you[1] = floor[1]+floor[3]+15
            velocity_y = 0
          elif floor[4] == 3 and floor[6]:
            you[1] = floor[1]+floor[3]+15
            velocity_y = 0
          if floor[4] == 5:
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        if you[1] == floor[1] and floor[0]<you[0]+12 and you[0]+3<floor[0]+floor[2]:
          if floor[4]!=3:
            if floor[4]!=1 and floor[4]!= 2:
              velocity_y = 0
              floored = True
              if floor[4] == 4:
                you[0] += floor[5]
              if floor[4] == 6:
                dj = True
              else:
                dj = False
          elif floor[4] == 3 and floor[6]:
            velocity_y = 0
            floored = True
          if floor[4] == 5:
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          game_menu()
        if event.key == K_a or event.key == K_LEFT:
          ap = True
        if event.key == K_d or event.key == K_RIGHT:
          dp = True
        if (event.key == K_SPACE or event.key == K_w or event.key == K_UP) and floored:
          pygame.mixer.music.load("jump.mp3")
          pygame.mixer.music.play()
          velocity_y -= 7
        elif (event.key == K_SPACE or event.key == K_w or event.key == K_UP) and dj:
          pygame.mixer.music.load("jump.mp3")
          pygame.mixer.music.play()
          velocity_y = -9
          dj = False
      if event.type == KEYUP:
        if event.key == K_a or event.key == K_LEFT:
          ap = False
        if event.key == K_d or event.key == K_RIGHT:
          dp = False

    for floor in blocks[level]:
      if floor[4]==4:
        pygame.draw.rect(DISPLAY,(140,140,140),(floor[6][0]+int(floor[2]/2),floor[1]+int(floor[3]/2),floor[6][1]-floor[6][0],1))
    for shot in shots:
      shot[0] += shot[2]*7
      if shot[2] < 0:
        DISPLAY.blit(fire,[shot[0]-5,shot[1]-5])
      else:
        DISPLAY.blit(pygame.transform.flip(fire,True,False),(shot[0]-5,shot[1]-5))
      for floor in blocks[level]:
        if (floor[0]<shot[0]<floor[0]+floor[2] and floor[1]<shot[1]<floor[1]+floor[3]) and (floor[4] != 3 or floor[6]):
          shots.pop(shots.index(shot))
          break
      if you[0]<shot[0]<you[0]+15 and you[1]-15<shot[1]<you[1]:
        velocity_y = 0
        velocity_x = 0
        pygame.mixer.music.load("die.mp3")
        pygame.mixer.music.play()
        timer = 0
        streak = None
        spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        streak = None
        spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
        
    if ap:
      if velocity_x > -5:
        velocity_x -= 0.2
    elif velocity_x < 0:
      velocity_x += 0.2
      if velocity_x > -0.2:
        velocity_x = 0
    if dp:
      if velocity_x < 5:
        velocity_x += 0.2
    elif velocity_x > 0:
      velocity_x -= 0.2
      if velocity_x < 0.2:
        velocity_x = 0


    for floor in blocks[level]:
      y = 0
      x = 0
      for i in range((int(floor[2]/10))*(int(floor[3]/10))):
        if floor[4] == 0:
          DISPLAY.blit(stone,(floor[0]+x,floor[1]+y))
        elif floor[4] == 1:
          if int(clock/5)%3 == 0:
            DISPLAY.blit(bounce,(floor[0]+x,floor[1]+y))
          elif int(clock/5)%3 == 1:
            DISPLAY.blit(bounce1,(floor[0]+x,floor[1]+y))
          else:
            DISPLAY.blit(bounce11,(floor[0]+x,floor[1]+y))
        elif floor[4] == 2:
          if int(clock/5)%3 == 0:
            DISPLAY.blit(bounce2,(floor[0]+x,floor[1]+y))
          elif int(clock/5)%3 == 1:
            DISPLAY.blit(bounce21,(floor[0]+x,floor[1]+y))
          else:
            DISPLAY.blit(bounce211,(floor[0]+x,floor[1]+y))
        elif floor[4] == 3 and floor[6]:
          DISPLAY.blit(warp,(floor[0]+x,floor[1]+y))
        elif floor[4] == 4:
          DISPLAY.blit(stone,(floor[0]+x,floor[1]+y))
        elif floor[4] == 5:
          DISPLAY.blit(kill,(floor[0]+x,floor[1]+y))
        elif floor[4] == 6:
          DISPLAY.blit(double,(floor[0]+x,floor[1]+y))
        x+=10
        if x == floor[2]:
          y+=10
          x = 0
      if floor[4] == 4:
        if floor[0] == floor[6][1] or floor[0] == floor[6][0]:
          floor[5] = -floor[5]
        floor[0]+=floor[5]
          
      if floor[4] == 3 and (clock+floor[7]) % floor[5] == 0:
        if floor[6]:
          floor[6] = False
        else:
          floor[6] = True
          if ((floor[0]<you[0]<floor[0]+floor[2])or(floor[0]<you[0]+15<floor[0]+floor[2])) and ((floor[1]<you[1]<floor[1]+floor[3])or(floor[1]<you[1]+15<floor[1]+floor[3])):
            velocity_y = 0
            velocity_x = 0
            pygame.mixer.music.load("die.mp3")
            pygame.mixer.music.play()
            timer = 0
            streak = None
            spawn(you,(blocks[level][0][0]+10,blocks[level][0][1]-50))
    DISPLAY.blit(pygame.transform.scale(endp,(endzones[level][2],endzones[level][3])),(endzones[level][0],endzones[level][1]))

    for cannon in cannons[level]:
      if cannon[2] < 0:
        DISPLAY.blit(cannon_png,(cannon[0],cannon[1]))
      else:
        DISPLAY.blit(pygame.transform.flip(cannon_png,True,False),(cannon[0],cannon[1]))
      if (clock+cannon[4]) % cannon[3] == 0:
        shots.append([cannon[0]+5,cannon[1]+5,cannon[2],(255,0,0)])
                
    if (endzones[level][0]<you[0]<endzones[level][0]+endzones[level][2] or endzones[level][0]<you[0]+15<endzones[level][0]+endzones[level][2]) and endzones[level][1]<you[1]<endzones[level][1]+endzones[level][3]:
      shots = []
      if streak != None:
        streak += 1
      if level == len(blocks)-1:
        t = 300
      else:
        t = 70
      clock = 0
      while 0 < t:
        t -= 1
        for event in pygame.event.get():
          for i in range(12):
            DISPLAY.blit(back,(x,y))
            x+=300
            if x == 1200:
              x = 0
              y += 300
          if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
              game_menu()
        myfont = pygame.font.SysFont('Cambria', 100)
        DISPLAY.blit(myfont.render("Level "+str(level+1)+" cleared!", False, (255, 255, 255)),(100,100))
        DISPLAY.blit(myfont.render("Time: "+str((int(timer/1800)))+":"+str((int(timer/30)%60))+"."+str((timer%30)*3), False, (255, 255, 255)),(100,210))
        if level == len(blocks)-1 and ttimer != None:
          DISPLAY.blit(myfont.render("Completed in: "+str((int(ttimer/1800)))+":"+str((int(ttimer/30)%60))+"."+str((ttimer%30)*3), False, (255, 255, 255)),(100,320))
        elif ttimer != None:
          DISPLAY.blit(myfont.render("Total time: "+str((int(ttimer/1800)))+":"+str((int(ttimer/30)%60))+"."+str((ttimer%30)*3), False, (255, 255, 255)),(100,320))
        if streak != None:
          DISPLAY.blit(myfont.render("Streak "+str(streak), False, (255, 255, 255)),(100,430))
        pygame.display.update()
        fpsClock.tick(FPS)
      timer= 0
      if level == len(blocks)-1:
        level = -1
        ttimer = 0
      level_up()
      velocity_y = 0
      velocity_x = 0
      dp = False
      ap = False
    
    myfont = pygame.font.SysFont('Cambria', 20)
    DISPLAY.blit(myfont.render(str((int(timer/1800)))+":"+str((int(timer/30)%60))+"."+str((timer%30)*3), False, (255, 255, 255)),(1000,30))
    foo = 1
    if dt:
      for i in trail:
        pygame.draw.circle(DISPLAY,(200,200,200),(int(i[0]),int(i[1])),foo)
        foo += 1
    if not 1170>you[0]>0:
      velocity_x = -velocity_x
      ch = you[0] - 600
      if ch > 3:
        ch = 3
      elif ch < -3:
        ch = -3
      you[0] -= ch
    if velocity_x == 0:
      DISPLAY.blit(char,(int(you[0]),int(you[1])-15))
    elif velocity_x > 0:
      if floored:
        if int(clock/3)%2 == 0:
          DISPLAY.blit(char1,(int(you[0]),int(you[1])-15))
        else:
          DISPLAY.blit(char2,(int(you[0]),int(you[1])-15))
      else:
        DISPLAY.blit(char3,(int(you[0]),int(you[1])-15))
    elif velocity_x < 0:
      if floored:
        if int(clock/3)%2 == 0:
          DISPLAY.blit(pygame.transform.flip(char1,True,False),(int(you[0]),int(you[1])-15))
        else:
          DISPLAY.blit(pygame.transform.flip(char2,True,False),(int(you[0]),int(you[1])-15))
      else:
        DISPLAY.blit(pygame.transform.flip(char3,True,False),(int(you[0]),int(you[1])-15))
    message = str(you[0])+','+str(int(you[1])-15)
    b = bytes(message, 'utf-8')
    s.sendall(b)
    data = s.recv(1024)
    pygame.display.update()
    fpsClock.tick(FPS)
    clock+=1
    timer+=1
    if ttimer != None:
      ttimer += 1

start()
run()
