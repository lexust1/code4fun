# O(V+E)
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


def bfs(graph, start, end):
    """
    Выполняет обход графа в ширину (Breadth-First Search, BFS) и
    вычисляет расстояние от начальной вершины до конечной.

    Функция использует очередь для обработки узлов графа. Каждый узел
    сначала проверяется на наличие в множестве посещенных узлов. Если
    узел не посещен, он добавляется в множество посещенных и в очередь.
    При этом обновляется расстояние от начального узла до текущего.
    Обход прекращается, как только найдена конечная вершина, и
    возвращается расстояние до неё.
    Если конечная вершина недостижима, возвращает float('inf').

    Args:
    graph (dict): Граф, представленный в виде словаря, где ключи -
        это узлы, а значения - множества соседних узлов.
    start (str): Начальный узел, с которого начинается обход.
    end (str): Конечный узел, до которого нужно вычислить расстояние.

    Returns:
    int: Расстояние от начальной до конечной вершины, если оно существует,
         иначе float('inf').
    """
    # Инициализируем множество для отслеживания посещенных узлов
    visited = set()
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Добавляем начальный узел в множество посещенных.
    visited.add(start)
    # Создаем словарь расстояний с бесконечностями
    distances = {i: float('inf') for i in graph}
    # Расстояние до стартовой вершины
    distances[start] = 0
    # Продолжаем выполнять цикл, пока очередь не пуста
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Проверяем, достигли ли искомой вершины, чтобы не ходить через
        # оставшийся граф. Своеобразная оптимизация.
        if vertex == end:
            return distances[end]
        # # Выводим узел, на каждом шаге. Но оформляем все в одну строку.
        # print(str(vertex), end=" ")
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Если сосед еще не был посещен, добавляем его в множество
            # посещенных и в очередь.
            if neighbour not in visited:
                # Помечаем соседа как посещенный.
                visited.add(neighbour)
                # Добавляем соседа в очередь для дальнейшего обхода.
                queue.append(neighbour)
                # Обновляем расстояние до соседа
                distances[neighbour] = distances[vertex] + 1
    return distances[end]


def main():
    # print(create_adj_list())
    # Связный граф без изолированных частей.
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
    # Граф с изоляцей вершины 2
    graph = {
        '0': {'12', '11', '1', '10'},
        '1': {'7', '0'},
        '2': set(),
        '3': {'11'},
        '4': {'10', '6'},
        '5': {'8', '13'},
        '6': {'4', '10'},
        '7': {'13', '1'},
        '8': {'12', '5'},
        '9': {'11'},
        '10': {'4', '0', '6'},
        '11': {'3', '14', '9', '0', '12'},
        '12': {'8', '11', '0'},
        '13': {'5', '7'},
        '14': {'11'}
    }
    print(bfs(graph, "0", "4"))
    print(bfs(graph, "0", "2"))


if __name__ == "__main__":
    main()