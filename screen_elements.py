
import pygame


class ScreenElements(pygame.sprite.Sprite):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = axis_x
        self.rect[1] = axis_y

        self.frame = 1
        self.tick = 0

    def draw(self, window):
        pass
    
    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()
    
    def animation(self, image: str, amount_images: int):
        self.ticks = (self.ticks + 1) % amount_images # quantidade de imagem do obj
        self.image = pygame.image.load(f"assets/{image}{str(self.ticks)}.png")   
    
    def collision(self, group, name):
        collide = pygame.sprite.spritecollide(self, group, True)  


class TextElement:
    text_screen: str
    size: int

    def __init__(self, text_screen, size):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text_screen, True, (255,255,255))
    
    def draw(self, window, axis_x, axis_y):
        window.blit(self.render, (axis_x, axis_y))
    
    def update_text(self, text_screen):
        self.render = self.font.render(text_screen, True, (255,255,255))