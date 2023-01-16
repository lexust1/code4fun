# Нарисуйте Архимедову спираль.
import turtle
from turtle import Screen
from math import cos, sin, pi


def main():
    screen = Screen()
    turtle.shape("turtle")
    x, y = 0, 0
    for part in range(5 * 360):
        dx = (part / 10) * cos(part * pi / 180)
        dy = (part / 10) * sin(part * pi / 180)
        turtle.goto(x + dx, y + dy)
    screen.exitonclick()


if __name__ == "__main__":
    main()

