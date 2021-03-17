# Version 1.1
from numpy import genfromtxt

puzzle = []

def PossibleValueAtPosition(row:int, col:int):		# possible value at (row, col)
	r=row//3*3
	c=col//3*3
	return {1,2,3,4,5,6,7,8,9}.difference(set(puzzle[r:r+3,c:c+3].flat)).difference(set(puzzle[row,:])).difference(set(puzzle[:,col]))

def SudokuSolver(n:int):
	if n==81:										# if end of list, problem solved
		return True
	(row,col) = divmod(n,9)
	if puzzle[row][col]>0:							# location filled, try next location
		if SudokuSolver(n+1)==True:
			return True								# if not return even true, will show all solutions
	else:
		l = PossibleValueAtPosition(row,col)
		for v in l:									# if l = empty set, bypass all 
			puzzle[row][col] = v					# try to fill a possible value v  
			if SudokuSolver(n+1)==True:
				return True							# if not return even true, will show all solutions
			puzzle[row][col] = 0					# unfill the value, blacktracking
	return False									# try all possible but fail

def main():
	global puzzle
	puzzle = genfromtxt('sudoku.csv', delimiter=',', dtype=int)
	print(puzzle)
	print()
	
	if SudokuSolver(0)==True:
		print(puzzle)
	else:
		print("No solution!")
	print()

if __name__ == "__main__":
	main()
