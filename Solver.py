# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Solver.py
# Holds the solver function.

import itertools, copy

import Checking

def solve(s, results):
	##This is going to be a horrible brute force algorithm.
	##For now.
	print("Entering Solve function.")
	for result in results:
		if not result.failure:
			continue ## If that segment didn't fail, then don't worry about it.
		current_s = copy.deepcopy(s)
		for poss in possibilities(result.locations, result.missing):
			for pt in poss:
				current_s.map[pt[0]] = pt[1]
			if Checking.check(current_s) == True:
				print("Solution: ")
				for pt in poss:
					loc = "("+str(pt[0][0]+1)+", "+str(pt[0][1]+1)+"): "+str(pt[1])
					print(loc)
				return current_s


def possibilities(locations, missing):
	l = [[(i, j) for j in missing] for i in locations]
	return [i for i in itertools.product(*l)]



if __name__ == "__main__":
	print(possibilities([(5,4),(1,2)],[5,2,3]))