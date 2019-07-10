import random
import time

class shield(object):
  name = ""
  block = 0
  def __init__(self,name,block):
   self.name = name
   self.block = block

class weapon(object):
  name = ""
  hit = 0
  crit = 0
  crit_prob = 0
  price = 0
  def __init__(self,name,hit,crit,crit_prob, price):
    self.name = name
    self.hit = hit
    self.crit = crit
    self.crit_prob = crit_prob
    self.price = price

class sweapon(object):
  name = ""
  hit = 0
  turns = 0
  price = 0
  mssg = ""
  def __init__(self,name,hit,turns,price,mssg):
    self.name = name
    self.hit = hit
    self.turns = turns
    self.price = price
    self.mssg = mssg

class eweapon(object):
  name = ""
  hit = 0
  crit = 0
  crit_prob = 0
  crit_prob_set = 0
  def __init__(self,name,hit,crit,crit_prob):
    self.name = name
    self.hit = hit
    self.crit = crit
    self.crit_prob = crit_prob
    self.crit_prob_set = crit_prob

class char(object):
  name = ""
  weapon = None
  second = None
  sheild = None
  silver = 0
  health = 0
  sethealth = 0
  typ = ""
  line = ""
  def __init__(self,name,weapon,second,health, typ, line, sheild,silver):
    self.name = name
    self.weapon = weapon
    self.second = second
    self.health = health
    self.typ = typ
    self.line = line
    self.sheild = sheild
    self.sethealth = health
    self.silver = silver

class enmy(object):
  name = ""
  eweapon = None
  shield = None
  st = 0
  health = 0
  typ = ""
  line = ""
  enrage = False
  silver = 0
  def __init__(self,name,eweapon,health, typ, line, shield,st,silver,enrage):
    self.name = name
    self.eweapon = eweapon
    self.health = health
    self.typ = typ
    self.line = line
    self.shield = shield
    self.sethealth = health
    self.enrage = enrage
    self.st = st
    self.silver = silver

class mission(object):
  name = ""
  mis = None
  comp = "No"
  unlock = ""
  def __init__(self,name,mis,unlock):
    self.name = name
    self.mis = mis
    self.unlock = unlock


def select(n):
  global you
  print("Hello and welcome! Please enter your name:")
  name = input().lower().capitalize()
  print("To start please choose a class: Warrior, Archer, Mage")
  while True:
    c = input()
    if c.lower().strip() == "warrior":
      print("Class selected! You are now "+name+", mighty warrior!")
      you = char(name,sword,None,30,"Warrior","",None,0+n)
      break
    elif c.lower().strip() == "archer":
      print("Class selected! You are now "+name+", a silent but deadly archer!")
      you = char(name,bow,None,20,"Archer","",None,0+n)
      break
    elif c.lower().strip() == "mage":
      print("Class selected! You are now "+name+", a wise powerful mage!")
      you = char(name,staff,None,25,"Mage","",None,0+n)
      break
    else:
      print("Sorry, please try again")

