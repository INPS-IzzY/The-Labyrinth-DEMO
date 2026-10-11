import pygame
import time
seconds = 0

class Monster:
    #cyclopses, hecatonkiries, sirens, harpies

    def __init__(self, x, y):
        self.image = "default mon"
        self.x = x
        self.y = y
        self.direction = 1
    def pathfinding():
        if plyr in sight():
            move.Monster(plyr.x, x)
    
    def render(self, surface):
        if self.direction == 1:
            print("facing right")
        elif self.direction == -1:
            print("facing left")
        if self.direction == 1:
            surface.blit(self.image, (self.x, self.y))
        else:
            surface.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))

class Siren(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("siren.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 200))

    def move(self, speed = 1):
        global seconds
        print(seconds)
        seconds += 1
        if seconds % 750 == 0:
            self.direction *= -1
        self.x += speed * self.direction
        print(seconds)
        
    def futurestuff():
        def sing():
            for event in pygame.event.get():
                    if event == pygame.plyr_proximity(20):
                        print("LALALALA")
        def swim():
            for event in pygame.event.get():
                if event == pygame.siren_inwater:
                    set.animation.Siren(swimming)
        def attack():
            for event in pygame.event.get():
                if event == pygame.plyr_proximity(3):
                    set.animation.Siren(swinging)
                    if Siren_hitbox.pos == plyr_hitbox.pos:
                        plyr_hp = plyr_hp - 10

class Harpy(Monster):
    direction = 1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("harpy.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 200))