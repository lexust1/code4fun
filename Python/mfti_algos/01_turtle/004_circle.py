# Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный 
# многоугольник с большим числом сторон будет выглядеть как окружность.
import turtle


def main():
    turtle.shape("turtle")
    for part in range(4):
        turtle.forward(50)
        turtle.left(90)
    

if __name__ == "__main__":
    main()