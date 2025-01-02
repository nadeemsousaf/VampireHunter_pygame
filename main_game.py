import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption('throwaway_name')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()