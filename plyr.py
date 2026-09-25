import pygame

class plyr:
    #Theseus
    def __init__(self, x, y):
        self.image = "default plyr"
        self.x = x
        self.y = y
        self.facing = True
          
    def render(self, surface):
        if self.facing:
            surface.blit(self.image, (self.x, self.y))
        else:
            surface.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))

    def move(self, keys, speed = 5):
        if keys[pygame.K_w]:
            self.y -= speed
            if self.y < 0:
                self.y += (speed * 5)
        if keys[pygame.K_d]:
            self.x += speed
            self.facing = True
            if self.x > 1180:
                self.x -= speed
                
        if keys[pygame.K_a]:
            self.x -= speed
            self.facing = False
            if self.x < 0:
                self.x += speed
                

class Theseus(plyr):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("theseus.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150))
        (self.image)
    