"""
1. Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
a. runner() – все фукнции вызываются по очереди.
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import Homework4

def runner(*args):
    if args:
        func_list = [*args]
    else:
        func_list = [getattr(Homework4, func) for func in dir(Homework4) if callable(getattr(Homework4, func))]
    return (func() for func in func_list)


"""
2. Создайте декоратор, который хранит результаты вызовы функции (за все время вызовов, не только текущий запуск программы)
"""


result = []
def my_dec(func):
    def wrapper(*args, **kwargs):
        global result
        new_func = func(*args, **kwargs)
        result.append(new_func)
    return wrapper


"""
3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
"""


def get_ranges(lst):
    res = lst[:1]
    for i in range(len(lst) - 1):
        if lst[i + 1] == lst[i] + 1:
            res.append('-')
        else:
            res.append(lst[i])
            res.append(',')
            res.append(lst[i + 1])
    res.append(lst[-1])
    out = []
    for el in range(len(res) - 1):
        if res[el] != res[el + 1]:
            out.append(str(res[el]))
    if res[-1] != out[-1]: out.append(str(res[-1]))
    return ''.join(out)


"""
4. В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма рейтингов, years.txt –
гистограмма годов.
"""


from collections import Counter

with open("ratings.list") as file_in, open("top250_movies.txt", 'w') as movie, open("ratings.txt", 'w') as file_rank, \
        open("year.txt", 'w') as file_year:
    text = file_in.readlines()
    ind = 0
    for line in text:
        if 'New  Distribution  Votes  Rank  Title' in line:
            ind = text.index(line)
            break
    text = text[ind + 1:ind + 1 + 250]
    years = []
    ranks = []

    for line in text:
        distribution, votes, rank, *title, year = line.strip().split()
        movie.write(' '.join(title) + '\n')
        ranks.append(rank)
        years.append(year[1:5])

    years_counter = Counter(years)
    for yr in sorted(set(years)):
        file_year.write(yr + ' ' + '+' * years_counter[yr] + '\n')

    ranks_counter = Counter(ranks)
    for rk in sorted(set(ranks)):
        file_rank.write(rk + ' ' + '+' * ranks_counter[rk] + '\n')


"""
Бинарные операции:
5. Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def fifth(n):
    answer = 1
    while n > 1 << answer: answer += 1
    return 1 << (answer - 1) if abs(n - (1 << (answer - 1))) < abs(n - (1 << answer)) else 1 << answer


"""
6. Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def sixth(n):
    dividers = []
    power = 1
    while 1 << power <= n:
        if not n % (1 << power):
            dividers.append(1 << power)
        power += 1
    return dividers[-1] if dividers else "doesn't exist"
