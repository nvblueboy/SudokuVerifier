# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Solver.py
# Holds the solver function.

def solve(s, results):
	##This is going to be a horrible brute force algorithm.
	##For now.
	print("Entering Solve function.")
	for result in results:
		if not result.failure:
			continue ## If that segment didn't fail, then don't worry about it.
		