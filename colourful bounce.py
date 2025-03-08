import pygame
import random
pygame.init()
spritecngclrevnt=pygame.USEREVENT+1
bgclrcngevnt=pygame.USEREVENT+2

BLUE=pygame.Color('lightblue')
PINK=pygame.Color('lightpink')
PURPLE=pygame.Color('lavender')

YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magenta')
WHITE=pygame.Color('white')
GREEN=pygame.Color('green')

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),
random.choice([-1,1])]
        
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False

        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundary_hit=True