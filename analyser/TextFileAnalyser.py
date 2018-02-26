class TextFileAnalyser:
    def __init__(self, statistics):
        self.results = []
        self.statistics = statistics

    def analyse(self, data):
        for line in data:
            for stat in self.statistics:
                stat.process_line(line)

        for stat in self.statistics:
            stat.calculate()
            self.results.append(stat.get_result())

    def print_statistics(self):
        print(self.results)
