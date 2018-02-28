import unittest
from analyser import TextFileAnalyser


class TestTextFileAnalyser(unittest.TestCase):
    def setUp(self):
        self.__analyser = TextFileAnalyser()

    def test_analyser(self):
        self.__analyser.analyse('file.txt')


if __name__ == '__main__':
    unittest.main()