def fight(enemy):
  ech = 0
  i = 1
  save = enemy.eweapon.hit
  while True:
    print("Oh no! The "+enemy.typ+" "+enemy.name+" is attacking you!")
    time.sleep(2)
    print(enemy.name+" "+enemy.line+" Their "+enemy.eweapon.name+" will do "+str(enemy.eweapon.hit)+" damage on a hit, and "+str(enemy.eweapon.crit)+" for critical damage! They have "+str(enemy.health)+" HP")
    time.sleep(4)
    while enemy.health > 0 and you.health > 0:
      print()
      do = input("What do you do?")
      if do.lower() == "f":
        ch = random.randint(1,(you.weapon.crit_prob))
        if ch == 1:
          print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.crit)+" damage! It's a critical hit!")
          enemy.health = enemy.health - you.weapon.crit
        else:
          print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.hit)+" damage!")
          enemy.health = enemy.health - you.weapon.hit
        if enemy.health < 0:
          enemy.health = 0
        print(enemy.name+ " is down to "+str(enemy.health)+" HP")
      elif do.lower() == "b":
        if you.sheild == None:
          print("Oops! No sheild equiped")
      elif do.lower() == "c":
        if you.second == None :
          print("Oops! No secondary weapon equiped!")
        elif you.second.turns == 0:
          print("This weapon has no uses left!")
        else:
          print(you.second.mssg+" "+enemy.name+"! It does "+str(you.second.hit)+"damage!")
          you.second.turns = you.second.turns - 1
          print(str(you.second.turns)+" uses left.")
          enemy.health = enemy.health - you.second.hit
          print(enemy.name+ " is down to "+str(enemy.health)+" HP")
      else:
        print(" Sorry, please try again.")
      print()
      time.sleep(1)
      if (enemy.health > 0) and do.lower() == "f":
        print("Now "+enemy.name+" is attacking you!")
        if ech == 1:
          print("Oh no! It's a critical hit! "+enemy.name+" did "+str(enemy.eweapon.crit)+" damage with their "+enemy.eweapon.name+"!")
          you.health = you.health - enemy.eweapon.crit
        else:
          print(enemy.name+" did "+str(enemy.eweapon.hit)+" damage with their "+enemy.eweapon.name+"!")
          you.health = you.health - enemy.eweapon.hit
        if you.health < 0:
          you.health = 0
        print("You have "+str(you.health)+" HP")
        ech = random.randint(1,(enemy.eweapon.crit_prob))
        if ech == 1:
          print(enemy.name + " prepares for a critical attack!")
      elif do.lower() == "b":
        if you.sheild == None:
          print("You have no sheild, so "+enemy.name+" does critical damage!")
          you.health = you.health - enemy.eweapon.crit
        else:
          if ech != 1:
            if you.sheild.block >= enemy.eweapon.hit:
              print("You blocked the enemy's attack!")
            else:
              print("Your sheild blocked some damage, but you still took "+str(enemy.eweapon.hit-you.sheild.block)+" damage.")
              you.health = you.health - (enemy.eweapon.hit-you.sheild.block)
          elif ech == 1:
            if you.sheild.block >= enemy.eweapon.crit:
              print("You blocked the enemy's attack!")
            else:
              print("Your sheild blocked some damage, but you still took "+str(enemy.eweapon.crit-you.sheild.block)+" damage.")
              you.health = you.health - (enemy.eweapon.crit-you.sheild.block)
        if you.health < 0:
          you.health = 0
        print("You have "+str(you.health)+" HP")
        ech = random.randint(1,(enemy.eweapon.crit_prob))
        if ech == 1:
          print(enemy.name + " prepares for a critical attack!")
      if enemy.health < int(round(enemy.sethealth/3)) and enemy.enrage == True:
        print("The enemy is enraged!")
        g = enemy.eweapon.crit
        i = 0
        enemy.eweapon.crit_prob = round(enemy.eweapon.crit_prob/2)
        enemy.enrage = False
        enemy.eweapon.hit = int(enemy.eweapon.hit*2)
        enemy.eweapon.crit = int(enemy.eweapon.crit*1.5)
    if i == 0:
        enemy.enrage = True
        enemy.eweapon.crit_prob = enemy.eweapon.crit_prob_set
        enemy.eweapon.hit = save
        enemy.eweapon.crit = g
    if you.health <= 0:
      enemy.health = enemy.sethealth
      return(False)
    else:
      enemy.health = enemy.sethealth
      print("Congratulations! You defeated "+enemy.name+"!")
      you.silver = you.silver + enemy.silver
      print("The enemy had "+str(enemy.silver)+" silver! You now have "+str(you.silver)+" silver!")
      return(True)

