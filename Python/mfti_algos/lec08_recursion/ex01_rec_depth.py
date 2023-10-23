# Упражнение №1: длина рекурсии
# С помощью функции fac(n) определите текущую установленную глубину
# рекурсии и сравните ваш результат с возвращаемым значением функции
# sys.getrecursionlimit(). Учтите, что sys.getrecursionlimit()
# возвращает максимальную глубину стека вызовов, а не максимальную
# глубину рекурсии для какой-либо функции.
from copy import deepcopy
import sys


def only_frac(n):
    # The base case.
    if n == 0:
        res = 1
        print(f"The base case (n = {n}): {res}")
        return res
    # The recursion case.
    res = n * frac(n - 1)
    print(f"The recursion case (n = {n}): {res}")
    return res


def frac(n, depth=1, max_depth=1):
    # The base case.
    if n == 0:
        res = 1, depth, max_depth
        print(f"The base case (n = {n}): "
              f"factorial = {res[0]}, "
              f"the current depth = {depth}, "
              f"the max depth = {max_depth}.")
        return res
    # The recursion case.
    res_cur = frac(n - 1, depth + 1, max(depth + 1, max_depth))
    res = n * res_cur[0], depth, res_cur[2]
    print(f"The recursion case (n = {n}): "
          f"factorial = {res[0]}, "
          f"the current depth = {res[1]}, "
          f"the max depth = {res[2]}.")
    return res


def main():
    frac(10)
    print(f"The Python recursion limit: {sys.getrecursionlimit()}")


if __name__ == "__main__":
    main()
