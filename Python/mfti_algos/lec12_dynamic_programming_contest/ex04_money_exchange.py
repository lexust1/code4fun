# Сдать решение задачи I-Размен денег
#
# Написать функцию make_exchange(money, coins), которая принимает сумму
# денег (целое число) и массив номиналов разменных монет (целых чисел)
# (возможно пустой) и возвращает количество способов произвести размен.
# Считаем, что разменных монет бесконечное множество.
#
# Формат выходных данных
# Число способов произвести размен. Способы 1+2 и 2+1 считаем тождественными.
#
# Примеры
# Ввод	        Вывод
# 4, [1,2]        3
#
# Ввод	        Вывод
# 10, [5,2,3]     4
def make_exchange(money, coins):
    """
    Calculate the number of ways to make change for a given amount
    of money using a set of coins.

    Parameters:
    money: The total amount for which we are making change.
    coins: A list of coin denominations.

    Returns:
    The number of ways to make change for the given amount.
    """
    # Initialize a list to store the number of ways
    # to make change for each amount.
    ways = [0] * (money + 1)
    # Base case: there is 1 way to make change for 0.
    ways[0] = 1
    # Update the ways list for each coin.
    for coin in coins:
        for amount in range(coin, money + 1):
            # For each amount, add the number of ways
            # to make change using the current coin.
            ways[amount] += ways[amount - coin]
    # Return the number of ways to make change for the given amount.
    return ways[money]


def main():
    print(make_exchange(4, [1, 2]))
    print(make_exchange(10, [5, 2, 3]))
    print(make_exchange(6, [1, 2, 3]))


if __name__ == "__main__":
    main()
