import pygame

class plyr:
    #Theseus
    def __init__(self, x, y):
        self.image = "default plyr"
        self.x = x
        self.y = y
            
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Theseus(plyr):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("theseus.png").convert_alpha()
        (self.image)