# Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.
from math import pi
import turtle
from turtle import Screen


def draw_circle(radius, n):
    for part in range(n):
        side = 2 * pi * radius / n
        turtle.forward(side)
        turtle.left(360 / n)

    # print(side) #use for pixel compensation.


def draw_arc(radius, n):
    for part in range(n):
        side = pi * radius / n
        turtle.forward(side)
        turtle.left(180 / n)


def main():
    screen = Screen()
    turtle.shape("turtle")
    # The face
    radius = 100
    n = 100
    comp = pi * radius / n
    turtle.goto(0, 0)
    turtle.begin_fill()
    draw_circle(100, 100)
    turtle.color("yellow")
    turtle.end_fill()
    turtle.color("black")
    # The right eye.
    turtle.penup()
    turtle.goto(40 + comp, 130)  # comp compensates pixels of side
    turtle.pendown()
    turtle.begin_fill()
    draw_circle(20, 20)
    turtle.color("blue")
    turtle.end_fill()
    turtle.color("black")
    # The left eye.
    turtle.penup()
    turtle.goto(-40 - comp, 130)
    turtle.pendown()
    turtle.begin_fill()
    draw_circle(20, 20)
    turtle.color("blue")
    turtle.end_fill()
    turtle.color("black")
    # The nose.
    turtle.penup()
    turtle.goto(comp, 130)
    turtle.pendown()
    turtle.width(5)
    turtle.right(90)
    turtle.forward(50)
    # The smile.
    turtle.penup()
    turtle.goto(-60 + comp, 80)
    turtle.setheading(270)
    turtle.pendown()
    turtle.color("red")
    turtle.width(5)
    draw_arc(60, 50)

    screen.exitonclick()


if __name__ == "__main__":
    main()




