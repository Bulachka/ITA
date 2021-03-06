"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""
[('Fizz' * (not i % 3) + 'Buzz' * (not i % 5)) or i for i in range(1, 101)]


"""
List practice"""


#Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
[el1 + el2 for el1 in 'ab' for el2 in 'bcd']

#Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
[::2]

#Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
lst2 = [str(int_) + 'a' for int_ in '1234']

#Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
lst2.pop(1)

#Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
lst3 = lst2[:]
lst3.append('2a')


"""
Tuple practice
"""

#Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
lst = ['a', 'b', 'c']
tpl = tuple(lst)

#Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
tpl = tuple(lst)

#Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', 2, 'python'

"""
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно выводились 
значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
"""
kortez = ([1, 2, 3], )


"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

def pairs(stroka):
    from collections import Counter
    group_numbers = Counter(stroka)
    result = {}
    for key, value in group_numbers.items():
        if key != ' ' and value > 1:
            result[key] = ((value*(value-1))//2)
    return result


"""
Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том 
порядке, в котором они встречаются в списке.
"""
[el for el in lst4 if lst4.count(el) == 1]

"""
Упорядоченный список.
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок, 
а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя, 
задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
"""


def zero(lst):
    answer = [int_ for int_ in lst if int_]
    answer.extend(lst.count(0)*[0])
    print(answer)