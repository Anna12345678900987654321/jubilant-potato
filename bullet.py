import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen, gun ):
        super(Bullet, self).__init__()
        self.screen=screen
        self.rect= pygame.Rect(0,0,5,10)
        self.color= 'black'
        self.speed=1
        self.rect.centerx= gun.rect.centerx
        self.rect.top= gun.rect.top
        self.y= float(self.rect.y)

    def add_bullet(self):
        pygame.draw.rect(self.screen,self.color, self.rect)
        self.y-=self.speed
        self.rect.y= self.y