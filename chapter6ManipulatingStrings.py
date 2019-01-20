#Table Printer

'''Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column 
right-justified. Assume that all the inner lists will contain the same number of strings.

For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
apples    Alice   dogs
oranges   Bob     cats
cherries  Carol   moose
banana    David   goose'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    tableDataLength = []
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            tableDataLength.append(len(tableData[i][j]))

    #print(tableDataLength)
    maxLength = max(tableDataLength)
    #print(maxLength)
    justifyWith = maxLength + 2

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            print(tableData[i][j].rjust(justifyWith), end = '')
        print()

printTable(tableData)

