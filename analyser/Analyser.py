from analyser.Statistic import *


class Analyser:
    """

    """
    # Setup statistics to gather
    STATS = [WordCountStatistic(),
             LineCountStatistic(),
             AvgLettersPerWordStatistic(),
             MostCommonLetterStatistic()]

    def __init__(self, stats=STATS):
        """

        :param stats:
        """
        self.__results = {}
        self.__statistics = stats

    @property
    def results(self):
        """

        :return:
        """
        return self.__results

    @staticmethod
    def __calculated_result(stat):
        """

        :param stat:
        :return:
        """
        stat.calculate()
        return stat.get_result()

    def _analyse(self, data):
        """

        :param data:
        :return:
        """
        for line in data:
            for stat in self.__statistics:
                stat.process_line(line)

        self.__results = {stat.description: self.__calculated_result(stat)
                          for stat in self.__statistics}

    def print_results(self):
        """

        :return:
        """
        for desc, res in self.results.items():
            print("{:<35s}: {}".format(desc, res))


class TextFileAnalyser(Analyser):
    """

    """
    def analyse(self, file):
        """

        :param file:
        :return:
        """
        with open(file, 'r') as data:
            super()._analyse(data)
