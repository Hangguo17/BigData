#Jerdon Helgeson
#import from csv 1

from collections import namedtuple
import csv

#will be using a namedTuple as an object to hold each line of the csv we read in
# tuple > dict because immutable and clean
#namedtuple data can be accessed by indexing: tR[0] OR by attribute name: tR.name

#TODO: WILL NOT BE USING NAMED TUPLE AS THE FORMAT CAN'T BE RETURNED FROM A FUNCTION
# &&& NAMEDTUPLES CAN'T HAVE DYNAMICALLY UPDATED ELEMENTS
#WILL INSTEAD USE A LISTLIST OR NESTDLIST
#MUST UPDATE IMPORTER AND RECORD BUILDER F(X)'s 

######TESTER CODE#######
TestRecord = namedtuple('TestRecord', ['name', 'age', 'ID','other'])
tR = TestRecord("Jerdon",22,1234,"I like long walks on the beach and pina coladas")

def testNamedTuple(tR):
    return 0
    

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
        record = build_record(row1)
    return record


def build_record(row1):
    #this will create an arbitrary namedtuple(struct) based on the first line of the csv
    #can return an arbitrary namedtuple structure
    #the named tuple has to be a global
    l = ''
    for col in row1:
        col = removeWhitespace(col)
        if l == '':
            l = col
        else:
            l = l + ', ' + col
    print(l)
    record = namedtuple('record',l)
    return record 


def removeWhitespace(string):
    return ''.join(string.split())

def numRows(fn):
    return 0

def create_grid(r):
    x = 0
    grid = []
    grid.append(r)
    while(x < 10):
        row = record()
        for i in r:
            row[i] = "myNameIsJeff"
        x = x+1
        
    return 0








    
#if __name__ == "__main__":
def main():
    file_name = 'CDHC.csv'
    r = importer(file_name)
    bbb[0] = 66    
    print(bbb)
