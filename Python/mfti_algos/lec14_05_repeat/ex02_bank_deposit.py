# Сдать решение задачи B-Банковский вклад
#
# Вклад в банке составляет x рублей. Ежегодно он увеличивается на p
# процентов, после чего дробная часть копеек отбрасывается. Каждый год
# сумма вклада становится больше. Надо определить, через сколько лет
# вклад составит не менее y рублей.
#
# Формат входных данных
# Три натуральных числа: x, p, y.
#
# Формат выходных данных
# Число лет, через сколько лет вклад составит не менее y рублей.
#
# Примеры
# Ввод	        Вывод
# 100 10 200      8
#
# Ввод	        Вывод
# 1 1 2           100
#
# Оставляем тот же подход, что было в lec06_arrays.
from decimal import Decimal, ROUND_DOWN


def create_input_data() -> list:
    """Create a list from a string."""
    inp_str = input("Input 3 integers divided by whitespace (x p y): ")
    input_data = [float(el) for el in inp_str.split()]
    return input_data


def trunc_copeck(x):
    """Trunc fractional part of copecks"""
    x = float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_DOWN))
    return x


def find_year(input_data: list) -> int:
    """Find a year when x > y."""
    x = input_data[0]
    p = input_data[1]
    y = input_data[2]
    year = 0
    while x < y:
        x = x * (1 + p / 100)
        x = trunc_copeck(x)
        year += 1
    return year


def main() -> None:
    """Main function that prints the year."""
    input_data = create_input_data()
    year = find_year(input_data)
    print(year)


if __name__ == "__main__":
    main()
