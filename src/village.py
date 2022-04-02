import numpy as np
import os
from colorama import Fore, Back, Style
import buildings
import characters
import play

class build:
    def __init__(self, m, n, base):
        pass

    def initbase(m,n,base):
        for i in range(m):
            for j in range(n):
                base[i][j] = Back.GREEN  + ' '

    def initwalls(self):
        for i in range(50,171):
            play.game.placebuilding(self,buildings.wall(1,1,100,i,15))
            play.game.placebuilding(self,buildings.wall(1,1,100,i,45))
        
        for i in range(15,46):
            play.game.placebuilding(self,buildings.wall(1,1,100,50,i))
            play.game.placebuilding(self,buildings.wall(1,1,100,170,i))

    def inithuts(self):
        play.game.placebuilding(self,buildings.hut(2,2,100,123,24))
        play.game.placebuilding(self,buildings.hut(2,2,100,87,32))
        play.game.placebuilding(self,buildings.hut(2,2,100,169,12))
        play.game.placebuilding(self,buildings.hut(2,2,100,169,50))
        play.game.placebuilding(self,buildings.hut(2,2,100,69,12))

    def initcannon(self):
        play.game.placebuilding(self,buildings.cannon(1,1,100,.2,123,27))
        play.game.placebuilding(self,buildings.cannon(1,1,100,.2,90,32))

    def inittownhall(self):
        play.game.placebuilding(self,buildings.townhall(4,3,100,108,29))

    def initspawnpoint(self):
        play.game.placebuilding(self,buildings.spawn(15,5))
        play.game.placebuilding(self,buildings.spawn(50,50))
        play.game.placebuilding(self,buildings.spawn(125,35))
        