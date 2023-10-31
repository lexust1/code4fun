# See rec2.png and graph_generate_permutations.py and
# generate_permutations_one_func.py
def generate_permutations(N: int, M: int = -1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом
    prefix. Упрощенная весрия
    """
    M = N if M == -1 else M
    prefix = prefix or []

    if M == 0:
        print(*prefix, end=", ", sep="")
        return

    for number in range(1, N + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()


generate_permutations(3)
