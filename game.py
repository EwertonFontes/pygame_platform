import pygame
import random
from screen_elements import ScreenElements, Hero, Enemy, TextElement

class GameScene: 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.all_platforms = pygame.sprite.Group()
        self.all_crystals = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()

        self.backgroud_image = ScreenElements("assets/bg.png", 0, 0, self.all_sprites)
        self.tree1 = ScreenElements("assets/tree1.png", 80, 250, self.all_sprites)
        self.tree2 = ScreenElements("assets/tree2.png", 450, 250, self.all_sprites)
        self.tree3 = ScreenElements("assets/tree1.png", 1060, 250, self.all_sprites)

        self.plat1 = ScreenElements("assets/plat1.png", 50, 550, self.all_sprites, self.all_platforms)
        self.plat2 = ScreenElements("assets/plat3.png", 430, 550, self.all_sprites, self.all_platforms)
        self.plat3 = ScreenElements("assets/plat2.png", 1080, 550, self.all_sprites, self.all_platforms)
        
        self.crystal1 = ScreenElements("assets/crystal.png", 520, 400, self.all_sprites, self.all_crystals)
        self.crystal2 = ScreenElements("assets/crystal.png", 870, 400, self.all_sprites, self.all_crystals)
        self.crystal3 = ScreenElements("assets/crystal.png", 1155, 400, self.all_sprites, self.all_crystals)

        self.enemy1 = Enemy("assets/enemy0.png", 520, 502, self.all_sprites, self.all_enemies)
        self.enemy2 = Enemy("assets/enemy0.png", 800, 502, self.all_sprites, self.all_enemies)
        self.enemy3 = Enemy("assets/enemy0.png", 200, 502, self.all_sprites, self.all_enemies)
        
        self.player = Hero("assets/idle0.png", 100, 250, self.all_sprites)

        self.hud = ScreenElements("assets/hud.png", 50, 50, self.all_sprites)
        self.change_scene = False
    
    def draw(self, window):
        self.all_sprites.draw(window)  

    def update(self):
        self.all_sprites.update()
        self.player.colisions(self.all_platforms, False, "platform")
        self.player.colisions(self.all_crystals, True, "crystal")
        self.player.colisions(self.all_enemies, False,"enemy")
        self.HUD()
    
    def HUD(self):
        if self.player.collections == 1:
            crystal = ScreenElements("assets/icon_crystal.png", 136, 126, self.all_sprites)
        elif self.player.collections == 2:
            crystal = ScreenElements("assets/icon_crystal.png", 160, 126, self.all_sprites)
        elif self.player.collections == 3:
            crystal = ScreenElements("assets/icon_crystal.png", 185, 126, self.all_sprites)

        if self.player.life == 3:
            life1 = ScreenElements("assets/icon_head.png", 140, 81, self.all_sprites)
            life2 = ScreenElements("assets/icon_head.png", 177, 81, self.all_sprites)
            life3 = ScreenElements("assets/icon_head.png", 214, 81, self.all_sprites)
        elif self.player.life == 2:
            life1 = ScreenElements("assets/icon_head.png", 140, 81, self.all_sprites)
            life2 = ScreenElements("assets/icon_head.png", 177, 81, self.all_sprites)
            life3 = ScreenElements("assets/icon_dead.png", 214, 81, self.all_sprites)
        elif self.player.life == 1:
            life1 = ScreenElements("assets/icon_head.png", 140, 81, self.all_sprites)
            life2 = ScreenElements("assets/icon_dead.png", 177, 81, self.all_sprites)
            life3 = ScreenElements("assets/icon_dead.png", 214, 81, self.all_sprites)
        else:
            life1 = ScreenElements("assets/icon_dead.png", 140, 81, self.all_sprites)
            life2 = ScreenElements("assets/icon_dead.png", 177, 81, self.all_sprites)
            life3 = ScreenElements("assets/icon_dead.png", 214, 81, self.all_sprites)
            self.gameover()

    def gameover(self):
        print('Game over')