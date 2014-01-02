def main(debug):
    from sudoku import Sudoku

    solved = [
    [2,4,8,3,9,5,7,1,6],
    [5,7,1,6,2,8,3,4,9],
    [9,3,6,7,4,1,5,8,2],
    [6,8,2,5,3,9,1,7,4],
    [3,5,9,1,7,4,6,2,8],
    [7,1,4,8,6,2,9,5,3],
    [8,6,3,4,1,7,9,2,5],
    [1,9,5,2,8,6,4,3,7],
    [4,2,7,9,5,3,8,6,1]]

    unsolved = [
    [0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5],
    [6,6,6,6,6,6,6,6,6],
    [7,7,7,7,7,7,7,7,7],
    [8,8,8,8,8,8,8,8,8]]

    sudoku = Sudoku(solved)
    unsolvedSudoku = Sudoku(unsolved)


    if debug: print 'test getRow'
    for i in range(9):
        try: 
            assert(solved[i] == sudoku.getRow(i))
        except: 
            if debug: print 'ERROR----->r:', solved[i], '\tmethod:', sudoku.getRow(i); exit()
        
    for i in range(9):
        try:    
            assert(unsolved[i] == unsolvedSudoku.getRow(i))
        except: 
            if debug: print 'ERROR----->r:', unsolved[i], '\tmethod:', unsolvedSudoku.getRow(i); exit()
    if debug: print 'passed getRow\n'

    if debug: print 'test getColumn'
    for i in range(9):
        columns = []
        for x in range(9):
            columns.append(solved[x][i])
        try: 
            assert(columns == sudoku.getColumn(i))
        except: 
            if debug: print 'ERROR----->c:', columns, '\tmethod:', sudoku.getColumn(i); exit()
        
    for i in range(9):
        columns = []
        for x in range(9):
            columns.append(unsolved[x][i])
        try: 
            assert(columns == unsolvedSudoku.getColumn(i))
        except: 
            if debug: print 'ERROR----->c:', columns, '\tmethod:', unsolvedSudoku.getColumn(i); exit()
    if debug: print 'passed getColumn\n'

    #-----------------------------------------------------------------------------------------
    if debug: print 'test countMissing'
    try: 
        assert(0 == sudoku.countMissing())
    except: 
        if debug: print 'ERROR----->m:', 0, '\tmethod:', sudoku.countMissing(); exit()

    try: 
        assert(9 == unsolvedSudoku.countMissing())
    except: 
        if debug: print 'ERROR----->m:', 9, '\tmethod:', unsolvedSudoku.countMissing(); exit()
    if debug: print 'passed countMissing\n'

    #-----------------------------------------------------------------------------------------

    if debug: print 'test countMissing row'
    try: 
        assert(0 == sudoku.countMissing(row = 0))
    except: 
        if debug: print 'ERROR----->m:', 0, '\tmethod:', sudoku.countMissing(row = 0); exit()

    try: 
        assert(9 == unsolvedSudoku.countMissing(row = 0))
    except: 
        if debug: print 'ERROR----->m:', 9, '\tmethod:', unsolvedSudoku.countMissing(row = 0); exit()
    if debug: print 'passed countMissing row\n'

    #-----------------------------------------------------------------------------------------

    if debug: print 'test countMissing column'
    try: 
        assert(0 == sudoku.countMissing(column = 0))
    except: 
        if debug: print 'ERROR----->m:', 0, '\tmethod:', sudoku.countMissing(column = 0); exit()

    try: 
        assert(1 == unsolvedSudoku.countMissing(column = 0))
    except: 
        if debug: print 'ERROR----->m:', 1, '\tmethod:', unsolvedSudoku.countMissing(column = 0); exit()
    if debug: print 'passed countMissing column\n'

    #-----------------------------------------------------------------------------------------

    if debug: print 'test willConflict'
    for row in range(9):
        for column in range(9):
            try: 
                assert(True == sudoku.willConflict(solved[row][column], row, column))
            except: 
                if debug: print 'ERROR----->C:', True, '\tmethod:', sudoku.willConflict(solved[row][column], (row, column)); exit()
    if debug: print 'passed willConflict\n'

    if debug: print sudoku.toString(), '\n'
    if debug: print unsolvedSudoku.toString()

    #test each square
    if debug: print 'test getSquare'
    assert([2,4,8,5,7,1,9,3,6] == sudoku.getSquare(1,0))
    assert([3,9,5,6,2,8,7,4,1] == sudoku.getSquare(1,4))
    assert([7,1,6,3,4,9,5,8,2] == sudoku.getSquare(1,8))
    assert([6,8,2,3,5,9,7,1,4] == sudoku.getSquare(5,0))
    assert([5,3,9,1,7,4,8,6,2] == sudoku.getSquare(5,4))
    assert([1,7,4,6,2,8,9,5,3] == sudoku.getSquare(5,8))
    assert([8,6,3,1,9,5,4,2,7] == sudoku.getSquare(7,0))
    assert([4,1,7,2,8,6,9,5,3] == sudoku.getSquare(7,4))
    assert([9,2,5,4,3,7,8,6,1] == sudoku.getSquare(7,8))
    if debug: print 'passed getSquare\n'
    
    #-----------------------------------------------------------------------------------------
    
    if debug: print 'test resolveAllPossibilities'
    
    #check to make sure all possibilities are default value
    for row in range(9):
        for column in range(9):
            assert(sudoku.matrix[row][column].possibleNumbers == [1,2,3,4,5,6,7,8,9])
            
    if debug: print '\tall possibleNumbers initialized correctly'
    
    #resolve solved board
    sudoku.resolveAllPossibilities()
    for row in range(9):
        for column in range(9):
            assert(sudoku.matrix[row][column].possibleNumbers == [])
            
    if debug: print '\tall possible numbers resolved correctly in solved sudoku'
            
    #resolve unsolved board
    unsolvedSudoku.resolveAllPossibilities()
    for row in range(9):
        for column in range(9):
            assert(unsolvedSudoku.matrix[row][column].possibleNumbers == [9])
    
    if debug: print '\tall possible numbers resolved correctly in unsolved sudoku'
    
    if debug: print 'passed resolveAllPossibilities\n'
    
if __name__ == '__main__':
    import sys
    debug = False
    try: 
        if sys.argv[1] == 'DEBUG': debug = True
    except: pass
    main(debug)