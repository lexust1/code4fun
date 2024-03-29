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


def bfs(graph, start, visited):
    """
    Выполняет обход графа в ширину (Breadth-First Search, BFS).

    Args:
    graph (dict): Граф, представленный в виде словаря, где ключи -
        это узлы, а значения - списки соседних узлов.
    start: Начальный узел, с которого начинается обход.

    Returns:
        component (list): Список узлов, образующих компоненту связности,
        начинающуюся с узла start.
    """
    # Добавляет с список посещенных вершин стартовую/текущую.
    visited.add(start)
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Инициализируем список под компоненту.
    component = []
    # Добавляем начальный узел в множество посещенных.
    visited.add(start)
    # Продолжаем выполнять цикл, пока очередь не пуста
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Добавляем вершину в компоненту.
        component.append(vertex)
        # Выводим узел, на каждом шаге. Но оформляем все в одну строку.
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
    return component


def find_components(graph):
    """
    Выполняет обход всех компонент связности в графе.

    Функция итерирует по всем узлам графа. Для каждого узла,
    который еще не был посещен в предыдущих обходах, она запускает
    алгоритм поиска в ширину (BFS) для выделения компоненты связности,
    к которой принадлежит этот узел. Каждая найденная компонента
    связности добавляется в список компонент.

    Args:
    graph (dict): Граф, представленный в виде словаря.
        Ключи словаря - это узлы графа, а значения - множества смежных
        узлов.

    Returns:
    components (list): Список, содержащий компоненты связности графа.
        Каждая компонента представлена списком узлов.
    """
    # Множество для отслеживания посещенных узлов.
    visited = set()
    # Список для хранения компонент связности.
    components = []
    # Итерация по всем узлам графа.
    for start in graph:
        # Проверка, был ли узел посещен ранее.
        if start not in visited:
            # Запуск BFS для новой компоненты связности, начиная с
            # узла start.
            component = bfs(graph, start, visited)
            # Добавление найденной компоненты связности в список.
            components.append(component)
    # Возврат списка компонент связности.
    return components


def main():
    # print(create_adj_list())
    # # Одна компонента
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
    # # Две компоненты (убрал ребро 6-2)
    # graph = {
    #     '0': {'12', '11', '1', '10'},
    #     '1': {'7', '0'},
    #     '2': set(),
    #     '3': {'11'},
    #     '4': {'10', '6'},
    #     '5': {'8', '13'},
    #     '6': {'4', '10'},
    #     '7': {'13', '1'},
    #     '8': {'12', '5'},
    #     '9': {'11'},
    #     '10': {'4', '0', '6'},
    #     '11': {'3', '14', '9', '0', '12'},
    #     '12': {'8', '11', '0'},
    #     '13': {'5', '7'},
    #     '14': {'11'}
    # }
    # Три компоненты (убрал ребро 6-2, 0-11, 11-12)
    graph = {
        '0': {'12', '1', '10'},
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
        '11': {'3', '14', '9'},
        '12': {'8', '0'},
        '13': {'5', '7'},
        '14': {'11'}
    }
    components = find_components(graph)
    # print(components)
    for i, component in enumerate(components):
        print(f"Компонента {i + 1}: {component}")


if __name__ == "__main__":
    main()
