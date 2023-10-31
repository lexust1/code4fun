# Полезно посмотреть картинку в этой же папке для обхода/траектории
# алгоритма.
def gen_bin(M, prefix=""):
    """
    Делает то же самое, что ниже, но в более простой форме.
    Две ветви по образовании всех возможных чисел. В алгоритме ниже
    мы просто загоняем эти две ветви в цикл. Аналогичные задания по
    формированию различных геометрических фигур.
    """
    if M == 0:
        print(prefix)
        return
    gen_bin(M - 1, prefix + "0")
    gen_bin(M - 1, prefix + "1")


def generate_number(N: int, M: int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащими нулями) в N-ричной
    системе счисления (N <= 10) длины M
    """
    prefix = prefix or []
    # The base case.
    if M == 0:
        print(prefix)
        return
    # The recursive case.
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


generate_number(2, 3)
gen_bin(3)
