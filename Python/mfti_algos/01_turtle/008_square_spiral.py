# Нарисуйте «квадратную» спираль.
import turtle
from turtle import Screen


def main():
    screen = Screen()
    turtle.shape("turtle")
    delta = 0
    for part in range(40):
        turtle.forward(50 + delta)
        turtle.left(90)
        delta += 10
    screen.exitonclick()


if __name__ == "__main__":
    main()
