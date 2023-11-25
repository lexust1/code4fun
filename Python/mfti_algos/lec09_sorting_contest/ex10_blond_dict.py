# Сдать решение задачи J-Словарь для блондинки
#
# Задача J: Словарь для блондинки
# Блондинка Даша любит решать кроссворды на латинском языке, пользуясь
# орфографическим словарем. Часто Даша отгадывает последние буквы слова
# и долго ищет каким словам подходит такая концовка. Она мечтает о
# словаре, где бы слова были разбиты на главы по количеству букв в
# слове и написаны задом наперед. Помогите ей составить такой словарь
# по заданному орфографическому словарю латинском языка.
#
# Формат входных данных
# В первой строке содержится единственное целое число N (1≤N≤100) —
# количество латинских слов в словаре. Далее следует N слов по одному
# слову на строку. Все слова состоят только из маленьких латинских букв.
# Общее количество слов на входе не превышает 100. Длина каждого слова
# не превосходит 15 символов.
#
# Формат результата
# Длина слов в данном блоке. На следующих строках слова задом наперед
# и исходное слово через пробел в лексикографическом порядке.
#
# Примеры
#
# Входные данные
# 3
# eucharis
# fittonia
# tagetes
#
# Результат работы
# 7
# setegat tagetes
# 8
# ainottif fittonia
# sirahcue eucharis

def create_input_data():
    """
    Function to create a list of input data from user input.

    Returns:
        arr: A list containing the user input data.
    """
    print("Input the data: ")
    arr = []
    while True:
        inp = input()
        if inp == " ":
            break
        arr.append(inp)
    return arr


def sort_words_pw(arr):
    """
    Sorts a list of words in reverse order, first by length and then
    by value using the built-in sorted method.

    Args:
        arr (list): A list of words to be sorted.

    Returns:
        output: The sorted words, formatted with their length and reverse.
    """
    # Get the length of the list
    length = int(arr[0])
    # Get the words to be sorted
    words = arr[1:]
    # Reverse the words
    rev_words = [word[::-1] for word in words]
    # Sort the reversed words by length and value
    sorted_words = sorted(rev_words, key=lambda x: (len(x), x))
    len_word = 0
    output = ""
    # Format the output
    for word in sorted_words:
        if len(word) != len_word:
            output += f"{len(word)}\n"
            len_word = len(word)
        output += f"{word} {word[::-1]}\n"
    return output


def sort_words(arr):
    """
    Sorts a list of words in descending order of length, and then
    in reverse order.

    Args:
        arr (list): A list of words.

    Returns:
        output: The sorted words in the specified format.
    """
    # Extract the length and words from the input array.
    length = int(arr[0])
    words = arr[1:]
    # Create a list of tuples with reverse words and amount of letters.
    word_lens = [(word[::-1], len(word)) for word in words]
    # Sort the list of word lengths using merge sort algorithm.
    sorted_word_lens = merge_sort(word_lens)
    len_word = 0
    output = ""
    # Format the output.
    for word_len in sorted_word_lens:
        if word_len[1] != len_word:
            output += f"{word_len[1]}\n"
            len_word = word_len[1]
        output += f"{word_len[0]} {word_len[0][::-1]}\n"
    return output


def merge_sort(arr):
    # The base case.
    if len(arr) <= 1:
        return
    # The recursive case.
    # Split into two halves.
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    # Sort two halves.
    merge_sort(left)
    merge_sort(right)
    # Merge two halves.
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        # Use two conditions in ony bypass rather than one (length and
        # lexicographically).
        if (left[i][1] < right[j][1] or
            (left[i][1] == right[j][1] and left[i][0] < right[j][0])):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    arr[:] = merged
    return arr


def main():
    # print(create_input_data())
    arr = ['3', 'eucharis', 'fittonia', 'tagetes']
    # arr = ['5', 'eucharis', 'fittonia', 'tagetes', 'curious', 'socks']
    print(sort_words_pw(arr))
    print(sort_words(arr))


if __name__ == "__main__":
    main()
