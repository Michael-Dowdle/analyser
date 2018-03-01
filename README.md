# Analyser
text file analyser for gathering statistics about data in a text file.

## Getting Started

There is no setup.py available for installing this package yet.
For now you can import the package by starting python3.6 whilst in the analyser directory
on the command line,  see example below:

-------------------
#> python3.6
>>> import analyser
-------------------

alternatively you can call the package directly from the command line to analyse a single
file, see example below:

---------------------------------------
#> python3.6 -m analyser <path to file>
---------------------------------------

### Prerequisites

This python package required python3.6

## Running the tests

All tests for the package can be ran from the command line in the analyser directory,
see below for example:

---------------------------------
#> python3.6 -m unittest discover
---------------------------------


## Documentation

All documentation can be found by using the built in python 'help' feature, see example:

-----------------------------------
#> python3.6
>>> import analyser
>>> help(analyser)
>>> help(analyser.TextFileAnalyser)
>>> help(analyser.Statistic)
-----------------------------------

If using the command line direct call to the package, you can use the --help or -h
argument to see the helper, see example:

---------------------------
#> python3.6 -m analyser -h
---------------------------