import unittest
import analyser


class TestMostCommonLetterStatistic(unittest.TestCase):
    def setUp(self):
        self.__stat = analyser.MostCommonLetterStatistic()

    def test_no_line(self):
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)

    def test_blank_line(self):
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)

    def test_single_letter(self):
        self.__stat.process_line('a')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_same_letter_single_word(self):
        self.__stat.process_line('aa')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_same_letter_multi_word(self):
        self.__stat.process_line('a a')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_different_letter(self):
        self.__stat.process_line('ab')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_multi_letter(self):
        self.__stat.process_line('aba')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_multi_letter_multi_word(self):
        self.__stat.process_line('a ab abc')
        self.__stat.calculate()
        self.assertEqual('a', self.__stat.result)

    def test_number(self):
        self.__stat.process_line('1')
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)

    def test_punctuation_char(self):
        self.__stat.process_line('!')
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)

    def test_tab_char(self):
        self.__stat.process_line('\t')
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)

    def test_new_line_char(self):
        self.__stat.process_line('\n')
        self.__stat.calculate()
        self.assertEqual('', self.__stat.result)


if __name__ == '__main__':
    unittest.main()
