import unittest
from analyser import *


class TestTextFileAnalyser(unittest.TestCase):
    def setUp(self):
        stats = [WordCountStatistic(),
                 LineCountStatistic(),
                 AvgLettersPerWordStatistic(),
                 MostCommonLetterStatistic()]
        self.__analyser = TextFileAnalyser(stats)

    def test_analyser(self):
        self.__analyser.analyse('file.txt')
        results = self.__analyser.results
        self.assertEqual(6, results.get(WordCountStatistic().description))
        self.assertEqual(3, results.get(LineCountStatistic().description))
        self.assertEqual(3.5, results.get(AvgLettersPerWordStatistic().description))
        self.assertEqual('s', results.get(MostCommonLetterStatistic().description))


if __name__ == '__main__':
    unittest.main()
