"""Module for defining statistic types and how to calculate them."""
from abc import ABC, abstractmethod
import collections
import re


class __StatisticBase(ABC):
    """Private base class to use for creating statistics."""

    def __init__(self, desc):
        """

        :param desc:
        """
        self.__description = desc
        self._result = ""
        super().__init__()

    @property
    def description(self):
        """

        :return:
        """
        return self.__description

    @property
    def result(self):
        """

        :return:
        """
        return self._result

    @abstractmethod
    def process_line(self, line):
        """

        :param line:
        :return:
        """
        pass

    @abstractmethod
    def calculate(self):
        """

        :return:
        """
        pass


class WordCountStatistic(__StatisticBase):
    def __init__(self):
        """

        """
        self.__wordCount = 0
        super().__init__("whitespace delimited word count")

    def process_line(self, line):
        """

        :param line:
        :return:
        """
        self.__wordCount += len(line.split())

    def calculate(self):
        self._result = self.__wordCount


class LineCountStatistic(__StatisticBase):
    """

    """
    def __init__(self):
        """

        """
        self.__lineCount = 0
        super().__init__("line count")

    def process_line(self, *_):
        """

        :param _:
        :return:
        """
        self.__lineCount += 1

    def calculate(self):
        """

        :return:
        """
        self._result = self.__lineCount


class AvgLettersPerWordStatistic(__StatisticBase):
    """

    """
    def __init__(self):
        """

        """
        self.__wordCount = 0
        self.__totalWordLengths = 0
        super().__init__("average number of letters per word")

    def process_line(self, line):
        """

        :param line:
        :return:
        """
        for word in line.split():
            self.__wordCount += 1
            self.__totalWordLengths += len(word)

    def calculate(self):
        """

        :return:
        """
        if self.__wordCount == 0:
            self._result = 0.0
        else:
            self._result = round(self.__totalWordLengths / self.__wordCount, 1)


class MostCommonLetterStatistic(__StatisticBase):
    """

    """
    def __init__(self):
        """

        """
        self.__letterFrequencyDict = collections.defaultdict(int)
        super().__init__("most common letter")

    def process_line(self, line):
        """

        :param line:
        :return:
        """
        for char in line:
            if re.compile('[A-Za-z]').match(char):
                self.__letterFrequencyDict[char.lower()] += 1

    def calculate(self):
        """

        :return:
        """
        if len(self.__letterFrequencyDict) == 0:
            self._result = ''
        else:
            self._result = sorted(self.__letterFrequencyDict,
                                 key=self.__letterFrequencyDict.__getitem__,
                                 reverse=True)[0]
