import pygame
from sys import exit

#47:34

pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption('Vampire Hunter')
clock = pygame.time.Clock()

graveyard_top = pygame.image.load('images/graveyard_top.png')
graveyard_bottom = pygame.image.load('images/graveyard_bottom.png')
font1 = pygame.font.Font('fonts/pixel.ttf', 50)
text_surface = font1.render('Vampire Hunter', False, 'white')

enemy = pygame.Surface((100,100))
enemy.fill('red')
enemy_x = 100
enemy_y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.blit(graveyard_top, (0,0))
    window.blit(graveyard_bottom, (0,150))
    window.blit(text_surface, (250,250))
    window.blit(enemy, (enemy_x,enemy_y))
    enemy_x -= 4
    if enemy_x < 0:
        enemy_x = 800
    pygame.display.update()
    clock.tick(60)