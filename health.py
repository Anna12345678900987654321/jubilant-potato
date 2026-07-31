import pygame.font

class Health():
    def __init__(self, screen, health, bg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=health
        self.text_color="black"
        self.font=pygame.font.SysFont("Roboto", 36)
        self.image_health(bg)

    def image_health(self, bg):
        self.health=self.font.render(str(self.stats.health), True, self.text_color, bg)
        self.health_rect=self.health.get_rect()
        self.health_rect.left=self.screen_rect.left+40
        self.health_rect.top=20

    def show_health(self):
        self.screen.blit(self.health, self.health_rect)
