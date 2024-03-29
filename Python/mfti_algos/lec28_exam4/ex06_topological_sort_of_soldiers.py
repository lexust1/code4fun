# Сдать решение задачи F-Построение
#
# Группа солдат-новобранцев прибыла в армейскую часть N666. После
# знакомства с прапорщиком стало очевидно, что от работ на кухне по
# очистке картофеля спасти солдат может только чудо.
#
# Прапорщик, будучи не в состоянии запомнить фамилии, пронумеровал
# новобранцев от 1 до N. После этого он велел им построиться по росту
# (начиная с самого высокого). С этой несложной задачей могут
# справиться даже совсем необученные новобранцы, да вот беда, прапорщик
# уверил себя, что знает про некоторых солдат, кто из них кого выше, и
# это далеко не всегда соответствует истине.
#
# После трех дней обучения новобранцам удалось выяснить, что знает (а
# точнее, думает, что знает) прапорщик. Помогите им, используя эти
# знания, построиться так, чтобы товарищ прапорщик остался доволен.
#
# Формат входных данных
# Сначала на вход программы поступают числа N и M
# (1 < N <= 100, 1 <= M <= 5000) – количество солдат в роте и количество
# пар солдат, про которых прапорщик знает, кто из них выше. Далее идут
# эти пары чисел A и B по одной на строке (1 <= A,B <= N), что означает,
# что, по мнению прапорщика, солдат A выше, чем B. Не гарантируется,
# что все пары чисел во входных данных различны.
#
# Формат выходных данных
# В первой строке выведите "Yes" (если можно построиться так, чтобы
# прапорщик остался доволен) или "No" (если нет).
#
# Примеры
# Ввод	Вывод
# 4 5     No
# 1 2
# 2 3
# 3 4
# 1 4
# 4 1
#
def create_adj_list():
    # Задаем число ребер (m) и вершин (n) графа
    n, m = [int(x) for x in input().split()]
    graph = {str(i): set() for i in range(1, n + 1)}
    # Проходим по всем ребрам графа
    for _ in range(m):
        # Считываем вершины, соединенные ребром
        v1, v2 = input().split()
        # Добавляем вершину v2 в множество соседей вершины v1
        graph[v1].add(v2)
    return graph


def dfs(graph, vertex, visited, stack, ans):
    """
    Функция для рекурсивного обхода графа и выполнения топологической
    сортировки при помощи dfs. Теперь также обнаруживает циклы в графе.

    Args:
    graph (dict): Граф, представленный в виде словаря множеств.
    vertex (str): Текущая вершина для обхода.
    visited (set): Множество посещенных вершин.
    stack (set): Множество вершин в текущем стеке вызова.
    ans (list): Список для сохранения порядка топологической сортировки.

    Returns:
    bool: Возвращает False, если найден цикл, иначе True.
    """
    # Добавление текущей вершины в множество посещенных и стек вызова
    visited.add(vertex)
    stack.add(vertex)
    # Перебор всех соседей
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            # Рекурсивный вызов для соседей
            if not dfs(graph, neighbour, visited, stack, ans):
                # Цикл найден
                return False
        elif neighbour in stack:
            # Цикл найден
            return False
    # Удаление вершины из стека вызова и добавление в список ans
    stack.remove(vertex)
    ans.append(vertex)
    return True


def tarjan(graph):
    """
    Функция для выполнения топологической сортировки графа. Теперь также
    проверяет наличие циклов в графе.

    Args:
    graph (dict): Граф, представленный в виде словаря множеств.

    Returns:
    list or str: "YES", если возможно топологическая сортировка,
    или строка "NO", если граф содержит циклы.
    """
    # Список для хранения порядка топологической сортировки
    ans = []
    # Множество для отслеживания посещенных вершин
    visited = set()
    # Множество для отслеживания вершин в текущем стеке вызова
    stack = set()
    # Вызов DFS для каждой непосещенной вершины (а не соседа), по сути,
    # со стартом из разных вершин.
    for vertex in graph:
        if vertex not in visited:
            # Обход в глубину для каждой вершины пока не дойдем до
            # цикла.
            if not dfs(graph, vertex, visited, stack, ans):
                # Цикл найден, топологическая сортировка невозможна
                return "NO"
    # # Реверсирование списка для получения правильного порядка
    # ans.reverse()
    # return ans
    return "YES"


def main():
    # graph = create_adj_list()
    # print(graph)
    # Case 1. Есть цикл
    graph = {'1': {'2', '4'}, '2': {'3'}, '3': {'4'}, '4': {'1'}}
    print(tarjan(graph))
    # Case 2. Нет цикла
    graph = {'1': {'4', '2'}, '2': {'3'}, '3': {'4'}, '4': set()}
    print(tarjan(graph))


if __name__ == "__main__":
    main()
