#Jerdon Helgeson
#import from csv 1

from collections import namedtuple
from collections import Counter
import csv
import os.path



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

######### PARSING & PRINTING########        
#importer is the container function for the rest of the smaller functions that import and parse the data
def importer(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|') #gets the reader of rows from the csv
        for row in reader: #returns only the first row of the csv
            row1 = row
            break
        record = build_record2(row1)
        g_n_tup = build_grid(reader)

        grid = g_n_tup[0]
        numRows = g_n_tup[1]
        #print_grid(100,grid)
    return (grid, record, numRows)

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
    return (grid, x)

def print_grid(num_rows, grid):
    x = 0
    for r in grid:
        print(r[1])
        if(x >= num_rows):
            break
        x = x+1

def printCol(grid, record, numRows):
    x = 0
    colNum = get_column_num(record)
    for r in grid:
        print(r[colNum])
        if(x >= numRows):
            break
        x = x+1




########  User Inputs  #########



def get_input():
    print("Enter File Name: ")
    file_name = input()
    if(file_name == ''):
        file_name = 'CDHCB.csv'
    print("Enter minimum Support Threshold (return for default value): ")
    sup = input()
    if(sup == ''):
        sup = .25
    print("Enter minimum Confidence Threshold (return for default value): ")
    conf = input()
    if(conf == ''):
        sup = .5
    return (file_name,sup,conf)


def get_itemset(colTup,value):
    if(type(value) == tuple):
        if(len(value) == 1):
            return 0
        elif(len(value) == 2):
            return 0
    else: return -1

def get_column_num(record): #gets column number based on name provided by user
    print("Enter Column Name: ")
    colName = input()
    x = 0
    if(colName == ''):
        return 3
    for i in record:
        if(i == colName):
            return x
        x = x + 1
    return 0
    

def get_options():
    print("What do you want to calculate?")
    print("1 for Support, 2 for Confidence, 3 for Lift, 4 to exit")
    print("Enter choice here and return: ")
    option = input()
    if(option == ''):
        return 0
    if(option == '1'):
        return 1
    if(option == '2'):
        return 2
    if(option == '3'):
        return 3
    if(option == '4'):
        return 4
    else:
        return -1




#####ASSOCIATION RULE CALCULATIONS#####


        
def strictSupport(numItems, numRows):
    return numItems/numRows


def strictConfidence(numRule, numItem):
    return numRule/numItem




def calcSupport(itemset, numRows):
    x = 0
    for i in itemset:
        x = x+1
    return x/numRows

def calcConfidence(itemsetR,itemsetX):
    #itemsetR is rule: total rows that contain both X and Y: X->Y when X and Y are itemsets
    
    x = 0
    r = 0
    for i in itemsetX: #itemsetX represents total rows that contains X
        x = x + 1
    for i in itemsetR:
        r = r + 1
    return r/x

def lift():
    return 0





####### Outputs #######

def dictToString(key, value):
    return str(key)+':'+str(value)
    

def SingleSupportOut(grid, record, numRows): #creates a outdoc containing the support values of individual items in a column
    x = 0
    colNum = get_column_num(record)
    L = []  # this will be a list of tuples: each tuple will contain a state and the number of times it was refereced in the column
            #gotta build a list of values first then use collections counter to make a dictionary of the values
    for r in grid:
        L.append(r[colNum])
        if(x >= numRows):
            break
        x = x+1
    counter = Counter(L)
    fileName = str(record[colNum])+"SingleSupport.txt"
    file = open(fileName,'w')
    for i in counter:
        sup = strictSupport(counter[i],numRows)
        dts = dictToString(i,sup)
        file.write(dts+"\n")
    file.close()
    


############ Main Function ############    
#if __name__ == "__main__":
def main():
    usrV = get_input()#usrV is returned user values of file_name, min support, and min confidence at indexes 0,1,2 respectively 
    grnTup = importer(usrV[0]) #grnTup is a tuple that contains the grid, record, and numRow at indexes 0,1,and 2 respectively
    #SingleSupportOut(grnTup[0],grnTup[1],grnTup[2])
    quitter = False
    while(quitter == False):
        opt = get_options()
        if(opt == 4):
            quitter = True
   
    