def fight_shielded(enemy):
  ech = 0
  i = 1
  shield = enemy.shield
  save = enemy.eweapon.hit
  if you.second != None:
    turns = you.second.turns
  while True:
    print("Oh no! The "+enemy.typ+" "+enemy.name+" is attacking you!")
    time.sleep(2)
    print(enemy.name+" "+enemy.line+" Their "+enemy.eweapon.name+" will do "+str(enemy.eweapon.hit)+" damage on a hit, and "+str(enemy.eweapon.crit)+" for critical damage! They have "+str(enemy.health)+" HP")
    time.sleep(4)
    tts = None
    while enemy.health > 0 and you.health > 0:
      if tts != None:
        tts = tts-1
      print()
      do = input("What do you do?")
      if do.lower() == "f":
        ch = random.randint(1,(you.weapon.crit_prob))
        if ch == 1:
          if enemy.shield > 0:
            print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.crit)+" damage to their sheild! It's a critical hit!")
            enemy.shield = enemy.shield - you.weapon.crit
            if enemy.shield <= 0:
              tts = enemy.st+1
              print("Shield down!")
              enemy.shield = 0
            print(enemy.name+ " has "+str(enemy.shield)+" shield!")
            print(enemy.name+ " has "+str(enemy.health)+" HP")
          else:
            print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.crit)+" damage! It's a critical hit!")
            enemy.health = enemy.health - you.weapon.crit
            if enemy.health < 0:
              enemy.health = 0
            print(enemy.name+ " is down to "+str(enemy.health)+" HP!")
          if tts == 0:
            print(enemy.name+"'s shield regenerated.")
            enemy.shield = shield
            tts = None
        else:
          if enemy.shield > 0:
            print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.hit)+" damage to their shield!")
            enemy.shield = enemy.shield - you.weapon.hit
            if enemy.shield <= 0:
              enemy.shield = 0
              tts = enemy.st
              print("Shield down!")
            print(enemy.name+ " has "+str(enemy.shield)+" shield!")
            print(enemy.name+ " has "+str(enemy.health)+" HP")
          else:
            print("You attack! Your "+you.weapon.name.lower()+" does "+str(you.weapon.hit)+" damage!")
            enemy.health = enemy.health - you.weapon.hit
            if enemy.health <= 0:
              enemy.health = 0
            print(enemy.name+ " is down to "+str(enemy.health)+" HP!")
          if tts == 0:
            print(enemy.name+"'s shield regenerated.")
            enemy.shield = shield
            tts = None
      elif do.lower() == "b":
        if you.sheild == None:
          print("Oops! No sheild equiped")
        if tts == 0:
          print(enmy.name+"'s shield regenerated.")
          enemy.shield = shield
          tts = None
      elif do.lower() == "c":
        if you.second == None:
          print("Oops! No secondary weapon equiped!")
        elif you.second.turns == 0:
          print("This weapon has no uses left!")
        else:
          you.second.turns = you.second.turns - 1
          print(str(you.second.turns)+" uses left.")
          if enemy.shield > 0:
            print(you.second.mssg+" "+enemy.name+"! It does "+str(you.second.hit)+"damage to the enemy's shield!")
            enemy.shield = enemy.shield - you.second.hit
            if enemy.shield <= 0:
              tts = enemy.st+1
              print("Shield down!")
              enemy.shield = 0
            print(enemy.name+ " has "+str(enemy.shield)+" shield!")
            print(enemy.name+ " has "+str(enemy.health)+" HP")
          else:
            print(you.second.mssg+" "+enemy.name+"! It does "+str(you.second.hit)+"damage to the enemy's shield!")
            enemy.health = enemy.health - you.second.hit
            if enemy.health < 0:
              enemy.health = 0
            print(enemy.name+ " is down to "+str(enemy.health)+" HP!")
          if tts == 0:
            print(enemy.name+"'s shield regenerated.")
            enemy.shield = shield
            tts = None
      else:
        print(" Sorry, please try again.")
      print()
      time.sleep(1)
      if (enemy.health > 0) and do.lower() == "f":
        print("Now "+enemy.name+" is attacking you!")
        if ech == 1:
          print("Oh no! It's a critical hit! "+enemy.name+" did "+str(enemy.eweapon.crit)+" damage with their "+enemy.eweapon.name+"!")
          you.health = you.health - enemy.eweapon.crit
        else:
          print(enemy.name+" did "+str(enemy.eweapon.hit)+" damage with their "+enemy.eweapon.name+"!")
          you.health = you.health - enemy.eweapon.hit
        if you.health < 0:
          you.health = 0
        print("You have "+str(you.health)+" HP")
        ech = random.randint(1,(enemy.eweapon.crit_prob))
        if ech == 1:
          print(enemy.name + " prepares for a critical attack!")
      elif do.lower() == "b":
        if you.sheild == None:
          print("You have no sheild, so "+enemy.name+" does critical damage!")
          you.health = you.health - enemy.eweapon.crit
        else:
          if ech != 1:
            if you.sheild.block >= enemy.eweapon.hit:
              print("You blocked the enemy's attack!")
            else:
              print("Your sheild blocked some damage, but you still took "+str(enemy.eweapon.hit-you.sheild.block)+" damage.")
              you.health = you.health - (enemy.eweapon.hit-you.sheild.block)
          elif ech == 1:
            if you.sheild.block >= enemy.eweapon.crit:
              print("You blocked the enemy's attack!")
            else:
              print("Your sheild blocked some damage, but you still took "+str(enemy.eweapon.crit-you.sheild.block)+" damage.")
              you.health = you.health - (enemy.eweapon.crit-you.sheild.block)
        if you.health < 0:
          you.health = 0
        print("You have "+str(you.health)+" HP")
        ech = random.randint(1,(enemy.eweapon.crit_prob))
        if ech == 1:
          print(enemy.name + " prepares for a critical attack!")
      if enemy.health < int(round(enemy.sethealth/3)) and enemy.enrage == True:
        print("The enemy is enraged!")
        g = enemy.eweapon.crit
        i = 0
        enemy.eweapon.crit_prob = round(enemy.eweapon.crit_prob/2)
        enemy.enrage = False
        enemy.eweapon.hit = int(enemy.eweapon.hit*2)
        enemy.eweapon.crit = int(enemy.eweapon.crit*1.5)
    if i == 0:
        enemy.enrage = True
        enemy.eweapon.crit_prob = enemy.eweapon.crit_prob_set
        enemy.eweapon.hit = save
        enemy.eweapon.crit = g
    if you.health <= 0:
      enemy.health = enemy.sethealth
      if you.second != None:
        you.second.turns = turns
      enemy.shield = shield
      return(False)
    else:
      enemy.health = enemy.sethealth
      enemy.shield = shield
      if you.second != None:
        you.second.turns = turns
      print("Congratulations! You defeated "+enemy.name+"!")
      you.silver = you.silver + enemy.silver
      print("The enemy had "+str(enemy.silver)+" silver! You now have "+str(you.silver)+" silver!")
      enemy.silver = int(enemy.silver * 0.6)
      return(True)












