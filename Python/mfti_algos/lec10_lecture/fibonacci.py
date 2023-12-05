import time


def fib_1(n):
    """The worst way."""
    # The base case.
    if n <= 1:
        return n
    # The recursive case.
    fib = fib_1(n - 1) + fib_1(n - 2)
    return fib


def fib_2(n):
    """From the lecture."""
    fib = [0, 1] + [0] * (n - 1)
    for idx in range(2, n + 1):
        fib[idx] = fib[idx - 1] + fib[idx - 2]
    return fib[-1]


def fib_3(n):
    """Used in the exercise about Tribonacci."""
    fib = [0, 1]
    for _ in range(2, n + 1):
        fib.append(sum(fib[-2:]))
    return fib[-1]


def main():
    n = 40
    # fib_1
    start_time = time.time()
    fib1 = fib_1(n)
    end_time = time.time()
    print(fib1, round(end_time - start_time, 6))
    # fib_2
    start_time = time.time()
    fib2 = fib_2(n)
    end_time = time.time()
    print(fib2, round(end_time - start_time, 6))
    # fib_3
    start_time = time.time()
    fib3 = fib_3(n)
    end_time = time.time()
    print(fib3, round(end_time - start_time, 6))


if __name__ == "__main__":
    main()
