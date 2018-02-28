import unittest
import analyser

# Setup analyser
tfa = analyser.TextFileAnalyser()

# Run analysis and gather results
tfa.analyse('file.txt')

# display statistics results
tfa.print_statistics()
