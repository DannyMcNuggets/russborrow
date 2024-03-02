import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestNormalize(unittest.TestCase):

    def test_normalize_empty_list(self):
        words = []
        result = main.normalize(words)
        expected = {}
        self.assertEqual(result, expected)

    # test instances count
    def test_normalize_instances(self):
        words = ['съешь', 'мягких', 'Съем']
        result = main.normalize(words)
        expected = {'съесть': ['съешь', 'Съем'], 'мягкий': ['мягких']}
        self.assertEqual(result, expected)

    # test emails
    def test_normalize_emails(self):
        words = ['testemail@mail.com', 'бобра', 'secondemail@mail.org']
        result = main.normalize(words)
        expected = {
        'testemail@mail.com': ['testemail@mail.com'], 
        'бобр': ['бобра'], 
        'secondemail@mail.org': ['secondemail@mail.org'], 
        }
        self.assertEqual(result, expected)

    # test basic text
    def test_normalize_basic(self):
        # Test the basic functionality of the normalize function
        words = ['Съешь', 'еще', 'этих', 'мягких', 'французских', 'булок', 'да',
        'выпей', 'же', 'чаю', 'Эх', 'чужак', 'Общий', 'съeм-съeм', 'цен', 'шляп', 'юфть', 'вдрызг']
        result = main.normalize(words)
        expected = {
            'съесть': ['Съешь'], 
            'ещё': ['еще'], 
            'этот': ['этих'], 
            'мягкий': ['мягких'], 
            'французский': ['французских'],
            'булка': ['булок'], 
            'да': ['да'], 
            'выпить': ['выпей'], 
            'же': ['же'], 
            'чай': ['чаю'], 
            'эх': ['Эх'], 
            'чужак': ['чужак'], 
            'общий': ['Общий'], 
            'съeм-съeм': ['съeм-съeм'],
            'цена': ['цен'], 
            'шляпа': ['шляп'], 
            'юфть': ['юфть'], 
            'вдрызг': ['вдрызг']
            }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
