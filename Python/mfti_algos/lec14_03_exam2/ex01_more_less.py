# Сдать решение задачи A-Больше-меньше
#
# Больше-меньше
# Вам дано выражение вида "a x b", где a и b - натуральные числа, а x -
# знак сравнения, '<' или '>'. Истинно ли данное выражение?
#
# Формат входных данных
# В первой строке число a, во второй знак сравнения, в третьей - число b.
# Оба числа - натуральные.
#
# Формат выходных данных
# Если выражение истинно, выведите YES, иначе NO
#
# Примеры
# Ввод	Вывод
# 1       YES
# <
# 2
#
#
# Ввод	Вывод
# 10      NO
# >
# 100

def create_input_data():
    arr = []
    print("Input the data: ")
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    return arr


def more_less(arr):
    a = int(arr[0])
    sign = arr[1]
    b = int(arr[2])
    if sign == ">":
        return "YES" if a > b else "NO"
    else:
        return "YES" if a < b else "NO"


def main():
    print(more_less(create_input_data()))


if __name__ == "__main__":
    main()
