# Упражнение №6
# Реализовать алгоритм поиска выигрышных и проигрышных позиций в
# аналогичной игре, но ходы делает король (только вправо, вниз и по
# диагонали).
def king_game_strategy(n, m):
    """
    Функция для определения выигрышных и проигрышных позиций в игре
    "Король в угол".
    Доска размером n x m заполняется символами '+' и '-', где '+'
    обозначает выигрышную позицию, а '-' обозначает проигрышную позицию
    для игрока, делающего ход из этой клетки.

    Args:
        n: Высота доски.
        m: Ширина доски.
    Returns:
         Доска с отмеченными выигрышными и проигрышными позициями."""
    # Инициализация доски
    board = [[" "] * m for _ in range(n)]
    # Правый нижний угол отмечается как '-'
    board[n - 1][m - 1] = "-"
    # Заполняем правую крайнюю вертикаль (справа налево).
    print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
    for i in range(n - 1, 0, -1):
        if board[i][m - 1] == "-":
            board[i - 1][m - 1] = "+"
            print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
        else:
            board[i - 1][m - 1] = "-"
            print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
    # Заполняем нижнюю крайнюю горизонталь (слева направо).
    for j in range(m - 1, 0, -1):
        if board[n - 1][j] == "-":
            board[n - 1][j - 1] = "+"
            print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
        else:
            board[n - 1][j - 1] = "-"
            print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
    # Заполняем оставшующюяся часть доски.
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            # Если есть хоть один знак -, куда может ходить король, ставим +.
            if board[i][j + 1] == "-" or board[i + 1][j + 1] == "-" or board[i + 1][j] == "-":
                board[i][j] = "+"
                print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
            # Иначе ставим минус (минус окружен плюсами на клетках, куда может сходить король).
            else:
                board[i][j] = "-"
                print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
    return board


def main():
    print(king_game_strategy(6, 6))


if __name__ == "__main__":
    main()
