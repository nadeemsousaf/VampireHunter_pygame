import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption('throwaway_name')
clock = pygame.time.Clock()

#for images: Image = pygame.image.load('pathname/')
sky = pygame.Surface((800,280))
sky.fill('blue')
grass = pygame.Surface((800,120))
grass.fill('green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.blit(sky, (0,0))
    window.blit(grass, (0,280))
    pygame.display.update()
    clock.tick(60)