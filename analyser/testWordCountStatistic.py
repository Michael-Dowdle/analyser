import unittest
from analyser import WordCountStatistic


class TestWordCountStatistic(unittest.TestCase):
    def setUp(self):
        self.__stat = WordCountStatistic()

    def test_no_line(self):
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_blank_line(self):
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_single_space(self):
        self.__stat.process_line(' ')
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_single_tab_char(self):
        self.__stat.process_line('\t')
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_single_new_line_char(self):
        self.__stat.process_line('\n')
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_single_letter(self):
        self.__stat.process_line('a')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_single_number(self):
        self.__stat.process_line('1')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_single_punctuation_char(self):
        self.__stat.process_line('!')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_single_word(self):
        self.__stat.process_line('word')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_single_space_separated_words(self):
        self.__stat.process_line('two words')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_multiple_space_separated_words(self):
        self.__stat.process_line('two   words')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_tab_char_separated_words(self):
        self.__stat.process_line('two\twords')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_new_line_separated_words(self):
        self.__stat.process_line('two')
        self.__stat.process_line('words')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_new_line_char_separated_words(self):
        self.__stat.process_line('two\nwords')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_multi_words_single_line(self):
        self.__stat.process_line('a few more words')
        self.__stat.calculate()
        self.assertEqual(4, self.__stat.result)

    def test_multi_words_multi_lines(self):
        self.__stat.process_line('a lot more')
        self.__stat.process_line('words across')
        self.__stat.process_line('many lines')
        self.__stat.calculate()
        self.assertEqual(7, self.__stat.result)


if __name__ == '__main__':
    unittest.main()
