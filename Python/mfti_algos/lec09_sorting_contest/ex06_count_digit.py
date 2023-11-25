# Сдать решение задачи F-Число вхождений цифры
#
# Заданная цифра в числе
# Сколько раз цифра d входит в десятичную запись числа n?
#
# Входные данные
#
# Число 0≤d≤9. Пробел. Целое положительное число n в десятичной
# системе (0 ≤ n ≤ 3·10 6) .
#
# Выходные данные
#
# Сколько раз цифра d входит в запись числа n.
#
# Примеры
#
# Вход/Input      Выход/Output
#
# 2 123           1
#
# 3 1323533       4
#
def count_digits(input_data: list) -> int:
    """
    Count the number of occurrences of a digit in a list of digits.
    Args:
        input_data (list): A list of digits.
    Returns:
        cnt: The number of occurrences of the first digit in the list.
    """
    cnt = 0
    for digit in input_data[1]:
        if digit == input_data[0]:
            cnt += 1
    return cnt


def main():
    """The entry point."""
    input_data = input("Input the data: ").split()
    # print(input_data)
    print(count_digits(input_data))


if __name__ == "__main__":
    main()
