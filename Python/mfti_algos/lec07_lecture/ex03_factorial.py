# Рекурсия на примере факториала, O(n)
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=2461s
def factorial(n):
    if n == 0:
        # print(1)
        return 1
    fact = n * factorial(n - 1)
    # print(fact)
    return fact


def main():
    n = 5
    print(factorial(n))


if __name__ == "__main__":
    main()
