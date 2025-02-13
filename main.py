import sys
import pygame
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30) #создание шрифта для игры

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Awesome Shooter Game")

FIGHTER_STEP = 0.5
fighter_image = pygame.image.load('images/fighter.png') # импорт изображения
fighter_width, fighter_height = fighter_image.get_size() # получить размер изображения
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height # начальное местоположение
fighter_is_moving_left, fighter_is_moving_right = False, False

BALL_STEP = 0.3
ball_image = pygame.image.load('images/ball.png') #Загрузка ball image
ball_width, ball_height = ball_image.get_size() #получить размер изображения
ball_x, ball_y = fighter_x + fighter_width / 2 - ball_width / 2, fighter_y - ball_height
ball_was_fired = False

ALIEN_STEP = 0.1
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0

game_is_running = True
while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE: #нажатие на пробел коробля
                ball_was_fired = True #меняется знаечение на true поя-ся шарик независимо есть ли или нет
                ball_x, ball_y = fighter_x + fighter_width / 2 - ball_width / 2, fighter_y - ball_height #текущее расположение коробля
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left  and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP

    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False #когда шарик выходит за пределы экраный значение меняется на false

    alien_y += ALIEN_STEP #на каждой итерации добалвяем alien_step

    if ball_was_fired:
        ball_y -= BALL_STEP # перемешение шарика вверх по экрану

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y)) #помещение изображении поверхности на screen поверхность
    screen.blit(alien_image, (alien_x, alien_y))#помещение alien_image на поверхности screen

    if ball_was_fired:
        screen.blit(ball_image, (ball_x, ball_y))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

game_over_text = game_font.render("Game Over", True, 'white') #текс
game_over_rect = game_over_text.get_rect() #помещение текста в прямоугольник
game_over_rect.center = (screen_width / 2, screen_height / 2) # координаты центра для отображения прямоугольника
screen.blit(game_over_text, game_over_rect) #помещение текста в прямоугольник
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()