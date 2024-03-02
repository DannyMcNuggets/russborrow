import os
import csv
import unittest
import pymorphy2
from src.russborrow import main

# def read_txt(text_file):
class TestReadTxt(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, "w") as test_file:
            pass 

        self.empty_file_path = "empty_file.txt"
        with open(self.empty_file_path, "w") as empty_file:
            pass 

    def tearDown(self):
        os.remove(self.test_file_path)
        os.remove(self.empty_file_path)
    
    # test the basic functionality of the read_txt function
    def test_read_txt_basic(self):
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, "w") as test_file:
            test_file.write("Съешь ещё этих мягких французских булок,\n")
            test_file.write("да выпей же чаю. Эх, чужак! Общий съём-съём цен шляп (юфть) — вдрызг!")

        result = main.read_txt(self.test_file_path)
        expected = ['Съешь', 'ещё', 'этих', 'мягких', 'французских', 'булок', 'да', 'выпей', 'же', 'чаю', 'Эх', 'чужак', 'Общий', 'съём-съём', 'цен', 'шляп', 'юфть', 'вдрызг']
        self.assertEqual(result, expected)

    # test emails
    def test_read_txt_email(self):
        with open(self.test_file_path, "w") as test_file:
            test_file.write("Ваш testemail@mail.com?")
        result = main.read_txt(self.test_file_path)
        expected = ['Ваш', 'testemail@mail.com']
        self.assertEqual(result, expected)

    # test handling of an empty text file
    def test_read_txt_empty_file(self):
        result = main.read_txt(self.empty_file_path)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
