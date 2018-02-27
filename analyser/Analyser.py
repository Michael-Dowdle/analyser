class TextFileAnalyser:
    def __init__(self, statistics):
        self.__results = []
        self.__statistics = statistics

    def analyse(self, data):
        for line in data:
            for stat in self.__statistics:
                stat.process_line(line)

        for stat in self.__statistics:
            stat.calculate()
            self.__results.append(stat.get_result())

    def print_statistics(self):
        for result in self.__results:
            print(result)
