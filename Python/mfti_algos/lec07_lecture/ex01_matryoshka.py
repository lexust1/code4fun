# Пример рекурсии на матрешке, O(n)
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=918s
def matryoshka(n):
    if n == 1:  # крайний случай
        print("Матрешечка")
    else:  # рекурсивный случай
        print("Верх матрешки n = ", n)
        matryoshka(n - 1)
        print("Низ матрешки n = ", n)


def main():
    matryoshka(5)


if __name__ == "__main__":
    main()
