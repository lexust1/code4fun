# Сдать решение задачи B-Сколько единиц в бинарной записи?
#
# Сколько 1 в бинарной записи числа
# Найти, сколько единиц содержит бинарная запись числа.
#
# Входные данные
#
# Целое неотрицательное число K.
#
# Выходные данные
#
# Сколько единиц содержит бинарная запись числа.
#
# Примеры
#
# Вход    Выход
#
# 5       2
#

def dec_to_bin(dec_number: str) -> int:
    """
    Converts a decimal number to binary and counts the number of '1's
    in the binary representation.

    Args:
        dec_number (int): The decimal number to convert.

    Returns:
        int: The count of '1's in the binary representation of the
            decimal number.
    """
    dec_number = int(dec_number)
    cnt = 0
    while dec_number > 0:
        remainder = dec_number % 2
        if remainder == 1:
            cnt += 1
        dec_number = dec_number // 2
    return cnt


def main():
    """The entry point."""
    inp = input("Input a not negative number: ")
    print(dec_to_bin(inp))

    # # The pythonic way.
    # print(sum(1 for el in bin(int(inp))[2:] if el == "1"))


if __name__ == "__main__":
    main()
