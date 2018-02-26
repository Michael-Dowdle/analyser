from abc import ABC, abstractmethod
import collections
import re


class StatisticBase(ABC):
    def __init__(self):
        self.result = ""
        super().__init__()

    @abstractmethod
    def process_line(self, line):
        pass

    @abstractmethod
    def calculate(self):
        pass

    def get_result(self):
        return self.result


class WordCountStatistic(StatisticBase):
    def __init__(self):
        self.wordCount = 0
        super().__init__()

    def process_line(self, line):
        self.wordCount += len(line.split())

    def calculate(self):
        self.result = self.wordCount


class LineCountStatistic(StatisticBase):
    def __init__(self):
        self.lineCount = 0
        super().__init__()

    def process_line(self, *_):
        self.lineCount += 1

    def calculate(self):
        self.result = self.lineCount


class AvgLettersPerWordStatistic(StatisticBase):
    def __init__(self):
        self.wordCount = 0
        self.totalWordLengths = 0
        super().__init__()

    def process_line(self, line):
        for word in line.split():
            self.wordCount += 1
            self.totalWordLengths += len(word)

    def calculate(self):
        self.result = round(self.totalWordLengths / self.wordCount, 1)


class MostCommonLetterStatistic(StatisticBase):
    def __init__(self):
        self.letterFrequencyDict = collections.defaultdict(int)
        super().__init__()

    def process_line(self, line):
        for char in line:
            if re.compile('[A-Za-z]').match(char):
                self.letterFrequencyDict[char.lower()] += 1

    def calculate(self):
        self.result = sorted(self.letterFrequencyDict,
                             key=self.letterFrequencyDict.__getitem__,
                             reverse=True)[0]
