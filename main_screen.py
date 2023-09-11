import pygame
from menu import MenuScene, GameOverScene
from game import GameScene

class MainScreen:
    def __init__(self, sizex, sizey, title):
        pygame.init()
        
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = GameScene()
        self.menu = MenuScene()

        self.quit = False
       
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
                self.quit = True


    def draw(self):
        #HERE WE PUT THE SCENES WE WANT DRAW!
        #if not self.menu.change_scene:
        #    self.menu.draw(self.window)
        #    self.menu.update()
        #elif not self.game.change_scene:
        #    self.game.draw(self.window)
        #    self.game.update()
        #else:
        #    self.loop = False
        pass


    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()            
            pygame.display.update()
        
        pygame.quit()
        return False if self.quit else True