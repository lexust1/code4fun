# Задача о кузнечике — количество способов
# Рассмотрим следующую задачу. На числовой прямой сидит кузнечик,
# который может прыгать вправо на одну или на две единицы.
# Первоначально кузнечик находится в точке с координатой 1. Определите
# количество различных маршрутов кузнечика, приводящих его в точку с
# координатой n.
#
# Обозначим количество маршрутов кузнечика, ведущих в точку с
# координатой n, как K[n]. Прежде всего заметим, что существует ровно
# один маршрут из точки 1 в точку 1 — он не содержит ни одного прыжка.
# В точку 2 можно прыгнуть единственным способом — из точки 1.
#
# Как вычислить K[n]? В точку кузнечик может попасть двумя способами —
# из точки при помощи прыжка длиной 2 и из точки прыжком длины 1.
# То есть число способов попасть в точку n равно сумме числа способов
# попасть в точку (n-1) и (n-2), что позволяет выписать рекуррентное
# оотношение: K[n] = K[n-1] + K[n-2].
#
# Можно заметить, что данная задача по сути свелась к числам Фибоначчи,
# поэтому мы не будем выписывать её решение.

# Упражнение №1
# Решите задачу о количестве способов достичь точки n из точки 1,
# если кузнечик умеет прыгать +1, +2 и +3.
def traj_num(N):
    """Кол-во траекторий, если кузнечик прыгает на +1, +2 или +3."""
    # Кузнечик может прыгать на 1, 2 или 3 единицы вправо.
    # Необходимо определить количество различных маршрутов, чтобы
    # добраться до точки n.
    #
    # Для этого используем динамическое программирование:
    # f(n) - количество маршрутов для достижения точки n.
    #
    # Кузнечик может попасть в точку n двумя способами:
    # 1. Прыжок из точки n-1 (на одну единицу).
    # 2. Прыжок из точки n-2 (на две единицы).
    # 3. Прыжок из точки n-3 (на три единицы).
    #
    # Таким образом, f(n) = f(n-1) + f(n-2) + f(n-3)
    # (сводится к поиску числа "трибоначчи").
    # Это означает, что количество маршрутов в точку n равно сумме
    # маршрутов в точки n-1, n-2 и n-3.
    # Используя эти начальные условия и рекурсивное соотношение,
    # мы можем вычислить f(n) для любого n.
    K = [0, 1, 1] + [0] * (N - 2)
    for i in range(3, N + 1):
        K[i] = K[i - 3] + K[i - 2] + K[i - 1]
    return K[N]


def main():
    N = 5
    print(traj_num(N))


if __name__ == "__main__":
    main()
