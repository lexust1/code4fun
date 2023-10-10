# Сдать решение задачи F-Наибольший общий делитель
#
# Необходимо найти НОД двух чисел, используя алгоритм Евклида.
#
# Формат входных данных
# На вход подаются два натуральных числа, по числу в новой строке.
#
# Формат выходных данных
# Одно число - НОД входных чисел.
#
# Примеры
# Ввод	Вывод
# 30      6
# 18
#
#
# Ввод	Вывод
# 1071    21
# 462

# Example of the algo:
# Initial Numbers:
# a = 30, b = 18
# Calculations:
# 30 mod 18 = 12 → a = 18, b = 12
# 18 mod 12 = 6  → a = 12, b = 6
# 12 mod 6 = 0   → a = 6,  b = 0
# Result:
# GCD(30, 18) = 6
# The complexity of O(log(min(a, b)))


def create_input_data() -> list:
    """Creates a list of input data."""
    arr = []
    print("Whitespace + Enter to finish.")
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(int(inp))
    return arr


def gcd(arr) -> int:
    """Calculates the greatest common divisor (GCD)."""
    a, b = arr
    while b != 0:
        a, b = b, a % b
    return a


def main() -> None:
    """The main function."""
    print(gcd(create_input_data()))


if __name__ == "__main__":
    main()
