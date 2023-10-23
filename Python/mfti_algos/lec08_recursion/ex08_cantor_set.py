# # Упражнение №8: Канторово множество
# # Нарисуйте Канторово множество. Канторово множество нулевого порядка -
# # горизонтальный отрезок. Удалив среднюю треть получим множество первого
# # порядка. Повторяя данную процедуру получим остальные множества.
import turtle


def cantor_set(turtle, depth, length, x, y):
    # The base case.
    if depth == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(length)
        return
    # The recursive case.
    # Draw the current line
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(length)
    # Move down for the next two recursive calls
    # Draw the left segment on the next level
    cantor_set(turtle, depth - 1, length / 3, x, y - 20)
    # Draw the right segment on the next level
    cantor_set(turtle, depth - 1, length / 3, x + length / 3 * 2, y - 20)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    cantor_set(turtle, 5, 360, 0, 0)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
