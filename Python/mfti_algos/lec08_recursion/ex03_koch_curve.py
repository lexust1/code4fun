# Упражнение №3: кривая Коха
# Нарисуйте кривую Коха. Процесс её построения выглядит следующим
# образом: берём единичный отрезок, разделяем на три равные части и
# заменяем средний интервал равносторонним треугольником без этого
# сегмента.
# В результате образуется ломаная, состоящая из четырёх звеньев
# длины 1/3. На следующем шаге повторяем операцию для каждого из
# четырёх получившихся звеньев и т. д… Предельная кривая и есть
# кривая Коха.

import turtle


def koch_curve(turtle, depth, length):
    # The base case.
    if depth == 0:
        turtle.forward(length)
        return
    # else:
    # The recursive case (a short version)
    # A list of rotation angles:
    angles = [60, -120, 60, 0]
    # Iterate over every little part of the chain.
    for angle in angles:
        koch_curve(turtle, depth - 1, length / 3)
        turtle.left(angle)
    # The recursive case (a long version)
    # koch_curve(turtle, depth - 1, length / 3)
    # turtle.left(60)
    # koch_curve(turtle, depth - 1, length / 3)
    # turtle.left(-120)
    # koch_curve(turtle, depth - 1, length / 3)
    # turtle.left(60)
    # koch_curve(turtle, depth - 1, length / 3)
    # turtle.left(0)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    koch_curve(turtle, 2, 180)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
