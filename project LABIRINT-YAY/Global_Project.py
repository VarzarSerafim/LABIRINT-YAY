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
scr_height= 600
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Global_Project")
#Разные важные вещи
FPS = 60

screen.fill((255, 255, 255))

#Переменная работы игры
game = True

clock = pygame.time.Clock()

#Подключаемся к папкам, где нужные файлы
path1 = os.path.join(os.getcwd(), "sprites")

path2 = os.path.join(os.getcwd(), "sounds")

#Подключаем все спрайты, и музыку
player_walk_1 = os.path.join(path2, "player_walk_1.ogg")
player_walk_1 = pygame.mixer.Sound(player_walk_1)

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

#Функция для стабилизации звука шагов, что-бы они происходили раз, в пол секунды.
player_wolk_tim = 0
def player_wolk_timing():
    global player_wolk_tim
    if player_wolk_tim == 30:
        player_walk_1.play()
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

#Класс игрока
class Player(GameSprite):
    def __init__(self, x, y, width, height, speed, x_con, y_con, mx_con, my_con, player_right_1, player_right_2, player_left_1, player_left_2, player_stay):
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
            player.anim(player_down_1, player_down_2)
            player_wolk_timing()
        if (pygame.key.get_pressed()[pygame.K_w] and self.rect.y >= self.y_con):
            self.rect.y -= self.speed
            player.anim(player_up_1, player_up_2)
            player_wolk_timing()
        if pygame.key.get_pressed()[pygame.K_d] == False and pygame.key.get_pressed()[pygame.K_a] == False and pygame.key.get_pressed()[pygame.K_w] == False and pygame.key.get_pressed()[pygame.K_s] == False:
            self.image = self.player_stay

#Создание врагов, и подобного
#player(Координаты x, координаты y, ширина, высота, скорость игрока, картинка игрока, коорднаты до кудого может дойти игрок. Первые 2, это начало. Вторые 2 координаты, это конечные)
player = Player(200, 350, 50, 80, 5, 0, 0, 450, 580, player_right_1, player_right_2, player_left_1, player_left_2, player_stay)

#Цикл игры
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((255, 255, 255))
    player.draw()
    player.move()
    
    pygame.display.update()
    clock.tick(FPS)