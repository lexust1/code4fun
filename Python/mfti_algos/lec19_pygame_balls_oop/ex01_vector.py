# Упражнение №1
# Создайте класс Vector с полями x и y, определите для него конструктор,
# метод __str__, необходимые арифметические операции:
#
# сложение (__add__)
# вычитание (__sub__)
# умножение на число справа (__mul__) и слева (__rmul__)
# отрицание (унарный минус __neg__)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector: {self.x}, {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(number * self.x, number * self.y)

    def __rmul__(self, number):
        return self.__mul__(number)

    def __neg__(self):
        return Vector(- self.x, - self.y)


def main():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(v3)
    v4 = v2 - v1
    print(v4)
    v5 = 3 * v1
    print(v5)
    v6 = v1 * 3
    print(v6)
    v7 = - v1
    print(v7)


if __name__ == "__main__":
    main()

