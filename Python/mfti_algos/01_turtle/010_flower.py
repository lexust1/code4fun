# Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую
# окружность.
import turtle
from turtle import Screen


def draw_circle(side, n):
    for part in range(n):
        turtle.forward(side)
        turtle.left(360 / n)


def main():
    screen = Screen()
    turtle.shape("turtle")
    for circle in range(6):
        draw_circle(1, 360)
        turtle.right(60)
    screen.exitonclick()


if __name__ == "__main__":
    main()
