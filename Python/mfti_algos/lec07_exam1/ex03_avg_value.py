# Сдать решение задачи C-Среднее значение последовательности,
# заканчивающейся нулем
#
# На вход программе подается последовательность чисел, заканчивающихся
# нулем. Сам ноль не входит в последовательность. Найти среднее значение
# последовательности. Для округления использовать функцию round(x, n).
# Где x - число, n - количество знаков после запятой.
#
# Формат входных данных
# Последовательность чисел, заканчивающихся нулем. Одно число в строку.
#
# Формат выходных данных
# Одно число — среднее значение. Округлить до двух цифр после запятой.
#
# Примеры
# Ввод	Вывод
# 4       5.67
# 8
# 5
# 0

def create_input_data() -> list:
    """Creates an array of values."""
    arr = []
    print(
        "Input a value.\nEvery value is a new line.\n"
        "Use 0 + Enter to quit."
    )
    while True:
        inp = input()
        if inp == "0":
            break
        arr.append(int(inp))
    return arr


def get_avg(arr) -> float:
    """Calculates the average."""
    avg = round(sum(arr) / len(arr), 2)
    return avg


def get_avg2(arr) -> float:
    """Calculates the average (not use sum and len functions)."""
    sum_arr = 0
    len_arr = 0
    for el in arr:
        sum_arr += el
        len_arr += 1
    avg = round(sum_arr / len_arr, 2)
    return avg


def main() -> None:
    """The main function."""
    print(get_avg(create_input_data()))


if __name__ == "__main__":
    main()
