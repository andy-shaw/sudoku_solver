'''
Author: Andy Shaw
Date:   12/6/2013

This program will generate a solved sudoku, and output to a file if specified
'''

import sudoku

def solver(toFile=None):
    #generate a sudoku using hill climbing
    
    
    
if __name__ == '__main__':
    import sys
    
    try:
        sys.argv[1] = filename
        file = open(filename, 'w')
    except:
        file = None
        print 'No valide file provided, so program will output to console.'
        
    solver(file)