# Упражнение №7: кривая дракона
# Нарисуйте кривую дракона. Кривая дракона нулевого порядка -
# горизонтальный отрезок. Разделим отрезок пополам и построим на нем
# прямой угол, получив кривую дракона первого порядка:
#
#
# На сторонах прямого угла снова построим прямые углы. При этом вершина
# первого угла находится справа от начальной точки A, а направления,
# в которых строятся вершины остальных углов, чередуются.
import turtle


def dragon_curve(turtle, depth, length, sign):
    # The basic case.
    if depth == 0:
        turtle.forward(length)
        return
    # The recursive case.
    turtle.left(-45 * sign)
    dragon_curve(turtle, depth - 1, length / 2 ** 0.5, 1)
    turtle.left(90 * sign)
    dragon_curve(turtle, depth - 1, length / 2 ** 0.5, -1)
    turtle.left(-45 * sign)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    dragon_curve(turtle, 7, 180, 1)

    turtle.exitonclick()


if __name__ == "__main__":
    main()