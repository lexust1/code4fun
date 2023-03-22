# Нарисуйте квадрат.
import turtle


def main():
    # The 1st method.
    turtle.shape("turtle")
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    # The 2nd method.
    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    for part in range(4):
        turtle.forward(50)
        turtle.left(90)


if __name__ == "__main__":
    main()
