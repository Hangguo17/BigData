#Jerdon Helgeson
#import from csv 1

from collections import namedtuple
import csv

#will be using a namedTuple as an object to hold each line of the csv we read in
# tuple > dict because immutable and clean
#namedtuple data can be accessed by indexing: tR[0] OR by attribute name: tR.name




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
    l = []
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


def create_grid():
    return 0


    
#if __name__ == "__main__":
def main():
    fn = 'MPCI.csv'
    r = importer(fn)
    print(r)
