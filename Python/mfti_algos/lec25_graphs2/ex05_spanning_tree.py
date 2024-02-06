# Сдать решение задачи E-Построить остовное дерево обходом в ширину
#
# Дан невзвешенный неориентированный связный граф. Вершины
# пронумерованы от 0. Трeбуется с помощью обхода в ширину построить
# остовное дерево.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа:
# n (2 <= n <= 1000) — число вершин в графе и m (1 <= m <= 20000) —
# число рёбер. В следующих m строках задаются ребра: по два числа в
# каждой строке — номера соединённых вершин.
#
# Формат выходных данных
# Требуется распечатать n-1 пару чисел, каждyю на новой строке.
# Каждая пара задаёт ребро в остовном дереве.
#
# Примеры
# Ввод
# 2 1
# 1 0
#
# Вывод
# 0 1
#
# Ввод
# 6 7
# 2 3
# 2 0
# 5 2
# 1 0
# 1 2
# 5 1
# 4 1
# Вывод
# 1 0
# 1 4
# 1 5
# 1 2
# 2 3
# Граф, который имеет циклы, может иметь несколько остовных деревеьв.
# Особенно это заметно, когда начинаешь из разных вершин. Также
# множества для хранения вершин может сыграть роль, т.к. в отличие от
# словаря порядок не гарантируется.
from collections import deque


def create_adj_list():
    # Задаем число ребер (m) и вершин (n) графа
    n, m = [int(x) for x in input().split()]
    graph = {str(i): set() for i in range(n)}
    # Проходим по всем ребрам графа
    for _ in range(m):
        # Считываем вершины, соединенные ребром
        v1, v2 = input().split()
        # Т.к. граф не направленный, смотри в обоих направлениях
        for v, u in (v1, v2), (v2, v1):
            graph[v].add(u)
    return graph


def bfs(graph, start):
    """
    Выполняет обход графа в ширину (BFS) и строит остовное дерево.

    Обход начинается с начальной вершины и продвигается через соседние
    вершины. Функция возвращает список рёбер, образующих остовное дерево
    графа.

    Args:
        graph (dict): Граф, представленный в виде словаря, где ключи -
            это узлы, а значения - множества соседних узлов.
        start (str): Начальный узел, с которого начинается обход.

    Returns:
        edges (list of tuple): Список рёбер остовного дерева.
    """
    # Инициализируем множество для отслеживания посещенных узлов
    visited = set()
    # Инициализируем лист под хранение ребер остовного дерева
    edges = []
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Добавляем начальный узел в множество посещенных.
    visited.add(start)
    # Продолжаем выполнять цикл, пока очередь не пуста
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Если сосед еще не был посещен, добавляем его в множество
            # посещенных и в очередь.
            if neighbour not in visited:
                # Помечаем соседа как посещенный.
                visited.add(neighbour)
                # Добавляем соседа в очередь для дальнейшего обхода.
                queue.append(neighbour)
                # Добавляем ребро к дереву
                edges.append((vertex, neighbour))
    return edges


def format_output_data(edges):
    """
    Выводит рёбра остовного дерева в удобочитаемом формате.

    Каждое ребро представляется парой вершин, разделённых пробелом.

    Args:
        edges (list of tuple): Список рёбер остовного дерева.
    """
    for vertices in edges:
        print(f"{vertices[0]} {vertices[1]}")


def main():
    # graph = create_adj_list()
    # print(graph)
    # # Связный граф без изолированных частей.
    # graph = {
    #     '0': {'12', '11', '1', '10'},
    #     '1': {'7', '0'},
    #     '2': {'6'},
    #     '3': {'11'},
    #     '4': {'10', '6'},
    #     '5': {'8', '13'},
    #     '6': {'4', '2', '10'},
    #     '7': {'13', '1'},
    #     '8': {'12', '5'},
    #     '9': {'11'},
    #     '10': {'4', '0', '6'},
    #     '11': {'3', '14', '9', '0', '12'},
    #     '12': {'8', '11', '0'},
    #     '13': {'5', '7'},
    #     '14': {'11'}
    # }
    graph = {
        '0': {'1', '2'},
        '1': {'0', '4', '2', '5'},
        '2': {'0', '1', '3', '5'},
        '3': {'2'},
        '4': {'1'},
        '5': {'1', '2'}
    }
    # print(bfs(graph, "0"))
    edges = bfs(graph, "1")
    format_output_data(edges)



if __name__ == "__main__":
    main()