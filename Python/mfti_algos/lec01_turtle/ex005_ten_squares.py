# Нарисуйте 10 вложенных квадратов.
import turtle


def main():
    turtle.shape("turtle")
    num_of_squares = 10
    square_side = 50
    delta = 10
    x, y = 0, 0
    for square in range(num_of_squares):
        for part in range(4):
            turtle.forward(square_side)
            turtle.left(90)
        x -= delta
        y -= delta
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        square_side += 2 * delta


if __name__ == "__main__":
    main()
