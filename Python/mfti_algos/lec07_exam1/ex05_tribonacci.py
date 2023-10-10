# Сдать решение задачи E-Первое число трибоначчи, превосходящее заданное
#
# Числа трибоначчи - последовательность целых чисел {t n }, заданная с
# помощью рекуррентного соотношения:
# t 0 = 0, t 1 = 0, t 2 = 1 , t n+3 = t n + t n+1 + t n+2
# Нужно найти номер первого числа трибоначчи, превосходящего заданное.
# Нумерация начинается с 0 .
#
# Формат входных данных
# Одно целое число.
#
# Формат выходных данных
# Одно число — номер первого числа трибоначчи, превосходящее заданное
# во входных данных число.
#
# Примеры
# Ввод	Вывод
# 10      7
#
# Ввод	Вывод
# 0       2
#
# Ввод	Вывод
# 13      8

# Example:
# 1. t0 = 0
# 2. t1 = 0
# 3. t2 = 1
# 4. t3 = t0 + t1 + t2 = 0 + 0 + 1 = 1
# 5. t4 = t1 + t2 + t3 = 0 + 1 + 1 = 2
# 6. t5 = t2 + t3 + t4 = 1 + 1 + 2 = 4
# 7. t6 = t3 + t4 + t5 = 1 + 2 + 4 = 7
# 8. t7 = t4 + t5 + t6 = 2 + 4 + 7 = 13
# 9. t8 = t5 + t6 + t7 = 4 + 7 + 13 = 24
# This value exceeds 20
# So, the sequence is 0, 0, 1, 1, 2, 4, 7, 13, 24,... and the first number that
# exceeds 20 in this sequence is 24. The index of this number in the sequence
# is 8 (considering the indexing starts at 0).

def get_tribonacci_idx(threshold) -> int:
    """Finds the number index in the Tribonacci sequence.

     Find the number index in the Tribonacci sequence that exceeds the
     threshold.
     """
    t_seq = [0, 0, 1]
    idx = 2
    while t_seq[-1] <= threshold:
        t_seq.append(sum(t_seq[-3:]))
        idx += 1
    return idx


def get_tribonacci_idx2(threshold) -> int:
    """Finds the number index in the Tribonacci sequence.

     Find the number index in the Tribonacci sequence that exceeds the
     threshold not using the builtin sum function and slices.
     """
    t_seq = [0, 0, 1]
    idx = 2
    sum_seq = 1
    while t_seq[idx] <= threshold:
        idx += 1
        t_seq.append(sum_seq)
        sum_seq += t_seq[idx]
    return idx


def main() -> None:
    """The main function."""
    threshold = int(input("Input a number (threshold): "))
    print("The index:", get_tribonacci_idx(threshold))


if __name__ == "__main__":
    main()
