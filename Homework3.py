"""
1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""


def price(m, n, s):
    rub = m * s
    kop = n * s
    if kop >= 100:
        rub += kop // 100
        kop -= rub * 100
    return "общая цена равна %d рублей %d копеек" % (rub, kop)


"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
•	my_string.split([chars]) возвращает список строк.
•	len(list) - количество элементов в списке
"""


def longest(sentence):
    sentence = sentence.translate({ord(i): None for i in ',.?;:!-'})
    len_let = [len(let) for let in sentence.split() if let.isalpha()]
    indx = len_let.index(max(len_let))
    return sentence.split()[indx]


"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. 
"""


def onlyNewLetters(stroka):
    res = []
    for letter in stroka:
        if letter not in res: res.append(letter)
    res = ''.join(res)
    res = res.replace(' ', '')
    return res


"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
Учитывать только английские буквы.
"""


import string
def countLettersCase(sent):
    countUp = 0
    countL = 0
    for l in sent:
        if l in string.ascii_lowercase: countL += 1
        elif l in string.ascii_uppercase: countUp += 1
    return countL, countUp

