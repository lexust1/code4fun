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
    return n, graph


def bfs(n, graph):
    # Словварь расстояний, по умолчанию не известен.
    distances = {str(v): None for v in range(n)}
    # Начинаем с нулевой вершины
    start_vertex = "0"
    # Расстояние до себя же равно 0
    distances[start_vertex] = 0
    # Создаем очередь
    queue = deque([start_vertex])
    # Пока очередь пуста
    while queue:
        # Достаем первывй элемент
        cur_v = queue.popleft()
        # Проходим всех его соседей
        for neigh_v in graph[cur_v]:
            # Если сосед еще не посещен (=> расстояние None)
            if distances[neigh_v] is None:
                # Считаем расстояние
                distances[neigh_v] = distances[cur_v] + 1
                # Добавляем в очередь, чтобы проверить и его соседей
                queue.append(neigh_v)
    return distances


def main():
    # print(create_adj_list())
    n, graph = (
        15,
        {
            '0': {'12', '11', '1', '10'},
            '1': {'7', '0'},
            '2': {'6'},
            '3': {'11'},
            '4': {'10', '6'},
            '5': {'8', '13'},
            '6': {'4', '2', '10'},
            '7': {'13', '1'},
            '8': {'12', '5'},
            '9': {'11'},
            '10': {'4', '0', '6'},
            '11': {'3', '14', '9', '0', '12'},
            '12': {'8', '11', '0'},
            '13': {'5', '7'},
            '14': {'11'}
        }
    )
    print(bfs(n, graph))


if __name__ == "__main__":
    main()
