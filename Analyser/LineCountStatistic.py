from analyser.StatisticABC import StatisticABC


class LineCountStatistic(StatisticABC):
    def __init__(self):
        self.lineCount = 0
        super().__init__()

    def process_line(self, *_):
        self.lineCount += 1

    def calculate(self):
        self.result = self.lineCount
