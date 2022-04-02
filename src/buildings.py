from colorama import Fore, Back, Style , init
init(autoreset=True)

class building:
    def __init__(self, height, width , health, x, y):
        self.height = height
        self.width = width
        self.health = health
        self.x = x
        self.y = y

class wall(building):
    def __init__(self, height, width , health, x, y):
        super().__init__(height, width , health, x ,y)
    
    def show(self,base):
        for i in range(self.height):
            for j in range(self.width):
                if self.health < 50 and self.health > 20:
                    base[self.y][self.x] = Style.DIM + Back.YELLOW + 'W'
                elif self.health < 20 and self.health >0:
                    base[self.y][self.x] = Back.RED + 'W'
                elif self.health > 50:
                    base[self.y][self.x] = Back.WHITE + 'W'
                else :
                    base[self.y][self.x] = Back.GREEN + ' '
        return base

class townhall(building):
    def __init__(self, height, width , health, x, y):
        super().__init__(height, width , health, x ,y)

    def show(self,base):
        for i in range(self.height):
            for j in range(self.width):
                if self.health < 50 and self.health > 20:
                    base[self.y+i][self.x+j] = Style.DIM + Back.LIGHTBLUE_EX + 'T'
                elif self.health < 20 and self.health >0:
                    base[self.y+i][self.x+j] = Back.RED + 'T'
                elif self.health > 50:
                    base[self.y+i][self.x+j] = Back.YELLOW + 'T'
                else:
                    base[self.y + i][self.x + j] = Back.GREEN + ' '
        return base

class hut(building):
    def __init__(self, height, width , health, x, y):
        super().__init__(height, width , health, x ,y)

    def show(self,base):
        for i in range(self.height):
            for j in range(self.width):
                if self.health < 50 and self.health > 20:
                    base[self.y+i][self.x+j] = Style.DIM + Back.YELLOW + 'H'
                elif self.health < 20 and self.health >0:
                    base[self.y+i][self.x+j] = Style.DIM + Back.RED + 'H'
                elif self.health > 50:
                    base[self.y+i][self.x+j] = Back.BLUE + 'H'
                else:
                    base[self.y + i][self.x + j] = Back.GREEN + ' '
        return base

class cannon(building):
    def __init__(self, height, width , health, damage, x, y):
        super().__init__(height, width , health, x ,y)
        self.damage = damage
        self.fire=False

    def shoot(self,troops):
        if self.health > 0:
            fireflag=False
            for troop in troops:
                if troop.y in range(self.x-7,self.x + self.width +7) and troop.x in range(self.y-6,self.y + self.height +6):
                    troop.health-=(self.damage)
                    fireflag=True
                    self.fire=True
            if (not fireflag):
                self.fire=False
                # if troop.health<=0:
                    # troops.remove(troop)
                # break

    def show(self, base):
        if self.fire:
            for i in range(self.height):
                for j in range(self.width):
                    if self.health < 50 and self.health > 20:
                        base[self.y+i][self.x+j] = Style.DIM + Back.YELLOW + 'C'
                        base[self.y+i+1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i+1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                    elif self.health < 20 and self.health >0:
                        base[self.y+i][self.x+j] = Style.DIM + Back.LIGHTGREEN_EX + 'C'
                        base[self.y+i+1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i+1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                    elif self.health > 50:
                        base[self.y+i][self.x+j] = Back.RED + 'C'
                        base[self.y+i+1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i-1][self.x+j+1] = Style.DIM + Back.RED + 'S'
                        base[self.y+i+1][self.x+j-1] = Style.DIM + Back.RED + 'S'
                    else:
                        base[self.y + i][self.x + j] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j+1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j+1] = Back.GREEN + ' '
            return base
        else:
            for i in range(self.height):
                for j in range(self.width):
                    if self.health < 50 and self.health > 20:
                        base[self.y+i][self.x+j] = Style.DIM + Back.YELLOW + 'C'
                        base[self.y + i+1][self.x + j+1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j+1] = Back.GREEN + ' '
                    elif self.health < 20 and self.health >0:
                        base[self.y+i][self.x+j] = Style.DIM + Back.LIGHTGREEN_EX + 'C'
                        base[self.y + i+1][self.x + j+1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j+1] = Back.GREEN + ' '
                    elif self.health > 50:
                        base[self.y+i][self.x+j] = Back.RED + 'C'
                        base[self.y + i+1][self.x + j+1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j+1] = Back.GREEN + ' '
                    else:
                        base[self.y + i][self.x + j] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j+1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i+1][self.x + j-1] = Back.GREEN + ' '
                        base[self.y + i-1][self.x + j+1] = Back.GREEN + ' '
            return base

class spawn(building):
    def __init__(self, x, y):
        self.health=0
        self.x = x
        self.y = y
        
    def show(self, base):
        base[self.y][self.x] = Back.BLACK + 'S'
        return base