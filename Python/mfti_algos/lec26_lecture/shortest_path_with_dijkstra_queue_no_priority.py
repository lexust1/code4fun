# Алгоритм Дейкстры с очередью, но с очередью без приоритетов.
# - Обход начинается с первой вершины
# - Из вершины определяется путь до каждого соседа. Если расстояние
# (путь) до соседа оказывается меньше, чем текущий, то мы таких соседей
# загоняем в очередь, что в дальнейшем посмотреь уже на соседей этих
# добавленных вершин. По сути, они становятся кандидатами для добавления
# в кратчайший путь.
# - После просмотра всех соседей текущей вершины, если в очереди есть
# вершины, мы начинаем просматривать их соседей. И так до тех пор,
# пока очередеь не закончится.
# Здесь важно обратить внимание, что очередь без приоритетов. Т.е.
# это означает, что некоторые вершины мы можем добавлять в очередь
# несколько раз и несколько раз через них искать кратчайшие пути
# от разных соседей. Так и должно быть, хотя это отчасти и снижает
# эффективность алгоритма, что может быть решено засчет очереди с
# приоритетом (различные виды куч).

# Асимптотическая сложность алгоритма Дейкстры с обычной очередью:
#
# 1. Инициализация: Создание и инициализация словаря расстояний
# (distances) и словаря предшественников (predecessors) для всех
# вершин требует O(V) операций, где V — количество вершин в графе.
#
# 2. Основной цикл алгоритма: В худшем случае каждая вершина и каждое
# ребро будут рассмотрены один или несколько раз. Вершина может быть
# добавлена в очередь несколько раз (каждый раз, когда находится
# более короткий путь до какого-либо её соседа), что потенциально
# увеличивает количество обработок каждой вершины.
#
# 3. Выбор вершины для обработки: Поскольку используется обычная
# очередь, выбор следующей вершины для обработки не требует
# дополнительных затрат времени сверх тех, что уже затрачены на
# добавление вершин в очередь. Однако, отсутствие приоритетов
# приводит к тому, что вершины обрабатываются в порядке их добавления,
# а не на основе наименьшего текущего расстояния.
#
# 4. Обновление расстояний: Для каждой вершины алгоритм проверяет
# всех её соседей. В худшем случае, когда граф плотный и каждая
# вершина соединена с каждой, это может потребовать до O(V)
# операций проверки для каждой вершины. Но поскольку каждое ребро
# рассматривается отдельно при обновлении расстояний, общее
# количество операций обновления можно оценить как O(E), где E —
# количество рёбер в графе.
#
# Итоговая асимптотическая сложность: Асимптотическая сложность
# алгоритма Дейкстры с использованием обычной очереди без приоритетов
# в целом будет O(V^2 + E) для плотных графов, где каждая вершина
# потенциально соединена с каждой другой, и O(V + E) в более
# разреженных графах. Однако, из-за возможности многократного
# добавления вершин в очередь без учёта их текущего минимального
# расстояния, этот метод может быть менее эффективен по сравнению
# с использованием очереди с приоритетами, где сложность составляет
# O((V + E)log V).
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
        # Добавляем обратное ребро в граф
        add_edge(graph, v2, v1, weight)
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
    else:
        # Если вершина v1 присутствует в графе, обновить словарь,
        # добавив v2 как ключ и вес как значение
        graph[v1][v2] = weight


