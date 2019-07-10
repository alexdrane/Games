import random
from random import *

file = open("Map.txt","w")
file2 = open("Data1.txt","w")

file2.write(str(0)+"\n")
file2.write(str(0)+"\n")
file2.write(str(0)+"\n")
file2.write(str(0)+"\n")
file2.write("False"+"\n")
file2.write("80"+"\n")

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
file2.close()
