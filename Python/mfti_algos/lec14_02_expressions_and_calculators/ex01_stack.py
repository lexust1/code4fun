# Упражнение №1
# Напишите программу, которая последовательно кладет в стек
# произвольный массив чисел, а затем распечатывает их , последовательно
# доставая, пока стек не пуст (например, набор (1,...,10)).

def work_with_stack(arr):
    _stack = []
    [_stack.append(el) for el in arr]
    while len(_stack) > 0:
        print(_stack.pop())


def main():
    work_with_stack([1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
