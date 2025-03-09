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
        self.image=pygame.Surface([width,height])
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
            
        if boundary_hit:
            pygame.event.post(pygame.event.Event(spritecngclrevnt))
            pygame.event.post(pygame.event.Event(bgclrcngevnt))
    
    def changeclr(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,GREEN,WHITE]))

def cngbgclr():

    global bgcolor
    bgcolor=random.choice([BLUE,PINK,PURPLE])

allspriteslist=pygame.sprite.Group()
sp1=Sprite(WHITE,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.x=random.randint(0,370)
allspriteslist.add(sp1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("colourful bounce!")
bgcolor=BLUE
screen.fill(bgcolor)
exit=False
clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==spritecngclrevnt:
            sp1.changeclr()
        elif event.type==bgclrcngevnt:
            cngbgclr()

    allspriteslist.update()
    screen.fill(bgcolor)
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()