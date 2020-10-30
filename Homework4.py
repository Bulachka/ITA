"""
1. Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, а значениями
кубы этих чисел.
"""


def make_cube():
    return {x: x ** 3 for x in range(1, 21)}


"""
2. Города
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране
он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры
Входные данные:
N = 2
str1 = 'Russia Moscow Petersburg Novgorod Kaluga'
str2 = 'Russia Moscow Petersburg Novgorod Kaluga'
3
Odessa
Moscow
Novgorod
Выходные данные
Ukraine
Russia
Russia
def towns(N, str1, str2, town):
    if town in str1.split(): return  str1.split()[0]
    else: return  str2.split()[0]
"""


# Вариант2 со словарями
def towns(*args):
    n = int(input('Please type number of countries: '))
    d = {}
    for i in range(n):
        country = input('Please type countries: ').split()
        name = country[0]
        cities = country[1:]
        for city in cities:
            d.setdefault(city, name)
    m = int(input('Please type number of towns: '))
    for i in range(m):
        print(d.get(input('Please type towns: ')))


"""
3. Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
"""


def different_ints_in_common(lst1, lst2):
    lst1.extend(lst2)
    return len(set(lst1))


"""
4. Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
"""


def different_ints(lst1, lst2):
    lst1.extend(lst2)
    from collections import Counter
    result = [int_ for int_ in lst1 if Counter(lst1)[int_] == 1]
    return len(result)


"""
5. Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые
знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi
строк, содержащих названия языков, которые знает i-й школьник.
Пример входных данных:
N = 3          # N количество школьников
M1 = 2          # M1 количество языков первого школьника
'Russian'    # языки первого школьника
'English'
M2 = 3          # M2 количество языков второго школьника
'Russian'
'Belarusian'
'English'
M3 = 3
'Russian'
'Italian'
'French'
Выходные данные
В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
M1_list = ['Russian', 'English']
M2_list = ['Russian', 'English', 'Belarusian']
M3_list = ['Russian', 'Italian', 'French']
common_list = [lan for lan in M1_list if lan in M2_list and lan in M3_list]
big_list = set(M1_list + M2_list + M3_list)
print(len(common_list))
for lan in common_list:
    print(lan)
print(len(big_list))
for lan in big_list:
    print(lan)
"""


# Вариант2 со словарями
def languages(*args):
    n = int(input('Please type number of students: '))
    d = {}
    for i in range(n):
        m = int(input('Please type number of languages for current student: '))
        for language in range(m):
            language = input('Please type language: ')
            if language in d:
                d[language] += 1
            else:
                d[language] = 1
    languages = [k for k in d.keys()]
    common_languages = [k for k, v in d.items() if v == n]
    print(len(common_languages), common_languages, len(d), languages, sep='\n')


"""
6. Слова
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих подряд, слова
разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных слов содержится
в этом тексте.
"""


def words(str_):
    lst = str_.split()
    return len(set(lst))


"""
7. Оглянемся назад
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции
и рекурсию).
"""


def evklid(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b
