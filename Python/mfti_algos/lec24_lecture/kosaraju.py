# https://www.programiz.com/dsa/strongly-connected-components
# https://favtutor.com/blogs/strongly-connected-components
# Алгоритм Косарайю - это метод в теории графов, используемый для
# нахождения сильно связанных компонент в ориентированном графе.
# Сильно связанная компонента графа - это максимальный подграф,
# в котором для любой пары вершин V и W существует путь от V к W и путь
# от W к V.
#
# Алгоритм Косарайю состоит из трёх основных шагов:
# 1. Первый проход DFS (Обход в глубину):
# Начиная с произвольной вершины, алгоритм выполняет обход в глубину
# по всем вершинам графа.
# По завершении обхода каждой вершины, она добавляется в стек.
# Этот шаг гарантирует, что вершины помещаются в стек в порядке
# убывания времени завершения.
#
# 2. Транспонирование графа:
# В графе меняются направления всех рёбер на противоположные.
# Таким образом, если в исходном графе было ребро из
# A в B, в транспонированном графе оно будет идти из B в A.
#
# 3. Второй проход DFS на транспонированном графе:
# Используя стек, созданный в первом проходе, алгоритм выполняет
# второй обход в глубину на транспонированном графе. Каждый раз,
# когда запускается DFS, исследуются все достижимые вершины, и весь
# исследованный подграф становится одной сильно связанной компонентой.
#
# В результате этих шагов, алгоритм эффективно идентифицирует все
# сильно связанные компоненты в ориентированном графе.
#
# Асимптотическая сложность алгоритма Косарайю для нахождения сильно
# связанных компонент в ориентированном графе составляет O(V+E), где
# V - количество вершин в графе, а
# E - количество рёбер.
#
# Давайте разберемся, почему именно так:

# Первый проход DFS: Обход в глубину для каждой вершины выполняется за
# O(V+E), так как каждая вершина и каждое ребро посещаются один раз.
# Транспонирование графа: Процесс транспонирования графа также имеет
# сложность O(V+E), поскольку необходимо пройтись по всем вершинам и
# рёбрам для изменения направления рёбер.
#
# Второй проход DFS на транспонированном графе: Подобно первому проходу,
# второй проход также требует O(V+E) времени, так как каждая вершина и
# каждое ребро снова посещаются один раз.
#
# Сложность каждого из этих шагов линейно зависит от суммы количества
# вершин и рёбер в графе. Таким образом, общая временная сложность
# алгоритма Косарайю равна O(V+E).
def dfs_pass_one(graph, vertex, visited, stack):
    """
    Выполняет первый проход обхода в глубину (DFS) для графа.
    Вершины добавляются в стек в порядке завершения их обработки.

    Args:
    graph (dict): Словарь, представляющий граф.
    vertex: Начальная вершина для DFS.
    visited (set): Множество посещенных вершин.
    stack (list): Стек для хранения порядка вершин.

    Returns:
    None.
    """
    # Добавляем текущую вершину в множество посещенных
    visited.add(vertex)
    # Перебор всех соседей текущей вершины
    for neighbour in graph[vertex]:
        # Если соседняя вершина еще не посещена, рекурсивно вызываем
        # эту же функцию
        if neighbour not in visited:
            dfs_pass_one(graph, neighbour, visited, stack)
    # Добавляем текущую вершину в стек после обработки всех ее соседей
    stack.append(vertex)


def transpose_graph(graph):
    """
    Транспонирует граф, меняя направления всех рёбер на противоположные.

    Args:
    graph (dict): Словарь, представляющий граф.

    Returns:
    dict: Транспонированный граф.
    """
    # Создание нового словаря для транспонированного графа
    transposed = {vertex: set() for vertex in graph}
    # Перебор всех вершин и их соседей в исходном графе
    for vertex in graph:
        for neighbour in graph[vertex]:
            # Добавление обратного ребра в транспонированный граф
            transposed[neighbour].add(vertex)
    return transposed


def dfs_pass_two(graph, vertex, visited, scc):
    """
    Выполняет второй проход обхода в глубину (DFS) для
    транспонированного графа. Определяет сильно связанные компоненты.

    Args:
    graph (dict): Транспонированный граф.
    vertex: Начальная вершина для DFS.
    visited (set): Множество посещенных вершин.
    scc (list): Список вершин текущей сильно связанной компоненты.

    Returns:
    None.
    """
    # Добавляем текущую вершину в множество посещенных
    visited.add(vertex)
    # Перебор всех соседей текущей вершины в транспонированном графе
    for neighbor in graph[vertex]:
        # Если соседняя вершина еще не посещена, рекурсивно вызываем
        # эту же функцию
        if neighbor not in visited:
            dfs_pass_two(graph, neighbor, visited, scc)
    # Добавляем текущую вершину в текущую сильно связанную компоненту
    scc.append(vertex)


def kosaraju(graph):
    """
    Выполняет алгоритм Косарайю для идентификации сильно связанных
    компонент в графе.

    Args:
    graph (dict): Словарь, представляющий граф.

    Returns:
    list: Список сильно связанных компонент.
    """
    # Шаг 1: Первый проход DFS и заполнение стека
    # Стек для хранения порядка обработки вершин
    stack = []
    # Множество для отслеживания посещенных вершин
    visited = set()
    # Вызов первого прохода DFS для каждой непосещенной вершины (а не
    # соседа), т.е. делаем dfs, начиная с разных вершин
    for vertex in graph:
        if vertex not in visited:
            dfs_pass_one(graph, vertex, visited, stack)
    # Шаг 2: Транспонирование графа
    # Перестройка графа с изменением направления всех рёбер
    transposed_graph = transpose_graph(graph)
    # Шаг 3: Второй проход DFS для определения сильно связанных
    # компонент в обратном порядке.
    # Очистка множества посещенных вершин для второго прохода
    visited.clear()
    # Список для хранения сильно связанных компонент (всех компонент)
    strongly_connected_components = []
    # Пока есть веришины в стеке
    while stack:
        # Извлекаем вершину из стека
        vertex = stack.pop()
        # Если вершины нет среди посещенных
        if vertex not in visited:
            # Список для текущей сильно связанной компоненты
            scc = []
            # Вызов второго прохода DFS для построения сильно связанной
            # компоненты
            dfs_pass_two(transposed_graph, vertex, visited, scc)
            # Добавление идентифицированной компоненты в список
            strongly_connected_components.append(scc)
    return strongly_connected_components


def main():
    graph = {
        "A": {"B"},
        "B": {"C", "D"},
        "C": {"A"},
        "D": {"E"},
        "E": {"F"},
        "F": {"D"},
        "G": {"F", "H"},
        "H": {"I"},
        "I": {"J"},
        "J": {"G"},
        "K": {"J"}
    }
    print(kosaraju(graph))
    # dfs_pass_one(graph, "A", set(), [])
    # transposed_graph = transpose_graph(graph)
    # count_strong_connected_components()
    # print(transposed_graph)
    # # print(kosaraju(graph))


if __name__ == "__main__":
    main()
