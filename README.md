# CSV Files Merger

Merges csv files according to timestamp column.
  - uses pandas lib
  - Reads 2 input csv files
  - Files timestamps donot have to be alined with each other:
     - file1 can start at time=12000.5 and file2 at time=15000. same with time finish
     - script selects only the overlap area and remove other entries.
     - timestams will be rounded to 0.1
     - all entries with no match from the other file on the same timestamp will be removed.

### Usage
```
$ python filesmerger.py inputFile-1.csv inputFile-2.csv outFile.csv
```
### Tech
The script uses few other projects and libraries:
* [Python] - One of the largest snakes in the world (wikipedia)
* [Pandas] - easy-to-use data structures and data analysis tools.

### Todos
 - Script to read files list instead of 2 files.
 - Option to specify files seperators (eg. "," "\t" "|" etc..)
 - Add property file for other configurations.

**Free scripts ? Hell Yeah!**

   [pandas]: <https://pandas.pydata.org/>
   [python]: <https://www.python.org/>
