# Упражнение №6. Страны и Языки
# Дан список стран и языков на которых говорят в этой стране в
# формате <Название Страны> : <язык1> <язык2> <язык3> ... в файле
# task5/input.txt. На ввод задается N - длина списка и список языков.
# Для каждого языка укажите, в каких странах на нем говорят.
#
# Ввод	                Вывод
# 3
# азербайджанский	Азербайджан
# греческий	        Кипр Греция
# китайский	        Китай Сингапур
def find_countries_by_language(file_path, languages):
    # Чтение файла и создание словаря соответствия языков и стран
    country_language_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            country, langs = line.split(':')
            for lang in langs.strip().split():
                country_language_data.setdefault(lang, []).append(country.strip())
    # Поиск стран для каждого языка
    result = {}
    for language in languages:
        result[language] = country_language_data.get(language, ["Язык не найден"])
    return result


def main():
    file_path = 'ex06/input.txt'
    languages = ['азербайджанский', 'греческий', 'китайский']
    print(find_countries_by_language(file_path, languages))


if __name__ == "__main__":
    main()
