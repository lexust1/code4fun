# Сдать решение задачи G-Долой списывание
#
# Во время контрольной работы профессор заметил, что некоторые студенты
# обмениваются записками. Сначала он хотел поставить им всем двойки,
# но в тот день профессор был добрым, а потому решил разделить
# студентов на две группы: списывающих и дающих списывать, и поставить
# двойки только первым. У профессора записаны все пары студентов,
# обменявшихся записками. Требуется определить, сможет ли он разделить
# студентов на две группы так, чтобы любой обмен записками
# осуществлялся от студента одной группы студенту другой группы.
#
# Формат входных данных
# В первой строке входного файла записаны два числа N и M - количество
# студентов и количество пар студентов, обменивающихся записками
# (1≤N≤1000, 0≤M≤20000). Далее в M строках расположены описания пар
# студентов: два числа, соответствующие номерам студентов,
# обменивающихся записками (нумерация студентов идёт с 0). Каждая пара
# студентов перечислена не более одного раза.
#
# Формат выходных данных
# Необходимо вывести ответ на задачу профессора. Если возможно
# разделить студентов на две группы - выведите номера вершин любой из
# этих групп(тех кому профессор поставит двойки =)) в одной строке
# через пробел, иначе выведите NO.
#
# Примеры
# Ввод	Вывод
# 5 2     0 1 3 4
# 2 0
# 2 3
#
#
# Ввод	Вывод
# 7 7     NO
# 1 6
# 0 1
# 1 5
# 5 3
# 4 2
# 6 2
# 6 0
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
    return graph


def dfs(graph, vertex, color, colors):
    """
    Рекурсивный обход в глубину для проверки двудольности графа.

    Args:
    graph (dict): Граф, представленный словарем смежности.
    vertex (str): Текущая вершина для обхода.
    color (int): Цвет текущей вершины (текущего стека).
    colors (dict): Словарь цветов вершин.

    Returns:
    bool: False, если найден цикл одного цвета, иначе True.
    """
    # Присваиваем цвет текущей вершине
    colors[vertex] = color
    # Перебираем соседей вершины
    for neighbour in graph[vertex]:
        # Если сосед еще не окрашен
        if colors[neighbour] == 0:
            # Если соседняя вершина ещё не посещена, то есть не
            # окрашена, то присваиваем ей цвет, противоположный текущей
            # вершине. Используем рекурсивный вызов функции dfs для этой
            # соседней вершины.
            if not dfs(graph, neighbour, -color, colors):
                # Если в процессе обхода была обнаружена проблема с
                # двудольностью (например, соседняя вершина, которая
                # уже окрашена в тот же цвет), то возвращаем False,
                # указывая на то, что граф не двудольный.
                return False
        elif colors[neighbour] == color:
            # Если сосед окрашен в цвет текущей вершины, это ошибка
            return False
    # Если цикл не найден, возвращаем True
    return True


def is_bipartite(graph):
    """
    Проверяет, является ли граф двудольным.

    Args:
    graph (dict): Граф в виде словаря смежности.

    Returns:
    mixed: "NO", если граф не двудольный, или список вершин одной доли.
    """
    # Инициализация цветов всех вершин нулями (не окрашены)
    colors = {vertex: 0 for vertex in graph}
    # Инициализация начального цвета
    color = 1
    # Перебираем все вершины графа
    for vertex in graph:
        # Если вершина не окрашена, начинаем обход с этой вершины
        if colors[vertex] == 0:
            if not dfs(graph, vertex, color, colors):
                # Граф не двудольный
                return "NO"
    # Собираем список вершин первой доли
    return [vertex for vertex, color in colors.items() if color == 1]


def main():
    # graph = create_adj_list()
    # graph = {'0': {'2'}, '1': set(), '2': {'3', '0'}, '3': {'2'}, '4': set()}
    graph = {'0': {'6', '1'}, '1': {'5', '6', '0'}, '2': {'6', '4'}, '3': {'5'}, '4': {'2'}, '5': {'3', '1'}, '6': {'2', '0', '1'}}
    print(graph)
    print(is_bipartite(graph))


if __name__ == "__main__":
    main()
