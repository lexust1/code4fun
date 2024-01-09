# Упражнение №6
# Включаем соударение шаров. Подсказка: изменение импульса шара при
# упругом столкновении с другим шаром выглядит так:
#
# Δp1=((−2m2m1+m2p1+2m1m1+m2p2)∗n)∗n
# где:
#
# p1 - импульс нашего шара
# m1 - масса нашего шара
# p2 - импульс второго шара
# m2 - масса второго шара
# n - единичный вектор нормали контакта (в нашем случае, вектор
# направленный от центра одного шара к центру другого), первая звездочка
# - скалярное умножение на n,  вторая - умножение вектора n на число.
import pygame
import random
import sys


class Vector:
    def __init__(self, x=0, y=0):
        """ Инициализирует экземпляр вектора с координатами x и y. """
        self.x = x
        self.y = y

    def __str__(self):
        """ Возвращает строковое представление вектора. """
        return f"Vector: {self.x}, {self.y}"

    def __add__(self, other):
        """ Определяет операцию сложения (+) для двух векторов. """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Определяет операцию вычитания (-) для двух векторов. """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        """ Определяет умножение вектора на число. """
        return Vector(number * self.x, number * self.y)

    def __rmul__(self, number):
        """ Позволяет умножать число на вектор. """
        return self.__mul__(number)

    def __neg__(self):
        """ Определяет унарный минус (инверсию) вектора. """
        return Vector(-self.x, -self.y)

    def __truediv__(self, number):
        """ Определяет деление вектора на число. """
        if number == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(self.x / number, self.y / number)

    def intpair(self):
        """ Возвращает пару целых чисел (x, y). """
        return int(self.x), int(self.y)

    def normalize(self):
        """ Нормализует вектор (приводит к единичной длине). """
        magnitude = (self.x ** 2 + self.y ** 2) ** 0.5
        if magnitude == 0:
            return Vector(0, 0)
        return Vector(self.x / magnitude, self.y / magnitude)

    def dot(self, other):
        """ Возвращает скалярное произведение двух векторов. """
        return self.x * other.x + self.y * other.y


class Ball:
    def __init__(self, radius=10, position=(0, 0), velocity=(0, 0), acceleration=100,
                 friction_coefficient=0.1, color=(255, 0, 0), mass=10):
        """ Инициализирует экземпляр шара с заданными параметрами. """
        self.radius = radius
        self.position = Vector(*position)
        self.velocity = Vector(*velocity)
        self.acceleration = acceleration
        self.friction_coefficient = friction_coefficient
        self.color = color
        self.mass = mass

    def apply_acceleration(self, acceleration_direction, dt):
        """ Применяет ускорение к шару. """
        self.velocity += acceleration_direction * self.acceleration * dt

    def apply_friction(self, dt):
        """ Применяет силу трения к шару. """
        friction_force = -self.friction_coefficient * self.velocity
        self.velocity += friction_force * dt

    def mirror_ball(self, width, height):
        """ Отражает шар от границ экрана. """
        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= width:
            self.velocity.x = -self.velocity.x
        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= height:
            self.velocity.y = -self.velocity.y

    def count_impulse(self, other):
        """ Вычисляет импульс во время столкновения с другим шаром. """
        n = (other.position - self.position).normalize()
        p1 = self.velocity * self.mass
        p2 = other.velocity * other.mass
        k1 = - 2 * other.mass / (self.mass + other.mass)
        k2 = 2 * self.mass / (self.mass + other.mass)
        bracket1 = k1 * p1 + k2 * p2
        bracket2 = Vector.dot(bracket1, n)
        delta_p1 = bracket2 * n
        delta_p2 = - delta_p1
        self.velocity += delta_p1 / self.mass
        other.velocity += delta_p2 / other.mass

    def collides_with(self, other):
        """ Проверяет столкновение с другим шаром. """
        distance = ((self.position.x - other.position.x) ** 2 + (self.position.y - other.position.y) ** 2) ** 0.5
        collision = distance <= self.radius + other.radius
        return collision

    def update_position(self, dt):
        """ Обновляет позицию шара. """
        self.position += self.velocity * dt

    def is_clicked(self, mouse_pos):
        """ Проверяет, был ли шар кликнут мышью. """
        return (self.position.x - mouse_pos[0]) ** 2 + (self.position.y - mouse_pos[1]) ** 2 <= self.radius ** 2

    def render(self, screen):
        """ Отрисовывает шар на экране. """
        pygame.draw.circle(
            screen,
            self.color,
            self.position.intpair(),
            self.radius
        )



def run_game():
    # Инициализирует модули Pygame
    pygame.init()
    # Задает размеры окна
    width, height = 500, 500
    # Создает окно игры
    screen = pygame.display.set_mode((width, height))
    # Устанавливает название окна
    pygame.display.set_caption('YAHOOOO')
    # Создает таймер для контроля времени
    clock = pygame.time.Clock()
    # Инициализирует список шаров
    balls = []
    # Хранит ссылку на выбранный шар
    selected_ball = None
    # Главный игровой цикл
    while True:
        # Контролирует скорость выполнения цикла
        dt = clock.tick(50) / 1000.0
        # Обрабатывает события Pygame
        for event in pygame.event.get():
            # Проверяет, закрыто ли окно
            if event.type == pygame.QUIT:
                sys.exit()
            # Выход из игры по нажатию ESC
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            # Проверка на нажатие кнопки мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Получает позицию мыши
                x, y = pygame.mouse.get_pos()
                ball_clicked = False
                for ball in balls:
                    # Проверяет, кликнули ли на шар
                    if ball.is_clicked((x, y)):
                        # Изменяет цвет выбранного шара
                        ball.color = (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255)
                        )
                        selected_ball = ball
                        ball_clicked = True
                        break
                # Если клик был не по шару, создает новый шар
                if not ball_clicked:
                    radius = random.randint(10, 30)
                    vx, vy = random.randint(-100, 100), random.randint(-100, 100)
                    balls.append(Ball(radius, (x, y), (vx, vy)))
        # Вектор для управления ускорением
        acceleration_direction = Vector()
        # Состояние клавиш
        keys = pygame.key.get_pressed()
        if selected_ball:
            # Управление выбранным шаром с клавиатуры
            if keys[pygame.K_LEFT]:
                acceleration_direction.x -= 1
            if keys[pygame.K_RIGHT]:
                acceleration_direction.x += 1
            if keys[pygame.K_UP]:
                acceleration_direction.y -= 1
            if keys[pygame.K_DOWN]:
                acceleration_direction.y += 1
            selected_ball.apply_acceleration(acceleration_direction, dt)
        # Проверка на столкновение шаров и расчет импульса
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if balls[i].collides_with(balls[j]):
                    balls[i].count_impulse(balls[j])
        # Очищает экран
        screen.fill((0, 0, 0))
        for ball in balls:
            # Применяет физические законы к шарам и отрисовывает их
            ball.apply_friction(dt)
            ball.update_position(dt)
            ball.mirror_ball(width, height)
            ball.render(screen)
        # Обновляет содержимое всего экрана
        pygame.display.flip()


def main():
    run_game()


if __name__ == "__main__":
    main()

