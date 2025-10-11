import pygame
import os
import sys
current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDHT = 1000
HEIGHT = 800

WHITE = 255,255,255
GRAY = 239,239,239
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('Плиточки')
FPS = 60
clock = pygame.time.Clock()

on_image_ = pygame.image.load('Glass.png').convert_alpha()
on_image = pygame.transform.scale(on_image_,(100,100))
of_image_ = pygame.image.load('of_glass.png')
of_image = pygame.transform.scale(of_image_,(100,100))
of_image.set_colorkey(WHITE)

p_1_image_ = pygame.image.load('player_1.png').convert_alpha()
p_1_image = pygame.transform.scale(p_1_image_,(90,90))
p_2_image_ = pygame.image.load('p_2.jpg').convert_alpha()
p_2_image = pygame.transform.scale(p_2_image_,(130,130))
p_2_image.set_colorkey(WHITE)

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
    def update(self):
        if pygame.sprite.spritecollide(self,player_group, False):
            self.on = False
            self.image = of_image
            maps_list[self.adr[0]][self.adr[1]] = 1


        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.on:
                if self.rect.left<pos[0]<self.rect.right and self.rect.top<pos[1]<self.rect.bottom:
                    list_player[NUM_HOD].step = True
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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hod = False
        self.step = False
        self.name = name
    def update(self):
        global NUM_HOD
        if self.hod:
            if not self.proverka():
                NUM_HOD += 1
                if NUM_HOD > len(list_player) - 1:
                    NUM_HOD = 0
                    list_player[NUM_HOD].hod = True
                list_player.remove(self)
                self.kill()
            if pygame.mouse.get_pressed()[0]:
                if self.step:
                    click_pos = pygame.mouse.get_pos()
                    if ((click_pos[0] - self.rect.center[0])**2 + (click_pos[1]-self.rect.center[0])**2)**0.5<=150:
                        self.rect.x = 10+click_pos[0]//100+100
                        self.rect.y = 10+click_pos[1]//100+100
                        self.step = False
                        NUM_HOD += 1
                        if NUM_HOD > len(list_player) - 1 :
                            NUM_HOD = 0
                            list_player[NUM_HOD].hod = True
    def proverka(self):
        pl = pygame.sprite.spritecollide(self,plitka_group,False)[0]
        x = pl.adr[1]
        y = pl.adr[0]
        list_hod = []
        for i in (-1,0,1):
            for j in (-1,0,1):
                index_y = y+i
                index_x = x+j
                if -1 < index_x < 7 and -1 < index_y < 7:
                    if maps_list[index_y][index_x] == 0:
                        list_hod.append(True)
        return True in list_hod
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
    screen.blit(text_render, (WIDHT//2-180,HEIGHT//2))

plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
list_player = []

NUM_HOD = 0
font = pygame.font.SysFont('Aria', 40)
running = True



player_1 = Player(p_1_image,10,10,'Dmitry')
player_group.add(player_1)
list_player.append(player_1)
player_2 = Player(p_2_image, 590, 590,'Pelmenhu')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod = True






drawmaps()
while running:

    game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
sys.exit()






