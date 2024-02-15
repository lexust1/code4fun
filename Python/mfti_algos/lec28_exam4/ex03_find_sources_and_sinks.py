# Сдать решение задачи C-Истоки и стоки
#
# Напомним, что вершина ориентированного графа называется истоком,
# если в нее не входит ни одно ребро и стоком, если из нее не выходит
# ни одного ребра.
#
# Ориентированный граф задан матрицей смежности. Найдите все вершины
# графа, которые являются истоками, и все его вершины, которые являются
# стоками.
#
# Формат входных данных
# Cначала вводится число n ( 1 ≤ n ≤ 100) – количество вершин в графе,
# а затем n строк по n чисел, каждое из которых равно 0 или 1, – его
# матрица смежности.
#
# Формат выходных данных
# Сначала в одну строку выведите все истоки, в следующей строке все
# стоки.
#
# Примеры
# Ввод
# 5
# 0 0 0 0 0
# 0 0 0 0 1
# 1 1 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Вывод
# 3 4
# 1 4 5
def create_adj_matrix():
    # Задаем число вершин (n)
    n = int(input())
    # Создаем список вершин (V) и словарь для отслеживания индексов
    # каждой вершины (index)
    graph = []
    for _ in range(n):
        row = [int(el) for el in input().split()]
        graph.append(row)
    return graph, n


def find_sources_and_sinks(graph, n):
    """
    Находит источники и стоки в заданном графе.

    Аргументы:
    graph (List[List[int]]): Матрица смежности, представляющая граф
    n (int): Количество узлов в графе

    Возвращает:
    Tuple[List[int], List[int]]: Кортеж, содержащий списки источников
        и стоков
    """
    # Инициализация списков для хранения источников и стоков
    sources = []
    sinks = []
    # Итерация по каждому узлу в графе
    for i in range(n):
        output = False
        input = False
        # Проверка наличия исходящих рёбер из текущего узла
        for el in graph[i]:
            if el == 1:
                output = True
        # Проверка наличия входящих рёбер в текущий узел
        for j in range(n):
            if graph[j][i] == 1:
                input = True
        # Определение, является ли текущий узел источником, стоком или
        # и тем, и другим
        if output and not input:
            sources.append(i + 1)
        elif not output and input:
            sinks.append(i + 1)
        elif not output and not input:
            sources.append(i + 1)
            sinks.append(i + 1)
    return sources, sinks


def format_result(sources, sinks):
    for el in sources:
        print(el, end=" ")
    print()
    for el in sinks:
        print(el, end=" ")
    print()


def main():
    # graph = create_adj_matrix()
    # print(graph)
    graph, n = (
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        5
    )
    sources, sinks = find_sources_and_sinks(graph, n)
    format_result(sources, sinks)


if __name__ == "__main__":
    main()
