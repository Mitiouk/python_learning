#Тестирование проекта при помощи класса utittest
#тест функции parser_rule
#test_01 Проверка того, как работает класс
#test_02 Проверка на целевой символ пустой строки
#test_03 Проверка на общую последовательность символов
#тест функции markovAlgorifm
#test_04 Добавление в начало строки
#test_05 Удаление первого вхождения
#test_06 Удаление всех вхождений
#test_07 Замена первого вхождения
#test_08 Замена всех вхождений



import unittest
from markov import parser_rule
from markov import markovAlgorifm

class markovTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, 1, 'Fail')

    def test_02(self):
        self.assertEqual(parser_rule('^'),"")

    def test_03(self):
        self.assertEqual(parser_rule('a'),"a")
    #========================================

    def test_04(self):
        self.assertEqual(markovAlgorifm([['', 'b', 1]], 'abab'), 'babab')

    def test_05(self):
        self.assertEqual(markovAlgorifm([['a', '', 1]], 'abab'), 'bab')

    def test_06(self):
        self.assertEqual(markovAlgorifm([['a', '', 0]], 'abab'), 'bb')

    def test_07(self):
        self.assertEqual(markovAlgorifm([['a', 'b', 1]], 'abab'), 'bbab')

    def test_08(self):
        self.assertEqual(markovAlgorifm([['a', 'b', 0]], 'abab'), 'bbbb')


if __name__ == '__main__':
    print('TEST MARKOV:', __name__)
    unittest.main()
