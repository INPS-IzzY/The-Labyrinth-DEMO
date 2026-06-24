# Pseudocode

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

import pygame
import sys
import math
import random as ran
import time
from mobs.enemies import Siren
from plyr import Theseus

pygame.init()
pygame.display.init()
pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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
        Sireny = Siren(12,21)
        Sireny.render(self.screen)
    
    def Theseus(self):
        self.theo = Theseus(640,360)
        self.theo.render(self.screen)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((255, 255, 255))
            self.scene.draw(self.screen)
            self.sirens()
            self.Theseus()
            keys = pygame.key.get_pressed()
            self.theo.move(keys)
            self.theo.render(self.screen)
            pygame.display.flip()
if __name__ == "__main__":
    Game().run()
