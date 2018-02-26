from abc import ABC, abstractmethod
import collections
import re


class _StatisticBase(ABC):
    def __init__(self):
        self._result = ""
        super().__init__()

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @abstractmethod
    def process_line(self, line):
        pass

    @abstractmethod
    def calculate(self):
        pass

    def get_result(self):
        return self._result


class WordCountStatistic(_StatisticBase):
    def __init__(self):
        self.__wordCount = 0
        super().__init__()

    def process_line(self, line):
        self.__wordCount += len(line.split())

    def calculate(self):
        self.result = self.__wordCount


class LineCountStatistic(_StatisticBase):
    def __init__(self):
        self.__lineCount = 0
        super().__init__()

    def process_line(self, *_):
        self.__lineCount += 1

    def calculate(self):
        self.result = self.__lineCount


class AvgLettersPerWordStatistic(_StatisticBase):
    def __init__(self):
        self.__wordCount = 0
        self.__totalWordLengths = 0
        super().__init__()

    def process_line(self, line):
        for word in line.split():
            self.__wordCount += 1
            self.__totalWordLengths += len(word)

    def calculate(self):
        self.result = round(self.__totalWordLengths / self.__wordCount, 1)


class MostCommonLetterStatistic(_StatisticBase):
    def __init__(self):
        self.__letterFrequencyDict = collections.defaultdict(int)
        super().__init__()

    def process_line(self, line):
        for char in line:
            if re.compile('[A-Za-z]').match(char):
                self.__letterFrequencyDict[char.lower()] += 1

    def calculate(self):
        self.result = sorted(self.__letterFrequencyDict,
                             key=self.__letterFrequencyDict.__getitem__,
                             reverse=True)[0]
