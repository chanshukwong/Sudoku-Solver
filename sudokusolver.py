# Version 1.1
from numpy import genfromtxt

def PossibleValueAtPosition(pz:[], row:int, col:int):	# possible value at (row, col)
	r=row//3*3
	c=col//3*3
	return {1,2,3,4,5,6,7,8,9}.difference(set(pz[r:r+3,c:c+3].flat)).difference(set(pz[row,:])).difference(set(pz[:,col]))

def SudokuSolver(pz:[], n:int):
	if n==81:									# if end of list, problem solved
		return True
	(row,col) = divmod(n,9)
	if pz[row][col]>0:								# location filled, try next location
		return SudokuSolver(pz, n+1)
	else:
		l = PossibleValueAtPosition(pz, row,col)
		for v in l:								# if l = empty set, bypass all 
			pz[row][col] = v						# try to fill a possible value v  
			if SudokuSolver(pz, n+1)==True:
				return True						# if not return even true, will show all solutions
		pz[row][col] = 0							# unfill the value, blacktracking
	return False									# try all possible but fail

def main():
	puzzle = genfromtxt('sudoku.csv', delimiter=',', dtype=int)
	print(puzzle)
	print()
	
	if SudokuSolver(puzzle, 0)==True:
		print(puzzle)
	else:
		print("No solution!")
	print()

if __name__ == "__main__":
	main()
