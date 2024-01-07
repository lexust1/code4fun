# Упражнение №4
# Цвет шарика. Пусть он зависит от скорости.
import sys
import pygame


def calculate_color(speed):
    # Нормализуем скорость для расчета цвета
    # Предположим, что максимальная скорость для "красного" цвета - 300
    normalized_speed = min(speed / 300, 1)
    # Интерполируем между зеленым (0,255,0) и красным (255,0,0)
    red = int(normalized_speed * 255)
    green = int((1 - normalized_speed) * 255)
    return red, green, 0


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
# Ускорение
acceleration = 100
# Трение
friction_coefficient = 0.1
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
    if keys[pygame.K_LEFT]:
        vx -= acceleration * dt
    if keys[pygame.K_RIGHT]:
        vx += acceleration * dt
    if keys[pygame.K_UP]:
        vy -= acceleration * dt
    if keys[pygame.K_DOWN]:
        vy += acceleration * dt
    # Рассчитываем силу трения
    friction_force_x = - friction_coefficient * vx
    friction_force_y = - friction_coefficient * vy
    # Применяем силу трения к скорости
    vx += friction_force_x * dt
    vy += friction_force_y * dt
    # Проверка условий для отражения от стенки
    if x - radius <= 0 or x + radius >= width:
        vx = - vx
    if y - radius <= 0 or y + radius >= height:
        vy = - vy
    # Обновление положения шарика
    x += vx * dt
    y += vy * dt
    # Рассчитываем величину скорости
    speed = (vx ** 2 + vy ** 2) ** 0.5
    # Рассчитываем цвет на основе скорости
    color = calculate_color(speed)
    # Очистка экрана
    screen.fill((0, 0, 0))
    # Рисование шарика
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    # Обновление содержимого окна
    pygame.display.flip()
