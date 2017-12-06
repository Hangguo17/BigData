#Jerdon Helgeson
#import from csv 1


from collections import namedtuple
from collections import Counter
import csv
import os



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
    if(option == "Test"):
        cwd = os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        try: os.makedirs(dir_path+'\TESTDIR')   #I MADE A FOLDER
        except OSError: #IF FOLDER ALREADY EXISTS pass
            pass
        svPath = dir_path+'\TESTDIR'
        flPath = svPath+'\TESTFILE.txt'
        fileT = open(flPath, 'w')
        fileT.write('This is a test')
        fileT.close()
        #output = open(os.path.join(dir_path, 'TESTDIR'), 'wb')
    else:
        return -1

def get_support_option():
    looper = True
    while(looper):
        print("Enter: 1 for Single Support, 2 for All Support")
        opt = input()
        if(opt == ''):
            return 0
        if(opt == '1'):
            return 1
        if(opt == '2'):
            return 2
        



#####ASSOCIATION RULE CALCULATIONS#####


        
def strictSupport(numItems, numRows):
    return numItems/numRows


def strictConfidence(numRule, numItem):
    return numRule/numItem


def allRules(grid, record, numRows):
    #ALLRULES IS RETURNING SETS OF EXTREMELY SIMILAR DATA, I THINK IT IS HIGHLY UNLIKELY THAT MORE THAN A FEW ROWS WILL HAVE THE SAME NUMBER OF RULES... THE COUNTING MUST BE OFF SOMEHOW
    Rules = []
    rCounter = 0
    numRecords = 0
    for r in record:
        numRecords = numRecords + 1
    while(rCounter < numRecords - 1):
        R1 = record[rCounter]
        rCounter2 = rCounter + 1
        while(rCounter2 < numRecords):
            R2 = record[rCounter2]
            ruleCtr = 0
            for row in grid:
                if((row[rCounter] == '1')and(row[rCounter2] == '1')): #MISPLACED BRACKET lol
                   ruleCtr = ruleCtr+1
            Rules.append((R1,R2,ruleCtr))
            rCounter2 = rCounter2 + 1
        rCounter = rCounter + 1
    #Total 630 Rules
    #Rules = msort(Rules)
    Rules = mergeSortRules(Rules,0,(len(Rules)-1))
    return Rules






def mergeSortRules(Rules, low, high):
    if(low == high):
        return Rules
    if(low == high - 1):
        if(Rules[low][2] > Rules[high][2]): #must be switched
            temp = Rules[low]
            Rules[low] = Rules[high]
            Rules[high] = temp
        return Rules
    mid = 0
    if(low < high):
        mid = int((low+high)/2) #gotta cast it to an int so its a whole number that can be used to access data in a list
        Rules = mergeSortRules(Rules, low, mid)
        Rules = mergeSortRules(Rules, mid+1, high)
        Rules = mergeRules(Rules, low, mid, high)
    return Rules

def mergeRules(Rules, low, mid, high): #more than 2 rules per array to be merged
    l = low
    m = mid+1
    tempL = []
    while(l <= mid and m <= high):
        if(Rules[l][2] < Rules[m][2]): #insert to temp in current order
            tempL.append(Rules[l])
            l = l+1
        else: # rules either have the same value or the high index is lower
            tempL.append(Rules[m])
            m = m+1
    while(l <= mid): #insert remaining low values if any
        tempL.append(Rules[l])
        l = l+1
    while(m <= high): #insert remaining high values if any
        tempL.append(Rules[m])
        m = m+1
    l = low
    for t in tempL:
        Rules[l] = t
        l = l+1
    return Rules


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

def ruleToString(rule):
    return rule[0] + ', ' + rule[1]+ ', ' + str(rule[2])
    

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
    
def AllSupportOut(grid,record,numRows):
    rNum = 0
      # this will be a list of tuples: each tuple will contain a state and the number of times it was refereced in the column
    cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print(dir_path)
    try: os.makedirs(dir_path+'\AllSupport')   #I MADE A FOLDER
    except OSError: #IF FOLDER ALREADY EXISTS pass
        pass
    svPath = dir_path+'\AllSupport/'
    for r in record:
        L = []
        x = 0
        for g in grid:
            L.append(g[rNum])
            if(x >= numRows):
                break
            x = x+1
        counter = Counter(L)
        fileName = str(record[rNum])+"SingleSupport.txt"
        flPath = svPath+fileName
        file = open(flPath, 'w')
        for i in counter:
            sup = strictSupport(counter[i],numRows)
            dts = dictToString(i,sup)
            file.write(dts+"\n")
        file.close()
        rNum = rNum+1
    print('')
    print("Created Support Files For Each Data Type")
    print('')
    
def RulesOut(Rules):
    cwd = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try: os.makedirs(dir_path+'\AllRules')
    except OSError: #IF FOLDER ALREADY EXISTS pass
        pass
    svPath = dir_path+'\AllRules/'
    fileName = "Rules.txt"
    flPath = svPath + fileName
    file = open(flPath, 'w')
    r = len(Rules)-1
    while(r > 0):
        file.write(ruleToString(Rules[r])+"\n")
        r = r-1
    file.close()
    

########## Option Controller ###########

def optCont(opt, grnTup):
    if(opt == 1): #Support chosen
        sopt = get_support_option()
        if(sopt == 1):SingleSupportOut(grnTup[0],grnTup[1],grnTup[2])
        elif(sopt == 2 or sopt == 0): AllSupportOut(grnTup[0],grnTup[1],grnTup[2])
    if(opt == 2): #Confidence chosen
        Rules = allRules(grnTup[0],grnTup[1],grnTup[2])
        RulesOut(Rules)
    if(opt == 3): #Lift Chosen
        print("Lift Coming Soon")
    if(opt == 0):
        printCol(grnTup[0],grnTup[1],grnTup[2])

############ Main Function ############    

def main():
    usrV = get_input()#usrV is returned user values of file_name, min support, and min confidence at indexes 0,1,2 respectively 
    grnTup = importer(usrV[0]) #grnTup is a tuple that contains the grid, record, and numRow at indexes 0,1,and 2 respectively
    quitter = False
    while(quitter == False):
        opt = get_options()
        if(opt == 4):
            quitter = True
        elif(opt == -1):
            print('try again')
        else: optCont(opt, grnTup)
   
    
if __name__ == '__main__':
    main()
