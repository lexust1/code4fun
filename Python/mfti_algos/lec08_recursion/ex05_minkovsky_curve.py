# Упражнение №5 кривая Минковского
# Нарисуйте кривую Минковского. Кривая Минковского нулевого порядка -
# горизонтальный отрезок. Затем на каждом шаге каждый из отрезков
# заменяется на ломанную, состоящую из 8 звеньев.
import turtle


def minkovsky_curve(turtle, depth, length):
    # The base case:
    if depth == 0:
        turtle.forward(length)
        return
    # The recursive case:
    angles = [90, -90, -90, 0, 90, 90, -90, 0]
    for angle in angles:
        minkovsky_curve(turtle, depth - 1, length / 8)
        turtle.left(angle)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    minkovsky_curve(turtle, 2, 8 * 180)

    turtle.exitonclick()


if __name__ == "__main__":
    main()