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
    except: print 'ERROR----->r:', s[i], '\tmethod:', sudoku.getRow(i); exit()
print 'passed getRow\n'

print 'test getColumn'
for i in range(9):
    columns = []
    for x in range(9):
        columns.append(s[x][i])
    try: assert(columns == sudoku.getColumn(i))
    except: print 'ERROR----->c:', columns, '\tmethod:', sudoku.getColumn(i); exit()
print 'passed getColumn\n'

print 'test countMissing'
try: assert(0 == sudoku.countMissing())
except: print 'ERROR----->m:', 9, '\tmethod:', sudoku.countMissing(); exit()
print 'passed countMissing\n'

print 'test willConflict'
for row in range(9):
    for column in range(9):
        try: assert(True == sudoku.willConflict(s[row][column], (row, column)))
        except: print 'ERROR----->C:', True, '\tmethod:', sudoku.willConflict(s[row][column], (row, column)); exit()
print 'passed willConflict\n'

print sudoku.toString()

#test each square
print 'test getSquare'
assert([2,4,8,5,7,1,9,3,6] == sudoku.getSquare(1,0))
assert([3,9,5,6,2,8,7,4,1] == sudoku.getSquare(1,4))
assert([7,1,6,3,4,9,5,8,2] == sudoku.getSquare(1,8))
assert([6,8,2,3,5,9,7,1,4] == sudoku.getSquare(5,0))
assert([5,3,9,1,7,4,8,6,2] == sudoku.getSquare(5,4))
assert([1,7,4,6,2,8,9,5,3] == sudoku.getSquare(5,8))
assert([8,6,3,1,9,5,4,2,7] == sudoku.getSquare(7,0))
assert([4,1,7,2,8,6,9,5,3] == sudoku.getSquare(7,4))
assert([9,2,5,4,3,7,8,6,1] == sudoku.getSquare(7,8))
print 'passed getSquare'