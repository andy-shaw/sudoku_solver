from sudoku import Sudoku

s = [
[2,4,8,3,9,5,7,1,6],
[5,7,1,6,2,8,3,4,9],
[9,3,6,7,4,1,5,8,2],
[6,8,2,5,3,9,1,7,4],
[3,5,9,1,7,4,6,2,8],
[7,1,4,8,6,2,9,5,3],
[8,6,3,4,1,7,9,2,5],
[1,9,5,2,8,6,4,3,7],
[4,2,7,9,5,3,8,6,1]]

sudoku = Sudoku(s)

print 'test getRow'
for i in range(9):
    try: assert(s[i] == sudoku.getRow(i))
    except: print 'r:', s[i], 'method:', sudoku.getRow(i); exit()
print 'passed getRow\n'

print 'test getColumn'
for i in range(9):
    columns = []
    for x in range(9):
        columns.append(s[x][i])
    try: assert(columns == sudoku.getColumn(i))
    except: print 'c:', columns, '\t', 'method:', sudoku.getColumn(i); exit()
print 'passed getColumn\n'

print 'test countMissing'
try: assert(0 == sudoku.countMissing())
except: print 'm:', 9, 'method:', sudoku.CountMissing(); exit()
print 'passed countMissing\n'

print sudoku.toString()

print s[2][3], sudoku.getSquare(2,3)