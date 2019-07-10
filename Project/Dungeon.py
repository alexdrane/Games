import random, pygame, sys,os
import math
from math import *
from pygame import *
from random import *
from sys import *


class projectile(object):
  pos = (0,0)
  velocity = (0,0)
  size = 0
  speed = 0
  friendly = False

  def __init__ (self,pos,target,speed,size,friendly,dam):
    self.friendly = friendly
    self.pos = pos
    self.speed = speed
    self.velocity = moveto(target[0],target[1],pos[0],pos[1],speed)
    self.size = size
    self.dam = dam

  def move(self):
    self.pos = (self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1])

  def fmove(self,x,y):
    self.pos = (self.pos[0]+x,self.pos[1]+y)

class enemy(object):
  health = 0
  pos = (0,0)
  image = None
  velocity = (0,0)
  speed = 0


  def __init__(self,health,pos,speed,dim):
    self.health = health
    self.max_health = health
    self.pos = pos
    self.speed = speed
    self.dead = False
    self.dim = dim
    #self.image = image

  def shoot():
    return(pos,(800,500),7)

  def fmove(self,x,y):
    self.pos = (self.pos[0]+x,self.pos[1]+y)

  def target(self,target):
    self.velocity = moveto(target[0],target[1],self.pos[0],self.pos[1],self.speed)

  def move(self):
    newpos = (self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1])
    move = True
    for wall in walls:
      if ((wall[0]*40)+xscroll<newpos[0]<(wall[0]*40)+xscroll+40 or (wall[0]*40)+xscroll<newpos[0]+self.dim[0]<(wall[0]*40)+xscroll+40) and ((wall[1]*40)+yscroll<newpos[1]<(wall[1]*40)+yscroll+40 or (wall[1]*40)+yscroll<newpos[1]+self.dim[1]<(wall[1]*40)+yscroll+40):
        move = False
    if move:
      self.pos = newpos

class wizard(enemy):
  health = 0
  pos = (0,0)
  image = None
  velocity = (0,0)
  speed = 0

  def __init__(self,pos):
    enemy.__init__(self,(20*dif),pos,3,(30,30))
    self.image = wiz
    self.dif = dif

  def calc(self):
    dist = 10000000
    for proj in projs:
      x = proj.pos[0]-self.pos[0]
      y = proj.pos[1]-self.pos[1]
      if sqrt((x*x)+(y*y)) < dist and proj.friendly:
        dist = sqrt((x*x)+(y*y))
        self.target(proj.pos)
        self.velocity = (-self.velocity[0],-self.velocity[1])
      
    if self.pos[0] < 80 or self.pos[0] > 1520 or self.pos[1] < 80 or self.pos[1] > 920:
      self.target((800,500))

    if 700<self.pos[0] < 900 or 400<self.pos[1] < 600:
      self.target((800,500))
      self.velocity = (-self.velocity[0],-self.velocity[1])

    if clock % 40 == 0:
      projs.append(projectile((self.pos[0]+15,self.pos[1]+15),(800,500),10,6,False,10*dif))

class rapid(enemy):
  health = 0
  pos = (0,0)
  image = None
  velocity = (0,0)
  speed = 0

  def __init__(self,pos):
    enemy.__init__(self,35*dif,pos,4,(40,40))
    self.image = rap

  def calc(self):
    dist = 10000000
    for proj in projs:
      x = proj.pos[0]-self.pos[0]
      y = proj.pos[1]-self.pos[1]
      if sqrt((x*x)+(y*y)) < dist and proj.friendly:
        dist = sqrt((x*x)+(y*y))
        self.target(proj.pos)
        self.velocity = (-self.velocity[0],-self.velocity[1])
      
    if self.pos[0] < 80 or self.pos[0] > 1520 or self.pos[1] < 80 or self.pos[1] > 920:
      self.target((800,500))

    if 700<self.pos[0] < 900 or 400<self.pos[1] < 600:
      self.target((800,500))
      self.velocity = (-self.velocity[0],-self.velocity[1])

    if clock % 8 == 0:
      projs.append(projectile((self.pos[0]+15,self.pos[1]+15),(800,500),15,4,False,4*dif))

