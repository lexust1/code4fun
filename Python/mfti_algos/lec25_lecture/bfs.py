# O(V+E)
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
    return graph


def bfs(graph, start):
    """
    Выполняет обход графа в ширину (Breadth-First Search, BFS).

    Args:
    graph (dict): Граф, представленный в виде словаря, где ключи -
        это узлы, а значения - списки соседних узлов.
    start: Начальный узел, с которого начинается обход.

    Описание работы:
    Функция использует очередь для обработки узлов графа. Каждый узел
    сначала проверяется на наличие в множестве посещенных узлов. Если
    узел не посещен, он добавляется в множество посещенных и в очередь.
    После этого узел обрабатывается (в данном случае выводится),
    а его соседи проверяются и добавляются в очередь, если они еще не
    посещены. Это продолжается до тех пор, пока очередь не опустеет.
    """
    # Инициализируем множество для отслеживания посещенных узлов
    visited = set()
    # Создаем двустороннюю очередь (deque) и помещаем в нее начальный
    # узел.
    queue = deque([start])
    # Добавляем начальный узел в множество посещенных.
    visited.add(start)
    # Продолжаем выполнять цикл, пока очередь не пуста
    while queue:
        # Извлекаем узел из начала очереди.
        vertex = queue.popleft()
        # Выводим узел, на каждом шаге. Но оформляем все в одну строку.
        print(str(vertex), end=" ")
        # Перебираем всех соседей текущего узла.
        for neighbour in graph[vertex]:
            # Если сосед еще не был посещен, добавляем его в множество
            # посещенных и в очередь.
            if neighbour not in visited:
                # Помечаем соседа как посещенный.
                visited.add(neighbour)
                # Добавляем соседа в очередь для дальнейшего обхода.
                queue.append(neighbour)
    # С целью форматирования
    print()


def main():
    # print(create_adj_list())
    graph = {
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

    bfs(graph, "0")


if __name__ == "__main__":
    main()
