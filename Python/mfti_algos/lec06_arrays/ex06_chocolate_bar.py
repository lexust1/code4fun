# Сдать решение задачи F-Шоколадка
#
# Саша, не сделал домашнюю работу, зато купил шоколадку. И, по глупости,
# начал распечатывать ее прямо на уроке... Шелест золотинки услышала
# учительница. Она хотела вызвать в школу родителей, но Саша уговорил
# ее не вызывать их, а дать дополнительное задание.
#
# Учительница внимательно посмотрела на шоколадку (она была размером
# 3х4 плиток), разделила на кусочки по две плитки и угостила всех,
# кто сделал домашнюю работу. А Сашу попросила написать программу,
# которая определяет, сколько существует способов деления шоколадки
# размером 3×N плиток на кусочки по две плитки.
#
# Для выполнения задания Саше нужна помощь.
#
# Примечание: все плитки в шоколадке пронумерованы, поэтому способы
# деления, симметричные относительно точки или оси могут будут разными.

# Формат входных данных
# На входе одно число N <= 10000
#
# Формат выходных данных
# Вывести одно число, количество способов разделить шоколадку.
#
# Примеры
# Ввод	Вывод
# 2       3
#
# Ввод	Вывод
# 4       11

def input_chocolate_length() -> int:
    """Creates input."""
    inp = int(input("Input the chocolate length (N <= 10000): "))
    return inp


def count_number_of_ways(inp: int) -> int | str:
    """Counts the number of ways how to divide the chocolate bar."""
    if inp == 0:  # 3 x 0
        mes = (
            "It is impossible to divide the chocolate bar because there is " 
            "no chocolate."
        )
        return mes
    elif inp % 2 != 0:  # 3 x 1, 3 x 3, 3 x 5, ...
        mes = (
            f"It is impossible to divide the chocolate bar because the amount "
            f"of chocolate pieces is odd: 3 x {inp}"
        )
        return mes
    elif inp == 2:  # 3 x 2
        return 3
    elif inp == 4:  # 3 x 2
        return 11
    elif inp > 4:  # 3 x 4, 3 x 6, 3 x 8, ...
        arr = [0] * (int(inp / 2))
        arr[0] = 3
        arr[1] = 11
        for idx in range(2, len(arr)):
            arr[idx] = 4 * arr[idx - 1] - arr[idx - 2]
        return arr[-1]


def main():
    inp = input_chocolate_length()
    ways = count_number_of_ways(inp)
    print(ways)


if __name__ == "__main__":
    main()
