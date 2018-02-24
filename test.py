# Import classes from your brand new package
from analyser.TextFileAnalyser import TextFileAnalyser
from analyser.WordCountStatistic import WordCountStatistic
from analyser.LineCountStatistic import LineCountStatistic

# Setup statistics to gather
statistics = [WordCountStatistic(), LineCountStatistic()]

# Setup analyser
analyser = TextFileAnalyser(statistics)

# Setup data handler
data = open('file.txt', 'r')

# Run analysis and gather results
analyser.analyse(data)

# display statistics results
analyser.print_statistics()