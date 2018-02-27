# Import class
from analyser import TextFileAnalyser

# Setup analyser
analyser = TextFileAnalyser()

# Run analysis and gather results
analyser.analyse('file.txt')

# display statistics results
analyser.print_statistics()
