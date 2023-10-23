# Упражнение №6: кривая Леви
# Нарисуйте кривую Леви. Она получается, если взять половину квадрата
# вида /\, а затем каждую сторону заменить таким же фрагментом и так
# далее.
import turtle


def levi_curve(turtle, depth, length):
    # The base case.
    if depth == 0:
        turtle.forward(length)
        return
    # The recursive case.
    turtle.left(45)
    # The 1st side.
    levi_curve(turtle, depth - 1, length / 2)
    turtle.left(-90)
    # The 2nd side.
    levi_curve(turtle, depth - 1, length / 2)
    turtle.left(45)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    levi_curve(turtle, 7, 10 * 180)

    turtle.exitonclick()


if __name__ == "__main__":
    main()