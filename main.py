# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# main.py
# Holds the main function.

import SegmentChecker, Sudoku, multithreading, Checking

def main():
	filename="testDataPassing.txt"
	s = Sudoku.readFile(filename)
	print(Checking.check(s))


if __name__ == "__main__":
	main()