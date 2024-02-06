# Сдать решение задачи I-Два коня
#
# На стандартной шахматной доске (8х8) живут 2 шахматных коня:
# Красный и Зеленый. Обычно они беззаботно скачут по просторам доски,
# пощипывая шахматную травку, но сегодня особенный день: у Зеленого
# оня День Рождения. Зеленый конь решил отпраздновать это событие
# вместе с Красным. Но для осуществления этого прекрасного плана им
# нужно оказаться на одной клетке. Заметим, что Красный и Зеленый
# шахматные кони сильно отличаются от черного с белым: они ходят не
# по очереди, а одновременно,и если оказываются на одной клетке, никто
# никого не съедает. Сколько ходов им потребуется, чтобы насладиться
# праздником?
#
# Формат входных данных
# На вход программы поступают координаты коней, записанные по с
# тандартным шахматным правилам (т.е. двумя символами - маленькая
# латинская буква (от a до h) и цифра (от 1 до 8), задающие столбец
# и строку соответственно).
#
# Формат выходных данных
# Требуется вывести наименьшее необходимое количество ходов, либо
# число -1, если кони не могут встретиться.
#
# Примеры
# Ввод
# a1 a3
# Вывод
# 1
# Спорный вопрос, могут ли вообще не встретиться кони. Вопрос только
# в количестве ходов.
from collections import deque


def create_input_data():
    """
    Запрашивает у пользователя ввод данных и возвращает начальное
    и конечное значения.
    """
    start = input()
    end = input()
    print()
    return start, end


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


def bfs_two_knights(graph, start1, start2):
    """
    Выполняет поиск в ширину (BFS) для определения минимального числа
    ходов, необходимых двум коням на шахматной доске, чтобы оказаться
    на одной клетке.

    Args:
    graph: Граф, представляющий шахматную доску, где узлы соответствуют
    клеткам доски, а ребра - возможным ходам коня.
    start1: Начальная позиция первого коня на доске.
    start2: Начальная позиция второго коня на доске.

    Returns:
    int: Минимальное количество ходов, чтобы два коня встретились на
    одной клетке.
    """
    # Инициализация очередей для каждого коня в формате
    # (вершина, расстояние)
    queue1 = deque([(start1, 0)])
    queue2 = deque([(start2, 0)])
    # Посещенные позиции первым конем
    visited1 = {start1}
    visited2 = {start2}
    # Пока в обеих очередях есть элементы
    while queue1 and queue2:
        # Расширяем поиск для первого коня
        # Извлечение вершины и расстояния для 1 коня
        pos1, dist1 = queue1.popleft()
        # Проходимся через все соседние ходы для текущей клетки
        for next_pos in graph[pos1]:
            # Если позиция уже посещена вторым конем
            if next_pos in visited2:
                # Возвращаем количество ходов (+1 для текущего хода)
                return dist1 + 1
            # Если позиция еще не посещена первым конем, добавляем в
            # очередь и список посещенных для 1 коня.
            if next_pos not in visited1:
                visited1.add(next_pos)
                queue1.append((next_pos, dist1 + 1))
        # Расширяем поиск для второго коня
        pos2, dist2 = queue2.popleft()
        for next_pos in graph[pos2]:
            # Если позиция уже посещена первым конем
            if next_pos in visited1:
                # Возвращаем количество ходов (+1 для текущего хода)
                return dist2 + 1
            # Если позиция еще не посещена вторым конем, добавляем в
            # очередь и список посещенных для 2 коня.
            if next_pos not in visited2:
                visited2.add(next_pos)
                queue2.append((next_pos, dist2 + 1))
    return -1  # Кони не могут встретиться


def main():
    chess_graph = create_chess_graph()
    start1 = "a1"
    start2 = "h8"
    print(bfs_two_knights(chess_graph, start1, start2))


if __name__ == "__main__":
    main()
