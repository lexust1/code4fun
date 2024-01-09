# Упражнение №2
# Используя класс Vector выведите координаты центра масс данного
# множества точек.
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

    @staticmethod
    def sum_vectors(vectors):
        total_x, total_y = 0, 0
        for vector in vectors:
            total_x += vector.x
            total_y += vector.y
        return Vector(total_x / len(vectors), total_y / len(vectors))


def main():
    points = [
        Vector(1, 2),
        Vector(3, 4),
        Vector(6, 8)
    ]
    print(Vector.sum_vectors(points))


if __name__ == "__main__":
    main()
