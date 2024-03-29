# Сдать решение задачи H-Постоение гамильтонова цикла
#
# Дан неориентированный граф содержащий гамильтонов цикл, требуется
# найти этот цикл.
#
# Формат входных данных
# На вход программе в первой строке подаются через пробел два числа:
# N (3 <= N <= 18) - число вершин в графе и M (1 <= M <= 200) -
# число ребер. В следующих M строках задаются ребра, по два числа в
# каждой строке - номера соединенных вершин.
#
# Формат выходных данных
# Требуется распечатать номера вершин, задающих гамильтонов цикл в
# графе.
# Номера вершин нужно вывести в порядке следования по циклу.
# Если циклов несколько вывести любой.
#
# Примеры
# Ввод	Вывод
# 3 3     0 2 1
# 0 2
# 0 1
# 1 2
#
#
# Ввод	Вывод
# 5 6     0 1 3 2 4
# 1 3
# 3 2
# 1 0
# 1 2
# 4 2
# 4 0
#
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
    return n, graph


def find_hamiltonian_cycle_with_dfs(graph, n, vertex="0", visited=None, path=None):
    """
    Находит гамильтонов цикл в графе.

    Args:
    graph (dict): Граф, представленный в виде словаря смежности,
        где ключи - это вершины, а значения - множества соседних вершин.
    n (int): Общее количество вершин в графе.
    vertex (str, optional): Текущая вершина, с которой начинается или
        продолжается поиск. По умолчанию "0".
    path (list, optional): Текущий путь, представленный списком вершин,
        по которым мы уже прошли. Используется в рекурсии для
        запоминания пройденного пути. По умолчанию None, что означает
        ачало нового пути.
    visited (set, optional): Множество посещенных вершин.
        Используется для предотвращения повторного посещения вершин в
        рамках текущего поиска цикла. По умолчанию None, что означает,
        что ни одна вершина еще не посещена.

    Returns:
    list or None: Список вершин, образующих гамильтонов цикл, или None,
        если цикл не найден.
    """
    # Если путь или множество посещенных вершин не инициализированы,
    # инициализируем их
    if path is None:
        path = []
    if visited is None:
        visited = set()
    # Добавляем текущую вершину в путь и в множество посещенных вершин
    visited.add(vertex)
    path.append(vertex)
    # Если длина пути равна количеству вершин в графе, проверяем,
    # образует ли путь цикл
    # Проверяем, есть ли ребро, возвращающее нас в начальную
    # вершину, чтобы замкнуть цикл
    if len(path) == n and path[0] in graph[path[-1]]:
        return path  # Возвращаем найденный цикл
    # Итерируем по соседям текущей вершины
    for neighbour in graph[vertex]:
        # Проверяем, посетили ли мы уже соседнюю вершину
        if neighbour not in visited:
            # Выполняем рекурсивный вызов для соседней вершины
            candidate = find_hamiltonian_cycle_with_dfs(graph, n, neighbour, visited, path)
            # Если рекурсивный вызов нашел цикл, возвращаем его
            if candidate is not None:
                return candidate
    # Если ни один из соседей не привел к успеху, удаляем текущую
    # вершину из пути и множества посещенных
    path.pop()
    visited.remove(vertex)
    # Возвращаем None, так как цикл не найден
    return None


def main():
    n, graph = create_adj_list()
    # n, graph = (
    #     5,
    #     {
    #         '0': {'4', '1'},
    #         '1': {'0', '2', '3'},
    #         '2': {'4', '3', '1'},
    #         '3': {'2', '1'},
    #         '4': {'0', '2'}
    #     }
    # )

    print(graph)
    cycle = find_hamiltonian_cycle_with_dfs(graph, n)

    if cycle is not None:
        print("Hamiltonian Cycle:", cycle)
    else:
        print("No Hamiltonian Cycle found")


if __name__ == "__main__":
    main()
