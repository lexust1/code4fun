# Упражнение №6
# Добавление шаров по нажатию кнопки мыши (добавить в том месте, где
# находится курсор)
import sys
import pygame
import numpy as np
import random


def change_color(vx, vy):
    # Рассчитываем величину скорости
    speed = (vx ** 2 + vy ** 2) ** 0.5
    # Нормализуем скорость для расчета цвета
    # Предположим, что максимальная скорость для "красного" цвета - 300
    normalized_speed = min(speed / 300, 1)
    # Интерполируем между зеленым (0,255,0) и красным (255,0,0)
    red = int(normalized_speed * 255)
    green = int((1 - normalized_speed) * 255)
    return red, green, 0


def accelerate_ball(vx, vy, acceleration, dt):
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
    return vx, vy


def add_friction(vx, vy, friction_coefficient, dt):
    # Рассчитываем силу трения
    friction_force_x = - friction_coefficient * vx
    friction_force_y = - friction_coefficient * vy
    # Применяем силу трения к скорости
    vx += friction_force_x * dt
    vy += friction_force_y * dt
    return vx, vy


def mirror_ball(vx, vy, x, y, radius, width, height):
    # Проверка условий для отражения от стенки
    if x - radius <= 0 or x + radius >= width:
        vx = - vx
    if y - radius <= 0 or y + radius >= height:
        vy = - vy
    return vx, vy


def manipulate_ball(ball, dt, width, height, screen):
    # Распаковываем данные одного шарика
    radius, x, y, vx, vy, acceleration, friction_coefficient = ball
    # Ускоряем шарик
    vx, vy = accelerate_ball(vx, vy, acceleration, dt)
    # Торможение шарика из-за трения
    vx, vy = add_friction(vx, vy, friction_coefficient, dt)
    # Отражаем шарик
    vx, vy = mirror_ball(vx, vy, x, y, radius, width, height)
    # Обновление положения шарика
    x += vx * dt
    y += vy * dt
    # Меняем цвет шарика
    color = change_color(vx, vy)
    # Рисование шарика
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    ball = radius, x, y, vx, vy, acceleration, friction_coefficient
    return ball


def check_collision(ball1, ball2):
    # Получаем радиусы и координаты шаров
    radius1, x1, y1 = ball1[0], ball1[1], ball1[2]
    radius2, x2, y2 = ball2[0], ball2[1], ball2[2]
    # Вычисляем расстояние между центрами шаров
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # Проверяем, меньше ли расстояние суммы радиусов
    return distance <= (radius1 + radius2)


def handle_collision(ball1, ball2):
    # Извлечение необходимых параметров шаров
    radius1, x1, y1, vx1, vy1, acceleration1, friction_coefficient1 = ball1
    radius2, x2, y2, vx2, vy2, acceleration2, friction_coefficient2 = ball2
    # Направление нормали (от центра ball1 к центру ball2)
    normal = np.array([x2 - x1, y2 - y1])
    normal = normal / np.linalg.norm(normal)
    # Направление, перпендикулярное нормали
    tangent = np.array([-normal[1], normal[0]])
    # Разложение скоростей на нормаль и тангент
    v1n = np.dot(normal, [vx1, vy1])
    v1t = np.dot(tangent, [vx1, vy1])
    v2n = np.dot(normal, [vx2, vy2])
    v2t = np.dot(tangent, [vx2, vy2])
    # Обновление скоростей после столкновения
    new_vx1 = v2n * normal[0] + v1t * tangent[0]
    new_vy1 = v2n * normal[1] + v1t * tangent[1]
    new_vx2 = v1n * normal[0] + v2t * tangent[0]
    new_vy2 = v1n * normal[1] + v2t * tangent[1]
    # Обновляем шары с новыми скоростями
    ball1 = radius1, x1, y1, new_vx1, new_vy1, acceleration1, friction_coefficient1
    ball2 = radius2, x2, y2, new_vx2, new_vy2, acceleration2, friction_coefficient2
    return ball1, ball2


def run_game(balls):
    # Инициализация Pygame
    pygame.init()
    # Установка размеров окна
    width = 500
    height = 500
    # Создание окна для отображения
    screen = pygame.display.set_mode((width, height))
    # Название окна
    pygame.display.set_caption('YAHOOOO')
    # Создание объекта Clock для управления временем
    clock = pygame.time.Clock()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Получение позиции курсора
                x, y = pygame.mouse.get_pos()
                # Генерация случайных значений
                # Радиус
                radius = random.randint(1, 50)
                # Cкорости
                vx = random.randint(-100, 100)
                vy = random.randint(-100, 100)
                # Ускорение
                acceleration = random.uniform(-200, 200)
                # Трение
                friction_coefficient = random.uniform(0, 1)
                # Создание нового шара с случайными параметрами
                new_ball = (radius, x, y, vx, vy, acceleration, friction_coefficient)
                balls.append(new_ball)
        # Обработка столкновений
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if check_collision(balls[i], balls[j]):
                    balls[i], balls[j] = handle_collision(balls[i], balls[j])
        # Очистка экрана
        screen.fill((0, 0, 0))
        for i, ball in enumerate(balls):
            balls[i] = manipulate_ball(ball, dt, width, height, screen)
        # Обновление содержимого окна
        pygame.display.flip()


def main():
    balls = [
        (20, 30, 60, 50, 50, 100, 0.1),
        (30, 60, 120, 50, 50, 100, 0.1)
    ]
    run_game(balls)


if __name__ == "__main__":
    main()
