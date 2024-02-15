from collections import deque


def create_chess_graph():
    """
    Создает граф, представляющий шахматную доску, где каждый узел -
    это клетка, а ребра - возможные ходы коня. Т.е. строим граф всех
    возможных ходов из любой клетки.

    Returns:
        dict: Граф, где ключи - это обозначения клеток шахматной доски
            (например, 'a1', 'b2' и т.д.), а значения - множества
            клеток, в которые конь может попасть из данной клетки одним
            ходом.
    """
    # Возможные ходы коня - векторы смещения по вертикали и горизонтали
    knight_moves = [
        (2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)
    ]
    # Список колонок
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # Инициализируем словарь под хранение графа
    graph = {}
    # Перебор всех клеток шахматной доски
    for row in range(8):  # Цикл по строкам
        for col in range(8):  # Цикл по столбцам
            # Создание обозначения клетки (например, 'a1', 'b2' и т.д.)
            vertex = columns[col] + str(row + 1)
            # Инициализация множества соседей для клетки
            graph[vertex] = set()
            # Перебор всех возможных ходов коня из текущей клетки
            for dx, dy in knight_moves:
                # Вычисление координат клетки, в которую конь может
                # переместиться
                new_row, new_col = row + dx, col + dy
                # Проверка, что клетка находится в пределах доски
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    # Если да, то добавляем эту клетку как соседнюю для
                    # хода конем
                    neighbor = columns[new_col] + str(new_row + 1)
                    graph[vertex].add(neighbor)
    return graph


def bfs(graph, start, end):
    """
    Выполняет обход графа в ширину (BFS) от начальной вершины до
    конечной.

    Args:
        graph (dict): Граф, представленный в виде словаря смежности,
            где ключи - это вершины, а значения - множества соседних
            вершин.
        start (str): Начальная вершина для обхода.
        end (str): Конечная вершина для поиска.

    Returns:
        dict: Словарь предшественников для каждой вершины, где ключ -
            это вершина, а значение - предшественник этой вершины на
            кратчайшем пути из start. Если путь до конечной вершины не
            найден, возвращает пустой словарь.
    """
    # Множество для отслеживания посещенных вершин
    visited = set()
    # Инициализация очереди для BFS и добавление в нее начальной вершины
    queue = deque([start])
    # Добавление начальной вершины в множество посещенных
    visited.add(start)
    # Словарь предшественников, изначально для всех вершин
    # предшественник неизвестен (None)
    predecessors = {i: None for i in graph}
    # Основной цикл обхода графа
    while queue:
        # Извлечение вершины из начала очереди
        vertex = queue.popleft()
        # Проверка, достигли ли мы конечной вершины
        if vertex == end:
            return predecessors
        # Перебор всех соседних вершин
        for neighbour in graph[vertex]:
            # Добавление непосещенных соседей в очередь и множество
            # посещенных
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                # Обновление предшественника для каждой посещенной
                # вершины
                predecessors[neighbour] = vertex
    # Возвращаем словарь предшественников
    return predecessors


def reconstruct_path(predecessors, start, end):
    """
    Восстанавливает путь от начальной вершины до конечной в графе,
    используя информацию о предшественниках каждой вершины.

    Args:
        predecessors (dict): Словарь предшественников, полученный
            после выполнения BFS. Ключи - это вершины графа, значения -
            предшественники вершин.
        start (str): Начальная вершина пути.
        end (str): Конечная вершина пути.

    Returns:
        list: Список вершин, представляющий путь от start до end.
              Если путь не существует, возвращает строку "No path".
    """
    # Инициализация текущей вершины как конечной вершины
    vertex = end
    # Инициализация списка для хранения пути
    path = []
    # Цикл для восстановления пути от конечной до начальной вершины
    while vertex != start:
        # Добавление текущей вершины в путь
        path.append(vertex)
        # Переход к предшественнику текущей вершины
        vertex = predecessors[vertex]
        # Проверка наличия пути (если нет предшественника, путь не
        # существует)
        if vertex is None:
            return "No path"
    # Добавление начальной вершины в путь
    path.append(start)
    # Путь получается в обратном порядке, поэтому его нужно
    # инвертировать
    return path[::-1]


def main():
    chess_graph = create_chess_graph()
    print(chess_graph, "\n")
    start = "d4"
    end = "f7"
    predecessors = bfs(chess_graph, start, end)
    path = reconstruct_path(predecessors, start, end)
    print(path)


if __name__ == "__main__":
    main()