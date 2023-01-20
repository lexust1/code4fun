# Нарисуйте пружину. Используйте функцию, рисующую дугу.
import turtle
from turtle import Screen


def draw_arc(side, n):
    for part in range(n):
        turtle.forward(side)
        turtle.right(180 / n)


def main():
    screen = Screen()
    turtle.shape("turtle")
    for coil in range(3):
        turtle.setheading(90)
        draw_arc(3, 100)
        turtle.setheading(90 + 180)
        draw_arc(1, 100)
    screen.exitonclick()


if __name__ == "__main__":
    main()
