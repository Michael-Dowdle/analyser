import unittest
from analyser import AvgLettersPerWordStatistic


class TestAvgLettersPerWordStatistic(unittest.TestCase):
    def setUp(self):
        self.__stat = AvgLettersPerWordStatistic()

    def test_no_line(self):
        self.__stat.calculate()
        self.assertEqual(0.0, self.__stat.result)

    def test_blank_line(self):
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual(0.0, self.__stat.result)

    def test_single_letter_single_word(self):
        self.__stat.process_line('a')
        self.__stat.calculate()
        self.assertEqual(1.0, self.__stat.result)

    def test_single_letter_multi_word(self):
        self.__stat.process_line('a a')
        self.__stat.calculate()
        self.assertEqual(1.0, self.__stat.result)

    def test_multi_letter_single_word(self):
        self.__stat.process_line('aa')
        self.__stat.calculate()
        self.assertEqual(2.0, self.__stat.result)

    def test_same_letter_count_multi_word(self):
        self.__stat.process_line('aa aa')
        self.__stat.calculate()
        self.assertEqual(2.0, self.__stat.result)

    def test_diff_letter_count_multi_odd_num_words(self):
        self.__stat.process_line('a aa aaa')
        self.__stat.calculate()
        self.assertEqual(2.0, self.__stat.result)

    def test_diff_letter_count_multi_even_num_words(self):
        self.__stat.process_line('a aa aaa aaaa')
        self.__stat.calculate()
        self.assertEqual(2.5, self.__stat.result)


if __name__ == '__main__':
    unittest.main()
