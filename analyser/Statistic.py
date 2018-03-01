"""Module for defining statistic types and how to calculate them."""
from abc import ABC, abstractmethod
import collections
import logging
import re


class __StatisticBase(ABC):
    """Private abstract base class to use for creating statistics."""

    def __init__(self, desc):
        """
        Initializer sets a description of the type of statistic,
        and a blank str result that will be set once calculated.

        :param desc:    description of the type of statistic.
        """
        self.__description = desc
        self._result = ""
        super().__init__()

    @property
    def description(self):
        """
        Property method for accessing private description attribute.

        :return:        the description of the statistic.
        """
        return self.__description

    @property
    def result(self):
        """
        Property method for accessing private result attribute.

        :return:        the result calculated for the statistic.
        """
        return self._result

    @abstractmethod
    def process_line(self, line):
        """
        Abstract method required to be defined by derived class
        to take a str line as parameter and process it.

        :param line:    the line to be processed.
        """
        pass

    @abstractmethod
    def calculate(self):
        """
        Abstract method required to be defined by derived class
        to calculate a statistic result for lines processed.
        """
        pass


class WordCountStatistic(__StatisticBase):
    """Derived class for calculating word count statistic."""

    def __init__(self):
        """
        Initializer sets a word count attribute as 0 and calls
        based class initializer, providing a description.
        """
        self.__wordCount = 0
        super().__init__("whitespace delimited word count")

    def process_line(self, line):
        """
        Method to process a line of data, adding the number
        of words in the line to the private word count attribute.

        :param line:    the line of data to be processed.
        """
        logging.debug("processing data line")
        self.__wordCount += len(line.split())

    def calculate(self):
        """
        Method to calculate statistic result, setting it to the
        total word count attribute value.
        """
        logging.debug("calculating result")
        self._result = self.__wordCount


class LineCountStatistic(__StatisticBase):
    """Derived class for calculating line count statistic."""

    def __init__(self):
        """
        Initializer sets a line count attribute as 0 and calls
        based class initializer, providing a description.
        """
        self.__lineCount = 0
        super().__init__("line count")

    def process_line(self, *_):
        """
        Method to process a line of data, incrementing the
        private line count attribute.

        :param line:    the line of data to be processed.
        """
        logging.debug("processing data line")
        self.__lineCount += 1

    def calculate(self):
        """
        Method to calculate statistic result, setting it to the
        total line count attribute value.
        """
        logging.debug("calculating result")
        self._result = self.__lineCount


class AvgLettersPerWordStatistic(__StatisticBase):
    """Derived class for calculating average letters per word statistic."""

    def __init__(self):
        """
        Initializer sets a word count attribute as 0, a
        total word lengths attribute as 0 and calls
        based class initializer, providing a description.
        """
        self.__wordCount = 0
        self.__totalWordLengths = 0
        super().__init__("average number of letters per word")

    def process_line(self, line):
        """
        Method to process a line of data, incrementing the
        private word count attribute and adding the word
        length to the private total word lengths attribute,
        for each word in the line.

        :param line:    the line of data to be processed.
        """
        logging.debug("processing data line")
        for word in line.split():
            self.__wordCount += 1
            self.__totalWordLengths += len(word)

    def calculate(self):
        """
        Method to calculate statistic result, setting it to the
        total word lengths divided by the total word count.
        """
        logging.debug("calculating result")
        if self.__wordCount == 0:
            self._result = 0.0
        else:
            self._result = round(self.__totalWordLengths / self.__wordCount, 1)


class MostCommonLetterStatistic(__StatisticBase):
    """Derived class for calculating most common letter statistic."""

    def __init__(self):
        """
        Initializer sets a blank letter frequency dictionary attribute
        using a default dictionary collection of type int, and calls
        based class initializer, providing a description.
        """
        self.__letterFrequencyDict = collections.defaultdict(int)
        super().__init__("most common letter")

    def process_line(self, line):
        """
        Method to process a line of data, incrementing a value for
        each letters entry location in the private letter
        frequency dictionary attribute. Inserting an entry if one
        does not already exist for that letter.

        .. note::   entry is only added/incremented if character
                    is a uppercase or lowercase letter.

        :param line:    the line of data to be processed.
        """
        logging.debug("processing data line")
        for char in line:
            if re.compile('[A-Za-z]').match(char):
                self.__letterFrequencyDict[char.lower()] += 1

    def calculate(self):
        """
        Method to calculate statistic result by sorting the letter
        frequency dictionary by the value(letter count) in reverse
        order, and then getting the key for the first entry in that
        sorted dictionary.
        """
        logging.debug("calculating result")
        if len(self.__letterFrequencyDict) == 0:
            self._result = ''
        else:
            self._result = sorted(self.__letterFrequencyDict,
                                  key=self.__letterFrequencyDict.__getitem__,
                                  reverse=True)[0]
