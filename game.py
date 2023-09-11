import pygame
import random
from screen_elements import ScreenElements, TextElement

class GameScene: 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        #self.backgroud_image = ScreenElements("assets/some_image.png", 0, 0, self.all_sprites)
        self.change_scene = False
    
    def draw(self, window):
        self.all_sprites.draw(window)  

    def update(self):
        self.all_sprites.update()

    
    def gameover(self):
        pass