# Список/лист смежности для хранения графа
#
# Список смежности - это структура данных, используемая для представления графа.
# Граф состоит из набора вершин (или узлов) и множества рёбер, соединяющих эти вершины.
# В списке смежности каждая вершина графа ассоциируется со списком или набором всех
# вершин, с которыми она напрямую соединена рёбрами.
#
# Основные характеристики списка смежности:
#
# - Вершины и их смежные вершины: Для каждой вершины в графе имеется список или набор,
#   содержащий все смежные с ней вершины.
#
# - Эффективность: Список смежности обычно более эффективен для разреженных графов, где
#   число рёбер много меньше, чем квадрат числа вершин.
#
# - Динамичность: Списки смежности легко модифицировать — добавлять или удалять
#   вершины и рёбра.
#
# - Направленные и ненаправленные графы: Может использоваться как для представления
#   направленных, так и ненаправленных графов. В случае ненаправленного графа, если
#   вершина A соединена с вершиной B, B будет присутствовать в списке смежности A, и
#   наоборот. Для направленного графа, если существует направленное ребро из A в B,
#   B будет присутствовать в списке смежности A, но не обязательно наоборот.
#
# - Память: Использование памяти зависит от числа вершин и рёбер. В общем случае,
#   оно пропорционально количеству рёбер.
#
# - Поиск смежных вершин: Очень эффективен, так как требует лишь просмотра
#   соответствующего списка или набора.
#
# - Поиск рёбер: Может быть менее эффективным, поскольку потребует проверки наличия
#   вершины в списке смежности другой вершины.
#
# Пример списка смежности для небольшого графа:
# - Вершина 1: [2, 3]
# - Вершина 2: [1, 4]
# - Вершина 3: [1, 4, 5]
# - Вершина 4: [2, 3]
# - Вершина 5: [3]
#
def create_adj_list():
    # Задаем число ребер (M) и вершин (N) графа
    M, N = [int(x) for x in input().split()]
    G = {}
    # Проходим по всем ребрам графа
    for _ in range(M):
        # Считываем вершины, соединенные ребром
        v1, v2 = input().split()
        # Для каждой пары вершин (v, u) и (u, v)
        for v, u in (v1, v2), (v2, v1):
            # Если вершина v еще не в графе, добавляем ее и создаем множество с соседней вершиной u
            if v not in G:
                G[v] = {u}
            # Если вершина v уже есть в графе, добавляем вершину u в множество соседей
            else:
                G[v].add(u)
    # Возвращаем граф в виде словаря с множествами соседей
    return G


def main():
    print(create_adj_list())


if __name__ == "__main__":
    main()