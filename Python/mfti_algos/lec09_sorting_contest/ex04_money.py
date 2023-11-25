# Сдать решение задачи D-Сколько надо денег?
#
# Деньги-1
# Студент покупает рис каждый день.
# В первую неделю рис стоит price монет.
# Каждый день (перед началом рабочего дня) цена риса увеличивается на
# delta монет (price = price + delta).
# Неделя - 7 дней.
# Студент покупал рис m недель.
#
# Написать программу (с циклом while), которая вычисляет сколько денег
# потратил студент.
#
# Нужны переменные:
#
# day - чтобы считать дни.
# Сначала day = 1.
# Если day == 8, то это первый день новой недели day = 1
# week - чтобы считать недели. Сначала week = 1.
# Если day == 8, то началась новая неделя week = week + 1
# Входные данные
#
# price - цена риса
#
# delta - на сколько увеличивается цена
#
# m - количество недель
#
# Выходные данные
#
# Число money - сколько денег потратил студент.
#
# Примеры
#
# Вход        Выход
#
# 10 1 1      91

def create_input_data() -> list:
    """
   Creates input data.

    Returns:
        arr: A list containing the price, weekly price change, and
            number of weeks.
    """
    print("Input the price, weekly price change, and a num of weeks: ")
    inp = input().split()
    arr = [int(el) for el in inp]
    return arr


def count_money(arr: list) -> int:
    """
    Calculates the total amount of money earned over a certain number
    of days.

    Parameters:
    - arr (list): A list containing three elements: the initial price
        per day (price), the increase in price per day (delta), and the
        number of weeks to calculate (weeks).

    Returns:
    - int: The total amount of money earned over the specified number
        of weeks.
    """
    price = arr[0]
    delta = arr[1]
    days = arr[2] * 7
    cnt = 0
    money = 0
    while days > 0:
        money += price + cnt * delta
        cnt += 1
        days -= 1
    return int(money)


def count_money_pw(arr: list) -> int:
    """
    An alternative "fast" way.
    """
    price = arr[0]
    delta = arr[1]
    days = arr[2] * 7
    money = (2 * price + (days - 1) * delta) * days / 2
    return int(money)


def main():
    """
    The entry point.
    """
    arr = create_input_data()
    print(count_money(arr))


if __name__ == "__main__":
    main()
