# Сдать решение задачи I-Максимум неполного массива
#
# В некотором физическом эксперименте показания прибора снимались с
# частотой 5 измерений в секунду. Эксперимент проводился в течение
# довольно большого времени, и в результате накопилось очень много
# данных.
#
# Ученых, которые проводили данный эксперимент, очень интересует,
# какое максимальное значение измеряемой величины достигалось во время
# измерения. Но вот беда: на остановку установки также требуется
# секунда времени, и в течение этого времени с установки могут
# приходить совершенно любые значения величины. В связи с этим,
# показания последних 5 измерений учитывать при поиске максимального
# значения не следует.
#
# Вам необходимо написать программу, которая в данном потоке чисел
# заранее неизвестной длины находит максимальное значение, отбрасывая
# при этом последние 5 измерений.
#
# Формат входных данных
# На вход вашей программе передается последовательность натуральных
# чисел -- результаты измерений. Каждое новое число передается с новой
# строки. Гарантируется, что длина входной последовательности не
# меньше 6 и не превосходит 10 9 . На конце последовательности
# передается число 0.
#
# Формат выходных данных
# Программа должна вывести на экран одно число -- максимальное значение
# входной последовательности за исключением последних 5 элементов.
#
# Примеры
# Ввод	Вывод
# 1       1
# 2
# 3
# 4
# 5
# 6
# 0
#
#
# Ввод	Вывод
# 1       373
# 5
# 2
# 15
# 373
# 232
# 43
# 21
# 5433
# 5312
# 0
def create_input_data() -> list:
    """Creates a list of values."""
    print(
        "Input a list of values. Every value is in a new line."
        "Use 0 + Enter to finish."
    )
    arr = []
    while True:
        inp = input()
        if inp == "0":
            break
        arr.append(int(inp))
    return arr


def clear_data(arr) -> list:
    """Removes the last five values (exclude some builtin functions)."""
    length = 0
    new_arr = []
    for _ in arr:
        length += 1
    for idx in range(length - 5):
        new_arr.append(arr[idx])
    return new_arr


def clear_data_pw(arr) -> list:
    """Removes the last five values in a more pythonic way."""
    arr = arr[:-5]
    return arr


def get_max(arr) -> int:
    """Finds the maximum in an array."""
    max_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el
    return max_el


def get_max_pw(arr) -> int:
    """Finds the max of an array in a more pythonic way."""
    return max(arr)


def main():
    """The main function."""
    arr = create_input_data()
    # arr = [1, 5, 2, 15, 373, 232, 43, 21, 5433, 5312]
    max_el = get_max(clear_data(arr))
    print(max_el)


if __name__ == "__main__":
    main()

