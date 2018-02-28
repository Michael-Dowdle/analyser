from abc import ABC, abstractmethod
import collections
import re


class __StatisticBase(ABC):
    def __init__(self, desc):
        self.__description = desc
        self._result = ""
        super().__init__()

    @property
    def description(self):
        return self.__description

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


class WordCountStatistic(__StatisticBase):
    def __init__(self):
        self.__wordCount = 0
        super().__init__("whitespace delimited word count")

    def process_line(self, line):
        self.__wordCount += len(line.split())

    def calculate(self):
        self.result = self.__wordCount


class LineCountStatistic(__StatisticBase):
    def __init__(self):
        self.__lineCount = 0
        super().__init__("line count")

    def process_line(self, *_):
        self.__lineCount += 1

    def calculate(self):
        self.result = self.__lineCount


class AvgLettersPerWordStatistic(__StatisticBase):
    def __init__(self):
        self.__wordCount = 0
        self.__totalWordLengths = 0
        super().__init__("average number of letters per word")

    def process_line(self, line):
        for word in line.split():
            self.__wordCount += 1
            self.__totalWordLengths += len(word)

    def calculate(self):
        if self.__wordCount == 0:
            self.result = 0.0
        else:
            self.result = round(self.__totalWordLengths / self.__wordCount, 1)


class MostCommonLetterStatistic(__StatisticBase):
    def __init__(self):
        self.__letterFrequencyDict = collections.defaultdict(int)
        super().__init__("most common letter")

    def process_line(self, line):
        for char in line:
            if re.compile('[A-Za-z]').match(char):
                self.__letterFrequencyDict[char.lower()] += 1

    def calculate(self):
        if len(self.__letterFrequencyDict) == 0:
            self.result = ''
        else:
            self.result = sorted(self.__letterFrequencyDict,
                                 key=self.__letterFrequencyDict.__getitem__,
                                 reverse=True)[0]
