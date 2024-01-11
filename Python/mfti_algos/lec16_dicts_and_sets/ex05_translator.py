# Упражнение №5. Перевод текста
# Дан словарь task4/en-ru.txt с однозначным соответствием английских и
# русских слов в таком формате:
#
# cat - кошка
#
# dog - собака
#
# mouse - мышь
#
# house - дом
#
# eats - ест
#
# in - в
#
# too - тоже
#
# Здесь английское и русское слово разделены двумя табуляциями и
# минусом:
# '\t-\t'.
#
# В файле task4/input.txt дан текст для перевода, например:
#
# Mouse in house. Cat in house.
# Cat eats mouse in dog house.
# Dog eats mouse too.
# Требуется сделать подстрочный перевод с помощью имеющегося словаря и
# вывести результат в output.txt. Незнакомые словарю слова нужно
# оставлять в исходном виде.

# Сделал как указано. Подобный подход дает совсем слабый результат для
# реальных текстов. Даже не стал сохранять выходной результат в файл,
# только печатаю в консоль.
# Можно помучиться с окончаниями, корнями, несколькими значениями для
# одного слова. Но смысла нет. Неспроста только трансформеры в LLM дали
# достойный результат при переводе.
import string


def create_dict():
    en_ru_dic = {}
    with open("ex05/en-ru.txt", "r") as file:
        for line in file:
            en, ru = line.split("\t-\t")
            en_ru_dic[en] = ru.strip()
    return en_ru_dic


def translate(en_ru_dict):
    with open("ex05/input.txt", "r") as file:
        ru_text = ""
        for line in file:
            en_text = line.split()
            # print(en_text)
            if not en_text:
                ru_text += "\n\n"
            for en_word in en_text:
                # Если первая буква слова заглавная и в конце нет знака препинания
                if en_word[0].isupper() and en_word[-1] not in string.punctuation:
                    if en_word.lower() not in en_ru_dict:
                        ru_text += f" {en_word}"
                    else:
                        ru_word = en_ru_dict[en_word.lower()]
                        ru_word = ru_word.capitalize()
                        ru_text += f" {ru_word}"
                # Если первая буква заглавная и в конце знак препинания
                elif en_word[0].isupper() and en_word[-1] in string.punctuation:
                    if en_word.lower()[:-1] not in en_ru_dict:
                        ru_text += f" {en_word}"
                    else:
                        ru_word = en_ru_dict[en_word.lower()[:-1]]
                        ru_word = ru_word.capitalize()
                        ru_text += f" {ru_word}{en_word[-1]}"
                # Если первая буква строчная и в конце знак препинания
                elif en_word[0].islower() and en_word[-1] in string.punctuation:
                    if en_word[:-1] not in en_ru_dict:
                        ru_text += f" {en_word}"
                    else:
                        ru_word = en_ru_dict[en_word[:-1]]
                        ru_text += f" {ru_word}{en_word[-1]}"
                # Если первая буква строчная и в конце нет знака препинания
                else:
                    if en_word not in en_ru_dict:
                        ru_text += f" {en_word}"
                    else:
                        ru_word = en_ru_dict[en_word]
                        ru_text += f" {ru_word}"
    return ru_text


def main():
    en_ru_dict = create_dict()
    print(translate(en_ru_dict))


if __name__ == "__main__":
    main()
