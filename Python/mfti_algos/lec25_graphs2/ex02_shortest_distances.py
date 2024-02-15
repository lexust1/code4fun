# Сдать решение задачи B-Поиск расстояний от заданной вершины до всех
# остальных
#
# Дан невзвешенный неориентированный связный граф. Вершины
# пронумерованы от 0. Трeбуется с помощью обхода в ширину найти
# расстояния от 0-й до всех остальных вершин.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа:
# n (2 <= n <= 1000) — число вершин в графе и
# m (1 <= m <= 20000) — число рёбер. В следующих m строках задаются
# ребра: по два числа в каждой строке — номера соединённых вершин.
#
# Формат выходных данных
# Требуется распечатать n чисел, каждое на новой строке. В первой
# строке — расстояния от 0-й вершины до 0-й, во второй - от 0-й до 1-й,
# в третьей — от 0-й до 2-й и т.д.
#
# Примеры
# Ввод	Вывод
# 2 1     0
# 1 0     1
#
#
#
# Ввод	Вывод
# 6 7
# 2 3     0
# 2 0     1
# 5 2     1
# 1 0     2
# 1 2     2
# 5 1     2
# 4 1
#
# O(V+E)
from collections import deque


def create_adj_list():
    # Задаем число вершин (n), ребер (m)
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


def bfs(graph):
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
    # Устанавливаем стартовую вершину
    start = "0"
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


def create_output(distances):
    for vertex in distances:
        print(f"{distances[vertex]}")

def main():
    graph = create_adj_list()
    # graph = {
    #     '0': {'2', '1'},
    #     '1': {'0', '2', '5', '4'},
    #     '2': {'0', '3', '5', '1'},
    #     '3': {'2'},
    #     '4': {'1'},
    #     '5': {'2', '1'}
    # }

    print(graph)
    distances = bfs(graph)
    print(distances)
    create_output(distances)


if __name__ == "__main__":
    main()