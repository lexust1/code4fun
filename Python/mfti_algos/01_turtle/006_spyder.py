# Нарисуйте паука с n лапами. Пример n = 12.
import turtle


def main():
    turtle.shape("turtle")
    n = 12
    for line in range(n):
        turtle.right(360/n)
        turtle.forward(100)
        turtle.goto(0, 0)


if __name__ == "__main__":
    main()
