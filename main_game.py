import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Vampire Hunter')
clock = pygame.time.Clock()

graveyard = pygame.image.load('images/graveyard6.jpg')
grass = pygame.image.load('images/grass.png')
font1 = pygame.font.Font('fonts/pixel.ttf', 50) #dafont.com
font2 = pygame.font.Font('fonts/GothicPixels.ttf', 50)
text_surface = font2.render('Vampire Hunter', False, 'red')

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
        self.health = 200
    def attack(self):
        possible_enemy = any_overlap(player,enemy_list)
        if possible_enemy != False:
            possible_enemy.damage()
    def damage(self):
        self.health -= 10
        player_hb.remove_health()
        if (self.health <= 0):
            self.vanquish()
    def vanquish(self):
        print("placeholder")

class Enemy():
    def __init__(self, x, y, normal, hurt):
        self.x = x
        self.y = y
        self.show = normal
        self.normal = normal
        self.hurt = hurt
        self.health = 100
    def attack(self):
        if (ob_overlap(player,self)):
            player.damage()
    def damage(self):
        self.show = self.hurt
        self.x += 45
        self.health -= 25
        if (self.health <= 0):
            self.vanquish()
        #pygame.time.delay(1000)
        #self.show = self.normal
    def vanquish(self):
        print("placeholder")

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        window.blit(self.image, (self.x, self.y))
        pos = pygame.mouse.get_pos

class HealthBar():
    def __init__(self,name,x,y,width,height):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.red_width = width
        self.green_width = width
    def draw(self):
        pygame.draw.rect(window, (255,0,0), pygame.Rect(self.x,self.y,self.red_width,self.height))
        pygame.draw.rect(window, (0,128,0), pygame.Rect(self.x,self.y,self.green_width,self.height))
    def remove_health(self):
        self.green_width -= 10

enemy_1 = Enemy(0, 240, pygame.image.load('images/enemy1.png'), pygame.image.load('images/enemy2.png'))
player = Player(pygame.image.load('images/player1.png'), pygame.image.load('images/player3.png'), pygame.image.load('images/player2.png'))
enemy_list = [enemy_1]
player_hb = HealthBar("player",30,30,100,20)

def ob_overlap(ob1, ob2):
    ob1_x1 = ob1.x
    ob1_x2 = ob1.x + ob1.show.get_width()
    ob2_x1 = ob2.x
    ob2_x2 = ob2.x + ob2.show.get_width()
    if (ob1_x1 <= ob2_x1 and ob1_x2 >= ob2_x1) or (ob2_x1 <= ob1_x1 and ob2_x2 >= ob1_x2):
        return True
    else:
        return False

def any_overlap(person, list):
    person_x1 = person.x
    person_x2 = person.x + person.show.get_width()
    for x in list:
        enemy_x1 = x.x
        enemy_x2 = x.x + x.show.get_width()
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
    window.blit(text_surface, (200,70))
    #for x in enemy_list:
    window.blit(enemy_1.show, (enemy_1.x,enemy_1.y))
    window.blit(player.show, (player.x,player.y))
    player_hb.draw()

    player.x += player.speed*player.x_dir
    enemy_1.x -= 4
    if enemy_1.x < 0:
        enemy_1.x = 800

    if any_overlap(player,enemy_list):
        print("Overlap")

    if player.x+player.show.get_width() < 0:
        player.x = 0+player.show.get_width()
    
    if player.x > 800:
        player.x = 800-player.show.get_width()

    for x in enemy_list:
        if (ob_overlap(player,x)==False):
            x.show = x.normal

    pygame.display.update()
    clock.tick(40)