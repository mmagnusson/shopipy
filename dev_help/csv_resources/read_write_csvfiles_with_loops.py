import csv

def readDescriptions(filename):
  with open(filename) as file:
    map = {}
    for row in csv.reader(file, delimiter=','):
      map[row[0]] = row[1]
  return map

def addDescriptions(filename, descriptions):
  with open(filename) as file:
    newRows = []
    for row in csv.reader(file, delimiter=','):
      key = row[0]
      description = descriptions[key]
      newRow = []
      newRow.append(row[0])
      newRow.append(description)
      newRow += row[1:]
      newRows.append(newRow)
    return newRows

def writeProcessed(filename, lines):
  with open(filename, 'wb') as file:
    csv.writer(file, delimiter=',').writerows(lines)

descriptions = readDescriptions('master.csv')
newLines = addDescriptions('file1.csv', descriptions)
writeProcessed('file1_out.csv', newLines);

# read the new file to make sure it worked
with open('file1_out.csv') as file:
  print('\n'.join([', '.join(row) for row in csv.reader(file, delimiter=',')]))

# references
# csv: https://docs.python.org/2/library/csv.html
# files: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# "with" statements: http://effbot.org/zone/python-with-statement.htm
# list comprehensions: https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# dictionary comprehensions: https://docs.python.org/2/tutorial/datastructures.html#dictionaries
# slicing: https://docs.python.org/2/tutorial/introduction.html#lists

#runnable -> http://runnable.com/U8ynra15Y-1MSHGq/read-and-write-csv-files-for-python