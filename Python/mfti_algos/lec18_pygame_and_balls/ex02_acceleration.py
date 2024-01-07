# Упражнение №2
# Добавим управление: пусть при нажатой клавише-стрелке, у шарика
# появляется ускорение в соответствующую сторону. Испульзуйте список
# pygame.key.get_pressed().
import sys
import pygame


# Инициализация Pygame
pygame.init()
# Установка размеров окна
width = 500
height = 500
# Радиус шарика
radius = 20
# Создание окна для отображения
screen = pygame.display.set_mode((width, height))
# Название окна
pygame.display.set_caption('YAHOOOO')
# Создание объекта Clock для управления временем
clock = pygame.time.Clock()
# Начальные координаты и скорость шарика
x = 30
y = 60
# Скорость по оси X и Y
vx = 50
vy = 50
# Главный цикл игры
while True:
    # Время, прошедшее с последнего кадра (из млс в с)
    dt = clock.tick(50) / 1000.0
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Завершение программы при нажатии Esc
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    # Ускорение в соответствии с нажатыми клавишами-стрелками
    acceleration = 100
    if keys[pygame.K_LEFT]:
        vx -= acceleration * dt
    if keys[pygame.K_RIGHT]:
        vx += acceleration * dt
    if keys[pygame.K_UP]:
        vy -= acceleration * dt
    if keys[pygame.K_DOWN]:
        vy += acceleration * dt
    # Проверка условий для отражения от стенки
    if x - radius <= 0 or x + radius >= width:
        vx = - vx
    if y - radius <= 0 or y + radius >= height:
        vy = - vy
    # Обновление положения шарика
    x += vx * dt
    y += vy * dt
    # Очистка экрана
    screen.fill((0, 0, 0))
    # Рисование шарика
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), radius)
    # Обновление содержимого окна
    pygame.display.flip()
