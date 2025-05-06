import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Vampire Hunter')
clock = pygame.time.Clock()

graveyard_top = pygame.image.load('images/graveyard_top.png')
graveyard_bottom = pygame.image.load('images/graveyard_bottom.png')
graveyard = pygame.image.load('images/graveyard6.jpg')
font1 = pygame.font.Font('fonts/pixel.ttf', 50)
text_surface = font1.render('Vampire Hunter', False, 'white')

class Player():
    def __init__(self, front, left, right):
        self.show = front
        self.front = front
        self.left = left
        self.right = right
        self.x = 0
        self.y = 120
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10

class Enemy():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        window.blit(self.image, (self.x, self.y))
        pos = pygame.mouse.get_pos

enemy_1 = Enemy(0, 120, pygame.image.load('images/enemy.png'))
player = Player(pygame.image.load('images/player10.png'), pygame.image.load('images/player5.png'), pygame.image.load('images/player4.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.y_dir = 1
                player.show = player.front
            elif event.key == pygame.K_UP:
                player.y_dir = -1
            elif event.key == pygame.K_LEFT:
                player.x_dir = -1
                player.show = player.left
            elif event.key == pygame.K_RIGHT:
                player.x_dir = 1
                player.show = player.right
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.y_dir = 0
            elif event.key == pygame.K_UP:
                player.y_dir = 0
            elif event.key == pygame.K_LEFT:
                player.x_dir = 0
            elif event.key == pygame.K_RIGHT:
                player.x_dir = 0

    window.blit(graveyard, (0,0))
    #window.blit(graveyard_top, (0,0))
    #window.blit(graveyard_bottom, (0,150))
    #window.blit(text_surface, (250,250))
    window.blit(enemy_1.image, (enemy_1.x,enemy_1.y))
    window.blit(player.show, (player.x,player.y))

    player.x += player.speed*player.x_dir
    enemy_1.x -= 4
    if enemy_1.x < 0:
        enemy_1.x = 800

    pygame.display.update()
    clock.tick(60)