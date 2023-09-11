
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

class Hero(ScreenElements):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(image, axis_x, axis_y, *groups)
        self.speed = 4
        self.grav = 1

        self.right = False
        self.left = False
        self.jump = False

        self.ticks = 0
        self.img = 0

        self.collections = 0
        self.life = 3

    
    def update(self, *args):
        self.gravity()
        self.moviments()
        self.drop()

    def gravity(self):
        self.speed += self.grav
        self.rect[1] += self.speed

        if self.speed >= 10:
            self.speed = 10

    def colisions(self, group, kill, name):
        collide = pygame.sprite.spritecollide(self, group, kill)

        if collide and name == 'platform':
            if self.rect[1] + 50 < collide[0].rect.top:
                if self.rect.left + 30 <= collide[0].rect.right:
                    if self.rect.right - 30 >= collide[0].rect.left:
                        self.rect.bottom = collide[0].rect.top
        
        if collide and name == 'crystal':
            self.collections += 1
        
        if collide and name == 'enemy':
            if self.rect.y + 90 < collide[0].rect.top:
                self.speed *= -1.4
                collide[0].kill()
            else:
                self.speed *= -1
                self.life -= 1
                collide[0].kill()

    
    def events(self, events):
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                self.right = True
            elif events.key == pygame.K_a:
                self.left = True
            elif events.key == pygame.K_SPACE:
                self.speed *= -1
        elif events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                self.right = False
            elif events.key == pygame.K_a:
                self.left = False
    
    def moviments(self):
        if self.right:
            self.rect[0] += 8
            self.animation_hero("walk", 4, 3)
            self.image = pygame.transform.flip(self.image, False, False)
        elif self.left:
            self.rect[0] -= 8
            self.animation_hero("walk", 4, 3)
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.animation_hero("idle", 4, 3)
    
    def animation_hero(self, name, ticks, limit):
        self.ticks += 1
        if self.ticks >= ticks:
            self.ticks = 0
            self.img += 1
        
        if self.img > limit:
            self.img = 0
        
        self.image = pygame.image.load(f"assets/{name}{str(self.img)}.png")
    
    def drop(self):
        if self.life > 0:
            if self.rect.y > 720:
                self.rect.x = 100
                self.rect.y = 250
                self.life -= 1

class Enemy(ScreenElements):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(image, axis_x, axis_y, *groups)
        self.ticks = 0
        self.img = 0

    def update(self):
        self.animation_enemy("enemy", 4, 3)

    def animation_enemy(self, name, ticks, limit):
        self.ticks += 1
        if self.ticks >= ticks:
            self.ticks = 0
            self.img += 1
        
        if self.img > limit:
            self.img = 0
        
        self.image = pygame.image.load(f"assets/{name}{str(self.img)}.png")

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