# Сдать решение задачи G-Степень строки

# Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку
# s^k = sss (k раз). Например, третьей степенью строки abc является
# строка аbсаbсаbс.
#
# Корнем k степени из строки s называется такая строка t
# (если она существует), что t^k = s.
#
# Ваша задача состоит в том, чтобы написать программу, находящую
# степень строки или корень из нее.
#
# Формат входных данных
# На вход программе подается 2 строки. Первая содержит строку S,
# вторая - степень k. Отрицательная степень означает взятие корня
# соответствующей степени.
#
# Формат выходных данных
# Вывести строку, являющуюуся ответом на задачу. Если такой строки
# нет, то нужно вывести 'NO SOLUTION' (без кавычек).
#
# Примеры
# Ввод	Вывод
# abc     abcabcabc
# 3
#
#
# Ввод	    Вывод
# abcdabcd    abcd
# -2
#
#
# Ввод	Вывод
# abcd    NO SOLUTION
# -4
#
# Эту функцию переработал, особенно что касается возведения в степень.
# Также внес небольшие изменения в извлечение корня.
def create_input_data() -> list:
    """Creates input data."""
    print("Input a string in the first line and power in the second line: ")
    arr = []
    while True:
        inp = input()
        if inp == "":
            break
        arr.append(inp)
    return arr


def choose_operation(arr) -> int | str:
    """Chooses between count_root and count_power"""
    # If power is negative.
    if int(arr[1]) < 0:
        return count_root(arr)
    # If power is positive.
    elif int(arr[1]) > 0:
        return count_power(arr)
    # If power is zero.
    else:
        return "Use positive or negative power, not zero."


def count_power(arr):
    original_string = arr[0]
    power = int(arr[1])
    result = ""
    current_string = original_string
    while power > 0:
        # Если текущая степень нечетна, добавляем текущую строку к результату
        if power % 2 == 1:
            result += current_string
        # Удваиваем текущую строку
        current_string += current_string
        # Делим степень на 2
        power //= 2
    return result


def count_root(arr):
    string = arr[0]
    root = -int(arr[1])
    if len(string) % root != 0:
        return "NO SOLUTION"
    potential_root = string[ : len(string) // root]
    for i in range(0, len(string), len(potential_root)):
        if string[i : i + len(potential_root)] != potential_root:
            return "NO SOLUTION"
    return potential_root


def main():
    arr = create_input_data()
    # print(arr)
    res = choose_operation(arr)
    print(res)



if __name__ == "__main__":
    main()
