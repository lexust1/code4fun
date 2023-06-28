# Рекурсия на пример НОД (наибольший общий делитель), алгоритм Евклида,
# O(log(min(a,b))
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=3546s
def gcd(a, b):
    if b == 0:
        return a
    else:
        print(f"a = {a} , b = {b}, a % b = {a % b}")
        return gcd(b, a % b)


def main():
    a = 6
    b = 8
    print(gcd(a, b))


if __name__ == "__main__":
    main()
