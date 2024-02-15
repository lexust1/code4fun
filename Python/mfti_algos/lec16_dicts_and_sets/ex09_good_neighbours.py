# Упражнение №9*. Добродушные соседи
# В одном очень дружном доме, где живет Фёдор, многие жильцы оставляют
# ключи от квартиры соседям по дому, например на случай пожара или
# потопа, да и просто чтобы покормили животных или полили цветы.
#
# Вернувшись домой после долгих странствий, Фёдор обнаруживает, что
# потерял свои ключи и соседей дома нет. Но вдруг у домофона он находит
# чужие ключи. Помогите Федору найти ключи от своей квартиры в
# квартирах соседей.
#
# На ввод подается файл input.txt, в котором в первой строке записано
# три числа через пробел N - номер квартиры Фёдора, M - номер квартиры
# от которой Федор нашел ключи, K - ключ от этой квартиры. Далее i-я
# строка хранит описание ключей запертых в i-й квартире в формате
# <m_i0 - номер квартиры> <k_i0 - ключ>,<m_i1 - номер квартиры> <k_i1 - ключ>,... ,
# причем реальные номера квартир "зашифрованы" ключем от i-й
# квартиры(Ki) и находятся по формуле
# m_ij' = m_ij - Ki. Номера квартир начинаются с 0 (кпримеру вторая строка файла соответствует 0-й квартире).
#
# Нужно вывести ключ от квартиры Федора или None если его найти
# не получилось.
#
#
# Ввод                Вывод
# 4 0 1               1
# 1 1,2 0,3 1,4 0
# 3 0
# 5 1,6 0
#
# 1 1
# 2 1
#
# Подсказка: используйте словарь для хранения ключей от еще не открытых
# комнат и множество для уже проверенных комнат.

# Необязательное (под звездочкой) задание. Можно вернуться после окончания курса.