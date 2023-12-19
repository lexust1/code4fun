# Сдать решение задачи A-Два хода конем
#
# Вам даны 2 координаты 2 клеток на шахматном поле.
# Нужно ответить на вопрос, можно ли попасть из одной клетки в другую
# за не более чем 2 хода конем. В случае, если попасть возможно, надо
# вывести количество ходов, за которое это можно сделать. Если попасть
# невозможно, следует вернуть -1.
#
# Формат входных данных
# На вход подаются числа от 1 до 8 в 4 строках. Первые 2 строки задают
# координаты начальной клетки, вторые 2 -- координаты конечной клетки.
#
# Формат выходных данных
# Одно число — количество ходов, за которые можно попасть из из одной
# клетки во вторую. Если невозможно -- вывести -1.
#
# Примеры
# Ввод	Вывод
# 1       1
# 1
# 2
# 3
#
#
# Ввод	Вывод
# 1       -1
# 1
# 8
# 8
#
def create_input():
    arr = []
    print("Input the data: ")
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(int(inp))
    return arr


def check_cell(arr):
    """
    Check if a cell is reachable.

    Args:
        arr (list): List of four integers representing the coordinates
        of the starting cell (x0, y0) and the target cell (x, y).

    Returns:
        int: 0 if the target cell is the same as the starting cell,
             1 if the target cell is reachable in one move,
             2 if the target cell is reachable in two moves,
            -1 if the target cell is not reachable.
    """
    # Define the possible knight moves
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    # Extract the coordinates from the input list
    x0, y0 = arr[0], arr[1]
    x, y = arr[2], arr[3]
    # Check if the target cell is the same as the starting cell
    if x0 == x and y0 == y:
        return 0
    # Check if the target cell is reachable in one knight move
    elif abs(x - x0) * abs(y - y0) == 2:
        return 1
    # Check if the target cell is reachable in two moves
    else:
        for dx, dy in moves:
            x_med, y_med = x0 + dx, y0 + dy
            if abs(x - x_med) * abs(y - y_med) == 2:
                return 2
    # If none of the conditions above are met, the target cell is
    # not reachable
    return -1


def main():
    # 1 1 1 1 => 0
    # 1 1 2 3 => 1
    # 1 1 4 4 => 2
    # 1 1 8 8 => -1
    print(check_cell(create_input()))


if __name__ == "__main__":
    main()
