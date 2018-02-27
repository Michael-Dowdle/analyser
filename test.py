# Import classes from your brand new package
from analyser.TextFileAnalyser import TextFileAnalyser
from analyser.Statistic import *


# Setup statistics to gather
statistics = [WordCountStatistic(),
              LineCountStatistic(),
              AvgLettersPerWordStatistic(),
              MostCommonLetterStatistic()]

# Setup analyser
analyser = TextFileAnalyser(statistics)

# Setup data handler
with open('file.txt', 'r') as data:
    # Run analysis and gather results
    analyser.analyse(data)

    # display statistics results
    analyser.print_statistics()
