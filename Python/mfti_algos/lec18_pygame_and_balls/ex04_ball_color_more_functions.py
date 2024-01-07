# Тоже самое, что в предыдущем файле, но оформил в виде функции боль
# большинство операций, чтобы код стал более читаемым.
# Упражнение №4
# Цвет шарика. Пусть он зависит от скорости.
import sys
import pygame


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


def run_game(x, y, vx, vy, acceleration, friction_coefficient):
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
        # Очистка экрана
        screen.fill((0, 0, 0))
        # Рисование шарика
        pygame.draw.circle(screen, color, (int(x), int(y)), radius)
        # Обновление содержимого окна
        pygame.display.flip()


def main():
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
    # Запуск
    run_game(x, y, vx, vy, acceleration, friction_coefficient)


if __name__ == "__main__":
    main()
