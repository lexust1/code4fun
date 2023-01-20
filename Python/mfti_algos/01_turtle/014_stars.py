# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11.
# Используйте функцию, рисующую звезду с n вершинами.
import turtle
from turtle import Screen


def draw_star(side, n):
    for part in range(n):
        turtle.forward(side)
        turtle.left(180 + 180 / n)


def main():
    screen = Screen()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    draw_star(200, 5)
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    draw_star(200, 11)

    screen.exitonclick()


if __name__ == "__main__":
    main()