#Импортирую все модули
#pygame > Для основы игры
#random > Для рандомной генерации
#os > Для загрузки файлов в игру из системы
import pygame
import random
import os
#Инициализирую pygame, и музыку к нему
pygame.init()
pygame.mixer.init()
#расширение экрана
scr_width = 800
scr_height = 600
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Global_Project")
#Разные важные вещи
FPS = 60

block_size = 40

map1 = ['11111111111111111111',
        '10010000000000001010',
        '10010011111111001010',
        '10000010000010000010',
        '11111110010000010000',
        '11111000011111111111',
        '11111110000001000000',
        '11111111110000001000',
        '10000000001111110000',
        '10000111000000000111',
        '10000000111111111000',
        '11111100000000000000',
        '11111111111110000000',
        '11111100000000011111',
        '11111111110011111111',
        '11111111110011111111']

map2 = ['11111111111111111111',
        '10011110000000000001',
        '10011110011111111101',
        '10011110011100000101',
        '10011110010000010001',
        '10000000010011111111',
        '11111111111001000001',
        '11111111111100001001',
        '10000000001111111001',
        '10000111000000000001',
        '10000000111111111111',
        '10000000000000000001',
        '11111111111110000001',
        '10000000000000000001',
        '10001111111111111111',
        '11111111111111111111']

screen.fill((255, 255, 255))

#Переменная работы игры
game = True

clock = pygame.time.Clock()

#Подключаемся к папкам, где нужные файлы
path1 = os.path.join(os.getcwd(), "sprites")

path2 = os.path.join(os.getcwd(), "Sound")

#Подключаем все спрайты, и музыку
# player_walk_1 = os.path.join(path2, "player_walk_1.png")
# player_walk_1 = pygame.mixer.Sound(player_walk_1)

# game_over_won = os.path.join(path2, "game-won.ogg")
# game_over_won = pygame.mixer.Sound(game_over_won)

# fonovaya_muzyika = os.path.join(path2, "fonovaya-muzyika-quotutopayuschiyquot-24696.ogg")
# pygame.mixer.music.load(fonovaya_muzyika)
# pygame.mixer.music.play()

# game_over_1 = os.path.join(path2, "opoveschenie-o-proigryishe.ogg")
# game_over_1 = pygame.mixer.Sound(game_over_1)

# udar_po_chemto = os.path.join(path2, "udar-po-litsu-2-24273.ogg")
# udar_po_chemto = pygame.mixer.Sound(udar_po_chemto)

# sohraneniya_1 = os.path.join(path2, "zvuk-sohraneniya.ogg")
# sohraneniya_1 = pygame.mixer.Sound(sohraneniya_1)

# otryitie_sunduka_1 = os.path.join(path2, "otkryitie-kryishki-sunduka-14895.ogg")
# otryitie_sunduka_1 = pygame.mixer.Sound(otryitie_sunduka_1)

player_stay = os.path.join(path1, "player_stay.png")

player_stay = os.path.join(path1, "player_stay.png")
player_stay = pygame.image.load(player_stay)

player_left_1 = os.path.join(path1, "player_left_1.png")
player_left_1 = pygame.image.load(player_left_1)

player_left_2 = os.path.join(path1, "player_left_2.png")
player_left_2 = pygame.image.load(player_left_2)

player_right_1 = os.path.join(path1, "player_right_1.png")
player_right_1 = pygame.image.load(player_right_1)

player_right_2 = os.path.join(path1, "player_right_2.png")
player_right_2 = pygame.image.load(player_right_2)

player_down_1 = os.path.join(path1, "player_down_1.png")
player_down_1 = pygame.image.load(player_down_1)

player_down_2 = os.path.join(path1, "player_down_2.png")
player_down_2 = pygame.image.load(player_down_2)

player_up_1 = os.path.join(path1, "player_up_1.png")
player_up_1 = pygame.image.load(player_up_1)

player_up_2 = os.path.join(path1, "player_up_2.png")
player_up_2 = pygame.image.load(player_up_2)

spider = os.path.join(path1, "spider.png")
spider = pygame.image.load(spider)

win = os.path.join(path1, "win.jpg")
win = pygame.image.load(win)

lost = os.path.join(path1, "lost.jpg")
lost = pygame.image.load(lost)


block_labirint = os.path.join(path1, "block_labirint.png")
block_labirint = pygame.image.load(block_labirint)



#Функция для стабилизации звука шагов, что-бы они происходили раз, в пол секунды.
player_wolk_tim = 0
def player_wolk_timing():
    global player_wolk_tim
    if player_wolk_tim == 30:
#        player_walk_1.play()
        player_wolk_tim = 0
    player_wolk_tim += 1
#Переменная ждя функции ниже
player_wolk_top = 0

