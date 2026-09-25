import pygame
import time


class Monster:
    #cyclopses, hecatonkiries, sirens, harpies
    def __init__(self, x, y):
        self.image = "default mon"
        self.x = x
        self.y = y
    def pathfinding():
        if plyr in sight():
            move.Monster(plyr.x, x)
    
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Siren(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("siren.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 200))

    def move(self, speed = 5):
        seconds = 0
        direction = 1
        while True:
            time.sleep(1)
            seconds += 1
            if seconds % 5 == 0:
                if direction == 1:
                    direction = -1
                if direction == -1:
                    direction = 1
            self.x += (speed * direction)
            
        
        
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
