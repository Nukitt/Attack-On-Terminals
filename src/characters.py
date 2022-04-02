from colorama import Back, Fore, Style ,init
init(autoreset=True)
import play
from buildings import *
import os
class character:
    def __init__(self, health, damage , x, y):
        self.health = health
        self.damage = damage
        self.x = x
        self.y = y

class king(character):
    def __init__(self, health, damage , x, y):
        super().__init__(health, damage , x, y)

    def attack(self,enemy,multiplier):
        for building in enemy:
            if isinstance(building, spawn):
                continue
            # if self.y == building.x +1 and self.x in range(building.y,building.y + building.height):
            #     building.health -= self.damage
            # elif self.y == building.x -1 and self.x in range(building.y,building.y + building.height):
            #     building.health -= self.damage
            # elif self.x == building.y +1 and self.y in range(building.x,building.x + building.width):
            #     building.health -= self.damage
            # elif self.x == building.y -1 and self.y in range(building.x,building.x + building.width):
            #     building.health -= self.damage
            if self.y in range(building.x-6,building.x + building.width +6) and self.x in range(building.y-4,building.y + building.height +4):
                building.health -= self.damage * multiplier
            # elif self.y == building.x -1 and self.x in range(building.y-1,building.y + building.height +1):
            #     building.health -= self.damage
            # elif self.x == building.y +1 and self.y in range(building.x-1,building.x + building.width +1):
            #     building.health -= self.damage
            # elif self.x == building.y -1 and self.y in range(building.x-1,building.x + building.width +1):
            #     building.health -= self.damage
        # exit()

    def moveup(self,king,base,multiplier):
        if king.x >2 and base[king.x -1][king.y] == Back.GREEN + ' ':
            if multiplier==2:
                if base[king.x-2][king.y] == Back.GREEN + ' ':
                    king.x -= 2
                else:
                    king.x -= 1
            else:
                king.x -= 1
    def movedown(self,king,base,multiplier):
        if king.x < 59 and base[king.x +1][king.y] == Back.GREEN + ' ':
            if multiplier==2:
                if base[king.x+2][king.y] == Back.GREEN + ' ':
                    king.x += 2
                else: 
                    king.x += 1
            else:
                king.x += 1
    def moveleft(self,king,base,multiplier):
        if king.y > 2 and base[king.x][king.y -1] == Back.GREEN + ' ':
            if multiplier==2:
                if base[king.x][king.y -2] == Back.GREEN + ' ':
                    king.y -= 2
                else:
                    king.y -= 1
            else:
                king.y -= 1
    def moveright(self,king,base,multiplier):
        if king.y < 234 and base[king.x][king.y +1] == Back.GREEN + ' ':
            if multiplier==2:
                if base[king.x][king.y +2] == Back.GREEN + ' ':
                    king.y += 2
                else:
                    king.y += 1
            else:
                king.y += 1
    def show(self,base):
        if self.health < 50 and self.health > 20:
            base[self.x][self.y] = Style.DIM + Back.YELLOW + 'K'
        elif self.health < 20 and self.health >0:
            base[self.x][self.y] = Style.DIM + Back.RED + 'K'
        elif self.health > 50:
            base[self.x][self.y] = Back.MAGENTA + Fore.LIGHTMAGENTA_EX + 'K'
        else:
            base[self.x][self.y] = Back.GREEN + ' '
        return base

class barbarians(character):
    def __init__(self, health, damage , x, y):
        super().__init__(health, damage , x, y)

    def attack(self, enemy):
        enemy.health -= self.damage  

    def show(self,base):
        base[self.x][self.y] = Back.YELLOW + Fore.LIGHTRED_EX + 'B'
        return base