# Сдать решение задачи C-Рыцари и лжецы
# Сколько рыцарей?
#
# На острове Буяне жили N человек, каждый из которых был либо рыцарем
# либо лжецом, встали в круг. Рыцари говорят только правду, лжецы всегда
# только лгут. Каждому человеку в кругу задали вопрос: «Кто ты и кто
# твой сосед слева: рыцарь или лжец?» При этом каждый человек сказал,
# что он – рыцарь. А ответы всех людей о левом соседе были записаны в
# следующем формате: 1 – рыцарь 0 – лжец. Все ответы записаны в строку
# через пробел. Последний спрошенный человек отвечал на вопрос о первом.
#
# Написать программу, которая по ответам жителей определяет, какое
# количество рыцарей заведомо присутствует в круге.
#
# Входные данные
#
# Первое число ( 1 < N ≤ 255 ) - количество жителей. Следующие N чисел
# (0 или 1), разделенных пробелами - ответы жителей.
#
# Примеры
#
# Вход            Выход
#
# 4               2
#
# 0  1  0  1
#

# Задача о рыцарях и лжецах — переборная. К счастью, перебор можно
# ограничить всего лишь двумя вариантами: первый человек — рыцарь или
# лжец?
# Предположив один из двух вариантов, можно однозначно вычислить,
# рыцарь или лжец следующий (так как человек с известным статусом сказал
# про человека слева) и так далее по индукции до первого.
#
# В процессе индукции можно считать, сколько у нас рыцарей. Когда по
# индукции выяснен статус первого жителя, проверяем, соответствует ли он
# нашему предположению. Если же соответствующих вариантов 2,
# то выбираем тот, в котором меньше рыцарей (то есть заведомо
# присутствует столькото, а может быть, есть и больше).

def create_input_data() -> list:
    """
    Prompts the user to input a list of integers and returns the list.

    Returns:
        arr: A list of integers entered by the user.
    """
    print("Input the data: ")
    arr = []
    while True:
        inp = input()
        if inp == "":
            break
        arr.extend(inp)
    arr = [int(el) for el in arr if el != " "]
    return arr


def count_with_first_status(array: list, status: int) -> int:
    """
    Counts the number of knights with the given first status in
    the array.

    Args:
        array (list): The list of answers (0 or 1) for each knight.
        status (int): The first status of the knights (0 or 1).

    Returns:
        knight_cnt: The number of knights with the given first status.
    """
    answer_list = array[1:]
    # member_num = array[0]
    # Initialize the count of knights with the given first status.
    knight_cnt = 1 if status == 1 else 0
    # Iterate over the answer_list and update the status and knight_cnt.
    for answer in answer_list:
        if status == 1 and answer == 0:
            status = 0
        elif status == 1 and answer == 1:
            status = 1
            knight_cnt += 1
        elif status == 0 and answer == 0:
            status = 1
            knight_cnt += 1
        elif status == 0 and answer == 1:
            status = 0
        else:
            print("Something strange happened.")
    return knight_cnt


def compare_answers(array: list) -> int:
    """
    Returns the minimum count.
    Args:
        array (list): List of integers representing the status of
        answers.
    Returns:
        ans: The minimum count.
    """
    ans = min(
        count_with_first_status(array, 1),
        count_with_first_status(array, 0)
    )
    return ans


def main():
    """The entry point."""
    array = create_input_data()
    print(compare_answers(array))


if __name__ == "__main__":
    main()