def dijkstra(graph, start):
    """
    Реализация алгоритма Дейкстры для нахождения кратчайших путей от
    начальной вершины до всех остальных при помощи очереди без
    приоритетов.

    Args:
    graph (dict): Граф, представленный в виде словаря смежности.
    start: Начальная вершина, с которой начинается поиск.

    Returns:
    dict: Словарь предшественников, который позволяет восстановить
    кратчайший путь от начальной вершины до всех остальных.
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
    # Создаем словарь предшественников
    predecessors = {i: None for i in graph}
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Находим новое расстояние до текущего соседа
            new_distance = distances[vertex] + graph[vertex][neighbour]
            # Если сосед не словаре расстояний (по сути, не посещен) или
            # вновь найденное расстояние до соседа оказывается меньше
            # текущего расстояния, то (здесь две версии, обе рабочии,
            # но надо менять словарь расстояний выше)
            # if neighbour not in distances or new_distance < distances[neighbour]:
            if new_distance < distances[neighbour]:
                # Обновляем расстояние до соседа
                distances[neighbour] = new_distance
                # И добавляем соседа в очередь, чтобы искать дальше уже
                # его соседей. Важный момент, что здесь нет приоритетов
                # в очереди. Это значит, что некоторые узлы могут быть
                # посещены несколько раз, что ухудшает эффективность
                # алгоритма.
                queue.append(neighbour)
                # Сохраняем предшественника для соседа
                predecessors[neighbour] = vertex
    return predecessors


# В лекции предлагается вариант восстановления через обратный счет,
# т.е. из длину пути до последнего узла мы вычитаем длину ребра до
# каждого соседа, смотрим совпадение и двигаемся вперед. Интресный
# поход. Вероятно, хорош, когда мы хотим сэкономить место под хранение
# предшественников. Но с предшественниками подход более прозрачный,
# меньше расчетов и просто список узлов вряд ли может занимать много
# места даже для больших графов. Поэтому сохраняем тот подход, который
# был и при BFS.
def reconstruct_path(predecessors, start, end):
    """
    Восстанавливает путь в графе от начальной до конечной вершины,
    используя предоставленный словарь предшественников.

    Args:
    predecessors (dict): Словарь, где ключи - это вершины, а значения -
    их предшественники. Получается в результате выполнения функции bfs.
    start (str): Начальная вершина пути.
    end (str): Конечная вершина пути.

    Returns:
    list: Список вершин, составляющих кратчайший путь от start до end.
          Возвращает "No path", если путь не существует.
    """
    # Начинаем с конечной вершины
    vertex = end
    path = []
    # Перемещаемся по предшественникам от конечной вершины к начальной
    while vertex != start:
        # Добавляем текущую вершину в путь
        path.append(vertex)
        # Получаем предшественника текущей вершины
        vertex = predecessors[vertex]
        # Если для вершины нет предшественника, путь не существует
        if vertex is None:
            return "No path"
    # Добавляем начальную вершину в путь как остаток пути
    path.append(start)
    # Возвращаем путь в правильном порядке от начальной до конечной
    # вершины, т.к. реконструкция идет с конца.
    return path[::-1]


def main():
    # graph = create_adj_list()
    # print(graph)
    # # Граф с изолированной областью
    # graph = {
    #     'A': {'B': 2.0, 'H': 15.0},
    #     'B': {'A': 2.0, 'C': 1.0, 'D': 5.0},
    #     'C': {'B': 1.0, 'D': 3.0, 'G': 1.0, 'F': 2.0},
    #     'D': {'B': 5.0, 'C': 3.0, 'F': 4.0, 'E': 6.0},
    #     'G': {'C': 1.0, 'F': 1.0},
    #     'F': {'C': 2.0, 'D': 4.0, 'G': 1.0, 'E': 7.0, 'H': 3.0},
    #     'E': {'D': 6.0, 'F': 7.0, 'I': 2.0},
    #     'H': {'F': 3.0, 'I': 12.0, 'A': 15.0},
    #     'I': {'E': 2.0, 'H': 12.0},
    #     'J': {'K': 2.0},
    #     'K': {'J': 2.0}
    # }
    # # Граф без изолированных областей.
    # graph = {
    #     'A': {'B': 2.0, 'H': 15.0},
    #     'B': {'A': 2.0, 'C': 1.0, 'D': 5.0},
    #     'C': {'B': 1.0, 'D': 3.0, 'G': 1.0, 'F': 2.0},
    #     'D': {'B': 5.0, 'C': 3.0, 'F': 4.0, 'E': 6.0},
    #     'G': {'C': 1.0, 'F': 1.0},
    #     'F': {'C': 2.0, 'D': 4.0, 'G': 1.0, 'E': 7.0, 'H': 3.0},
    #     'E': {'D': 6.0, 'F': 7.0, 'I': 2.0},
    #     'H': {'F': 3.0, 'I': 12.0, 'A': 15.0},
    #     'I': {'E': 2.0, 'H': 12.0}
    # }
    # Граф без изолированных областей, изменил C-F/С-F с 2 на 3,
    # чтобы избежать неоднозначность путей для проверки.
    graph = {
        'A': {'B': 2.0, 'H': 15.0},
        'B': {'A': 2.0, 'C': 1.0, 'D': 5.0},
        'C': {'B': 1.0, 'D': 3.0, 'G': 1.0, 'F': 3.0},
        'D': {'B': 5.0, 'C': 3.0, 'F': 4.0, 'E': 6.0},
        'G': {'C': 1.0, 'F': 1.0},
        'F': {'C': 3.0, 'D': 4.0, 'G': 1.0, 'E': 7.0, 'H': 3.0},
        'E': {'D': 6.0, 'F': 7.0, 'I': 2.0},
        'H': {'F': 3.0, 'I': 12.0, 'A': 15.0},
        'I': {'E': 2.0, 'H': 12.0}
    }
    predecessors = dijkstra(graph, "A")
    print(predecessors)
    path = reconstruct_path(predecessors, "A", "H")
    print(path)


if __name__ == "__main__":
    main()
