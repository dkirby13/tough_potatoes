import pygame

#global contests


#colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (129, 69, 19)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Main_Potato(pygame.sprite.Sprite):
    def _init_(self):
        super()._init()
        width = 40
        height = 60
