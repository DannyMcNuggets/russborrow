import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestFindBorrowed(unittest.TestCase):

    # short version of borrowed dictionary 
    borrowed_words = {
    'бумеранг': {'Value': '— (язык даруг) bumariny, через англ. boomerang', 'Origin': 'Из аборигенов Австралии', 'Repeats': 0},
    'вилла': {'Value': '— villa, из итал. villa, из лат. villa «сельский дом»', 'Origin': 'Из английского', 'Repeats': 0},
    'банкрот': {'Value': '— bancarotta — rotta «сломанная лавочка»', 'Origin': 'Из итальянского', 'Repeats': 0}
    }

    def test_find_borrowed_basic(self):
        normalized_words = {
        'банкрот': ['Банкрот']
        }

        result = main.find_borrowed(normalized_words, self.borrowed_words)
        expected = {
            'банкрот': {
                'Value': '— bancarotta — rotta «сломанная лавочка»',
                'Origin': 'Из итальянского',
                'Repeats': 1,
                'Instances': ['Банкрот']
            }
        }
        
        self.assertEqual(result, expected)

    def test_find_borrowed_empty(self):
        normalized_words = {
        'молоко': ['Молоко']
        }
        result = main.find_borrowed(normalized_words, self.borrowed_words)
        expected = {}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
