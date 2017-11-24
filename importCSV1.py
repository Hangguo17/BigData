#Jerdon Helgeson
#import from csv 1

from collections import namedtuple
import csv


#WILL NOT BE USING NAMED TUPLE AS THE FORMAT CAN'T BE RETURNED FROM A FUNCTION
# &&& NAMEDTUPLES CAN'T HAVE DYNAMICALLY UPDATED ELEMENTS
#WILL INSTEAD USE A LISTLIST OR NESTDLIST
#MUST UPDATE IMPORTER AND RECORD BUILDER F(X)'s 

######TESTER CODE#######
TestRecord = namedtuple('TestRecord', ['name', 'age', 'ID','other'])
tR = TestRecord("Jerdon",22,1234,"test string")

    

def import_print():
    with open('MPCI.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)
            break
########################










########EXECUTED CODE############

        
#importer is the container function for the rest of the smaller functions that import and parse the data
def importer(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') #gets the reader of rows from the csv
        for row in reader: #returns only the first row of the csv
            row1 = row
            break
        record = build_record2(row1)
        grid = build_grid(reader)
        print_grid(100,grid)
    return record 

def build_record2(row1):
    record = []
    for col in row1:
        col = removeWhitespace(col)
        record.append(col)
    return record


def removeWhitespace(string):
    return ''.join(string.split())

def numRows(reader):
    ctr = 0
    for row in reader:
        ctr = ctr+1
    return ctr

def build_grid(reader):
    x = 0
    grid = []
    for row in reader:
        grid.append(row)
        x = x+1
    return grid

def print_grid(num_rows, grid):
    x = 0
    for r in grid:
        print(r[1])
        if(x >= num_rows):
            break
        x = x+1


#####ASSOCIATION RULE CALCULATIONS#####


    
#if __name__ == "__main__":
def main():
    file_name = 'CDHC.csv'
    r = importer(file_name)
    
