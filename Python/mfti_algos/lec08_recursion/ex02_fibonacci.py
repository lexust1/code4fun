# Упражнение №2: числа Фибоначчи
# Напишите программу, вычисляющую n-ное число Фибоначчи.
# Используйте рекурсивные вызовы функций. Пример:
#
# Ввод	Вывод
# 7       13
#
#
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Сложность O(2^n).

def fibonacci(n):
    # The base case.
    if n == 0 or n == 1:
        res = n
        print(f"The base case (n = {n}): {res}")
        return res
    # The recursion case.
    # # The first recursive subcase:
    # res1 = fibonacci(n - 1)
    # print(f"The first recursive subcase: {res1}.")
    # # The second recursive subcase
    # res2 = fibonacci(n - 2)
    # print(f"The second recursive subcase: {res2}")
    # res = res1 + res2
    res = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"The recursive case (n = {n}): {res}")
    return res


def main():
    n = 7
    print(fibonacci(n))


if __name__ == "__main__":
    main()

