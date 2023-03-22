# Нарисуйте 10 вложенных правильных многоугольников.
# Используйте функцию, рисующую правильный n-угольник.
from math import pi, sin
import turtle
from turtle import Screen


def draw_polygon(side, n):
    for part in range(n):
        turtle.forward(side)
        turtle.left(360 / n)


def main():
    screen = Screen()
    side = 50
    delta_side = 10
    for n in range(3, 13):
        # Count circle radius for polygon and set the star point and
        # angle.
        radius = side / (2 * sin(360 / (2 * n) * pi / 180))
        # print(radius)
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(radius, 0)
        turtle.pendown()
        turtle.left(180 - (180 * (n - 2) / (2 * n)))
        # Draw every polygon.
        draw_polygon(side, n)
        # Set the start point.
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.setheading(0)
        side += delta_side
    screen.exitonclick()


if __name__ == "__main__":
    main()
