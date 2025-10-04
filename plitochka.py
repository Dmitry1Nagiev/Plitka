import pygame
import os
import sys
current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 1000
HEIGHT = 800

WHITE = 255,255,255
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('Плиточки')
FPS = 60
clock = pygame.time.Clock()

on_image = pygame.image.load('Glass.png').convert_alpha()

p_1_image = pygame.image.load('player_1.png').convert_alpha()
p_2_image = pygame.image.load('player_2.png').convert_alpha()
maps_list = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]


class Plitka(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.on = True
        self.adr = (self.rect.y // 100, self.rect.x // 100)
def drawmaps():
    for i in range(0,7):
        for j in range(0,7):
            x = 100 * i
            y = 100 * j
            pos = (x,y)
            plitka = Plitka(pos)
            plitka_group.add(plitka)

class Player(pygame.sprite.Sprite):
    def __init__(self,image,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        p_1_image.set_colorkey(WHITE)
        p_2_image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hod = False
        self.step = False
        self.name = name

def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
    if len(player_group) == 1:
        text = f'Лучший игрок:{list_player[0].name}'
    else:
        text = f'Ход игрока - {list_player[NUM_HOD].name}'
    text_render = font.render(text, 'red', True)


plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
list_player = []

NUM_HOD = 0
font = pygame.font.SysFont('Aria', 40)
running = True

drawmaps()
player_1 = Player(p_1_image,10,10,'Dmitry')
player_group.add(player_1)
list_player.append(player_1)
player_2 = Player(p_2_image, 610, 610,'Pelmenhu')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod = True






while running:

    game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    clock.tick(FPS)