#Класс для спрайтов
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(image, (self.rect.w, self.rect.h))

    #Отрисовка спрайтов
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Spider(GameSprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(image, (self.rect.w, self.rect.h))
    
    def sp_move(self):
        if self.rect.y >= 0:
            self.rect.y -= 5


class Enemy(GameSprite):
    def __init__(self, x, y, w, h, image_left, speed, x2):
        image = image_left
        super().__init__(x, y, w, h, image)
        self.x1 = x
        self.x2 = x2
        self.speed = speed
        self.image_left = self.image
        self.image_right = pygame.transform.flip(self.image, True, False)
        if self.x1 > self.x2:
            self.speed *= -1
            self.image = self.image_left
        else:
            self.image = self.image_right


    def move(self):       
        if self.x2 > self.x1:
            if self.rect.x >= self.x1 and self.rect.x <= self.x2:
                self.rect.x += self.speed
            else:
                self.speed *= -1
                self.rect.x += self.speed
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            if self.rect.x >= self.x2 and self.rect.x <= self.x1:
                self.rect.x += self.speed
            else:
                self.speed *= -1
                self.rect.x += self.speed
                self.image = pygame.transform.flip(self.image, True, False)

#Класс игрока
class Player(GameSprite):
    def __init__(self, x, y, width, height, speed, x_con, y_con, mx_con, my_con, player_right_1, player_right_2, player_left_1, player_left_2, player_stay, player_down_1, player_down_2, player_up_1, player_up_2):
        super().__init__(x, y, width, height, player_stay)
        self.x_con = x_con
        self.y_con = y_con
        self.mx_con = mx_con
        self.my_con = my_con
        self.speed = speed
        self.player_right_1 = pygame.transform.scale(player_right_1, (self.rect.w, self.rect.h))
        self.player_right_2 = pygame.transform.scale(player_right_2, (self.rect.w, self.rect.h))
        self.player_left_1 = pygame.transform.scale(player_left_1, (self.rect.w, self.rect.h))
        self.player_left_2 = pygame.transform.scale(player_left_2, (self.rect.w, self.rect.h))
        self.player_stay = pygame.transform.scale(player_stay, (self.rect.w, self.rect.h))
        self.player_down_1 = pygame.transform.scale(player_down_1, (self.rect.w, self.rect.h))
        self.player_down_2 = pygame.transform.scale(player_down_2, (self.rect.w, self.rect.h))
        self.player_up_1 = pygame.transform.scale(player_up_1, (self.rect.w, self.rect.h))
        self.player_up_2 = pygame.transform.scale(player_up_2, (self.rect.w, self.rect.h))

    #Функция для анимации
    def anim(self, one, two):
        global player_wolk_top
        if player_wolk_top <= 15:
            self.image = one
        elif player_wolk_top > 15 and player_wolk_top <= 30:
            self.image = two
        elif player_wolk_top > 30:
            player_wolk_top = 0
        player_wolk_top += 1

    #Функция для движения
    def move(self): 
        RectX, RectY = self.rect.topleft
        if (pygame.key.get_pressed()[pygame.K_d] and self.rect.x <= self.mx_con):
            self.rect.x += self.speed
            player.anim(self.player_right_1, self.player_right_2)
            player_wolk_timing()
        if (pygame.key.get_pressed()[pygame.K_a] and self.rect.x >= self.x_con): 
            self.rect.x -= self.speed
            player.anim(self.player_left_1, self.player_left_2)
            player_wolk_timing()
        if (pygame.key.get_pressed()[pygame.K_s] and self.rect.y <= self.my_con):
            self.rect.y += self.speed
            player.anim(self.player_down_1, self.player_down_2)
            player_wolk_timing()
        if (pygame.key.get_pressed()[pygame.K_w] and self.rect.y >= self.y_con):
            self.rect.y -= self.speed
            player.anim(self.player_up_1, self.player_up_2)
            player_wolk_timing()
        if pygame.key.get_pressed()[pygame.K_d] == False and pygame.key.get_pressed()[pygame.K_a] == False and pygame.key.get_pressed()[pygame.K_w] == False and pygame.key.get_pressed()[pygame.K_s] == False:
            self.image = self.player_stay
        for Block in blocks:
            if self.rect.colliderect(Block.rect):
                self.rect.topleft = RectX, RectY

# spider
#spider1 = Spider(150, 350, 50, 50, spider, 3, 600, 3)
#spider2 = Spider(200, 100, 50, 50, spider, 3, 400, 3)
#enemies = [spider1, spdier2]

spider1 = Spider(150, 350, 50, 50, spider)
spider2 = Spider(600, 50, 50, 50, spider)
enemies = [spider1, spider2]



blocks = []

def levelUP(map2, player_x, player_y, enemies1):
    blocks.clear()
    player.rect.x = player_x
    player.rect.y = player_y
    enemies.clear()
    enemies.extend(enemies1)
    x = 0
    y = 0
    for i in map2:
        for j in i:
            if j == '1':
                block = GameSprite(x, y, block_size, block_size, block_labirint)
                blocks.append(block)
            x += block_size
        y += block_size
        x = 0






#Создание врагов, и подобного
#player(Координаты x, координаты y, ширина, высота, скорость игрока, картинка игрока, коорднаты до кудого может дойти игрок. Первые 2, это начало. Вторые 2 координаты, это кwонечные)
player = Player(70, 45, 20, 32, 5, 0, 0, 800, 580, player_right_1, player_right_2, player_left_1, player_left_2, player_stay, player_down_1, player_down_2, player_up_1, player_up_2)
player.level = 1

player.win = False
player.lost = False
levelUP(map1, 70, 45, [spider1, spider2])

#Цикл игры

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not player.win and not player.lost:        
        screen.fill((255, 255, 255))
        player.draw()
        player.move()
        spider1.draw()
        spider1.sp_move()
        spider2.draw()
        spider2.sp_move()
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                player.lost = True
        for block in blocks:
            block.draw()
        if player.rect.bottom >= 580:
            if player.level == 1:
                player.level = 2
                levelUP(map2, 70, 45, [spider1, spider2])
            elif player.level == 2:
                player.win = True          
    elif player.win:   
        screen.blit(win,(0,0))
    elif player.lost:   
        screen.blit(lost,(0,0))

            
    
    
    pygame.display.update()
    clock.tick(FPS)