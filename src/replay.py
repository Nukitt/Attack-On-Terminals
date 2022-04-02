import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
from py import builtin
import village
import buildings
import input
import characters
import time
import os
import sys
import time
import subprocess
import builtins

class game:
    buildings=[]
    troops=[]
    moves=[]
    ragemultiplier=1
    ragestarttime=0
    frame=0
    def __init__(self,replayfile):
        # Setting base's size
        cols,rows = 236,53
        base=[[' ' for i in range(cols)] for j in range(rows)]
        self.buildbase(rows,cols,base)
        self.buildwalls()
        self.buildhuts()
        self.buildcannon()
        self.buildtownhall()
        self.buildspawnpoint()

        king = characters.king(100,32,15,20)
        subprocess.Popen(['mpg123', './src/sounds/coc.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # viewbase=1
        replayname="replays/"+replayfile
        file=open(replayname,"r")
        filearr=[]
        for line in file:
            if line=="None":
                filearr.append(None)
            filearr.append(line)
        length=len(filearr)
        while length>0:
            self.showbase(cols,rows,base,king)
            user_input = str(filearr[self.frame])
            print(user_input)
            if user_input != None:
                if user_input[0] == 'w':
                    base[king.x][king.y] = Back.GREEN + ' '
                    king.moveup(king,base,self.ragemultiplier)
                elif user_input[0] == 's':
                    base[king.x][king.y] = Back.GREEN + ' '
                    king.movedown(king,base,self.ragemultiplier)
                elif user_input[0] == 'a':
                    base[king.x][king.y] = Back.GREEN + ' '
                    king.moveleft(king,base,self.ragemultiplier)
                elif user_input[0] == 'd':
                    base[king.x][king.y] = Back.GREEN + ' '
                    king.moveright(king,base,self.ragemultiplier)
                elif user_input[0] == ' ':
                    king.attack(self.buildings,self.ragemultiplier)
                elif user_input[0] == 'k':
                    self.placetroop(characters.barbarians(100,15,50,50))
                    subprocess.Popen(['mpg123', './src/sounds/barbspawn.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif user_input[0] == 'j':
                    self.placetroop(characters.barbarians(100,15,5,15))
                    subprocess.Popen(['mpg123', './src/sounds/barbspawn.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif user_input[0] == 'l':
                    self.placetroop(characters.barbarians(100,15,35,125))
                    subprocess.Popen(['mpg123', './src/sounds/barbspawn.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                elif user_input[0] == 'h':
                    subprocess.Popen(['mpg123', './src/sounds/heal.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # print("\nHealing")
                    # self.heal(self.troops)
                    king.health=min(100,king.health*1.5)
                elif user_input[0] == 'r':
                    subprocess.Popen(['mpg123', './src//sounds/rage.mp3', '2>', '/dev/null'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.ragestarttime=time.time()
                    self.ragemultiplier=2

            if time.time()-self.ragestarttime>=10:
                self.ragemultiplier=1
            self.placetroop(king)
            self.cannonshoot(self.troops)
            self.showbase(cols,rows,base,king)
            self.frame+=1
            length-=1
    def play(self):
        pass
    
    def placebuilding(self,building):
        self.buildings.append(building)

    def placetroop(self,troop):
        self.troops.append(troop)

    def buildbase(self,m,n,base):
        village.build.initbase(m,n,base)

    def buildwalls(self):
        village.build.initwalls(self)

    def buildhuts(self):
        village.build.inithuts(self)

    def buildcannon(self):
        village.build.initcannon(self)

    def buildtownhall(self):
        village.build.inittownhall(self)

    def buildspawnpoint(self):
        village.build.initspawnpoint(self)

    def cannonshoot(self,troops):
        for building in self.buildings:
            if isinstance(building,buildings.cannon):
                building.shoot(troops)

    # def heal(self,troops):
    #     for troop in troops:
    #         troop.health=troop.health + troop.health/2

    def showbase(self,cols,rows,base,king):
        cannonhealth=0
        townhallhealth=0
        huthealth=0
        for troop in self.troops:
            base=troop.show(base)
        
        for building in self.buildings:
            base=building.show(base)
            if isinstance(building,buildings.cannon):
                cannonhealth+=building.health
            if isinstance(building,buildings.townhall):
                townhallhealth+=building.health
            if isinstance(building,buildings.hut):
                huthealth+=building.health
        
        sys.stdout.write("\033[%d;%dH" % (0, 0))
        # sys.stdout.write('\033[?25l')
        # sys.stdout.write('\x1b[?25l')
        # sys.stdout.write('\b'*14160)
        row=[]
        for i in range(rows):
            for j in range(cols):
                # print(base[i][j], end='')
                if i==15 and j==5:
                    sys.stdout.write(Back.GREEN + ' ')
                if i==2 and j==3:
                    sys.stdout.write(Back.CYAN + Fore.RED + "King's Health : " + str(max(round(king.health),0)))
                if king.health<=0:
                    os.system('clear')
                    print("You lose")
                    sys.exit()
                if cannonhealth<=0 and huthealth<=0 and townhallhealth<=0:
                    os.system('clear')
                    print("You win")
                    sys.exit()
                else:
                    sys.stdout.write(base[i][j])
                # row.append(base[i][j])
            # print(''.join(row))
