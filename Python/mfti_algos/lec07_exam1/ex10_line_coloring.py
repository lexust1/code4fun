# Сдать решение задачи J-Раскраска прямой
#
# Напротив Васиного дома поставили забор, состоящий из 10^9 дощечек.
# Каждый день, выгдядывая в окно, он видел, что часть забора с
# дощечки l_i до дощечки r_i красят в цвет c_i . При этом он записывал,
# какой отрезок забора в какой цвет красили. Эти данные он предоставил
# Вам и просил ответить на вопрос: в какой цвет будут выкрашены
# интересующие Васю дощечки через N дней? Изначально все дощечки
# были цвета 0.
#
# Формат входных данных
# На первой строке вводится число 0 <= N <= 100 - количество дней.
# Далее на 3*N строках идут тройки чисел (каждое в новой строке):
# 1 <= l_i <= ri <= 10^9 и 0 <= c_i <= 10^6.
# Далее идет число 0 < M <= 100 - число интересующих Васю дощечек.
# Далее на M строках номера дощечек.
#
# Формат выходных данных
# Вывести M чисел, разделенных пробелами - цвета дощечек.
#
# Примеры
# Ввод	Вывод
# 3       2 1
# 4
# 6
# 2
# 7
# 19
# 6
# 13
# 15
# 1
# 2
# 5
# 14
#

# Распишем ввод и вывод для наглядности:
# Ввод
# Число дней равно 3.
# 3
# 1-й день: красим с 4 по 6 дощечки в цвет 2.
# 4
# 6
# 2
# 2-й день: красим с 7 по 19 дощечки в цвет 6.
# 7
# 19
# 6
# 3-й день: красим с 13 по 15 дощечки в цвет 1.
# 13
# 15
# 1
# Количество интересующих Васю дощечек - это 2 шт.
# 2
# Вопрос 1. В какой цвет покрашена 5 дощечка. (Ответ: 2)
# 5
# Вопрос 3. В какой цвет покрашена 14 дощечка. (Ответ: 1)
# 14
#
def create_input_data() -> list:
    """Creates the input_data."""
    print(
        "Input every value on a new line."
        "Whitespace + Enter to finish."
    )
    arr = []
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(int(inp))
    return arr


def parse_data(arr):
    """Parses the data."""
    # A number of days.
    num_days = arr[0]
    # A line range (from 3 to 6, for example) and the color tor
    # the range.
    line_range_and_colors = arr[1:3 * num_days + 1]
    # A number of interesting lines.
    num_lines = arr[3 * num_days + 1]
    # Line's ids.
    line_ids = arr[-num_lines:]
    return num_days, line_range_and_colors, num_lines, line_ids


def get_colored_lines(num_days, line_range_and_colors, num_lines, line_ids):
    # Initial colors
    colors = [0] * num_lines
    for day in range(num_days):
        clr_idx = 0
        for line_id in line_ids:
            if (line_range_and_colors[0 + day * 3] <= line_id <= line_range_and_colors[1 + day * 3]):
                colors[clr_idx] = line_range_and_colors[2 + day * 3]
            clr_idx += 1
    return colors


def main():
    """The main function."""
    # arr = [3, 4, 6, 2, 7, 19, 6, 13, 15, 1, 2, 5, 14]
    # print(parse_data(arr))
    arr = create_input_data()
    print(get_colored_lines(*parse_data(arr)))


if __name__ == "__main__":
    main()
