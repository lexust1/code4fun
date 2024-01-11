# Упражнение №4. Подсчет слов
# Дан текст на некотором языке. Требуется подсчитать сколько раз каждое
# слово входит в этот текст и вывести десять самых часто употребяемых
# слов в этом тексте и количество их употреблений.
#
# В качестве примера возьмите файл с текстом лицензионного соглашения
# Python /usr/share/licenses/python/LICENSE.
#
# Подсказка №1: Используйте словарь, в котором ключ -- слово, а
# знчение -- количество таких слов.
#
# Подсказка №2: Точки, запятые, вопросы и восклицательные знаки перед
# обработкой замените пробелами(используйте punctuation из модуля string).
#
# Подсказка №3: Все слова приводите к нижнему регистру при помощи
# метода строки lower().
#
# Подсказка №4: По окончании сбора статистики нужно пробежать по всем
# ключам из словаря и найти ключ с максимальным значением.
import re
import string


def read_txt():
    with open("ex04/LICENSE.txt", "r") as file:
        text = file.read()
    return text


def remove_links(text):
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    return re.sub(url_pattern, "", text)


def remove_punctuation_and_numbers(text):
    translator = str.maketrans('', '', string.punctuation + string.digits)
    return text.translate(translator)


def remove_blank_lines_and_reduce_whitspaces(text):
    text = re.sub(r"^\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text)
    return text


def count_words(text):
    words = {}
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def find_most_frequent_words(words, n):
    top_n = sorted(words.items(), key=lambda x: x[1], reverse=True)[:n]
    return top_n


def main():
    text = read_txt()
    text = remove_links(text)
    text = remove_punctuation_and_numbers(text)
    text = text.lower()
    text = remove_blank_lines_and_reduce_whitspaces(text)
    print(text)
    words = count_words(text)
    print(find_most_frequent_words(words, 10))


if __name__ == "__main__":
    main()
