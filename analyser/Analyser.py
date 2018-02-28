from analyser.Statistic import *


# Setup statistics to gather
temp_stats = [WordCountStatistic(),
              LineCountStatistic(),
              AvgLettersPerWordStatistic(),
              MostCommonLetterStatistic()]


class __Analyser:
    def __init__(self, statistics=temp_stats):
        self.__results = {}
        self.__statistics = statistics

    @staticmethod
    def __calculated_result(stat):
        stat.calculate()
        return stat.get_result()

    def _analyse(self, data):
        for line in data:
            for stat in self.__statistics:
                stat.process_line(line)

        self.__results = {stat.description: self.__calculated_result(stat)
                          for stat in self.__statistics}

    def print_statistics(self):
        for desc, res in self.__results.items():
            print("{:<35s}: {}".format(desc, res))


class TextFileAnalyser(__Analyser):
    def analyse(self, file):
        with open(file, 'r') as data:
            super()._analyse(data)
