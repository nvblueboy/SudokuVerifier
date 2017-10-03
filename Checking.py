# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Checking.py
# Holds the function used to check if a solution is correct (with multithreading)
# 

import Sudoku, multithreading, SegmentChecker

def check(s):
	rows = s.getRows()
	cols = s.getColumns()
	boxes = s.getBoxes()
	row_t = multithreading.ReturningThread(target=SegmentChecker.checkSegments, args=[rows])
	col_t = multithreading.ReturningThread(target=SegmentChecker.checkSegments, args=[cols])
	box_t = multithreading.ReturningThread(target=SegmentChecker.checkSegments, args=[boxes])
	row_t.start()
	col_t.start()
	box_t.start()

	row_t.join()
	col_t.join()
	box_t.join()

	row_failed = row_t.getReturnValue().failure
	col_failed = col_t.getReturnValue().failure
	box_failed = box_t.getReturnValue().failure

	if row_failed or col_failed or box_failed:			
		print("row_t:\n" + str(row_t.getReturnValue()))
		print("col_t:\n" + str(col_t.getReturnValue()))
		print("box_t:\n" + str(box_t.getReturnValue()))
		return [i.getReturnValue() for i in [row_t, col_t, box_t]] ##Return all Segment Results.
	else:
		return True