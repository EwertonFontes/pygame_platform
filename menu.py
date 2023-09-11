import pygame
from screen_elements import ScreenElements

class MenuScene:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        #self.backgroud_image = ScreenElements("assets/some_image.png", 0, 0, self.all_sprites)
        self.change_scene = False
        
    def draw(self, window):
        self.all_sprites.draw(window)
    
    def update(self):
        self.all_sprites.update()
    
    def events(self, event):
        pass


class GameOverScene(MenuScene):
    def __init__(self, image):
        super().__init__(image)
    
    