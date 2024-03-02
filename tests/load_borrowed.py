import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestLoadBorrowed(unittest.TestCase):

    TOTAL_WORDS_IN_BORROWED_DIC = 4228

    def test_load_borrowed_length(self):
        borrowed_dictionary = main.load_borrowed()
        result = len(borrowed_dictionary)
        expected = self.TOTAL_WORDS_IN_BORROWED_DIC
        self.assertEqual(result, expected)

    def test_load_borrowed_loading(self):
        borrowed_dictionary = main.load_borrowed()
        expected_entry = {'бумеранг': {'Value': '— (язык даруг) bumariny, через англ. boomerang', 'Origin': 'Из аборигенов Австралии', 'Repeats': 0}}
        key, value = next(iter(borrowed_dictionary.items()))
        result = {key: value}
        self.assertEqual(result, expected_entry) 

    def test_load_borrowed_loading_last(self):
        borrowed_dictionary = main.load_borrowed()
        expected_entry = {'яой': {'Value': '— やおい (гомосексуальные мужские отношения в манге и аниме)', 'Origin': 'Из японского', 'Repeats': 0}}
        key, value = next(iter(reversed(borrowed_dictionary.items())))
        result = {key: value}
        self.assertEqual(result, expected_entry)

if __name__ == '__main__':
    unittest.main()
