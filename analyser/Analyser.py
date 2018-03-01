"""Module for analysing data and capturing results."""
import logging

class Analyser:
    """Class for analysing data from arbitrary source."""

    def __init__(self, stats):
        """
        Initializer sets an empty dictionary attribute for results,
        and a list attribute of statistics to be captured.

        :param stats:   statistics to gather during analysis.
                        Must be a list of statistic objects,
                        with the following methods:
                            description() -> str: description
                            result() -> result
                            process_line(str: line)
                            calculate()
        """
        self.__results = {}
        self.__statistics = stats

    @property
    def results(self):
        """
        Property method for accessing private results attribute.

        :return:        a dictionary of statistic analysis results.
                            key     : stat description
                            value   : calculated result
        """
        return self.__results

    @staticmethod
    def __calculated_result(stat):
        """
        Static method to calculate statistic result and return it.

        :param stat:    statistic to calculate.
        :return:        result for statistic.
        """
        stat.calculate()
        return stat.result

    def _analyse(self, data):
        """
        Method for analysing data.

        Applies statistic analysis for each line of data,
        to each statistic type provided at initialization.

        Finally sets results attribute with each statistics
        description and calculated result.

        :param data:    data to be analysed.
        """
        logging.debug("analysing data")
        for line in data:
            for stat in self.__statistics:
                stat.process_line(line)

        logging.debug("calculating statistic results")
        self.__results = {stat.description: self.__calculated_result(stat)
                          for stat in self.__statistics}

    def print_results(self):
        """
        Method to print statistic description and results
        to the default set standard out using:
            print("{:<35s}: {}"

            left aligning each statistic description
            padding to 35 characters, and then the
            statistic result. e.g.
                <statistic description>            : <result>
        """
        logging.debug("printing statistic results")
        for desc, res in self.results.items():
            print("{:<35s}: {}".format(desc, res))


class TextFileAnalyser(Analyser):
    """Derived class for analysing text files."""

    def analyse(self, file):
        """
        Overloaded method for analysing data from text file.
        Opens text file with read permissions using with statement,
        and calling on the base class analyse, passing the data
        as an argument.

        :param file:    path of text file to open and analyse.
        """
        with open(file, 'r') as data:
            super()._analyse(data)
