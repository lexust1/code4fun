import copy
import random
import sys
import time

import matplotlib.pyplot as plt


def is_sorted(a):
    n = len(a)
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False

    return True


def average_execution_time(f, *args):
    t = 0
    N = 5
    for i in range(N):
        _args = copy.deepcopy(args)
        t -= time.time()
        f(*_args)
        t += time.time()

    return t / N


def plot_fib_results(*args):
    n = range(1, 15)
    for i, (name, impl) in enumerate(args):
        t = [average_execution_time(impl, _n) for _n in n]
        plt.plot(n, t, label=name)

    plt.title('Вычисление чисел Фибоначчи')
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('Время выполнения, с')
    plt.tight_layout()
    plt.show()


def shuffle(x):
    z = list(x)
    random.shuffle(z)
    return z


_length = [100, 500, 1000, 2000, 5000]
_reversed = (
    'отсортированный в обратном порядке',
    lambda x: list(reversed(x)),
    None
)
_partially_reversed = (
    'частично отсортированный',
    lambda x: list(x[:len(x) // 2]) + list(x[:len(x) // 2 - 1:-1]),
    None
)
_sorted = (
    'отсортированный',
    list,
    3
)
_shuffled = (
    'неотсортированный',
    shuffle,
    None
)


def sort_results(sort_name, cases):
    def f(*args):
        for case, change, cut in cases:
            for i, (name, impl) in enumerate(args):
                t = []
                for _l in _length[:cut]:
                    t.append(average_execution_time(impl, change(range(_l))))
                plt.plot(_length[:cut], t, label=name)

            plt.title('{} ({} массив)'.format(sort_name, case))
            plt.legend()
            plt.xlabel('n')
            plt.ylabel('Время выполнения, с')

            plt.tight_layout()
            plt.show()

    return f


plot_bubble_sort_results = sort_results('Сортировка пузырьком', [
    _reversed,
    _partially_reversed,
    _sorted,
])

plot_quick_sort_results = sort_results('Быстрая сортировка', [
    _partially_reversed,
    _reversed,
    _shuffled,
    _sorted
])

plot_merge_sort_results = sort_results('Сортировка слиянием', [
    _shuffled,
    _sorted,
    _reversed
])

plot_sort_results = sort_results('Различные сортировки', [
    _sorted,
    _shuffled,
])


def plot_search_results(length):
    def f(*args):

        for m, r, case in [(2, 1, 'Произвольный массив'), (1, 0, '«Хороший» массив')]:
            data = {}

            for _l in length:
                data[_l] = list(range(_l * m))
                for i in range(_l * r):
                    data[_l].pop(random.randrange(m * _l - i))

            for i, (name, impl) in enumerate(args):
                t = [average_execution_time(impl, data[_l], data[_l][-20]) for _l in length]
                plt.plot(length, t, label=name)

            plt.title(case)
            plt.legend()
            plt.xlabel('n')
            plt.ylabel('Время выполнения, с')

            plt.tight_layout()
            plt.show()

    return f


plot_search_results_small = plot_search_results([1000, 2000, 5000, 10000, 15000, 20000])
plot_search_results_huge = plot_search_results([5000, 10000, 15000, 20000, 35000, 40000])

sys.setrecursionlimit(20000)
