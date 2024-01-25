# Сдать решение задачи C-Разноцветные холмы
#
# В Банановой республике очень много холмов, соединенных мостами.
# На химическом заводе произошла авария, в результате чего испарилось
# экспериментальное удобрение "зован". На следующий день выпал цветной
# дождь, причем он прошел только над холмами. В некоторых местах падали
# красные капли, в некоторых – синие, а в остальных – зеленые, в
# результате чего холмы стали соответствующего цвета. Президенту
# Банановой республики это понравилось, но ему захотелось покрасить
# мосты между вершинами холмов так, чтобы мосты были покрашены в цвет
# холмов, которые они соединяют. К сожалению, если холмы разного цвета,
# то покрасить мост таким образом не удастся. Посчитайте количество
# таких "плохих" мостов.
#
# Формат входных данных
# В первой строке входных данных содержится число N (0 < N ≤ 100) –
# количество холмов. Далее идет матрица смежности, описывающая наличие
# мостов между холмами (1 – мост есть, 0 – нет). После матрицы
# смежности идёт пустая строка , и в последней строке записано N чисел,
# обозначающих цвет холмов: 1 – красный; 2 – синий; 3 – зеленый.
#
# Формат выходных данных
# Выведите одно число – количество "плохих" мостов.
#
# Примеры
# -> 7 -> 0 1 0 0 0 1 1 -> 1 0 1 0 0 0 0 -> 0 1 0 0 1 1 0 ->
# 0 0 0 0 0 0 0 -> 0 0 1 0 0 1 0 -> 1 0 1 0 1 0 0 -> 1 0 0 0 0 0 0 -> ->
# 1 1 1 1 1 3 3 -- <- 4
def create_input_data():
    adj_matrix = []
    n = 0
    cnt = 0
    colors = []
    while True:
        inp = input()
        if inp == "  ":  # Double whitespace to finish the input.
            break
        if cnt == 0:
            n = int(inp)
        elif cnt < n + 1:
            adj_matrix.append([int(el) for el in inp.split()])
        elif inp == " ":  # One whitespace for empty line.
            continue
        else:
            colors = [int(el) for el in inp.split()]
        cnt += 1
    return n, adj_matrix, colors


def count_bad_bridges(n, adj_matrix, colors):
    """
    Подсчитывает количество "плохих" мостов в графе, представленном
    матрицей смежности и цветами вершин.

    Args:
    - n (int): Количество вершин в графе.
    - adj_matrix (list of lists): Матрица смежности графа.
    - colors (list): Цвета вершин.

    Returns:
    - cnt (int): Количество "плохих" мостов в графе.
    """
    # Инициализация счетчика "плохих" мостов
    cnt = 0
    # Итерация по строкам матрицы смежности
    for i in range(n):
        # Итерация по столбцам, начиная с i-го элемента,
        # чтобы не перебирать элементы ниже диагонали
        for j in range(i, n):
            # Условие для подсчета "плохого" моста: наличие ребра
            # и различие цветов вершин, которые это ребро соединяет
            if adj_matrix[i][j] == 1 and colors[i] != colors[j]:
                cnt += 1
    return cnt


def main():
    # arr = (
    #     7,
    #     [
    #         [0, 1, 0, 0, 0, 1, 1],
    #         [1, 0, 1, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 0, 1, 0],
    #         [1, 0, 1, 0, 1, 0, 0],
    #         [1, 0, 0, 0, 0, 0, 0]
    #     ],
    #     [1, 1, 1, 1, 1, 3, 3]
    # )
    # print(count_bad_bridges(*arr))
    print(count_bad_bridges(*create_input_data()))


if __name__ == "__main__":
    main()
