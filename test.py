from analyser import *

# Setup statistics
stats = [WordCountStatistic(),
         LineCountStatistic(),
         AvgLettersPerWordStatistic(),
         MostCommonLetterStatistic()]

# Setup analyser
tfa = TextFileAnalyser(stats)

# Run analysis and gather results
tfa.analyse('file.txt')

# display statistics results
tfa.print_results()
