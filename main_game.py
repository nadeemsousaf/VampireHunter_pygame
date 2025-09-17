import pygame
from sys import exit
#import random

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Vampire Hunter')
clock = pygame.time.Clock()
sprite_pause = False

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

graveyard = pygame.image.load('images/graveyard6.jpg')
grass = pygame.image.load('images/grass.png')
font1 = pygame.font.Font('fonts/pixel.ttf', 50) #dafont.com
font2 = pygame.font.Font('fonts/GothicPixels.ttf', 50)
font3 = pygame.font.Font('fonts/pixel.ttf', 20)
text_surface = font2.render('Vampire Hunter', False, RED)

enemy_kill_count = 0

class Player():
    def __init__(self, front, left, right, hurt_f, hurt_l, hurt_r):
        self.show = front
        self.front = front
        self.left = left
        self.right = right
        self.hurt_f = hurt_f
        self.hurt_l = hurt_l
        self.hurt_r = hurt_r
        self.x = 150
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
        #print("hurt")
        self.health -= 10
        self.x -= 45
        player_hb.remove_health(10)

        if self.show == self.front:
            self.show = self.hurt_f
        elif self.show == self.left:
            self.show = self.hurt_l
        else:
            self.show = self.hurt_r
        
        if (self.health <= 0):
            self.vanquish()
    def vanquish(self):
        vanquish_text = font1.render("You Died",False,RED)
        window.blit(vanquish_text, (100, 160))
        global sprite_pause 
        sprite_pause = True
    def reset(self): #placeholder for better practice
        self.x = 150
        self.y = 245
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
        self.health = 200
        self.show = self.front
        player_hb.reset()

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
    def get_xy(self):
        return (self.x,self.y)
    def damage(self):
        self.show = self.hurt
        self.x += 45
        self.health -= 25
        enemy_hb.remove_health(25)
        if (self.health <= 0):
            self.vanquish()
    def vanquish(self): #reuse enemy?- reset currently
        global enemy_kill_count
        enemy_kill_count += 1
        self.x = 800
        self.health = 100
        enemy_hb.restore()
    def reset(self):
        self.x = 800
        self.y = 240
        self.health = 100
        enemy_hb.restore()

class Button():
    def __init__(self, x, y, normal_img, hover_img):
        self.x = x
        self.y = y
        self.show = normal_img
        self.normal_img = normal_img
        self.hover_img = hover_img
        self.rect = pygame.Rect(x,y,normal_img.get_width(),normal_img.get_height())
        self.action = None
    def draw(self):
        window.blit(self.show, (self.x, self.y))
    def set_click_response(self,action):
        self.action = action #a function
    def update(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos): #mouse hovering
            self.show = self.hover_img
            #print("hover")
            if event.type == pygame.MOUSEBUTTONDOWN: #button clicked
                self.show = self.normal_img #sleep to show clicked button?
                #print("click")
                if self.action != None:
                    self.action() #no values into function
        else:
           self.show = self.normal_img 
           return None

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
        self.create_label()
    def remove_health(self,by):
        self.green_width -= by
    def reset(self):
        self.green_width = 100
    def create_label(self):
        label_text = font3.render(self.name,False,RED)
        window.blit(label_text, (self.x, self.y-20)) #change to be an equation that uses height, width and font size
    def change_coord(self,x,y):
        if x != False:
            self.x = x
        if y != False:
            self.y = y
    def restore(self):
        self.green_width = self.red_width

enemy_1 = Enemy(800, 240, pygame.image.load('images/enemy1.png'), pygame.image.load('images/enemy2.png'))
player = Player(pygame.image.load('images/player1.png'), pygame.image.load('images/player3.png'), pygame.image.load('images/player2.png'),pygame.image.load('images/player1_red.png'), pygame.image.load('images/player3_red.png'), pygame.image.load('images/player2_red.png'))
enemy_list = [enemy_1]
player_hb = HealthBar("player",30,30,100,20)
enemy_hb = HealthBar("enemy",enemy_1.get_xy()[0],enemy_1.get_xy()[1]-10,100,10)
buttons = {"restart_button":Button(285,150,pygame.transform.scale(pygame.image.load('images/restartBN.jpg'), (100,50)),pygame.transform.scale(pygame.image.load('images/restartBA.jpg'), (100,50))),"quit_button":Button(405,150,pygame.transform.scale(pygame.image.load('images/quitBN.jpg'), (100,50)),pygame.transform.scale(pygame.image.load('images/quitBA.jpg'), (100,50)))}
buttons["restart_button"].set_click_response(lambda : restart_game())
buttons["quit_button"].set_click_response(lambda: quit_game())

def ob_overlap(ob1, ob2): #dif. overlap standards for enemy- still working on
    ob1_x1 = ob1.x
    ob1_x2 = ob1.x + ob1.show.get_width()
    ob2_x1 = ob2.x
    ob2_x2 = ob2.x + ob2.show.get_width()
    ob1_line = (ob1_x2-ob1_x1)/2 + (ob1_x2-ob1_x1)/4
    if (ob1_x1 <= ob2_x1 and ob1_line >= ob2_x1) or (ob2_x1 <= ob1_x1 and ob2_x2 >= ob1_line):
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

def draw_buttons():
    for button in buttons:
        buttons[button].draw()

def quit_game():
    pygame.quit()
    exit()

def restart_game():
    global sprite_pause
    sprite_pause = False
    player.reset()
    enemy_1.reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
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
        for button in buttons:
            buttons[button].update(event)

    window.blit(graveyard, (0,0))
    window.blit(grass, (0,70))
    window.blit(text_surface, (200,70))
    #for x in enemy_list:
    window.blit(enemy_1.show, (enemy_1.x,enemy_1.y))
    window.blit(player.show, (player.x,player.y))
    enemy_1.attack()

    enemy_kill_text = font3.render(f'enemy kill count: {enemy_kill_count}',False,RED)
    window.blit(enemy_kill_text, (640, 20))

    player_hb.draw() #fix ownership here- classes to own their healthbars
    enemy_hb.draw()
    enemy_hb.change_coord(enemy_1.get_xy()[0],False)

    if sprite_pause == False: #test
        player.x += player.speed*player.x_dir
        enemy_1.x -= 4
        if enemy_1.x < 0:
            enemy_1.x = 800

        '''
        if any_overlap(player,enemy_list):
            print("Overlap")
        '''

        if player.x+player.show.get_width() < 0:
            player.x = 0+player.show.get_width()
        
        if player.x > 800:
            player.x = 800-player.show.get_width()

        for x in enemy_list:
            if (ob_overlap(player,x)==False):
                x.show = x.normal
    else:
        draw_buttons()

    pygame.display.update()
    clock.tick(40)