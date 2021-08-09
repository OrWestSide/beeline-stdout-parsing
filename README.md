# Beeline stdout Parsing

This project was developed in the context of the programming assignment
put by Agile Actors for the Backend Software Engineer in Python. It is a 
simple script that parses an output log file and returns the required metrics.
It was developed using Python 3. Only standard library modules have been
used, hence no `requirements.txt` file was supplied.

Without loss of generality, the script parses a single file that contains 
a single query metrics. Also, even though the instructions stated that it 
should parse the file in a single scan, for code readability, re-usability
and modularity, we extract each metric in different scans.

## Usage
The way to use this script is this:
```
> python3 src/main.py
```
You can supply input arguments that specify the path of the file to be read
and the path of the files that the output will be written to. To get help,
use this:
```
> python3 src/main.py -h
```

Author: Orestis Zekai<br>
OS: Ubuntu 18.04<br>
IDE: Pycharm 2021 Professional Edition
