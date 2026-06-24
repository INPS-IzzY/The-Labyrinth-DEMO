import pygame


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
        (self.image)
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
