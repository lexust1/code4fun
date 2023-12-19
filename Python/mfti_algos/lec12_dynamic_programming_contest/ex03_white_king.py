# Сдать решение задачи F-Белый король
#
# На шахматной доске стоят белый король и черный конь. Конь неподвижен,
# король может ходить на одну клетку вправо, на одну клетку вверх или
# наискосок вправо-вверх. Посчитайте, сколькими способами король может
# дойти до клетки h8, начав с клетки a1. Королю нельзя попадать под
# атаку коня. Самого коня есть тоже нельзя.
#
# Строки шахматной доски пронумерованы числами от 1 до 8, столбцы б
# уквами от a до h. Строка 1 - самая нижняя, столбец a - самый левый.
#
# Формат входных данных
# В единственной строке - позиция коня. Позиция - это два символа,
# буква столбца и номер строки, например a3.
#
# Формат выходных данных
# Одно число — результат.
#
# Примеры
# Ввод	Вывод
# 0       1
# c4
#
# Ввод	Вывод
# 4       4
# d8
# c7
# d7
# d6
# e5

def create_input_data():
    print("Input the data")
    inp = input()
    row = int(inp[1])
    d_col = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    col = d_col[inp[0]]
    pos = row, col
    return pos


def create_allowed(pos):
    """
    Generate a 2D grid to represent knight's move on a chess board.

    Args:
        pos (tuple): A pair showing the current position of knight.

    Returns:
        allowed (list of list): A 2D list with possible moves marked
        as 1.
    """
    # Initializing grid with 1
    allowed = [[1] * (8 + 1) for _ in range(8 + 1)]
    # Setting boundary condition for grid
    for k in range(8 + 1):
        allowed[k][0] = 0
        allowed[8][k] = 0
    # Possible moves for knight
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    # Setting current position as non-allowed
    allowed[pos[0]][pos[1]] = 0
    # Marking the cells where knight can move as non-allowed
    for move in moves:
        if 0 < pos[0] + move[0] < (8 + 1) and 0 < pos[1] + move[1] < (8 + 1):
            allowed[pos[0] + move[0]][pos[1] + move[1]] = 0
    return allowed


def calculate_ways(allowed):
    """
    Calculates number of ways given allowed operations.

    Parameters:
    allowed (2D list): A 2D list with allowed operations.

    Returns:
    int: Result at position arr[1][8].
    """
    # Initialize a 2D array with all elements as 0
    arr = [[0] * (8 + 1) for _ in range(8 + 1)]
    arr[7][1] = 1
    for i in range(7, 0, -1):
        for j in range(1, 8 + 1):
            # If operation is allowed
            if allowed[i][j]:
                # Skip the initial position
                if i == 7 and j == 1:
                    continue
                # Update the current cell value
                arr[i][j] = arr[i + 1][j] + arr[i + 1][j - 1] + arr[i][j - 1]
    # Print the 2D array
    for i in range(8 + 1):
        print(f"{arr[i]}\n")
    return arr[1][8]


def visualize_board(allowed):
    print(
        f"{allowed[0]}\n{allowed[1]}\n{allowed[2]}\n{allowed[3]}\n{allowed[4]}"
        f"\n{allowed[5]}\n{allowed[6]}\n{allowed[7]}\n{allowed[8]}\n"
    )


def main():
    # print(create_input_data())
    # print(create_allowed((4, 3)))
    # visualize_board(create_allowed((4, 3)))
    pos = create_input_data()
    print(pos)
    allowed = create_allowed(pos)
    visualize_board(allowed)
    # visualize_board()
    print(calculate_ways(allowed))


if __name__ == "__main__":
    main()
