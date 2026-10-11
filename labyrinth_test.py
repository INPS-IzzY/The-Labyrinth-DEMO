"""# Pseudocode

# Start function

# Menu
# - Play button
# TODO: Different versions or ways to start the game

# All runs start in the NPC area
# - Talk to Ariadne
# - Ariadne ties the string around your waist

# Theseus
# - Can move in two directions [left, right]
# - Can pick up items (e.g., sword, shield) 
# - Can use items [e]
# - Interact [q]
# - Can strike with weapons - starts with a sword
    # - Light attack [Left click]
    # - Heavy attack [Right click]
    # - Can block with weapon [space]
# Can jump - jumping [up arrow]
# Dodge-roll [double tap down arrow to dodge-roll backwards]
# Player can spot dodge and parry [spot-dodge is down arrow, parry is space at the perfect time]




# - Can interact with NPCs (e.g., talk to Ariadne, ask for hints [e]
# - Can check inventory [I]

#Bugs
#9/24 siren moves correctly but does not flip and stil registers as going the same direction even though it goes a diff direciton
Harpy not rendering
"""
"""IMPORTANT .\.venv312\Scripts\Activate.ps1
python labyrinth_test.py"""

import pygame
import sys
import math
import random as ran
import time
from mobs.enemies import Harpy, Siren
from plyr import Theseus

pygame.init()
pygame.display.init()
pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
#plyr cant go passed 0 or 1280 on the x axis, and 0 or 720 on the y axis

class Scene:
    def handle_event(self, ev): pass
    def update(self): pass
    def draw(self, surf): pass

class MenuScene(Scene):
    def __init__(self, game):
        self.game = game
        self.options = ["PLAY", "QUIT"]
        self.sel = 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("The Labyrinth")
        self.scene: Scene = MenuScene(self)

    def sirens(self):
        self.Sireny = Siren(12,310)
        self.Sireny.render(self.screen)

    def sirensMove(self):
        self.Sireny.move()
        self.Sireny.render(self.screen)
        print(self.Sireny.x)

    def harpy(self):
        self.harp = Harpy(500,100)
        self.harp.render(self.screen)
    
    def TheseusInitial(self):
        self.theo = Theseus(640,360)
        self.theo.render(self.screen)

    def TheseusMove(self):
        keys = pygame.key.get_pressed()
        self.theo.move(keys)
        self.theo.render(self.screen)

    #def Update(self):
    

    def ground(self):
        self.image = pygame.image.load("ground.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1280, 210))
        self.screen.blit(self.image, (0, 510))

    def run(self):
        
        self.TheseusInitial()
        self.sirens()
        self.harpy()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((255, 255, 255))
            self.scene.draw(self.screen)
            self.TheseusMove()
            self.sirensMove()
            self.ground()
            pygame.display.flip()
            

if __name__ == "__main__":
    Game().run()
