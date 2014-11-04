# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 06:13:28 2014
 
@author: imbenzene
"""

#Imported Libraries
import sys, csv, time

# Cross-product and notations are borrowed from the Peter Norvig's Sudoku program <http://norvig.com/sudoku.html>
#5 Global Variables
rows     = 'ABCDEFGHI'
cols     = '123456789'
partSolved={} # dictionary for partially solved cells from input csv file
cells=[] 
neighbors={}

#Indexing individual cells in the Sudoku grid using a cross-product of rows & cols 
def cross_product(rows, cols):
    RxC=[]
    for r in rows:
        for c in cols:
            RxC.append(r+c)
    return RxC


# Read the input Sudoku csv matrix and return the values as a one line string
def readInputCSV(inputFile):
    reader = csv.reader(open(inputFile, "rb"))
    inputList =""
    for row in reader:
        for col in row:
            if col not in '0123456789': #Elements has to be digits from 0-9
                return 0
            inputList = inputList + col #add rows to the string (a unit row matrix)
    if len(inputList)!= 81: #Check for total number of cells
        return 0
    return inputList

#Create cells, units and neighbors using cells address notation
def parseInput(inputMatrix):
    cells  = cross_product(rows, cols)

    #For each element finding it neighbors= same row elements + same column elements + same 1x9 block
    foo = ([cross_product(rows, c) for c in cols] +
            [cross_product(r, cols) for r in rows] +
            [cross_product(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
    

    units = dict((s, [u for u in foo if s in u]) for s in cells)
    neighbors = dict((s, set(sum(units[s],[]))-set([s]))for s in cells)
    
    i=0
    for r in rows:
        for c in cols:
            partSolved[r+c]=inputMatrix[i]
            i = i +1
    return cells, neighbors, partSolved

#display original matrix
def printOriginal():
    i=0
    lt=[]
    for r in rows:
        for c in cols:
            i=i+1
            if i==9:
                lt.append(partSolved[r+c])
                print lt
                lt=[]
                i=0
            else:
                lt.append(partSolved[r+c])

#first pass to initiate blank rows/columns with '0-9' values
def initiate():
    possValues=[]
    for u in partSolved:
        if partSolved[u]=='0':
            partSolved[u]= '123456789' #Substituting with all possible values
            possValues.append(u)
    return possValues


#Recursive function: Runs recursively till it removes values which are redundant/contradictory
def solve(possValues, counter):
    if len(possValues)==0:
        return True
    
    for r in possValues: 
        if len(partSolved[r])>1: #cell is unsolved
            for p in neighbors[r]: #neighbor sanity check
                x = partSolved[p] #recalculate neighbor values
                if len(x)==1: #cell is solved
                    partSolved[r]=partSolved[r].replace(x,"") #possible value list is truncated
                
    new_possValues=[]
    partCounter=0

    for r in possValues:
        ln = len(partSolved[r])
        if ln>1:
            new_possValues.append(r)
            partCounter = partCounter + ln 

    if partCounter == counter: #deadlock
        return False

    if not new_possValues:
        return True
    else:
        solve(new_possValues, partCounter)


def printSolution(outputFile):
    i=0
    possValues=[] #temperary list for display purpose
    result=[] #list fot csv output file
    for r in rows:
        for c in cols:
            i=i+1
            if i==9:
                possValues.append(partSolved[r+c])
                print possValues
                result.append(possValues)
                possValues=[]
                i=0
            else:
                possValues.append(partSolved[r+c])
    #Saving the file as the second argument            
    with open(outputFile, "wb") as f:
        solMatrix = csv.writer(f, delimiter=',', lineterminator='\n')
        solMatrix = csv.writer(f)
        solMatrix.writerows(result)
    
if __name__ == "__main__":
    inputMatrix = readInputCSV(sys.argv[1])

    #Unit Testing done
    if inputMatrix==0:
        print "Input file is not in the correct format"
        sys.exit()

    #parsing the matrix cells
    cells, neighbors, partSolved = parseInput(inputMatrix)

    print "Original Sudoku Matrix"

    printOriginal()
    
    timestamp1 = time.time()
    possValues =initiate()
    counter=0 #initial counter - counter is to find the number of possible values in the possValues_list
    solve(possValues, counter)
    print "Solution Matrix"

    printSolution(sys.argv[2])
    timestamp2 = time.time()
    print "The recursive sudoku solving algorithm took %.6f seconds" % (timestamp2 - timestamp1)
