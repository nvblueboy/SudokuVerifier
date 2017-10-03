# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# SegmentChecker.py
# Contains a function that can check a Sudoku object for correctness.

class SegmentResult():
	def __init__(self,failure,locations=[],missing=set()):
		self.failure = failure
		self.locations = locations
		self.missing = missing
	def isFailure():
		return self.failure
	def __str__(self):
		string = "Segment Result: \n Failure: " +str(self.failure)
		if self.failure:
			string += "\nDuplicate locations: " + " ".join(["("+str(i)+","+str(j)+")" for (i, j) in self.locations])
			string += "\nMissing numbers: " + " ".join([str(i) for i in self.missing])
		return string


def checkSegments(segments):
	#Given a list of dictionaries, generate a SegmentResult to describe if that segment is passing or not.
	result = SegmentResult(False)
	for segment in segments:
		reverse = {i:[] for i in range(1,10)}
		for k in segment.keys():
			reverse[segment[k]].append(k)
		for k in reverse.keys():
			if len(reverse[k]) != 1:
				result.failure=True
				if len(reverse[k]) == 0:
					result.missing.add(k)
				else:
					result.locations = result.locations + reverse[k]
	return result