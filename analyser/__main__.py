from analyser.TextFileAnalyser import *
from analyser.Statistic import *
import argparse


parser = argparse.ArgumentParser(description='Analyse text file and produce statistics.')
parser.add_argument('file', type=str, help='path of text file to analyse')

args = parser.parse_args()

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
