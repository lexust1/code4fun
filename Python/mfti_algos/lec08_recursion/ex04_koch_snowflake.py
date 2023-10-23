# Упражнение №4: снежинка Коха
# Три копии кривой Коха, построенные (остриями наружу) на сторонах
# правильного треугольника, образуют замкнутую кривую бесконечной длины,
# называемую снежинкой Коха. Нарисуйте ee.
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


def koch_snowflake(turtle, depth, length):
    # Build a snowflake using the koch curves.
    angles = [0, -120, -120]
    for angle in angles:
        turtle.left(angle)
        koch_curve(turtle, depth, length)


def main():
    turtle.shape("turtle")
    turtle.speed("fastest")
    # koch_curve(turtle, 2, 180)
    koch_snowflake(turtle, 4, 180)

    turtle.exitonclick()


if __name__ == "__main__":
    main()