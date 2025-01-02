import pygame
from sys import exit

#42:40

pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption('throwaway_name')
clock = pygame.time.Clock()

#for images: Image = pygame.image.load('pathname/')
sky = pygame.Surface((800,280))
sky.fill('blue')
grass = pygame.Surface((800,120))
grass.fill('green')
font1 = pygame.font.Font('fonts/pixel.ttf', 50)
text_surface = font1.render('throwaway_name', False, 'purple')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.blit(sky, (0,0))
    window.blit(grass, (0,280))
    window.blit(text_surface, (300,50))
    pygame.display.update()
    clock.tick(60)