class melee(enemy):

  health = 0
  pos = (0,0)
  image = None
  velocity = (0,0)
  speed = 0

  def __init__(self,pos):
    enemy.__init__(self,30,pos,4,(30,30))
    self.image = wiz

  def calc(self):
    self.target((800,500))

  def move(self):
    newpos = (self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1])
    move = True
    for wall in walls:
      if (((wall[0]*40)+xscroll<newpos[0]<(wall[0]*40)+xscroll+40 or (wall[0]*40)+xscroll<newpos[0]+30<(wall[0]*40)+xscroll+40) and ((wall[1]*40)+yscroll<newpos[1]<(wall[1]*40)+yscroll+40 or (wall[1]*40)+yscroll<newpos[1]+30<(wall[1]*40)+yscroll+40)) or sqrt(((800-self.pos[0])*(800-self.pos[0]))+((500-self.pos[0])*(500-self.pos[0]))) < 350:
        move = False
        self.explode()
        self.dead = True
    if move:
      self.pos = newpos

  def explode(self):
    for wall in walls:
      if ((wall[0]*40)+xscroll+20-self.pos[0])*((wall[0]*40)+xscroll+20-self.pos[0])+((wall[1]*40)+yscroll+20-self.pos[1])*((wall[1]*40)+yscroll+20-self.pos[1]) < 14400:
        walls.remove(wall)
    if sqrt((800-self.pos[0])*(800-self.pos[0])+(500-self.pos[0])*(500-self.pos[0])) < 350:
      global health
      health -= 20
      
      
    


def generate():
  file = open("Map.txt","w")
  above = ".........................................."
  y = -1
  for i in range(27):
    mapd = ""
    prev = ""
    x = 0
    for i in range(42):
      if (16<x<26 and 10<y<15):
        new = "."
      else:
        new = choice(["#",".",".",".",".",".",".","."])
        if (prev == "#"or above[x]=="#")and randint(1,2) == 2:
          new = "#"
        if new == ".":
          if randint(1,3000) == 12:
            new = "/"
      x += 1
      prev = new
      mapd += new
    file.write(mapd+"\n")
    above = mapd
    y += 1
  

  file.close()

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

def movefrom(mx,my,x,y,speed):
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
  return(-vx,-vy)



def end():
  # saves data and cleans up
  scrollwrite(xscroll,yscroll,traveldx,traveldy)
  writesave(walls)
  pygame.quit()
  sys.exit()

def scrollread():
  # reads precise position data
  file = open("Data1.txt","r")
  lines=file.readlines()
  file.close()
  if lines[4] == "False":
    generate()
  return(int(lines[0]),int(lines[1]),int(lines[2]),int(lines[3]),int(lines[5]))

def scrollwrite(x,y,tx,ty):
  # writes precise position data
  file = open("Data1.txt","w")
  file.write(str(x)+"\n")
  file.write(str(y)+"\n")
  file.write(str(tx)+"\n")
  file.write(str(ty)+"\n")
  file.write("True"+"\n")
  file.write(str(int(health)))
  file.close()
  

def readsave():
  # reads map.txt containing the map
  locs = []
  file = open("Map.txt","r")
  lines=file.readlines()
  y = -1
  for line in lines:
    x = -1
    for foo in list(line):
      if foo != ".":
        locs.append([x,y])
      x += 1
    y += 1
  file.close()
  return(locs)

def writesave(walls):
  # writes map.txt containing the map
  file = open("Map.txt","w+")
  for y in range(27):
    newline = ""
    for x in range(42):
      new = "."
      for wall in walls:
        if wall[0] == x-1 and wall[1] == y-1:
          new = "b"
      newline += new
    file.write(newline+"\n")
  file.close()

