# Сдать решение задачи G-Числа
#
# Витя хочет придумать новую игру с числами. В этой игре от игроков
# требуется преобразовывать четырехзначные числа не содержащие нулей
# при помощи следующего разрешенного набора действий:
#
# Можно увеличить первую цифру числа на 1, если она не равна 9.
# Можно уменьшить последнюю цифру на 1, если она не равна 1.
# Можно циклически сдвинуть все цифры на одну вправо.
# Можно циклически сдвинуть все цифры на одну влево.
# Например, применяя эти правила к числу 1234 можно получить числа
# 2234, 1233, 4123 и 2341 соответственно. Точные правила игры Витя
# пока не придумал, но пока его интересует вопрос, как получить из
# одного числа другое за минимальное количество операций.
#
# Формат входных данных
# Во входном файле содержится два различных четырехзначных числа,
# каждое из которых не содержит нулей.
#
# Формат выходных данных
# Программа должна вывести последовательность четырехзначных чисел,
# не содержащих нулей. Последовательность должна начинаться первым из
# данных чисел и заканчиваться вторым из данных чисел, каждое
# последующее число в последовательности должно быть получено из
# предыдущего числа применением одного из правил. Количество чисел
# в последовательности должно быть минимально возможным.
#
# Примеры
# Ввод
# 1234
# 4321
# Вывод
# 1234
# 2234
# 3234
# 4323
# 4322
# 4321
from collections import deque


def create_neighbours(number):
    """
    Создает множество соседних чисел для заданного четырехзначного
    числа.

    Соседи числа генерируются с использованием следующих правил:
    - Увеличение первой цифры на 1, если она не равна 9.
    - Уменьшение последней цифры на 1, если она не равна 1.
    - Циклический сдвиг всех цифр на одну позицию вправо.
    - Циклический сдвиг всех цифр на одну позицию влево.

    Args:
        number (str): Четырехзначное число в виде строки.

    Returns:
        set: Множество четырехзначных чисел (в виде строк), которые
        могут быть получены из исходного числа с помощью разрешенных
        операций.
    """
    neighbours = set()
    # Увеличить первую цифру числа на 1, если она не равна 9
    if number[0] != "9":
        neighbours.add(str(int(number[0]) + 1) + number[1:])
    # Уменьшить последнюю цифру числа на 1, если она не равна 1
    if number[-1] != "1":
        neighbours.add(number[:-1] + str(int(number[-1]) - 1))
    # Циклически сдвинуть все цифры на одну позицию вправо
    neighbours.add(number[-1] + number[:-1])
    # Циклически сдвинуть все цифры на одну позицию влево
    neighbours.add(number[1:] + number[0])
    return neighbours


def renew_graph(graph, vertex, neighbours):
    """
    Обновляет граф, добавляя соседей для заданной вершины.

    Функция обновляет граф путем добавления соседних вершин для
    указанной вершины.
    Если вершина еще не присутствует в графе, она добавляется с ее
    соседями.
    Если вершина уже существует в графе, ее список соседей обновляется
    путем добавления новых соседей.

    Args:
        graph (dict): Граф, представленный словарем, где ключи - это
        вершины, а значения - множества их соседей.
        vertex (str): Вершина, для которой необходимо добавить соседей.
        neighbours (set): Множество соседей, которые нужно добавить к
        данной вершине.

    Returns:
        dict: Обновленный граф с добавленными соседями для указанной
        вершины.
    """
    # Проверяем, существует ли вершина в графе
    if vertex not in graph:
        # Если вершина отсутствует, добавляем ее и назначаем ее соседей
        graph[vertex] = neighbours
    else:
        # Если вершина уже существует, обновляем ее соседей
        graph[vertex].update(neighbours)
    # for neighbour in neighbours:
    #     if neighbour not in graph:
    #         graph[neighbour] = {vertex}
    #     else:
    #         graph[neighbour].update(vertex)
    # Возвращаем обновленный граф
    return graph


def bfs(start, end):
    """
    Выполняет поиск кратчайшего пути от начальной вершины до конечной в
    графе с использованием обхода в ширину (BFS).

    Функция строит граф на лету, начиная с начальной вершины и добавляя
    соседние вершины по мере обхода.
    Для каждой вершины сохраняется ее предшественник, что позволяет
    восстановить путь после достижения конечной вершины.
    Обход продолжается до тех пор, пока не будет найдена конечная
    вершина или пока не будут исследованы все доступные вершины.

    Args:
        start (str): Начальная вершина пути, представленная
            четырехзначным числом в виде строки.
        end (str): Конечная вершина пути, представленная четырехзначным
            числом в виде строки.

    Returns:
        dict: Словарь предшественников, позволяющий восстановить
        кратчайший путь от начальной до конечной вершины. Ключи словаря
        - вершины, значения - предшественники каждой вершины в пути.
    """
    # Инициализируем начальных соседей и создаем часть графа из
    # начальной вершины и ее соседей
    graph = {}
    neighbours = create_neighbours(start)
    graph = renew_graph(graph, start, neighbours)
    # Инициализируем множество для отслеживания посещенных узлов
    visited = set()
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Добавляем начальный узел в множество посещенных.
    visited.add(start)
    # Создаем словарь предшественников
    predecessors = {}
    # Продолжаем выполнять цикл, пока очередь не пуста
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Проверяем, достигли ли искомой вершины, чтобы не ходить через
        # оставшийся граф. Своеобразная оптимизация.
        if vertex == end:
            return predecessors
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Если сосед еще не был посещен, добавляем его в множество
            # посещенных и в очередь.
            if neighbour not in visited:
                # Помечаем соседа как посещенный.
                visited.add(neighbour)
                # Добавляем соседа в очередь для дальнейшего обхода.
                queue.append(neighbour)
                # Сохраняем предшественника для соседа
                predecessors[neighbour] = vertex
                # Создаем новых соседей для соседа (следующий слой)
                neighbours = create_neighbours(neighbour)
                # Обновляем граф, добавляя новых соседей для соседа
                # (следующий слой)
                graph = renew_graph(graph, neighbour, neighbours)
    return predecessors


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


def format_output(path):
    for vertex in path:
        print(vertex)


def main():
    initial_number = "1234"
    final_number = "4321"
    # neighbours = create_neighbours(initial_number)
    # print(neighbours)
    # graph = {}
    # graph[initial_number] = neighbours
    # print(graph)
    predecessors = bfs(initial_number, final_number)
    print(predecessors)
    path = reconstruct_path(predecessors, initial_number, final_number)
    print(path)
    format_output(path)


if __name__ == "__main__":
    main()
