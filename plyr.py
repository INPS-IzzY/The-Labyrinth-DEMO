import pygame

class plyr:
    #Theseus
    def __init__(self, x, y):
        self.image = "default plyr"
        self.x = x
        self.y = y
          
    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def move(self, keys, speed = 5):
        if keys[pygame.K_w]:
            self.y =- speed
        if keys[pygame.K_d]:
            self.x =+ speed
        if keys[pygame.K_a]:
            self.x =- speed

class Theseus(plyr):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("theseus.png").convert_alpha()
        (self.image)
    