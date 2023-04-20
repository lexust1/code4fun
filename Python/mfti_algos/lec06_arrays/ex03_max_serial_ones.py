# Сдать решение задачи C-Максимальное число подряд идущих 1
#
# Вводится последовательность, состоящая только из 0 и 1. Необходимо
# найти максимальное количество 1, идущих подряд (без 0 между ними).
#
# Формат входных данных
# В первой строке задается натуральное N<=10000 , длина массива,
# далее идут N чисел 0 или 1 -- элементы массива.
# Каждое число вводится с новой строки.
#
# Формат выходных данных
# Одно число — результат.
#
# Примеры
# Ввод	Вывод
# 4       2
# 1
# 1
# 0
# 1
#
def create_input_data():
    """Create an array."""
    arr = []
    while True:
        inp = input("Input numbers, where the first element is the array "
                    "length and the other elements are 1 or 0 (or press"
                    "Enter to stop): ")
        if inp.strip() == "":
            break
        else:
            arr.append(int(inp))
    return arr


def count_max(arr):
    """Counts max serial ones."""
    length = arr[0]
    cnt = 0
    max_cnt = 0
    for idx in range(1, length + 1):
        if arr[idx] == 1:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        elif arr[idx] == 0:
            cnt = 0
        else:
            print("Something strange.")
    return max_cnt


def count_max_pw(arr):
    """The same as count_max but a more pythonic way."""
    cnt = 0
    max_cnt = 0
    for el in arr[1:]:
        if el == 1:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        elif el == 0:
            cnt = 0
        else:
            print("Something strange.")
    return max_cnt


def main():
    arr = create_input_data()
    print(f"Initial array: {arr}")
    max_cnt = count_max(arr)
    print(f"The first method: {max_cnt}")
    max_cnt = count_max_pw(arr)
    print(f"The second method: {max_cnt}")


if __name__ == "__main__":
    main()

