# Упражнение №2
# Вам даны числа N и M, количество вершин и ребер ориентированного
# графа. Далее идет M строк вида u, v, w, где u и v задают начало и
# конец ребра, а w - его вес. В конце дано число - стартовая вершина.
# Посчитайте кратчайшие расстояния до всех вершин, используя алгоритм
# Дейкстры за O(N^2).
from collections import deque


def create_adj_list():
    """
    Создает представление графа в виде списка смежности.

    Returns:
    graph: dict, представление графа в виде списка смежности
    """
    # Вводим количество вершин (n) и рёбер (m)
    n, m = [int(x) for x in input().split()]
    # Инициализируем граф
    graph = {}
    # Добавляем рёбра с весом
    for _ in range(m):
        v1, v2, weight = input().split()
        weight = float(weight)
        # Добавляем ребро в граф
        add_edge(graph, v1, v2, weight)
    return graph


def add_edge(graph, v1, v2, weight):
    """
    Добавляет ребро между двумя вершинами с заданным весом в граф.

    Args:
    graph (dict): Граф, в который будет добавлено ребро.
    v1: Первая вершина ребра.
    v2: Вторая вершина ребра.
    weight: Вес ребра.
    """
    if v1 not in graph:
        # Если вершина v1 отсутствует в графе, добавить её с словарём,
        # содержащим v2 как ключ и вес как значение
        graph[v1] = {v2: weight}
        if v2 not in graph:
            graph[v2] = {}
    else:
        # Если вершина v1 присутствует в графе, обновить словарь,
        # добавив v2 как ключ и вес как значение
        graph[v1][v2] = weight


def dijkstra_queue_without_priority(graph, start):
    """
    Реализация алгоритма Дейкстры для нахождения кратчайших расстояний
    от начальной вершины до всех остальных при помощи очереди без
    приоритетов.

    Args:
    graph (dict): Граф, представленный в виде словаря смежности.
    start: Начальная вершина, с которой начинается поиск.

    Returns:
    dict: Словарь кратчайших расстояний от стартвоой вершины до всех
        остальных вершины.
    """
    # Создание словаря для хранения кратчайших расстояний от start до
    # каждой вершины
    # distances = {}
    distances = {i: float("inf") for i in graph}
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Установка расстояния до начальной вершины равным 0
    distances[start] = 0
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Находим новое расстояние до текущего соседа
            new_distance = distances[vertex] + graph[vertex][neighbour]
            # Если сосед не словаре расстояний (по сути, не посещен) или
            # вновь найденное расстояние до соседа оказывается меньше
            # текущего расстояния, то
            if new_distance < distances[neighbour]:
                # Обновляем расстояние до соседа
                distances[neighbour] = new_distance
                # И добавляем соседа в очередь, чтобы искать дальше уже
                # его соседей. Важный момент, что здесь нет приоритетов
                # в очереди. Это значит, что некоторые узлы могут быть
                # посещены несколько раз, что ухудшает эффективность
                # алгоритма.
                queue.append(neighbour)
    return distances


# Результаты наивного алгоритма могут отличаться (может не доходить до
# некоторых вершин), т.к. он больше заточены на поиск расстояния между
# двумя конкретными вершинами, а не на поиск расстояния до все вершин.
# "Наивная реализация алгоритма Дейкстры может эффективно находить
# кратчайшее расстояние между двумя конкретными вершинами в некоторых
# случаях, но она может столкнуться с трудностями при попытке
# определить кратчайшие расстояния от одной вершины ко всем остальным
# в графе из-за способа, которым она выбирает следующую вершину для
# рассмотрения.
#
# Проблема с наивной реализацией заключается в том, что она не всегда
# гарантирует, что выбранная следующая вершина для рассмотрения
# является той, которая минимизирует текущее известное расстояние до
# всех не посещенных еще вершин. В результате, если в графе есть более
# короткий путь, проходящий через вершины, которые еще не были
# рассмотрены, наивная реализация может пропустить эти пути, оставив
# некоторые расстояния как бесконечно далекие (обозначенные inf).
#
# Такое поведение объясняется тем, что наивная реализация опирается
# на локальный выбор следующей вершины без учета общей картины
# кратчайших путей в графе. Это отличается от более продвинутых
# реализаций, таких как использование очереди с приоритетами (кучи),
# которая каждый раз выбирает для рассмотрения вершину с наименьшим
# текущим известным расстоянием до стартовой вершины. Это обеспечивает,
# что все вершины будут рассмотрены в порядке увеличения расстояний,
# гарантируя нахождение глобально оптимальных кратчайших путей ко
# всем доступным вершинам в графе.
def dijkstra_naive(graph, start):
    """
    Реализация алгоритма Дейкстры для нахождения кратчайших путей от
    начальной вершины до всех остальных.

    Args:
    graph (dict): Граф, представленный в виде словаря смежности.
    start: Начальная вершина, с которой начинается поиск.

    Returns:
    predecessors: Список предшественников кратчайшего пути.
    """
    # Инициализация множества посещенных вершин
    visited = set()
    # Создание словаря для хранения кратчайших расстояний от start до
    # каждой вершины
    distances = {i: float("inf") for i in graph}
    # Установка расстояния до начальной вершины равным 0
    distances[start] = 0
    # Добавление начальной вершины в множество посещенных
    visited.add(start)
    # Текущая вершина для рассмотрения
    vertex = start
    # Ведем рассмотрение, пока количество посещенных вершин не
    # сравняется с количеством вершин в графе.
    while len(visited) != len(graph):
        # Инициализация переменных для поиска ближайшего непосещенного
        # соседа
        min_distance = float("inf")
        candidate = None
        # Перебираем всех соседей текущей вершины.
        for neighbour in graph[vertex]:
            # Если соседа еще не посещали
            if neighbour not in visited:
                # Находим новое расстояние до текущего соседа
                new_distance = distances[vertex] + graph[vertex][neighbour]
                # Если это расстояние меньше расстояние, которое уже
                # хранится, обновляем его
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                # Если найденной расстояние (путь) до соседа оказывается
                # короче, чем все предыдущие, то сосед переходит в
                # кандидаты, как вершина кратчайшего пути.
                if new_distance < min_distance:
                    candidate = neighbour
                    min_distance = new_distance
        # Если кандидата нет, значит мы обошли все вершины текущей
        # компоненты, и пытаемся попасть в вершину из другой компоненты,
        # которая недостижима.
        if candidate is None:
            print("Все вершины данной компоненты посещены. "
                  "Остальные вершины из стартовой вершины недостижимы.")
            return distances
        # Либо мы добавляем финального кандидата на кратчайший путь и
        # сохряняем его предсшественника для востановления в будущем
        else:
            visited.add(candidate)
            vertex = candidate
    # Возвращаем множество посещенных вершин
    return distances


def main():
    # graph = create_adj_list()
    # print(graph)
    graph = {
        'A': {'B': 2.0, 'H': 15.0},
        'B': {'C': 1.0, 'D': 5.0},
        'C': {'D': 3.0, 'G': 1.0},
        'D': {'F': 4.0, 'E': 6.0},
        'G': {'F': 1.0},
        'F': {'C': 2.0, 'H': 3.0},
        'E': {'F': 7.0, 'I': 2.0},
        'I': {'H': 12.0},
        'H': {},
        'J': {'K': 2.0},
        'K': {}
    }

    distances = dijkstra_queue_without_priority(graph, "A")
    print(distances)
    distances = dijkstra_naive(graph, "A")
    print(distances)


if __name__ == "__main__":
    main()