#weapons
sword = weapon("Sword",3,4,3,0)
bow = weapon("Bow", 2,10,5,0)
staff = weapon("Magic Staff",3,5,4,0)

b1 = weapon("Sturdy Bow",4,15,6,100)
b2 = weapon("Steel Bow",6,20,6, 200)
b3 = weapon("Bow of the True",9,25,7, 400)
b4 = weapon("Unflinching Bow",7,30,4, 800)
ai=[b1,b2,b3,b4]

st1 = weapon("Sorcerer's Staff",5,9,4,100)
st2 = weapon("Wind Staff",7,10,4,200)
st3 = weapon("Earth staff",9,14,4,400)
st4 = weapon("Fire staff",11,16,4,800)
mi = [st1,st2,st3,st4]

s1 = weapon("Sturdy Sword",5,7,3,100)
s2 = weapon("Steel sword", 7,9,4,200)
s3 = weapon("Sharpened Sword",10,13,3,400)
s4 = weapon("Sword of the slayer",15,20,3,800)
wi = [s1,s2,s3,s4]

#secondary weapons
clb = sweapon("Steel Mace",8,4,0,"You swing your steel mace")
dag = sweapon("Sly Dagger", 12,3,0,"You throw your sly dagger")
book = sweapon("Book of Runes",10,3,0,"Your book af light fires a beam of light at")

