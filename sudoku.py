'''
Author: Andy Shaw
Date:   12/5/2013

This class represents a sudoku.  The internal state will be a 2-dimensional array.
0's (zeros) are unresolved numbers.
'''

emptyCharacters = [' ', 0, '-', '_']

class Block:
    '''Block of each sudoku element'''
    def __init__(self, number=None):
        self.number = number
        self.possibleNumbers = [1,2,3,4,5,6,7,8,9]

class Sudoku:
    '''Sudoku class'''
    def __init__(self, matrix):
        #initialize matrix
        self.matrix = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []]
        for row in range(9):
            for column in range(9):
                self.matrix[row].append(Block(matrix[row][column]))

    def getRow(self, rowIndex):
        '''get the row provided by the index'''
        row = []
        for column in self.matrix[rowIndex]:
            row.append(column.number)
        return row
        
    def getColumn(self, columnIndex):
        '''get the column provided by the index'''
        column = []
        for row in self.matrix:
            column.append(row[columnIndex].number)
        return column

    def countMissing(self, row=None, column=None):
        '''return number of 0's in sudoku'''
        count = 0
        #if there's no row or column, get the whole sudoku
        if row is None and column is None:
            for x in self.matrix:
                for num in x:
                    if num.number in emptyCharacters:
                        count += 1
                        
        #if the column was provided, check that column
        elif row is None and column is not None:
            for num in self.getColumn(column):
                if num in emptyCharacters:
                    count += 1
                    
        #if the row was provided, check that row
        elif column is None and row is not None:
            for num in self.getRow(row):
                if num in emptyCharacters:
                    count += 1
        
        #if both the column and the row are provided, bad
        else: raise Exception('Row and Column should not be provided together')
        
        return count
        
    def willConflict(self, num, row, column):
        '''if you put num at coord (row, column), is there a conflict?'''
        
        #check row
        for x in self.getRow(row):
            if x is num: return True
        
        #check column
        for x in self.getColumn(column):
            if x is num: return True
        
        #check square
        for x in self.getSquare(row, column): 
            if x is num: return True
        
        #else no conflict
        return False
        
    def toString(self):
        s = ''
        for row in range(9):
            for column in range(9):
                if (column+1) % 3 == 0: s += str(self.matrix[row][column].number) + ' '
                else: s += str(self.matrix[row][column].number)
                
            if (row+1) % 3 == 0: s += '\n\n' 
            else: s += '\n'
        
        return s
        
    def getSquare(self, x, y):
        '''return a list containing the 3x3 square that contains the element at x,y'''
        s = []
        if 0 <= y < 3:
            if 0 <= x < 3:
                for i in range(3):
                    for j in range(3):
                        s.append(self.matrix[i][j].number)
            elif 3 <= x < 6:
                for i in range(3,6):
                    for j in range(3):
                        s.append(self.matrix[i][j].number)
            elif 6 <= x < 9:
                for i in range(6,9):
                    for j in range(3):
                        s.append(self.matrix[i][j].number)
                        
        elif 3 <= y < 6:
            if 0 <= x < 3:
                for i in range(3):
                    for j in range(3,6):
                        s.append(self.matrix[i][j].number)
            elif 3 <= x < 6:
                for i in range(3,6):
                    for j in range(3,6):
                        s.append(self.matrix[i][j].number)
            elif 6 <= x < 9:
                for i in range(6,9):
                    for j in range(3,6):
                        s.append(self.matrix[i][j].number)
                        
        elif 6 <= y < 9:
            if 0 <= x < 3:
                for i in range(3):
                    for j in range(6,9):
                        s.append(self.matrix[i][j].number)
            elif 3 <= x < 6:
                for i in range(3,6):
                    for j in range(6,9):
                        s.append(self.matrix[i][j].number)
            elif 6 <= x < 9:
                for i in range(6,9):
                    for j in range(6,9):
                        s.append(self.matrix[i][j].number)
        return s
        
    def resolveAllPossibilities(self):
        for row in range(9):
            for column in range(9):
                #verify that if a number has already been set, then there are no possibilities
                if not self.matrix[row][column].number in emptyCharacters:
                    self.matrix[row][column].possibleNumbers = []
            
                #remove everything that is in the row from possibilities
                for num in self.getRow(row):
                    try:
                        self.matrix[row][column].possibleNumbers.remove(num)
                    except:
                        #always want to remove, no matter what
                        pass
                        
                #remove everything that is in the column from possibilities
                for num in self.getColumn(column):
                    try:
                        self.matrix[row][column].possibleNumbers.remove(num)
                    except:
                        #always want to remove, no matter what
                        pass
                        
                #remove everything that is in the square from the possibilities
                #NOTE: This will do unnecessary calculations per square, change if time is issue
                for num in self.getSquare(row, column):
                    try:
                        self.matrix[row][column].possibleNumbers.remove(num)
                    except:
                        #always want to remove, no matter what
                        pass

    def solveSingles(self):
        for row in range(9):
            for column in range(9):
                if len(self.matrix[row][column].possibleNumbers) is 1:
                    if not self.willConflict(self.matrix[row][column].possibleNumbers[0], row, column):
                        self.matrix[row][column].number = self.matrix[row][column].possibleNumbers[0]