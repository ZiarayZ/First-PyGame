import os,random,pygame,time

file = open("leaderboard.txt","r")
print("Leader Board:" + "\n" + file.read())
file.close()

class Blocker(object):
    def __init__(self,wx,wy):
        self.rect = pygame.Rect(wx,wy,48,48)
        blocks.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_blocker(self):
        self.active = False

class Particle1(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles1.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle2(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles2.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle3(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles3.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle4(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles4.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle5(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles5.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle6(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles6.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle7(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles7.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle8(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles8.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle9(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles9.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Particle10(object):
    def __init__(self):
        self.rect = pygame.Rect(0,1000,2,2)
        particles10.append(self)

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy

    def reset_particle(self):
        self.active = False

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(50,800,60,60)
        self.onGround = True
        self.turns = 0
        self.dscore = 0

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    self.onGround = True
                    self.turns = 0
                if dy < 0:
                    self.rect.top = wall.rect.bottom
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if ((self.rect.y < block.rect.y - 50) == False) and self.rect.x > block.rect.x:
                    self.rect.left = block.rect.right
                if ((self.rect.y < block.rect.y - 50) == False) and self.rect.x < block.rect.x:
                    self.rect.right = block.rect.left
                if self.rect.y < block.rect.y - 50:
                    self.rect.bottom = block.rect.top
                    self.move(6,0)
                    self.onGround = True
                    self.turns = 0
        for spike in spikes:
            if self.rect.colliderect(spike.rect):
                self.rect = pygame.Rect(50,800,60,60)
                self.dscore += 1

class EnemyH(object):
    def __init__(self,wx,wy):
        enemiesH.append(self)
        self.rect = pygame.Rect(wx,wy,48,48)
        self.direction = "left"

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                    self.direction = "left"
                if dx < 0:
                    self.rect.left = wall.rect.right
                    self.direction = "right"
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

    def reset_enemy(self):
        self.active = False

class EnemyV(object):
    def __init__(self,wx,wy):
        enemiesV.append(self)
        self.rect = pygame.Rect(wx,wy,48,48)
        self.direction = "down"

    def move(self,dx,dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    self.direction = "up"
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    self.direction = "down"

    def reset_enemy(self):
        self.active = False


#Walls/Platforms and Spikes
class Wall(object):
    def __init__(self,wx,wy):
        walls.append(self)
        self.rect = pygame.Rect(wx,wy,48,48)

    def reset_wall(self):
        self.active = False

class Spike(object):
    def __init__(self,wx,wy):
        spikes.append(self)
        self.rect = pygame.Rect(wx,wy,48,48)

    def reset_spike(self):
        self.active = False

#Variable Stuff
levels = [[
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
    "W   E               W",
    "W                   W",
    "W                   W",
    "W          WWWWWWW  W",
    "W                   W",
    "W                   W",
    "W               W   W",
    "W  WWWWW            W",
    "W                   W",
    "W                 WWW",
    "W                   W",
    "W                   W",
    "W      WWWWWW       W",
    "W                   W",
    "W                   W",
    "W                   W",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "     WE              ",
    "     W           W   ",
    "W    W              W",
    "W   WW          WW  W",
    "W    W              W",
    "W    W           W  W",
    "W    W              W",
    "WW   W       WWWWW  W",
    "W    W              W",
    "W    W           W  W",
    "WW   W              W",
    "W    WW             W",
    "W    W           W  W",
    "W    W            W W",
    "W   WW              W",
    "     W               ",
    "     W               ",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
    "W E                 W",
    "W                  WW",
    "W                   W",
    "W                   W",
    "WW                 WW",
    "W                   W",
    "W                   W",
    "W                 WWW",
    "W                   W",
    "W                   W",
    "W        W          W",
    "W                   W",
    "WW       W          W",
    "W                   W",
    "         W           ",
    "                     ",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
    "W E                 W",
    "WWWWW               W",
    "W                   W",
    "W                   W",
    "W                   W",
    "WW                  W",
    "W                   W",
    "W                    W",
    "WWWWWWWWWWWWWWWWWW   W",
    "W                W  W",
    "W                W  W",
    "   WWWWWWW  WWWWWW   ",
    "   W     W       W   ",
    "WWWW            WWWWW",
    "W     W       W     W",
    "W                   W",
    "WWWWWWWDDDDDDDWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   WWW",
    "W                     W",
    "W                     W",
    "W                 W   W",
    "WE                 W  W",
    "WDDDDDDDDDDDDDDDDDDD  W",
    "W                     W",
    "W                     W",
    "W       W           WWW",
    "W                  DW",
    "                 D   ",
    "                     ",
    "WWWDDDDDDDDDDDDDD   W",
    "W                  W ",
    "W                  W ",
    "W                  W ",
    "W                  W ",
    "WWWDDDDDDWWDDDDDDWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
    "W                   W",
    "W  WWDDDDD          W",
    "W   WWWWWWDDDDD     W",
    "W   WWWWWWWWWWWDD   W",
    "WW  W               W",
    "W   W               W",
    "W   W               W",
    "W   W             DDW",
    "WW  W          DDDWWW",
    "W   W       DDDWWWWWW",
    "W   W               W",
    "W   W               W",
    "WW  WDDDDD          W",
    "W   WE    DDD       W",
    "W   W        DD     W",
    "W   W               W",
    "WWWWWDDDDDW         W",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WSSSSSWSWWWWWWWWWWWWW",
    "W       VW          W",
    "W  H     WE         W",
    "W   WW   W          W",
    "W    W   W          W",
    "W    W   W         WW",
    "WW   W   W        W W",
    "W    W   W          W",
    "W    W   W          W",
    "W    W   WW         W",
    "W   WW   W          W",
    "W    W   W         WW",
    "W    W   W          W",
    "W    W   W          W",
    "WW   W   W  V   V   W",
    "W    W   W  W       W",
    "W    W      W      HW",
    "W    WV     WWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WDDDDDDDDDDDDDDDDDDDW",
    "WE                  WWW",
    "W                     W",
    "WWWH             WH   W",
    "WWWWWWWWWWWWWWWWWWW   W",
    "WDDDDDDDDDDDDDDDDDDW  W",
    "W                     W",
    "W                     W",
    "W   HW              WWW",
    "W   WWWWWWWWWWWWWWWWWWW",
    "W  WDDDDDDDDDDDDDDDDW",
    "W                   WWW",
    "W                     W",
    "WWW              W    W",
    "WWWWWWWWWWWWWWWWWWW   W",
    "WWWWDDDDDDDDDDDDDDDW  W",
    "W                     W",
    "W                     W",
    "W  W               HWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWE",
    "D                  B ",
    "D                  B ",
    "W  WWWWWWWWWWWWWWWWWW",
    "    D              B ",
    "    D              B ",
    "WWWWW  WWWWWWWWWWWWWW",
    "        D          B ",
    "        D          B ",
    "WWWWWWWWW  WWWWWWWWWW",
    "            D      B ",
    "            D      B ",
    "WWWWWWWWWWWWW  WWWWWW",
    "                D  B ",
    "                D  B ",
    "WWWWWWWWWWWWWWWWW  WW",
    "W                  BS",
    "W                  BS",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WWWWWWWWWWWWWWWWWWWWW",
    "                   E ",
    "     B               ",
    "                B    ",
    " BBB                 ",
    "          B          ",
    "                     ",
    "  B                  ",
    "     B               ",
    "           B         ",
    "                B    ",
    "                     ",
    "      B              ",
    "                     ",
    "  B             B    ",
    "        B      B     ",
    "                     ",
    "    B                ",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
],[
    "WDDDDDDWWWDDWWDDDWWWW",
    "WE                  W",
    "W                   W",
    "W   WWWB D W  WWW    W",
    "W    D B D D  D      W",
    "W    D   DWD  DD    W",
    "W    D   D D  D     W",
    "     D   D D  DDD    ",
    "    VVVVVVVVVVVVVV   ",
    "W                 D W",
    "W   DDD DDHHD DD   BW",
    "    DHH DDDHD DHD    ",
    "    DDH DHDHD D  DB  ",
    "WDDDDHH DHDDD DHD   W",
    "W   DDD DHHDD DD    W",
    "W                  WW",
    "W                   W",
    "W  WH               W",
    "WWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWW",
]]
enemiesH = []
enemiesV = []
walls = []
spikes = []
blocks = []
particles1 = []
particles2 = []
particles3 = []
particles4 = []
particles5 = []
particles6 = []
particles7 = []
particles8 = []
particles9 = []
particles10 = []
for turn in range(200):
    Particle1()
    Particle2()
    Particle3()
    Particle4()
    Particle5()
    Particle6()
    Particle7()
    Particle8()
    Particle9()
    Particle10()
player = Player() #Create a player object from class
colour = (100,128,255)
wall_colour = (255,255,255)
particle_colour = (220,220,220)
spike_colour = (128,128,128)
if str(input("Do you have a save?\n>: ")).lower() == "yes":
    slot = str(input("Name the save.\n>: ")).lower()
    file = open("saves/" + slot + ".txt","r")
    words = file.read().split()
    name = words[0]
    player.dscore = int(words[1])
    startTime2 = int(words[2])
    endTime = int(words[3])
    levelTurn = int(words[4])
else:
    name = str(input("What is your name? (Leader Board, One Word)\n>: "))
    endTime = 0
    startTime2 = 0
    levelTurn = 0
    particle_start_time = time.time() * 2
speed = 2

#Start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#Set up Display
pygame.display.set_caption("Jump to escape!")
width = 1000
height = 950
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
myfont = pygame.font.SysFont("Arial", 25, True, False)
level = levels[levelTurn]
x = y = 0
for row in level: 
    for col in row:
        if col == "W":#W - Wall
            Wall(x,y)
        if col == "D":#D - Death block
            Spike(x,y)
        if col == "H":#H - Horizontal death block
            EnemyH(x,y)
        if col == "V":#V - Vertical death block
            EnemyV(x,y)
        if col == "B":#B - Blocker
            Blocker(x,y)
        if col == "E":#E - Escape
            end_rect = pygame.Rect(x,y,48,48)
        x += 48
    y += 48
    x = 0

label3 = myfont.render(("| Arrow keys = Move | Space = Change Ability | Backspace = Restart Level | ESC = Quit |"), False, (0,0,0))
#Start Game
running = True
startTime1 = int(time.time())
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            if colour == (100,128,255):
                colour = (255,128,100)
                speed = 6
            else:
                colour = (100,128,255)
                speed = 2

    #Enemy movement
    for enemy in enemiesH:
        if enemy.direction == "left":
            enemy.move(-5,0)
        if enemy.direction == "right":
            enemy.move(5,0)
        enemy.move(0,3)
        if enemy.rect.colliderect(player.rect):
            player.rect = pygame.Rect(50,800,60,60)
            player.dscore += 1
        if enemy.rect.y == 720:
            enemy.rect.y = 0
    for enemy in enemiesV:
        if enemy.direction == "up":
            enemy.move(0,-5)
        if enemy.direction == "down":
            enemy.move(0,5)
        if player.rect.colliderect(enemy.rect):
            player.rect = pygame.Rect(50,800,60,60)
            player.dscore += 1
    for block in blocks:
        block.move(6,0)
        if block.rect.x > width + 5:
            block.rect.x = -60
    if time.time() - particle_start_time > 2:
        particle_start_time = time.time() * 2
        for particles in particles1,particles2,particles3,particles4,particles5,particles6,particles7,particles8,particles9,particles10:
            for particle in particles:
                particle.rect.y = 1000

    #Allow Player to move
    user_input = pygame.key.get_pressed()

    if user_input[pygame.K_ESCAPE]:
        if str(input("Would you like to save?\n>: ")).lower() == "yes":
            slot = str(input("Name the save.\n>: ")).lower()
            file = open("saves/" + slot + ".txt", "w")
            file.write(name + " " + str(player.dscore) + " " + str(startTime1) + " " + str(int(time.time())) + " " + str(levelTurn))
            file.close()
            print("Saved")
            running = False
            break
        else:
            running = False
            break
    for particles in particles1,particles2,particles3,particles4,particles5,particles6,particles7,particles8,particles9,particles10:
        for particle in particles:
            particle.move(random.randint(-3,3),random.randint(0,5))
    if user_input[pygame.K_BACKSPACE]:
        player.rect.x = 50
        player.rect.y = 800
    if user_input[pygame.K_UP]:
        if player.onGround:
            if player.turns <= 5:
                for particle in particles1:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 10 and player.turns > 5:
                for particle in particles2:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 15 and player.turns > 10:
                for particle in particles3:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 20 and player.turns > 15:
                for particle in particles4:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 25 and player.turns > 20:
                for particle in particles5:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 30 and player.turns > 25:
                for particle in particles6:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 35 and player.turns > 30:
                for particle in particles7:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 40 and player.turns > 35:
                for particle in particles8:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns <= 45 and player.turns > 40:
                for particle in particles9:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            if player.turns == 45:
                for particle in particles10:
                    particle.rect.x = player.rect.x + random.choice([random.randint(0,5),random.randint(55,60)])
                    particle.rect.y = player.rect.y + random.randint(50,60)
            player.move(0,-5)
            player.turns += 1
        else:
            player.move(0,3)
        if player.turns > 45 and speed == 2:
            player.turns = 0
            particle_start_time = time.time()
            player.onGround = False
        elif player.turns > 35 and speed == 6:
            player.turns = 0
            particle_start_time = time.time()
            player.onGround = False
    elif player.rect.y < (height - 60):
        player.move(0,3)
        
    if user_input[pygame.K_DOWN]:
        player.move(0,3)
        
    if user_input[pygame.K_LEFT]:
        player.move(-speed,0)
    if player.rect.x < -59:
        player.rect.x = width
        
    if user_input[pygame.K_RIGHT]:
        player.move(speed,0)
    if player.rect.x > width:
        player.rect.x = -59
        
    if player.rect.colliderect(end_rect):
        del walls[:]
        del spikes[:]
        del enemiesH[:]
        del enemiesV[:]
        del blocks[:]
        levelTurn += 1
        try:
            level = levels[levelTurn]
        except IndexError:
            score = name + "'s Score         = Deaths: " + str(player.dscore) + ", Time: " +str(int(time.time())-int(startTime2)+endTime-startTime1) + "s"
            file = open("leaderboard.txt", "r+")
            file.read()
            file.write(score + "\n")
            file.close()
            running = False
            break
        x = y = 0
        for row in level:
            for col in row:
                if col == "W":
                    Wall(x,y)
                if col == "D":
                    Spike(x,y)
                if col == "H":
                    EnemyH(x,y)
                if col == "V":
                    EnemyV(x,y)
                if col == "B":
                    Blocker(x,y)
                if col == "E":
                    end_rect = pygame.Rect(x,y,48,48)
                x += 48
            y += 48
            x = 0
        player.rect.x = 50
        player.rect.y = 800

    #Draw Screen
    screen.fill((0,0,0))
    for wall in walls:
        pygame.draw.rect(screen,wall_colour,wall.rect)
    for spike in spikes:
        pygame.draw.rect(screen,spike_colour,spike.rect)
    for enemy in enemiesH:
        pygame.draw.rect(screen,spike_colour,enemy.rect)
    for enemy in enemiesV:
        pygame.draw.rect(screen,spike_colour,enemy.rect)
    for block in blocks:
        pygame.draw.rect(screen,wall_colour,block.rect)
    for particles in particles1,particles2,particles3,particles4,particles5,particles6,particles7,particles8,particles9,particles10:
        for particle in particles:
            pygame.draw.rect(screen,particle_colour,particle.rect)
    pygame.draw.rect(screen,(255,0,0),end_rect)
    pygame.draw.rect(screen,colour,player.rect)
    label1 = myfont.render(("Deaths: " + str(player.dscore)), False, (0,0,0))
    label2 = myfont.render(("Time: " + str(int(time.time())-int(startTime2)+endTime-startTime1) + "s"), False, (0,0,0))
    screen.blit(label1, (50,915))
    screen.blit(label2, (865,915))
    screen.blit(label3, (80,14))
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
