# Сдать решение задачи J-Задача о рюкзаке
#
# Дано N предметов. Каждый из них имеет вес w i и стоимость p i .
# Также имеется рюкзак вместимостью W. От вас требуется найти такой
# набор предметов, что их суммарная стоимость максимальна, а суммарный
# вес не превосходит вместимость рюкзака. Ответом на задау надо будет
# вывести стоимость такого набора.
#
# Формат входных данных
# На первых двух строках даны натуральные числа N и W, не
# превосходящие 100. На следующих 2*M строках даны пары чисел
# натуральных w i ≤ 100 и p i ≤ 1000.
#
# Формат выходных данных
# Одно число - стоимость набора.
#
# Примеры
# Ввод	Вывод
# 5       13
# 13
# 3
# 1
# 4
# 6
# 5
# 4
# 8
# 7
# 9
# 6
#
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