def checkbounds(pos):
  if -800<pos[0]<2400 and -800<pos[1]<1800:
    return(False)
  else:
    return(True)
          

def load():
  # loads the graphics, starts up GUI
  global FPS,fpsClock,DISPLAY,wall_image,floor_image,char,chars1,chars2,wiz,clock,projs,rap
  pygame.init()
  pygame.mixer.pre_init(44100, 16, 4, 4096)
  pygame.mixer.init()
  FPS = 30
  fpsClock = pygame.time.Clock()
  DISPLAY = pygame.display.set_mode((1600,1000),FULLSCREEN)
  wall_image = pygame.image.load("Wall.png").convert_alpha()
  floor_image = pygame.image.load("Floor.png").convert_alpha()
  char = pygame.image.load("Char.png").convert_alpha()
  chars1 = pygame.image.load("Charstep1.png").convert_alpha()
  chars2 = pygame.image.load("Charstep2.png").convert_alpha()
  wiz = pygame.image.load("Wiz.png").convert_alpha()
  rap = pygame.image.load("rap.png").convert_alpha()
  main()

def main():

  # main game loop
  global walls,xscroll,yscroll,traveldx,traveldy,projs,clock,health,dif
  xscroll,yscroll,traveldx,traveldy,health = scrollread()
  walls = readsave()
  movement_y = 0
  movement_x = 0
  clock = 0
  disp_map = False
  toggle = False
  terrs = [[3,2,5],[8,8,8],[1,4,4],[3,4,4]]
  SPWNPROB = terrs[0]
  projs = []
  ens = []
  dif = 1
  while True:
    dist = sqrt((traveldx*traveldx) + (traveldy*traveldy))
    dif = sqrt((traveldx*traveldx)+(traveldy*traveldy))/5000
    if clock % 30 == 0:
      if  dist > 30000:
        SPWNPROB = terrs[2]
      elif dist > 20000:
        SPWNPROB = terrs[1]
      elif dist > 10000:
        SPWNPROB = terrs[3]
      else:
        SPWNPROB = terrs[0]
    DISPLAY.fill((100,100,100))
    # event handling loop - sets the movement for the scroll
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          end()
        if event.key == K_w:
          movement_y += 5
        if event.key == K_s:
          movement_y += -5
        if event.key == K_a:
          movement_x += 5
        if event.key == K_d:
          movement_x += -5
        if event.key == K_m:
          disp_map = not disp_map
      if event.type == KEYUP:
        if event.key == K_w:
          movement_y -= 5
        if event.key == K_s:
          movement_y -= -5
        if event.key == K_a:
          movement_x -= 5
        if event.key == K_d:
          movement_x -= -5
      if event.type == MOUSEBUTTONDOWN:
        mx,my = pygame.mouse.get_pos()
        if disp_map:
          newloc = [int((mx-800)*91.2),int((my-500)*91.2)]
          if newloc[0]>32000:
            newloc[0] = 32000
          elif newloc[0]<-32000:
            newloc[0] = -32000
          if newloc[1]>32000:
            newloc[1] = 32000
          elif newloc[1]<-32000:
            newloc[1] = -32000
          if not (-800<newloc[0]-traveldx<800)and not(-800<newloc[1]-traveldy<800):
            traveldx,traveldy = newloc[0],newloc[1]
            generate()
            walls = readsave()
        else:
          if event.button == 1:
            projs.append(projectile((800,500),(mx,my),25,3,True,8))
          if event.button == 3:
            walls.append([int((mx-xscroll)/40),int((my-yscroll)/40)])
        


    # this section checks if it is ok to move - is there a wall in the way?
    movex = True
    movey = True
    for wall in walls:
      if 16<wall[0]<22 and  10<wall[1]<14:
        if (wall[0]*40)+xscroll == 750 and movement_x == 5 and (((wall[1]*40)+yscroll<=485<(wall[1]*40)+yscroll+40)or((wall[1]*40)+yscroll<515<=(wall[1]*40)+yscroll+40)):
          movex = False
        if (wall[0]*40)+xscroll+40 == 850 and movement_x == -5 and (((wall[1]*40)+yscroll<=485<(wall[1]*40)+yscroll+40)or((wall[1]*40)+yscroll<515<=(wall[1]*40)+yscroll+40)):
          movex = False
        if (wall[1]*40)+yscroll == 445 and movement_y == 5 and (((wall[0]*40)+xscroll<=790<(wall[0]*40)+xscroll+40)or((wall[0]*40)+xscroll<810<=(wall[0]*40)+xscroll+40)):
          movey = False
        if (wall[1]*40)+yscroll+40 == 555 and movement_y == -5 and (((wall[0]*40)+xscroll<=790<(wall[0]*40)+xscroll+40)or((wall[0]*40)+xscroll<810<=(wall[0]*40)+xscroll+40)):
          movey = False
        if (790<(wall[0]*40)+xscroll<810 or 790<(wall[0]*40)+xscroll+40 < 810) and (485<(wall[1]*40)+yscroll < 515 or 485<(wall[1]*40)+yscroll+40 < 515):
          yscroll -= movement_y
          xscroll -= movement_x
          traveldx += movement_x
          traveldy += movement_y
          for proj in projs:
            proj.fmove(-movement_x,-movement_y)
          for en in ens:
            en.fmove(-movement_x,-movement_y)
          movex = False
          movey = False
          

    # adds to the scroll if movement is ok
    if not disp_map:
      if movey:
        yscroll += movement_y
        for proj in projs:
          proj.fmove(0,movement_y)
        for en in ens:
          en.fmove(0,movement_y)
        if -32000<traveldy+movement_y<32000: 
          traveldy -= movement_y
      if movex:
        xscroll += movement_x
        if -32000<traveldx+movement_x<32000: 
          traveldx  -= movement_x
        for proj in projs:
          proj.fmove(movement_x,0)
        for en in ens:
          en.fmove(movement_x,0)

    # every time the scroll hits the size of one tile (40px) the coordinates to the map shift, and the scroll resets.
    #This happens for x and y. However there is currently a problem with this section, resulting in the random movement of walls
  
    if yscroll > 40:
      yscroll -= 40
      newtop = True
      for wall in walls:
        wall[1]+=1
      for wall in walls:
        if wall[1] > 30:
          walls.pop(walls.index(wall))
        if wall[1] == -1:
          newtop = False
      if newtop:
        for i in range(randint(1,SPWNPROB[0])):
          walls.append([randint(1,40),-1])
        for wall in walls:
          if wall[1] == 0 and randint(1,SPWNPROB[1]) == 2:
            walls.append([wall[0],-1])
          elif wall[1] == -1 and wall[0] < 40 and randint(1,SPWNPROB[2]) < 3:
            walls.append([wall[0]+1,-1])
        for wall in walls:
          if wall in walls[:walls.index(wall)]:
            walls.remove(wall)
      if randint(1,15) == 3:
        posbs = []
        for x in range(1,41):
          g = False
          if not [x,-1] in walls:
            posbs.append([int(x*40),int(-40)])
            g = True
        if g:
          new = choice(posbs)
          if randint(1,8)<=7:
            ens.append(wizard((new[0],new[1])))
          else:
            ens.append(rapid((new[0],new[1])))

    elif yscroll < -40:
      yscroll += 40
      newbottom = True
      for wall in walls:
        wall[1]-=1
      for wall in walls:
        if wall[1] < -5:
          walls.pop(walls.index(wall))
        if wall[1] == 25:
          newbottom = False
      if newbottom:
        for i in range(randint(1,SPWNPROB[0])):
          walls.append([randint(1,40),25])
        for wall in walls:
          if wall[1] == 24 and randint(1,SPWNPROB[1]) == 2:
            walls.append([wall[0],25])
          elif wall[1] == 25 and wall[0] > 0 and randint(1,SPWNPROB[2]) < 3:
            walls.append([wall[0]-1,25])
        for wall in walls:
          if wall in walls[:walls.index(wall)]:
            walls.remove(wall)
      if randint(1,15) == 3:
        posbs = []
        for x in range(1,41):
          g = False
          if not [x,26] in walls:
            posbs.append([int(x*40),int(26*40)])
            g = True
            
        if g:
          new = choice(posbs)
          if randint(1,8)<=7:
            ens.append(wizard((new[0],new[1])))
          else:
            ens.append(rapid((new[0],new[1])))

              

    if xscroll > 40:
      xscroll -= 40
      newside = True
      for wall in walls:
        wall[0]+=1
      for wall in walls:
        if wall[0] > 45:
          walls.pop(walls.index(wall))
        if wall[0] == -1:
          newside = False
      if newside:
        for i in range(randint(1,SPWNPROB[0])):
          walls.append([-1,randint(1,25)])
        for wall in walls:
          if wall[0] == 0 and randint(1,SPWNPROB[1]) == 2:
            walls.append([-1,wall[1]])
          elif wall[0] == -1 and wall[1] < 25 and randint(1,SPWNPROB[2]) < 3:
            walls.append([-1,wall[1]+1])
        for wall in walls:
          if wall in walls[:walls.index(wall)]:
            walls.remove(wall)
      if randint(1,15) == 3:
        posbs = []
        for y in range(1,26):
          g = False
          if not ([-1,y] in walls):
            posbs.append([int(-1*40),int(y*40)])
            g = True
        if g:
          new = choice(posbs)

          if randint(1,8)<=7:
            ens.append(wizard((new[0],new[1])))
          else:
            ens.append(rapid((new[0],new[1])))
            
    elif xscroll < -40:
      xscroll += 40
      newside = True
      for wall in walls:
        wall[0]-=1
      for wall in walls:
        if wall[0] < -5:
          walls.pop(walls.index(wall))
        if wall[0] == 40:
          newside = False
      if newside:
        for i in range(randint(1,SPWNPROB[0])):
          walls.append([40,randint(1,25)])
        for wall in walls:
          if wall[0] == 39 and randint(1,SPWNPROB[1]) == 2:
            walls.append([40,wall[1]])
          elif wall[0] == 40 and wall[1] > 0 and randint(1,SPWNPROB[2]) < 3:
            walls.append([40,wall[1]-1])
        for wall in walls:
          if wall in walls[:walls.index(wall)]:
            walls.remove(wall)
      if randint(1,15) == 3:
        posbs = []
        for y in range(1,26):
          g = False
          if not ([40,y] in walls):
            posbs.append([int(40*40),int(y*40)])
            g = True
        if g:
          new = choice(posbs)
          if randint(1,8)<=7:
            ens.append(wizard((new[0],new[1])))
          else:
            ens.append(rapid((new[0],new[1])))
    
    for wall in walls:
      if -2<wall[0]<41 and -2<wall[1]<26:
        DISPLAY.blit(wall_image,((wall[0]*40)+xscroll,(wall[1]*40)+yscroll))



    # if there is no wall, a floor is displayed
    for y in range(-1,26):
      for x in range(-1,41):
        if [x,y] in walls:
          pass
        else:
          DISPLAY.blit(floor_image,((x*40)+xscroll,(y*40)+yscroll))

    if -810<traveldx<810 and -510<traveldy<510:
      displayhome = True
    else:
      displayhome = False

    if displayhome:
      for wall in walls:
        if (740-traveldx<(wall[0]*40)+xscroll<860-traveldx or 740-traveldx<(wall[0]*40)+40+xscroll<860-traveldx) and (440-traveldy<(wall[1]*40)+yscroll<560-traveldy or 440-traveldy<(wall[1]*40)+40+yscroll<560-traveldy):
          walls.pop(walls.index(wall))
    if displayhome:
      pygame.draw.rect(DISPLAY,(0,100,0),(780-traveldx,480-traveldy,40,40))

    for proj in projs:
      pygame.draw.circle(DISPLAY,(255,0,0),(int(proj.pos[0]),int(proj.pos[1])),proj.size)
      proj.move()
      cont = True
      for wall in walls:
        if (wall[0]*40)+xscroll<=proj.pos[0]<=(wall[0]*40)+xscroll+40 and (wall[1]*40)+yscroll<=proj.pos[1]<=(wall[1]*40)+yscroll+40:
          if proj.friendly == False:
            walls.remove(wall)
          cont = False
      for en in ens:
        x,y = (en.pos[0]-proj.pos[0]+(en.dim[0]/2))*(en.pos[0]-proj.pos[0]+(en.dim[0]/2)),(en.pos[1]-proj.pos[1]+(en.dim[1]/2))*(en.pos[1]-proj.pos[1]+(en.dim[1]/2))
        if  x+y < 780 and proj.friendly:
          en.health -= proj.dam
          if en.health < 1:
            ens.remove(en)
          cont = False
      if not proj.friendly and 785<=proj.pos[0]<=815 and 485<=proj.pos[1]<=515:
        health -= proj.dam
        cont = False
      if health < 1:
        health = 80
        ens = []
        projs = []
        generate()
        xscroll,yscroll = (0,0)
        traveldx,traveldy = (0,0)
        walls = readsave()
        cont = False
      if cont:
        if checkbounds(proj.pos):
          projs.remove(proj)
      else:
        if len(projs) > 0:
          projs.remove(proj)

    for en in ens:
      en.move()
      DISPLAY.blit(en.image,en.pos)
      pygame.draw.rect(DISPLAY,(255,0,0),(en.pos[0]+1,en.pos[1]+en.dim[1]+5,en.health*(en.dim[0]/en.max_health),5))
      pygame.draw.rect(DISPLAY,(255,255,255),(en.pos[0],en.pos[1]+en.dim[1]+3,en.dim[0]+2,7),2)
      en.calc()
      if checkbounds(en.pos) or en.dead:
        ens.remove(en)

      
      
    
    # this section handles charachter animation
    if movement_x == 0 and movement_y == 0:
      DISPLAY.blit(char,(785,485))
    elif movement_x > 0:
      if int(clock/4)%4 == 0 or int(clock/4)%4 == 2:
        DISPLAY.blit(char,(785,485))
      elif int(clock/4)%4 == 1:
        DISPLAY.blit(chars1,(785,485))
      elif int(clock/4)%4 == 3:
        DISPLAY.blit(chars2,(785,485))
    else:
      if int(clock/4)%4 == 0 or int(clock/4)%4 == 2:
        DISPLAY.blit(pygame.transform.flip(char,True,False),(785,485))
      elif int(clock/4)%4 == 1:
        DISPLAY.blit(pygame.transform.flip(chars1,True,False),(785,485))
      elif int(clock/4)%4 == 3:
        DISPLAY.blit(pygame.transform.flip(chars2,True,False),(785,485))

    pygame.draw.rect(DISPLAY,(200,0,0),(50,50,health*4,50))
    pygame.draw.rect(DISPLAY,(200,200,200),(50,50,322,52),3)

    if disp_map:
      pygame.draw.rect(DISPLAY,(255,255,255),(450,150,700,700))
      pygame.draw.rect(DISPLAY,(0,0,0),(447,147,706,706),3)
      pygame.draw.rect(DISPLAY,(0,100,0),(796,496,8,8))
      DISPLAY.blit(char,(int(780+(traveldx/91.2)),int(480+(traveldy/91.2))))

    #updates screen and clock
    pygame.display.update()
    fpsClock.tick(FPS)
    clock += 1


#game runs from here
load()
