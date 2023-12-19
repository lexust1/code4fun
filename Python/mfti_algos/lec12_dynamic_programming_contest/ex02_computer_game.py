# Сдать решение задачи D-Компьютерная игра
#
# Герою компьютерной игры нужно перебраться от одного края экрана к
# другому, перепрыгивая по платформам. При этом при прыжке с одной
# платформы на соседнюю, у героя уходит |y2-y1| единиц энергии, где y1 и
# y2 – высоты, на которых расположены эти платформы. Кроме того, у
# героя есть суперприем, который позволяет перескочить через платформу,
# но на это затрачивается 3*|y3-y1| единиц энергии. Конечно же, энергию
# следует расходовать максимально экономно.
#
# Вам известны высоты всех платформ в порядке от левого края до
# правого. Необходимо найти, какое минимальное количество энергии
# потребуется герою, чтобы добраться с первой платформы до последней.
#
# Формат входных данных
# В первой строке - количество платформ (0 < n <= 30000). Далее на
# каждой из n строк записана высота , на которой расположена очередная
# платформа.
#
# Формат выходных данных
# Одно число — минимальное количество энергии, которую должен потратить
# герой на преодоление платформ.
#
# Примеры
# Ввод	Вывод
# 3       9
# 1
# 5
# 10
#
#
# Ввод	Вывод
# 1       0
# 1
#
#
# Ввод	Вывод
# 2       6
# 20
# 14
#
def create_input_data():
    y = []
    print("Input the data: ")
    while True:
        inp = input()
        if inp == " ":
            break
        y.append(int(inp))
    return y


def calculate_min_cost(y):
    """
    Calculate the minimum cost to reach the last element in the list 'y'.

    Args:
        y (list): A list of integers representing the elements.

    Returns:
        int: The minimum cost to reach the last element.
    """
    # Get the first element which represents the size of the list.
    n = y[0]
    # If the size is 1, then no cost is required.
    if n == 1:
        return 0
    # Initialize the cost list with initial values.
    cost = [float("inf"), 0, abs(y[2] - y[1])] + [0] * (n - 2)
    # Calculate the minimum cost iteratively.
    for i in range(3, n + 1):
        # Check if the cost of jumping from the position two places
        # before is less than the cost of jumping from the position
        # just before.
        if 3 * abs(y[i - 2] - y[i]) > abs(y[i - 1] - y[i]):
            # If so, update the cost for position 'i' as the cost at the
            # position one place before plus the absolute difference
            # between the values at positions 'i' and 'i - 1'.
            cost[i] = cost[i - 1] + abs(y[i - 1] - y[i])
        else:
            # Otherwise, update the cost for position 'i' as the cost
            # at the position two places before plus three times the
            # absolute difference between the values at positions 'i'
            # and 'i - 2'.
            cost[i] = cost[i - 2] + 3 * abs(y[i - 2] - y[i])
    return cost[-1]


def main():
    print(calculate_min_cost(create_input_data()))


if __name__ == "__main__":
    main()
