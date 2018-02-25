from analyser.StatisticABC import StatisticABC


class AvgLettersPerWordStatistic(StatisticABC):
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
