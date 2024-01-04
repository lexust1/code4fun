# Конечно, расскажу о различных видах задач о рюкзаке:
#
# 1. **0/1 Задача Рюкзака**: Это самый известный вариант. Представьте,
# что у вас есть рюкзак, который может вместить определенный вес, и
# набор предметов, каждый из которых имеет свой вес и ценность. Задача
# состоит в том, чтобы выбрать набор предметов так, чтобы их общая
# ценность была максимальной, но при этом суммарный вес не превышал
# вместимость рюкзака. Вы можете взять предмет целиком или вообще не
# брать.
#
# 2. **Задача Рюкзака с Частичным Включением**: Отличается от 0/1
# задачи тем, что вы можете взять часть предмета, а не только целиком.
# Например, если у вас есть золотой слиток, вы можете взять только
# часть этого слитка.
#
# 3. **Многомерная Задача Рюкзака**: В этой версии задачи у вас есть
# несколько ограничений (не только вес). Например, у вас может быть
# ограничение по весу и объему одновременно. Вы должны выбрать предметы
# так, чтобы удовлетворить все ограничения.
#
# 4. **Задача Рюкзака с Множественными Рюкзаками**: Здесь у вас не
# один, а несколько рюкзаков, каждый с разными ограничениями по
# вместимости. Задача — распределить предметы между рюкзаками так,
# чтобы максимизировать общую ценность.
#
# 5. **Динамическая Задача Рюкзака**: В этой версии задачи предметы
# могут появляться и исчезать со временем, и вам нужно решать, когда и
# какие предметы взять, чтобы максимизировать общую ценность.
#
# Эти задачи часто встречаются в областях оптимизации ресурсов,
# финансового планирования и логистики. Они также являются
# классическими примерами проблем, решаемых методами дискретной
# оптимизации и динамического программирования.

# Асимптотическая сложность алгоритмов для разных видов задач о рюкзаке
# зависит от методов решения и специфики задачи:
#
# 0/1 Задача Рюкзака: Классический метод решения - динамическое
# программирование. Асимптотическая сложность составляет O(nW),
# где n - количество предметов, а W - вместимость рюкзака. Это означает,
# что время выполнения зависит от количества предметов и вместимости
# рюкзака.
#
# Задача Рюкзака с Частичным Включением: Обычно решается методом
# жадного алгоритма, который имеет асимптотическую сложность O(n log n)
# из-за необходимости сортировки предметов. Однако, следует учесть, что
# этот алгоритм не всегда дает оптимальное решение.
#
# Многомерная Задача Рюкзака: Сложность зависит от количества измерений
# (ограничений). Если использовать динамическое программирование,
# сложность будет O(nW1W2...Wk), где W1, W2, ..., Wk - ограничения по
# различным измерениям (например, вес, объем). Это делает задачу
# значительно сложнее с увеличением числа измерений.
#
# Задача Рюкзака с Множественными Рюкзаками: Если применять
# динамическое программирование, сложность будет O(nW1W2...Wm),
# где W1, W2, ..., Wm - вместимость каждого рюкзака. Эта задача может
# быстро стать вычислительно сложной при увеличении числа рюкзаков.
#
# Динамическая Задача Рюкзака: Сложность варьируется в зависимости от
# того, как часто меняются доступные предметы и ограничения. Она может
# варьироваться от O(nW), как в классической задаче, до более сложных
# вариантов, если учитывать динамические изменения.
# Динамическое программирование в данном случае позволяет уйти от
# O(2^n) - полный перебор к O(n * m)
def backpack(n, max_weight, weights, values):
    """
    Calculate the maximum value that can be achieved with a given
    weight limit and items with individual weights and values.

    Args:
        max_weight (int): The maximum weight the backpack can hold.
        weights (list): The weights of the items.
        values (list): The values of the items.

    Returns:
        int: The maximum value that can be achieved.
    """
    n = len(values)
    # Initialize a DP table
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] <= j:
                # Item can be included in the optimal subset
                dp[i][j] = max(
                    dp[i - 1][j],  # Item is not included
                    values[i - 1] + dp[i - 1][j - weights[i - 1]]
                    # Item is included
                )
            else:
                # Item can't be included in the optimal subset
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]  # Return the maximum value that can be achieved


def main():
    n = 13
    max_weight = 13
    weights = [3, 4, 5, 8, 9]
    values = [1, 6, 4, 7, 6]
    print(backpack(n, max_weight, weights, values))


if __name__ == "__main__":
    main()
