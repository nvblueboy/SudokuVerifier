# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Multithreading.py
# Handles the multithreading portion of the check function.

import SegmentChecker, Sudoku, multithreading

def main():
	filename="rowsCols.txt"
	s = Sudoku.readFile(filename)
	print(check(s))


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

	print("row_t" + str(row_t.getReturnValue()))
	print("col_t" + str(col_t.getReturnValue()))
	print("box_t" + str(box_t.getReturnValue()))

if __name__ == "__main__":
	main()