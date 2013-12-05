'''
Author: Andy Shaw
Date:   12/5/2013

This class represents a sudoku.  The internal state will be a 2-dimensional array.
0's (zeros) are unresolved numbers.
'''

class Sudoku:
    '''Sudoku class'''
    def __init__(self, matrix):
        self.matrix = matrix
        
    def getRow(self, rowIndex):
        '''get the row provided by the index'''
        return self.matrix[rowIndex]
        
    def getColumn(self, columnIndex):
        '''get the column provided by the index'''
        x = []
        for row in self.matrix:
            x.append(row[columnIndex])
        return x

    def countMissing(self):
        '''return number of 0's in sudoku'''
        count = 0
        for x in self.matrix:
            for y in x:
                if y == 0:
                    count += 1
        return count
        
    def toString(self):
        rowLen = 29
        s = ''
        #top line
        s += '='*(rowLen) + '\n'
        for row in range(9):
            s += '||'
            
            for column in range(9):
                if (column+1) % 3 == 0:s += str(self.matrix[row][column]) + '||'
                else:s += str(self.matrix[row][column]) + '  '
                
            if (row+1) % 3 == 0: s += '\n' + '='*(rowLen) + '\n'
            else: s += '\n' + '-'*(rowLen) + '\n'
        
        return s
        
    def getSquare(self, x, y):
        '''return a 1-dimensional array containing the 3x3 square that contains the element at x,y'''
        s = []
        if 0 <= x < 3:
            if 0 <= y < 3:
                for i in range(3):
                    for j in range(3):
                        s.append(self.matrix[i][j])
            elif 3 <= y < 6:
                for i in range(3,6):
                    for j in range(3):
                        s.append(self.matrix[i][j])
            elif 6 <= y < 9:
                for i in range(6,9):
                    for j in range(3):
                        s.append(self.matrix[i][j])
                        
        elif 3 <= x < 6:
            if 0 <= y < 3:
                for i in range(3):
                    for j in range(3,6):
                        s.append(self.matrix[i][j])
            elif 3 <= y < 6:
                for i in range(3,6):
                    for j in range(3,6):
                        s.append(self.matrix[i][j])
            elif 6 <= y < 9:
                for i in range(6,9):
                    for j in range(3,6):
                        s.append(self.matrix[i][j])
                        
        elif 6 <= x < 9:
            if 0 <= y < 3:
                for i in range(3):
                    for j in range(6,9):
                        s.append(self.matrix[i][j])
            elif 3 <= y < 6:
                for i in range(3,6):
                    for j in range(6,9):
                        s.append(self.matrix[i][j])
            elif 6 <= y < 9:
                for i in range(6,9):
                    for j in range(6,9):
                        s.append(self.matrix[i][j])
        return s