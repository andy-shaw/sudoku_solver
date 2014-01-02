'''
Author: Andy Shaw
Date:   12/6/2013

This program will generate a solved sudoku, and output to a file if specified
'''

from sudoku import Sudoku

emptyCharacters = [' ', 0, '-', '_']

def parseBoard(data):
    grid = []
    for line in data:
        row = []
        
        #remove empty lines from parsing
        if len(line) is 1: continue
        
        #if it is a number or a white space add it to the row
        for ch in line.split():
            if ch in '1234567890': 
                row.append(int(ch))
            elif ch in emptyCharacters:
                row.append('-')
            
        #check if length is good
        if len(row) is not 9: raise Exception('incorrect sudoku format in provided file')
        
        grid.append(row)
    
    #check if sudoku has proper amount of rows
    if len(grid) is not 9: raise Exception('incorrect sudoku format in provided file')
    
    return (Sudoku(grid))

def solver(sudoku):
    i = 0

    while sudoku.countMissing() and i < 100:
        i += 1
    
        for row in range(9):
            for column in range(9):
                if len(sudoku.matrix[row][column].possibleNumbers) > 0:
                    print row, column, '\t', sudoku.matrix[row][column].possibleNumbers
        
        sudoku.solveSingles()
        sudoku.resolveAllPossibilities()
        
        x = raw_input()
        
        print sudoku.toString()
    
    
if __name__ == '__main__':
    import sys

    #attempt to open file
    try:
        input = sys.argv[1]
        file = open(input, 'r')
    except:
        print 'invalid file name: could not open file'
        exit()
    
    data = file.readlines()
    file.close()
    sudoku = parseBoard(data)
    print sudoku.toString()
    
    solver(sudoku)