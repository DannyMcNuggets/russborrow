import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

class TestCsvOutput(unittest.TestCase):
    expanded_output_path = "temp_output.csv"
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

    def test_output_csv_basic(self):
        main.output_file_csv(self.expanded_output_path, self.ready_dictionary)
        
        result = []
        with open(self.expanded_output_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                result.append(row)

        os.remove(self.expanded_output_path)

        expected = [
            ["Word", "Value", "Origin", "Repeats", "Instances"],
            ["банкрот", "— bancarotta — rotta «сломанная лавочка»", "Из итальянского", "1", "Банкрот"],
            ["бумеранг", "— (язык даруг) bumariny, через англ. boomerang", "Из аборигенов Австралии", "1", "бумеранг"],
            ["вилла", "— villa, из итал. villa, из лат. villa «сельский дом»", "Из итальянского", "1", "виллу"]
        ]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
