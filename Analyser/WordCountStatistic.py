from analyser.StatisticABC import StatisticABC


class WordCountStatistic(StatisticABC):
    def __init__(self):
        self.wordCount = 0
        super().__init__()

    def process_line(self, line):
        self.wordCount += len(line.split())

    def calculate(self):
        self.result = self.wordCount
