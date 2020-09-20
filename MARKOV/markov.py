# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os, sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_rule(_name):
    #Открыть файл для чтения
    #Читать строку вида: XXX YYY Z
    #Где XXX - P шаблон подстановки
    #   YYY - Q симводы подстроки подстановки
    #   Z- признак финальной подстановки
    # Функция возвращает список типа:
    # ([XXX1, YYY2, Z3], [XXX2, YYY2, Z2] ...   [XXXn, YYYn, Zn])
    _dir = os.getcwd()
    _file = _dir + '\\' + _name
    print('Правила из файла:',_file)

    res = list()  # пустое правило
    f = open(_file, 'r')

    for line in f:
        ln = line.rstrip('\r\n')    #убираем нечитаемые символы
        ln= ln.split(' ')           #разделяем на список разделитель - пробел
        res.append(ln)              #добавляем в результат
    f.close()
    return res

def read_word(_name):
    #Читать строку
    #Вернуть переменную со строкой

    _dir = os.getcwd()
    _file = _dir + '\\' + _name
    print('Слово из файла:', _file)

    res = list()  # пустое правило
    f = open(_file, 'r')
    str = f.read()
    f.close()
    str.rstrip()
    return str

#парсер правил, если '^' - возвращаем ''
def parser_rule(a):
    if a == '^':
        return ""
    return a

#Запись в файл
def out_to_file(_name,_str):
    _dir = os.getcwd()
    _file = _dir + '\\' + _name
    print('Вывод результата в файл:', _file)
    f = open(_name, 'a')
    f.write(_str)
    f.write('\n')
    f.close()

def markovAlgorifm(_p, _s):
    _slovo = _s     #слово
    _pravilo = _p   #правило
    i = 0           # счётчик

    while i < len(_pravilo):
        pattern = parser_rule(_pravilo[i][0])
        podstava = parser_rule(_pravilo[i][1])
        final_flag = int(_pravilo[i][2])

        res = _slovo.find(pattern)
        if res != -1:
            _slovo = _slovo.replace(pattern, podstava, 1)
            i = 0  # Возвращаемся к началу алгоритма
            if final_flag:
                break
        else:
            i = i + 1
    return _slovo  # Результат:

#=============================================================
#=============================================================

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(__name__)
    print('MARKOV RUNed')
#Начало алгоритма:=====================================================

#Чтение входных данных
#slovo = '1001001'
#pravilo = [['a', 'b', 0]]



res = markovAlgorifm(read_rule('rule_2.txt'), read_word('word.txt'))
print(res)
out_to_file('result.txt', res)

#===========================================================================