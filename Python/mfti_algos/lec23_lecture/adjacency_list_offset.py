def create_edges_and_offset(adj_list):
    """
    Преобразует список смежности графа в список ребер и список офсетов.

    Args:
    adj_list (dict): Список смежности графа, где ключи - это вершины,
                     а значения - списки смежных вершин.

    Returns:
    tuple: Возвращает кортеж, содержащий два элемента:
           - список ребер (edges, list): Список ребер графа, где каждое
            ребро представлено парой вершин.
           - список офсетов (offset, list): Список офсетов для каждой
           вершины, показывающий начало и конец ребер в списке edges.
    """
    edges = []  # Инициализация списка ребер
    offset = [0]  # Начальный офсет устанавливается в 0
    # Перебор всех вершин и их соседей
    for node in sorted(adj_list.keys()):
        for neighbor in sorted(adj_list[node]):
            # Добавляем ребро, если оно еще не добавлено (избегаем дублирования)
            if node < neighbor:
                edges.append(node)
                edges.append(neighbor)
        # Обновляем офсет после добавления ребер текущей вершины
        offset.append(len(edges))
    return edges, offset

def convert_to_adj_list(edges, offset):
    """
    Преобразует список ребер и соответствующий список офсетов обратно
    в список смежности.

    Args:
    edges (list): Список ребер графа, где каждое ребро представлено парой вершин.
    offset (list): Список офсетов, показывающий начало и конец ребер
    для каждой вершины в списке edges.

    Returns:
    dict: Список смежности графа.
    """
    adj_list = {}  # Инициализация списка смежности
    # Перебор офсетов для каждой вершины
    for i in range(len(offset) - 1):
        adj_list[i] = []  # Инициализация списка смежности для вершины i
        # Перебор ребер, соответствующих вершине i
        for j in range(offset[i], offset[i + 1]):
            # Добавляем соседнюю вершину, если она не равна текущей
            if edges[j] != i:
                adj_list[i].append(edges[j])
    return adj_list


def main():
    # Начальный список смежности
    adj_list = {
        0: [1],
        1: [0, 2, 3],
        2: [1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    edges, offset = create_edges_and_offset(adj_list)
    print("Edges:", edges)
    print("Offset:", offset)

    # Ваши данные
    edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
    offset = [0, 1, 4, 6, 9, 10]

    # Преобразование в список смежности
    adj_list = convert_to_adj_list(edges, offset)
    print("Список смежности:", adj_list)


if __name__ == "__main__":
    main()