#sheilds
cloak = shield("Steel cloak",15)
war = shield("Metal shield",9)
wall = shield("Magic wall", 11)


# enemy weapons
club = eweapon("Goblin Club",2,4,6)
devclub = eweapon("devestating ogre club", 1,10,3)
razespear = eweapon("Razing spear of the Darkblade", 10,25,6)
devclub2 = eweapon("devestating ogre club", 2,10,4)
ss = eweapon("Summoning staff", 4,11,5)
# enemies
goblin1 = enmy("Gruckelhuft", club, 28,"goblin","likes to play nasty!",None,None, 25,False)
ogre1 = enmy("Burk", devclub, 32,"ogre","will probably smash you with his critical!",None,None, 75,True)
darkblade = enmy("Gul Oruk", razespear,500, "darkblade of the fith realm","is a all powerful warrior of the Dark.",None,None,500,False)
witch2 = enmy("Gruntilda",ss, 30,"shielded witch","is a powerful witch of the three!",12,1,200,False)
witch1 = enmy("Hag Ural",devclub2, 34,"ogre guard","is protected by a strange sheild...",4,3,100,True)


you = None

def m1():
  con = None
  print("You attack the shielded witch!")
  while True:
    l = fight_shielded(witch1)
    if l == False:
      print("You have failed to defeat the "+witch1.typ+" "+witch1.name+". ")
      con = input("Continue? yes/no").lower()
      if con == "yes":
        print("Restarting at the last checkpoint...")
        time.sleep(4)
        you.health = you.sethealth
      else:
        break
    else:
      break
  if con == "yes" or con == None:
    input("As you loot "+witch1.name+", you notice something. A secondary weapon!")
    if you.typ == "Warrior":
      you.second = clb
    elif you.typ == "Archer":
      you.second = dag
    elif you.typ == "Mage":
      you.second = book
    print("Your secondary weapon is the "+you.second.name+"! It does "+str(you.second.hit)+"when used. However, it can only be used "+str(you.second.turns)+" times per battle. This should help you fight the witch!")
    while True:
      l = fight_shielded(witch2)
      if l == False:
        print("You have failed to defeat the "+witch2.typ+" "+witch2.name+". ")
        con = input("Continue? yes/no").lower()
        if con == "yes":
          print("Restarting at the last checkpoint...")
          time.sleep(4)
          you.health = you.sethealth
        else:
          break
      else:
        break
  if con == "yes" or con == None:
    mis1.comp = "Yes"
    mis2.unlock = "Yes"

def m2():
  print("")

def m3():
  print("")

mis1 = mission("Hunt for the sheilded witch", m1, "Yes")
mis2 = mission("The vault", m2, "No")
mis3 = mission("The bandits", m3, "No")
missions = [mis1,mis2,mis3]

