import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestCleanAndSplit(unittest.TestCase):

    # check empty
    def test_clean_and_split_empty(self):
        string = ""
        result = main.clean_and_split(string)
        self.assertEqual(result, [])

    # check non-alpha-numeric symbols
    def test_clean_and_split_special(self):
        string = '"@#$%^&*()_+=-{}[]|:;"<>,.?/~"'
        result = main.clean_and_split(string)
        self.assertEqual(result, [])

    # check blank spaces
    def test_clean_and_split_spaces(self):
        string = "А если      тут   будет несколько пробелов?     Сработает ли?"
        result = main.clean_and_split(string)
        expected = ['А', 'если', 'тут', 'будет', 'несколько', 'пробелов', 'Сработает', 'ли']
        self.assertEqual(result, expected)

    # check cyrilycs and latin
    def test_clean_and_split_latin_cyrilic(self):
        string = "Привет, Hello, Привіт"
        result = main.clean_and_split(string)
        expected = ['Привет', 'Hello', 'Привіт']
        self.assertEqual(result, expected)

    # tesh hyphens and dashes
    def test_clean_and_split_words_with_dashes(self):
        string = "Зашел - вышел, чуть-чуть какой-нибудь - ушел!"
        result = main.clean_and_split(string)
        expected = ['Зашел', 'вышел', 'чуть-чуть', 'какой-нибудь', 'ушел']
        self.assertEqual(result, expected)

    # test numbers
    def test_clean_and_split_numeric(self):
        string = "123 456 слово1 789 2слово"
        result = main.clean_and_split(string)
        expected = ['123', '456', 'слово1', '789', '2слово']
        self.assertEqual(result, expected)

    # test emails
    def test_read_txt_email(self):
        string = "Ваш testemail@mail.com?"
        result = main.clean_and_split(string)
        expected = ['Ваш', 'testemail@mail.com']
        self.assertEqual(result, expected)

    # check ordinary text
    def test_clean_and_split_basic(self):
        string = "Съешь ещё этих мягких французских булок, да выпей же чаю. Эх, чужак! Общий съём-съём цен шляп (юфть) — вдрызг!"
        result = main.clean_and_split(string)
        expected = ['Съешь', 'ещё', 'этих', 'мягких', 'французских', 'булок', 'да', 'выпей', 'же', 'чаю', 
        'Эх', 'чужак', 'Общий', 'съём-съём', 'цен', 'шляп', 'юфть', 'вдрызг']

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
