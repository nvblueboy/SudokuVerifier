# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Sudoku.py
# Contains the class to represent a Sudoku puzzle, and the file IO required to read it.

class Sudoku():
	def __init__(self):
		self.rows = [[str(j) + str(i) for i in range(9)] for j in range(9)]
	def __init__(self,rows):
		self.rows = rows
	def __str__(self):
		return "\n\n".join([" ".join([str(i) for i in row]) for row in self.rows])
	def getRows(self):
		return self.rows
	def getColumns(self):
		cols = []

		for col in range(9):
			l = []

			for row in range(9):
				l.append(self.rows[row][col])
			cols.append(l)

		return cols
	def getBoxes(self):
		boxes = []

		for b_x in range(3):
			for b_y in range(3):
				##Use a nested for loop to loop through the boxes.
				box = []

				for x in range(3):
					for y in range(3):
						##Loop through the inside of the box.
						box.append(self.rows[(b_y * 3) + y][(b_x * 3) + x])
				boxes.append(box)
				
		return boxes


def readFile(filename):
	fileHandle = open(filename, "r")
	lines = fileHandle.readlines()
	fileHandle.close()
	outList = []

	for line in lines:
		splitLine = line.replace(" ","").replace("\n","").split(",")
		outLine = []

		for entry in splitLine:
			try:
				outLine.append(int(entry))
			except:
				print("Cannot parse "+entry+" into a number.")
		outList.append(outLine)

	return Sudoku(outList)

if __name__ == "__main__":
	s = readFile("testData.txt")
	print(s)
	print(s.getColumns())
	print(s.getBoxes())