# Быстрое возведение в степень при помощи рекурсии, O(log(n))
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=3929s
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        res = power(base, exponent // 2)
        print(res * res)
        return res * res
    else:
        res = power(base, (exponent - 1) // 2)
        print(base * res * res)
        return base * res * res


def main():
    base = 3
    exponent = 3
    print(power(base, exponent))


if __name__ == "__main__":
    main()
