# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# SegmentChecker.py
# Contains a function that can check a 2d list for correctness.

def checkSegments(segments):
	correct = True
	for segment in segments:
		d = {i:False for i in range(1,10)}
		for i in segment:
			d[i] = True
		if False in d.values():
			correct = False
	return correct