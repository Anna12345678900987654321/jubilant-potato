import pygame, control
from gun import Gun
from pygame.sprite import Group
from zombie import Zombie 
from stats import Stats
from scores import Scores
from health import Health

def run():
    pygame.init()
    screen=pygame.display.set_mode((1200, 500))
    pygame.display.set_caption("Zombie")
    bg='lightblue'
    screen.fill(bg)
    running=True
    gun= Gun(screen)
    zombie= Group()
    bullets=Group()
    stats=Stats()
    scores=Scores(screen, stats, "red")
    health=Health(screen, stats, bg)
    control.zombie_army(screen, zombie)
    while running:
        pygame.display.flip()
        control.events(gun, bullets, screen, zombie, scores, stats, health)
        gun.update()
        bullets.update()
        control.remove_bullets(bullets)
        control.gun_kill(stats, screen, gun, health, zombie, bullets, bg)
    pygame.quit()







run()