def area():
  bp = 100
  b = 1.5
  while True:
    while True:
      try:
        buy = int(input("Who would you like to visit? In order press numbers 1 - 4 to visit the Armoury, the Medic, the Cheif or the Arena"))
      except ValueError:
        print("Sorry, please try again")
      else:
        break
    if buy == 1:
      print("You go to the armoury. Ttamy, the dwarf weapon smith, greets you.")
      print("Items for sale today:")
      if you.typ == "Warrior":
        weps = wi
      elif you.typ == "Archer":
        weps = ai
      elif you.typ == "Mage":
        weps = mi
      print("You have "+str(you.silver)+" silver")
      cnt = 1
      for i in weps:
        print(str(cnt)+") "+i.name+": "+str(i.hit)+" damage for a hit, "+str(i.crit)+" damage for a critical. Costs: "+str(i.price) +" silver.")
        cnt += 1
      yn = input("Would you like to buy, "+you.name+"? yes/no")
      if yn.lower() == "yes" :
        while True:
          try:            
            num = int(input("Enter the number of the weapon you would like to buy:"))
          except ValueError:
            print("Please try again")
          else:
            break
        if weps[num-1].price > you.silver:
          print("Sorry, not enough silver")
        else:
          you.silver = you.silver - weps[num-1].price
          you.weapon = weps[num-1]
          print("Your weapon is now "+you.weapon.name+"!") 
    elif buy == 2: 
      print("Grindalf greets you")
      print("You have "+str(you.silver)+" silver")
      yn = input("'Would you like to boost your health, "+you.name+"?' Costs: "+str(int(bp))+" silver yes/no")
      if yn.lower() == "yes" :
        if you.silver >= bp:
          you.sethealth = int(you.sethealth*b)
          print("You now have "+str(you.sethealth)+" HP")
          bp = bp*1.5
          you.silver = int(you.silver-bp)
          if b > 1.1:
            b = b-0.1
        else:
          print("Not enough silver")
    elif buy == 3:
      you.health = you.sethealth
      print("The cheif, Al Darob, greets you. Available missions:")
      cnt = 1
      print()
      for m in missions:
        print(str(cnt)+") Mission: "+m.name)
        print("Unlocked: "+m.unlock)
        print("Completed: "+m.comp)
        print()
        cnt += 1
      while True:
        try:
          inp = int(input("Enter the number of the mission:"))
        except ValueError:
          print("Please try again")
        else:
          break
      if inp > cnt or inp < 1:
        print("Enter a number in the range")
      elif missions[inp-1].unlock == "No":
        print("Mission must be unlocked first")
      else:
        missions[inp-1].mis()
    elif buy == 4: 
      input("Welcome to the Arena! here you fight enemy players! If you win you gain silver, but if you lose... Then you lose your silver. You must have at least 20 silver to begin.")
      while True:
        mon = 0
        print(str(you.silver)+" silver")
        if you.silver >= 20:
          yn = input("Would you like to enter the arena? yes/no").lower()
          if yn == "yes":
            you.health = you.sethealth
            #sec = you.second
            #you.second = None
            while mon >you.silver or mon < 20:
              while True:
                try:
                  mon = int(input("How much would you like to risk? Must be at least 20 silver but can't be more than your silver"))
                except ValueError:
                  print("Please try again")
                else:
                  break
            name = ""
            conts = ["c","b","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","x","z","ch","ck","ll","th"]
            v = ["a","e","i","o","u","e"]
            vls = ["oo","ei","ie","ai","ee"]
            for i in range(len(v)):
              vls.append(v[i])
            for i in range(1,random.randint(3,6)):
              if i % 2 == 1:
                name = name + conts[random.randint(0,random.randint(1,len(conts)-1))] 
              else:
                name = name + vls[random.randint(0,random.randint(1,len(vls)-1))]
            name = name.capitalize()
            i = ["Warrior","Mage","Archer"]
            tp = i[random.randint(0,2)]
            i = random.randint(0,3)
            if i == 0:
              ree = True
            else:
              ree = False
            monv = mon
            if monv > 150:
              monv = 150
            if tp == "Warrior":
              wep = eweapon("Sword",int(you.weapon.hit*(random.randint(100+monv,120+monv)/200)),int(you.sheild.block*(random.randint(80+monv,100+monv))/200),you.weapon.crit_prob-1)
            elif tp == "Archer":
              wep = eweapon("Bow",int(you.weapon.hit*(random.randint(40+monv,60+monv)/200)),int(you.sheild.block*(random.randint(80+monv,100+monv))/200),you.weapon.crit_prob+2)
            elif tp == "Mage":
              wep = eweapon("Staff",int(you.weapon.hit*(random.randint(40+monv,60+monv)/200)),int(you.sheild.block*(random.randint(80+monv,100+monv))/200),you.weapon.crit_prob+1)
            ran = enmy(name, wep, you.health ,tp,"wants your silver!",None,None,int(mon*random.randint(60,110)/100),ree)
            
            l = fight(ran)
            if l == False:
              print("You give "+str(mon)+" to "+ran.name+"... Better luck next time!")
              you.silver = you.silver - mon
            #you.second = sec
            
          elif yn == "no":
            break
          else:
            print("Please try again")
        else:
          break

      
    else:
      print("Sorry, please try again.")

