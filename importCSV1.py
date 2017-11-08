#Jerdon Helgeson
#import from csv 1


TestRecord = namedtuple('Record', 'name, age, title, department, paygrade')

def testNamedTuple(tR):
    #as the name states... this will test the namedTuple

def import_print():
    import csv
    with open('MPCI.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)

def build_record:
    #this will create an arbitrary namedtuple(struct) based on the first line of the csv
    
    
def create_grid:
    

def main():
    import_print()
