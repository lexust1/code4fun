# Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный 
# многоугольник с большим числом сторон будет выглядеть как окружность.
import turtle


def main():
    turtle.shape("turtle")
    # Number of parts.
    n = 100
    for part in range(n):
        turtle.forward(1000/n)
        turtle.left(360/n)
    

if __name__ == "__main__":
    main()
