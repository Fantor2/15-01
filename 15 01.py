import pygame
import sys
from config import *
from ball import *
from stick import Stick

# здесь определяются константы,
# классы и функции


def point_in_rect(pointx, pointy, rectx, recty , rect_width, rect_height):
    inx = rectx <= pointx <=rectx + rect_width
    iny = recty <=pointy <=recty + rect_height
    return inx and iny
# здесь происходит инициация,
# создание объектов
stick=Stick()
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
#Кординаты ракетки
stick.x =stick.OFFSET
stick.y =(SCREEN_HEIGHT - stick.HEIGHT) // 2
#скорость ракетки
stick.speed_y =0
#
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
    # передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Выход за края экрана
    # левый
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x = -ball_speed_x

    # правый
    if ball_x >= SCREEN_WIDTH - r:
        # летел направо - полетел налево
        ball_speed_x = -ball_speed_x
        
    #Верхний
    if ball_y <=r:
        ball_speed_y = -ball_speed_y
    #Нижний
    if ball_y >= SCREEN_HEIGHT - r:
        ball_speed_y = -ball_speed_y
        
    stick.y +=stick.speed_y
    if stick.y <=0:
        stick.y =0
    elif stick.y >= SCREEN_HEIGHT - Stick.HEIGHT:
        stick.y = SCREEN_HEIGHT - Stick.HEIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        stick.y -= 15
    elif keys[pygame.K_DOWN]:
        stick.y += 15
    #проверяем что мяч попал в ракетку
    #вычисляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx=ball_x - r
    mid_lefty=ball_y
    
    mid_rightx=ball_x + r
    mid_righty=ball_y
    
    mid_topx= ball_x
    mid_topy= ball_y -r
    
    mid_bottomx = ball_x
    mid_bottomy = ball_y + r
    #правая граница ракетки
    if point_in_rect(mid_leftx, mid_lefty , stick.x , stick.y , stick.WIDTH, stick.HEIGHT):
        ball_speed_x = -ball_speed_x
    #верхняя граница ракетки
    if point_in_rect(mid_bottomx, mid_bottomy , stick.x , stick.y , stick.WIDTH, stick.HEIGHT):
        ball_speed_y = -ball_speed_y
    #нижняя граница ракетки
    if point_in_rect(mid_topx, mid_topy , stick.x , stick.y , stick.WIDTH, stick.HEIGHT):
        ball_speed_y = -ball_speed_y
    # обновление экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc,ORANGE, (stick.x, stick.y, Stick.WIDTH, Stick.HEIGHT))
    pygame.display.update()
