import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestBorrowedInstance(unittest.TestCase):

    words = ['Банкрот', 'продал', 'бумеранг', 'чтобы', 'купить', 'виллу']
    found_borrowed = {
            'банкрот': {
                'Value': '— bancarotta — rotta «сломанная лавочка»',
                'Origin': 'Из итальянского',
                'Repeats': 1,
                'Instances': ['Банкрот']
            },

            'бумеранг': {
                'Value': '— (язык даруг) bumariny, через англ. boomerang',
                'Origin': 'Из аборигенов Австралии',
                'Repeats': 1,
                'Instances': ['бумеранг']
            },

            'вилла': {
                'Value': '— villa, из итал. villa, из лат. villa «сельский дом»',
                'Origin': 'Из итальянского',
                'Repeats': 1,
                'Instances': ['виллу']
            }
        }

    def test_borrowed_class_exists(self):
        instance = main.Borrowed(self.words, self.found_borrowed)
        self.assertIsInstance(instance, main.Borrowed)

    def test_borrowed_class_len(self):
        instance = main.Borrowed(self.words, self.found_borrowed)
        result = instance.len
        expected = 6
        self.assertEqual(result, expected)

    def test_borrowed_class_bor(self):
        instance = main.Borrowed(self.words, self.found_borrowed)
        result = instance.bor
        expected = 3
        self.assertEqual(result, expected)

    def test_borrowed_class_percent(self):
        instance = main.Borrowed(self.words, self.found_borrowed)
        result = instance.percent 
        expected = 50
        self.assertEqual(result, expected)

    def test_borrowed_class_dict(self):
        instance = main.Borrowed(self.words, self.found_borrowed)
        result = instance.dict 
        expected = self.found_borrowed
        self.assertEqual(result, expected)

    def test_borrowed_class_empty_dict(self):
        found_borrowed_empty = {}
        instance = main.Borrowed(self.words, found_borrowed_empty)
        result = instance.dict
        expected = {}
        self.assertEqual(result, expected)

    def test_borrowed_class_empty_words(self):
        word_empty = []
        instance = main.Borrowed(word_empty, self.found_borrowed)
        result = instance.percent 
        expected = 0
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
