# Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую
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
    delta = 0
    for circle in range(10):
        turtle.setheading(90)
        draw_circle(3, 100 + delta)
        turtle.setheading(270)
        draw_circle(3, 100 + delta)
        delta += 20
    screen.exitonclick()


if __name__ == "__main__":
    main()


