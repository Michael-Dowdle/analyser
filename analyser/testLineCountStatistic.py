import unittest
import analyser


class TestLineCountStatistic(unittest.TestCase):
    def setUp(self):
        self.__stat = analyser.LineCountStatistic()

    def test_no_line(self):
        self.__stat.calculate()
        self.assertEqual(0, self.__stat.result)

    def test_single_blank_line(self):
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_single__space_line(self):
        self.__stat.process_line(' ')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_multi_blank_line(self):
        self.__stat.process_line('')
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_single_line(self):
        self.__stat.process_line('single line')
        self.__stat.calculate()
        self.assertEqual(1, self.__stat.result)

    def test_multi_line(self):
        self.__stat.process_line('multiple')
        self.__stat.process_line('lines')
        self.__stat.calculate()
        self.assertEqual(2, self.__stat.result)

    def test_blank_first_line(self):
        self.__stat.process_line('')
        self.__stat.process_line('blank line')
        self.__stat.process_line('at beginning')
        self.__stat.calculate()
        self.assertEqual(3, self.__stat.result)

    def test_blank_middle_line(self):
        self.__stat.process_line('blank line in')
        self.__stat.process_line('')
        self.__stat.process_line('the middle')
        self.__stat.calculate()
        self.assertEqual(3, self.__stat.result)

    def test_blank_last_line(self):
        self.__stat.process_line('blank line')
        self.__stat.process_line('at the end')
        self.__stat.process_line('')
        self.__stat.calculate()
        self.assertEqual(3, self.__stat.result)


if __name__ == '__main__':
    unittest.main()
