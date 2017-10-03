# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# main.py
# Holds the main function.

import sys

import SegmentChecker, Sudoku, multithreading, Checking, Solver

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 "+sys.argv[0]+" <filename>")
		return
	filename=sys.argv[1]
	s = Sudoku.readFile(filename)
	status = Checking.check(s)
	if status != True:
		print(Solver.solve(s, status))
	else:
		print("That is a correct puzzle!")


if __name__ == "__main__":
	main()