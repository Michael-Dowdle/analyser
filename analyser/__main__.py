from analyser import *
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
text_analyser = TextFileAnalyser(statistics)

# Run analysis and gather results
text_analyser.analyse(args.file)

# display statistics results
text_analyser.print_statistics()
