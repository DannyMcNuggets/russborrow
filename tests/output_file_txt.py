import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestOutputTxt(unittest.TestCase):

    expanded_output_path = "temp_output.txt"
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
    ready_dictionary = main.Borrowed(words, found_borrowed)

    def test_output_txt_basic(self):
        main.output_file_txt(self.expanded_output_path, self.ready_dictionary)
        result = []
        with open(self.expanded_output_path, "r") as file:
            result = [line.strip() for line in file if line.strip()]
        os.remove(self.expanded_output_path)

        expected = [ 'Out of a total of 6 words, 3 are borrowed, comprising 50.0% of the total.', 
        '1x: банкрот — bancarotta — rotta «сломанная лавочка» – Из итальянского.', 
        'В тексте встречается: Банкрот',
        '1x: бумеранг — (язык даруг) bumariny, через англ. boomerang – Из аборигенов Австралии.', 
        'В тексте встречается: бумеранг',
        '1x: вилла — villa, из итал. villa, из лат. villa «сельский дом» – Из итальянского.', 
        'В тексте встречается: виллу'
        ]

        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()
