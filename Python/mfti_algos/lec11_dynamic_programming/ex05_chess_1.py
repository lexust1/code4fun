# Игра с ферзём
#
# Рассмотрим игру «Ферзя в угол» для двух игроков.
# В левом верхнем углу доски размером N*M находится ферзь, который
# может двигаться только вправо-вниз. Игроки по очереди двигают ферзя,
# то есть за один ход игрок может переместить ферзя либо по вертикали
# вниз, либо по горизонтали вправо, либо во диагонали вправо-вниз.
# Выигрывает игрок, который поставит ферзя в правый нижний угол.
# еобходимо определить, какой из игроков может выиграть в этой игре
# независимо от ходов другого игрока (имеет выигрышную стратегию).
#
# Будем заполнять доску знаками «+» и «-». Знак «+» будет означать,
# что данная клетка является выигрышной для ходящего с неё игрока
# (то есть если ферзь стоит в этой клетке, то игрок, который делает
# ход, может всегда выиграть), а знак «-» означает, что он проигрывает.
# Клетки последней строки, последнего столбца и диагонали, ведущей из
# правого нижнего угла необходимо отметить, как «+», так как если ферзь
# стоит в этой клетке, то ходящий игрок может выиграть одним ходом.
#
# Но в правом нижнем углу необходимо поставить знак «-» — если ферзь
# стоит в углу, то тот игрок, которых должен делать ход, уже проиграл.
#
#
# Теперь рассмотрим две клетки, из которых можно пойти только в те
# клетки, в которых записан знак «+». В этих клетках нужно записать
# знак «-» — если ферзь стоит в этих клетках, то какой бы ход не сделал
# ходящий игрок, ферзь окажется в клетке, в которой стоит знак «+», то
# есть выигрывает ходящий игрок. Значит, тот, кто сейчас ходит — всегда
# проигрывает.
#
#
# Но теперь в те клетки, из которых можно попасть в клетку, в которой
# стоит знак «-» за один ход, необходимо записать знак «+» — если ферзь
# стоит в этой клетке, то игрок, который делает ход, может выиграть,
# если передвинет ферзя в клетку, в которой стоит знак «-»:
#
#
# Дальше таблица заполняется аналогично. В клетке ставиться знак «+»,
# если есть ход, который ведет в клетку, в которой стоит знак «--». В
# клетке ставится знак «-», если все ходы из этой клетки ведут в клетки,
# в которых записан знак «+».
#
# Продолжая таким образом, можно определить выигрывающего игрока для
# любой начальной клетки.
#
# Упражнение №5
# Реализовать алгоритм поиска выигрышных и проигрышных позиций в игре с
# ферзём на прямоугольном поле M на N, где N — высота, а M — ширина
# поля.
def queen_game_strategy(n, m):
    """
    Функция для определения выигрышных и проигрышных позиций в игре
    "Ферзь в угол".
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
    # Отмечаем последний ряд и последний столбец как '+'
    for j in range(m):
        board[n - 1][j] = "+"
    for i in range(n):
        board[i][m - 1] = "+"
    # Отмечаем диагональ как '+'
    for d in range(min(m, n)):
        board[d][d] = "+"
    # Правый нижний угол отмечается как '-'
    board[n - 1][m - 1] = "-"
    print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
    # Заполнение оставшейся части доски (идем из правого нижнего угла)
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if board[i][j] != " ":
                continue
            # Если все соседние клетки (вправо, вниз, по диагонали) отмечены как '+', клетка отмечается как '-'
            elif board[i + 1][j + 1] == "+" and board[i][j + 1] == "+" and board[i + 1][j] == "+":
                board[i][j] = "-"
                print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                # Определеям какая из сторон у "поддоски" больше, чтобы совместить заполнение одной из сторон
                # c диагональю.
                if i < j:
                    # Используем для подсчета более длинной стороны.
                    len_d = 0
                    # Заполням все, что левее минуса плюсами
                    for d in range(j - 1, -1, -1):
                        board[i][d] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                    # Заполняем все, что по диагонали слева и выше минуса плюсами.
                    for d in range(i - 1, -1, -1):
                        board[d][j] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                        len_d += 1
                        board[d][j - len_d] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                else:
                    len_d = 0
                    # Заполняем все, что по диагонали слева и выше минуса плюсами.
                    for d in range(j - 1, -1, -1):
                        board[i][d] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                        len_d += 1
                        board[i - len_d][d] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
                    # Заполняем все, что левее минуса плюсами
                    for d in range(i - 1, -1, -1):
                        board[d][j] = "+"
                        print(f"{board[0]}\n{board[1]}\n{board[2]}\n{board[3]}\n{board[4]}\n{board[5]}\n")
            else:
                print("Something strange.")
    return board


def main():
    print(queen_game_strategy(6, 6))


if __name__ == "__main__":
    main()