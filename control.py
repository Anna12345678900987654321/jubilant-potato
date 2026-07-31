import pygame, sys 
from bullet import Bullet
from zombie import Zombie 
import time
from health import Health

def events(gun, bullets, screen, zombie, scores, stats, health):
    gun.add_gun()
    zombie.draw(screen)
    scores.show_scores()
    health.show_health()
    zombie.update()
    for b in bullets.sprites():
        b.add_bullet()
    collisions=pygame.sprite.groupcollide(bullets, zombie, True, True)
    if collisions:
        for z in collisions.values():
            stats.score+=10*len(z)
        scores.image_score("red")
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                gun.move_right=True
            if e.key == pygame.K_a:
                gun.move_left=True
            if e.key == pygame.K_SPACE:
                b= Bullet(screen, gun)
                bullets.add(b)
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                gun.move_right=False
            if e.key == pygame.K_a:
                gun.move_left=False

def remove_bullets(bullets):
    for b in bullets.copy():
        if b.rect.bottom <=0:
            bullets.remove(b)
    print(len(bullets))





def zombie_army(screen, zombies):
    zombie=Zombie(screen)
    zombie_width=zombie.rect.width
    zombie_x= int((screen.get_width()-2*zombie_width)/zombie_width)
    zombie_height=zombie.rect.height
    zombie_y=int((screen.get_height()-2*zombie_height)/zombie_height)
    for row in range(zombie_y):
        for z in range(zombie_x):
            zombie=Zombie(screen)
            zombie.x=zombie_width+zombie_width*z
            zombie.y=zombie_height+zombie_height*row
            zombie.rect.x=zombie.x
            zombie.rect.y=zombie.y
            zombies.add(zombie)




def gun_kill(stats, screen, gun, health, zombies, bullets, bg):
    if stats.health==0:
        sys.exit()
    screen_rect=screen.get_rect()
    isKill=False
    for z in zombies.sprites():
        if z.rect.bottom>=screen_rect.bottom:
            isKill=True
            break
    if pygame.sprite.spritecollideany(gun, zombies) or isKill:
        stats.health-=1
        health.image_health(bg)
        zombies.empty()
        bullets.empty()
        zombie_army(screen, zombies)
        gun.create_gun()
        time.sleep(2)
    