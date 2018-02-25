from analyser.StatisticABC import StatisticABC
import collections
import re


class MostCommonLetterStatistic(StatisticABC):
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
