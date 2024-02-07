# O(V+E).
# Отличие от реконструкции пути в том, что там по предшественникам
# мы делали востановление для одного из кратчайших путей. А здесь мы
# находим ребра, которые лежат на абсолютно любых кратчайших путях,
# которых может быть несколько.
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
    distances (dict): Словарь расстояний от стартовой вершины до всех
        других вершин.
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
    return distances


def find_vertices(graph, end1, end2):
    """
    Находит все вершины в графе, которые лежат на каком-либо кратчайшем
    пути между двумя заданными вершинами.

    Для этого выполняется два обхода в ширину (BFS) из каждой из
    заданных вершин.
    Затем проверяется, удовлетворяет ли каждая вершина в графе условию
    принадлежности к кратчайшему пути.

    Args:
        graph (dict): Граф, представленный в виде словаря смежности,
            где ключи - это вершины, а значения - множества
            соседних вершин.
        end1 (str): Начальная вершина кратчайшего пути.
        end2 (str): Конечная вершина кратчайшего пути.

    Returns:
        list: Список вершин, которые лежат на кратчайшем пути между
        end1 и end2, или пустой список, если путь между вершинами не
        существует.
    """
    # Вычисляем кратчайшие расстояния от end1 и end2 до всех вершин
    dist_end1 = bfs(graph, end1)
    dist_end2 = bfs(graph, end2)
    # Проверяем, существует ли путь от end1 до end2
    if dist_end1[end2] == float('inf'):
        # Путь не существует
        return []
    # Инициализируем лист под хранение вершин на кратчайших путях.
    vertices_on_paths = []
    # Перебираем все вершины
    for vertex in graph:
        # Проверяем условие, удовлетворяет ли вершина условию
        # кратчайшего пути.
        if dist_end1[vertex] + dist_end2[vertex] == dist_end1[end2]:
            vertices_on_paths.append(vertex)
    # Возвращаем все вершины на кратчайших путях между вершинами.
    return vertices_on_paths


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
    print(find_vertices(graph, "6", "8"))
    print(find_vertices(graph, "11", "13"))


if __name__ == "__main__":
    main()
