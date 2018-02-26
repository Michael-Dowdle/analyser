from abc import ABC, abstractmethod


class StatisticABC(ABC):
    def __init__(self):
        self.result = ""
        super().__init__()

    @abstractmethod
    def process_line(self, line):
        pass

    @abstractmethod
    def calculate(self):
        pass

    def get_result(self):
        return self.result
