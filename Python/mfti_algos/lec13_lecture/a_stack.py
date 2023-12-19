# Простая реализация стека через список.
_stack = []

def push(x):
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


# if __name__ == "__main__":
