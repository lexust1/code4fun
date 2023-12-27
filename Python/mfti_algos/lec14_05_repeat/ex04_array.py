# Сдать решение задачи D-Обработка массива чисел
#
# На вход программа получает набор чисел, заканчивающихся решеткой.
# Вам требуется найти: среднее, максимальное и минимальное число в
# последовательности. Так же нужно вывести cумму остатков от деления
# суммы троек на последнее число тройки (каждые 3 введеных числа
# образуют тройку).
#
# Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6
# среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5
# максимум: 6
# минимум: 1
# сумма остатков троек:
# (1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3
#
# Среднее выводить, округлив до трех знаков после запятой.
# Для этого нужно использовать функцию round(x, 3)
#
# Того ваша программа должна вывести: 3.5 6 1 3
#
# Подумайте, имеет ли смысл хранить всю последовательность.
#
# Формат входных данных
# Последовательность чисел, заканчивающися '#'. Все числа от 1 до 100.
# Количество чисел в последовательности кратно трем. Одно число на
# строку.
#
# Формат выходных данных
# Четыре числа, разделенных пробелом.
#
# Примеры
# Ввод	Вывод
# 1       3.5 6 1 3
# 2
# 3
# 4
# 5
# 6
#
#
#
# Оставляем тот же подход, что было в lec06_arrays.
from typing import Union


def create_input_data() -> list:
    """Creates input data."""
    arr = []
    print("Input the values that satisfy the following conditions:\n"
          "-  1 <= value <= 100;\n"
          "-  A number of the numbers divisible by 3;\n"
          "-  One line - one number;\n"
          "-  The last element is #:")
    while True:
        inp = input()
        if inp == "#":
            break
        else:
            arr.append(int(inp))
    return arr


def count_avg(arr: list) -> float:
    """Counts the average of array."""
    sum_arr = 0
    cnt = 0
    for el in arr:
        sum_arr += el
        cnt += 1
    return round(sum_arr / cnt, 3)


def count_avg_pw(arr: list) -> float:
    """Counts the average (a more pythonic way)."""
    return round(sum(arr) / len(arr), 3)


def find_max(arr: list) -> Union[int, float]:
    """Finds the maximum of the array."""
    max_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el
    return max_el


def find_max_pw(arr: list) -> Union[int, float]:
    """Finds the maximum of the array (a more pythonic way)."""
    return max(arr)


def find_min(arr: list) -> Union[int, float]:
    """Finds the minimum of the array."""
    el_min = arr[0]
    for el in arr:
        if el < el_min:
            el_min = el
    return el_min


def find_min_pw(arr: list) -> Union[int, float]:
    """Finds the minimum of the array (a more pythonic way)."""
    return min(arr)


def count_remainders(arr: list) -> float:
    """Counts remainders."""
    cnt = 1
    sum_el = 0
    sum_rem = 0
    for el in arr:
        sum_el += el
        if cnt % 3 == 0:
            sum_rem += sum_el % el
            sum_el = 0
        cnt += 1
    return sum_rem


def count_remainders_pw(arr: list) -> float:
    """Counts remainders (a more pythonic way)."""
    sum_arr = sum([
        sum(arr[idx : idx + 3]) % arr[idx + 2]
        for idx in range(0, len(arr) - 1, 3)
    ])
    return sum_arr


def main() -> None:
    arr = create_input_data()

    average = count_avg(arr)
    average_pw = count_avg_pw(arr)

    max_el = find_max(arr)
    max_el_pw = find_max_pw(arr)

    min_el = find_min(arr)
    min_el_pw = find_min_pw(arr)

    sum_rem = count_remainders(arr)
    sum_rem_pw = count_remainders_pw(arr)

    print(f'{average} {max_el} {min_el} {sum_rem}')
    # print(f'{average_pw} {max_el_pw} {min_el_pw} {sum_rem_pw}')


if __name__ == "__main__":
    main()
