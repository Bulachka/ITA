"""
1. Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
a. runner() – все фукнции вызываются по очереди
"""
import Homework4


def runner():
    for func in dir(Homework4):
        item = getattr(Homework4, func)
        if callable(item):
            item()


if __name__ == '__main__':
    runner()

"""
b. runner(‘func_name’) – вызывается только функцию func_name.
"""


def runner1(func_name):
    func_name()


"""
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


def runner2(*args):
    for item in args:
        if callable(item):
            item()


"""
2. Создайте декоратор, который хранит результаты вызовы функции (за все время вызовов, не только текущий запуск программы)
"""
result = []


def my_dec(func):
    def wrapper(*args, **kwargs):
        global result
        result.append(func)
        new_func = func(*args, **kwargs)
        return new_func

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
"""
f = open('ratings.list')
print(f.readline())

"""
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма рейтингов, years.txt –
гистограмма годов.
"""

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
    return dividers[-1]
