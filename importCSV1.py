#Jerdon Helgeson
#import from csv 1

from collections import namedtuple

#will be using a namedTuple as an object to hold each line of the csv we read in
# tuple > dict because immutable and clean
#namedtuple data can be accessed by indexing: tR[0] OR by attribute name: tR.name

TestRecord = namedtuple('TestRecord', ['name', 'age', 'ID','other'])
tR = TestRecord("Jerdon",22,1234,"I like long walks on the beach and pina coladas")

def testNamedTuple(tR):
    #as the name states... this will test the namedTuple
    return 0
    

def import_print():
    import csv
    with open('MPCI.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)

def build_record():
    #this will create an arbitrary namedtuple(struct) based on the first line of the csv
    return 0
    
def create_grid():
    return 0
    
#if __name__ == "__main__":
def main():
    import_print()
