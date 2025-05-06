import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Vampire Hunter')
clock = pygame.time.Clock()

graveyard = pygame.image.load('images/graveyard6.jpg')
grass = pygame.image.load('images/grass.png')
font1 = pygame.font.Font('fonts/pixel.ttf', 50)
text_surface = font1.render('Vampire Hunter', False, 'white')

class Player():
    def __init__(self, front, left, right):
        self.show = front
        self.front = front
        self.left = left
        self.right = right
        self.x = 0
        self.y = 245
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
    def attack(self):
        possible_enemy = any_overlap(player,enemy_list)
        if possible_enemy != False:
            possible_enemy.vanquish()

class Enemy():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def vanquish(self):
        print("hit")
        #self.x = self.x-30

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        window.blit(self.image, (self.x, self.y))
        pos = pygame.mouse.get_pos

enemy_1 = Enemy(0, 240, pygame.image.load('images/enemy1.png'))
player = Player(pygame.image.load('images/player1.png'), pygame.image.load('images/player3.png'), pygame.image.load('images/player2.png'))
enemy_list = [enemy_1]

def ob_overlap(ob1, ob2):
    ob1_x1 = ob1.x
    ob1_x2 = ob1.x + ob1.show.get_width()
    ob2_x1 = ob2.x
    ob2_x2 = ob2.x + ob2.image.get_width()
    if (ob1_x1 <= ob2_x1 and ob1_x2 >= ob2_x1) or (ob2_x1 <= ob1_x1 and ob2_x2 >= ob1_x2):
        return True
    else:
        return False

def any_overlap(person, list):
    person_x1 = person.x
    person_x2 = person.x + person.show.get_width()
    for x in list:
        enemy_x1 = x.x
        enemy_x2 = x.x + x.image.get_width()
        if (person_x1 <= enemy_x1 and person_x2 >= enemy_x1) or (enemy_x1 <= person_x1 and enemy_x2 >= person_x2):
            return x
    return False

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
            elif event.key == pygame.K_SPACE:
                player.attack()
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
    window.blit(grass, (0,70))
    window.blit(text_surface, (250,70))
    window.blit(enemy_1.image, (enemy_1.x,enemy_1.y))
    window.blit(player.show, (player.x,player.y))

    player.x += player.speed*player.x_dir
    enemy_1.x -= 4
    if enemy_1.x < 0:
        enemy_1.x = 800

    if ob_overlap(player,enemy_1):
        print("Overlap")

    if player.x+player.show.get_width() < 0:
        player.x = 0+player.show.get_width()
    
    if player.x > 800:
        player.x = 800-player.show.get_width()

    pygame.display.update()
    clock.tick(40)