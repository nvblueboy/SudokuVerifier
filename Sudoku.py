# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Sudoku.py
# Contains the class to represent a Sudoku puzzle, and the file IO required to read it.

class Sudoku():
	def __init__(self):
		self.map = {(i,j):0 for i in range(9) for j in range(9)}
	def __init__(self,rows):
		##Create a dictionary from a list of lists: Row, then column.
		self.map = {(i,j):0 for i in range(9) for j in range(9)}
		for i in range(len(rows)):
			for j in range(len(rows[0])):
				self.map[(i,j)] = rows[i][j]
	def __str__(self):
		output = []
		for i in range(9):
			partial = []
			for j in range(9):
				partial.append(str(self.map[(i,j)])) 
			output.append("  ".join(partial))
		return "\n\n".join(output)
	def getRows(self):
		output = []
		for i in range(9):
			partial = {}
			for j in range(9):
				partial[(i,j)] = self.map[(i,j)]
			output.append(partial)
		return output
	def getColumns(self):
		output = []
		for j in range(9):
			partial = {}
			for i in range(9):
				partial[(i,j)] = self.map[(i,j)]
			output.append(partial)
		return output
	def getBoxes(self):
		boxes = []
		for b_x in range(3):
			for b_y in range(3):
				##Use a nested for loop to loop through the boxes.
				box = {}
				for x in range(3):
					for y in range(3):
						##Loop through the inside of the box.
						i = b_y * 3 + y
						j = b_x * 3 + x
						box[(i,j)] = self.map[(i,j)]
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
	import SegmentChecker
	s = readFile("rows.txt")
	print(s)
	print(s.getRows())
	print(s.getColumns())
	print(s.getBoxes())
	# print(SegmentChecker.checkSegments(s.getBoxes()))
	# print(SegmentChecker.checkSegments(s.getRows()))
	# print(SegmentChecker.checkSegments(s.getColumns()))