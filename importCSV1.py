#Jerdon Helgeson
#import from csv 1


def import_print():
    import csv
    with open('MPCI.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)

def main():
    import_print()