def game():
  select(0)
  time.sleep(1)
  input("You begin your adventures in the deep woods of the lost. Many villanous scum lurk in this area, and you only have "+str(you.health)+" HP. However, as a "+you.typ+" you know you can rely on your trusty "+you.weapon.name.lower()+" to get you out of a hard situation. Press f to use you weapon in a fight.")
  while(True):
    l=fight(goblin1)
    if l == False:
      print("You have failed to defeat the "+goblin1.typ+" "+goblin1.name+". Restarting at the last checkpoint...")
      time.sleep(4)
      you.health = you.sethealth
    else:
      break
  you.health = you.sethealth
  input("Victourious, you continue on. However, as you pass, you notice the goblins stash. Curious, you decide to investigate.")
  if you.typ == "Warrior":
    you.sheild = war
  elif you.typ == "Archer":
    you.sheild = cloak
  elif you.typ == "Mage":
    you.sheild = wall
  input("A "+you.sheild.name+"! This will block "+str(you.sheild.block)+" damage off the next turn when used by pressing b!")
  input("You hear a deep moan. An Ogre! It's time to test out your new "+you.sheild.name+"...")
  while(True):
    l=fight(ogre1)
    if l == False:
      print("You have failed to defeat the "+ogre1.typ+" "+ogre1.name+". Restarting at the last checkpoint...")
      time.sleep(4)
      you.health = you.sethealth
    else:
      break
  input("As you leave the forest, you have to stop yourself just before you skid of a cliff. You curse yourself. You'll have to go back.")
  time.sleep(4)
  input("Suddenly you feel a change. Your health has not regenerated after defeating Burk. You are left on "+str(you.health)+"HP! You feel a cold presence behind your back. Turning, you see a dark figure. Gul Orok, the darkblade, stands in front of you.")
  print()
  time.sleep(1)
  l = fight(darkblade)
  while(True):
    if l == False:
      print("Laughing, Gul Orok throws your dead body of the cliff, and walks off into the forest...")
      time.sleep(4)
      break
    else:
      break
  input("1 day later...")
  input("You wake in a strange bed. Strange mutterings fill your head. How is this possible? You ...... Died. But it seems somehow you are now alive.")
  input("A figur walks to your side. Straining your eyes, you can make them out as an elf.")
  g = input("'Greetings, stranger! Good to see you awake! How do you feel?' Fine/Awful")
  if g.lower() == "fine":
    input("'Glad to hear it! You certainly look better than the corpse I dragged in here yestarday!'")
  elif g.lower() == "awful":
    input("'Well so would I after being impaled and thrown of a cliff! Don't worry, the ressurection potion works slower on some")
  input("'Welcome to the town, your home-from-home. It is for most people since the Darkblades enslaved the four realms! How rude of me, not introducing myself. My name is Grindalf, an elf and the town medic. I managed to save you with a ressurection potion, but you should be more careful. Things like that are rare nowdays.'")
  input("'In the town you can find many people. You can buy weapons, spells, sheilds, potions, you name it and we have it! Well at least some of it. The Darklades took the rest.'")
  you.sethealth = int(you.sethealth*1.5)
  you.health = you.sethealth
  input("Your going to need some more health. I'm boosting your health to "+int(you.sethealth)+" HP. You can come to me and have your health boosted for some silver anytime.")
  input("'Well first, you should buy some new gear. That lot was no good after you ... you know. Then go to the cheif. There you can find a mission. The cheif is organising the hunt for a witch right now, I belive. You might need some new gear. Also anytime you can go to the tavern to try earn money. Good luck, "+you.typ.lower()+"!'")
  area()

def test(n):
  select(n)
  if you.typ == "Warrior":
    you.sheild = war
  elif you.typ == "Archer":
    you.sheild = cloak
  elif you.typ == "Mage":
    you.sheild = wall
  #if you.typ == "Warrior":
  #  you.second = clb
  #elif you.typ == "Archer":
  #  you.second = dag
  #elif you.typ == "Mage":
   # you.second = book
  you.sethealth = int(you.sethealth*1.5)
  area()

test(100)
game()
