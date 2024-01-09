# Упражнение №3
# Используя информацию из предыдущей лабораторной, напишите добавление
# шарика по нажатию кнопки мыши. Все шарики должны отскакивать от
# стенок. Соударение шаров - не нужно.
#
# Что понадобится для этого (подсказки):
#
# класс Ball, с методами update(self, dt) (для обновления координат),
# render(self, canvas) (для рисования, canvas - это наш объект screen
# из Pygame).
#
# кончно, все координаты и скорости представим объектами класса Vector
#
# в классе Vector нам пригодится дополнительный метод intpair(self),
# который вернет координаты округленные и в виде кортежа (т.е. в виде,
# в котором удобно скормить их Pygame-у)
import pygame
import random
import sys


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector: {self.x}, {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(number * self.x, number * self.y)

    def __rmul__(self, number):
        return self.__mul__(number)

    def __neg__(self):
        return Vector(- self.x, - self.y)

    def intpair(self):
        return int(self.x), int(self.y)

    @staticmethod
    def sum_vectors(vectors):
        total_x, total_y = 0, 0
        for vector in vectors:
            total_x += vector.x
            total_y += vector.y
        return Vector(total_x / len(vectors), total_y / len(vectors))


class Ball:
    def __init__(self,
                 radius=10,
                 position=(0, 0),
                 velocity=(0, 0),
                 acceleration=100,
                 friction_coefficient=0.1):
        self.radius = radius
        self.position = Vector(*position)
        self.velocity = Vector(*velocity)
        self.acceleration = acceleration
        self.friction_coefficient = friction_coefficient

    def apply_acceleration(self, acceleration_direction, dt):
        self.velocity += acceleration_direction * self.acceleration * dt

    def apply_friction(self, dt):
        friction_force = -self.friction_coefficient * self.velocity
        self.velocity += friction_force * dt

    def mirror_ball(self, width, height):
        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= width:
            self.velocity.x = -self.velocity.x
        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= height:
            self.velocity.y = -self.velocity.y

    def update_position(self, dt):
        self.position += self.velocity * dt

    def update(self, dt, acceleration_direction):
        self.apply_acceleration(acceleration_direction, dt)
        self.apply_friction(dt)
        self.update_position(dt)
        self.mirror_ball(500, 500)

    def render(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            self.position.intpair(),
            self.radius
        )


def run_game():
    pygame.init()
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('YAHOOOO')
    clock = pygame.time.Clock()

    balls = []
    # balls = [
    #     Ball(20, (100, 100), (50, 60), 100, 0.1),
    #     Ball(25, (200, 200), (-70, 80), 100, 0.1),
    #     Ball(15, (300, 300), (20, -30), 100, 0.1)
    # ]

    while True:
        dt = clock.tick(50) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                radius = random.randint(10, 30)
                vx, vy = random.randint(-100, 100), random.randint(-100, 100)
                # acceleration = 100
                # friction_coefficient = 0.1
                balls.append(Ball(radius, (x, y), (vx, vy)))
                # balls.append(Ball(radius, (x, y), (vx, vy), acceleration, friction_coefficient))
        acceleration_direction = Vector()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            acceleration_direction.x -= 1
        if keys[pygame.K_RIGHT]:
            acceleration_direction.x += 1
        if keys[pygame.K_UP]:
            acceleration_direction.y -= 1
        if keys[pygame.K_DOWN]:
            acceleration_direction.y += 1

        screen.fill((0, 0, 0))
        for ball in balls:
            ball.update(dt, acceleration_direction)
            ball.render(screen)
        pygame.display.flip()


def main():
    run_game()


if __name__ == "__main__":
    main()
