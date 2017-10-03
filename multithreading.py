# Sudoku Solver, CPSC380 Project 1
# Dylan Bowman, 2250585, bowma128@mail.chapman.edu
# 
# Multithreading.py
# Handles the multithreading portion of the check function.
 
import threading

class ReturningThread(threading.Thread):
	def __init__(self,target, args):
		threading.Thread.__init__(self)
		self.target = target
		self.args = args
		self._return = [0]
	def run(self):
		ThreadedFunction(self.target, self.args, self._return);
	def getReturnValue(self):
		return self._return[0]


def ThreadedFunction(target, args, returnPoint):
	returnPoint[0] = target(*args)


if __name__ == "__main__":
	def func(n, tdName):
		for i in range(n):
			print(tdName+" " +str(i))
		return n
	t1 = ReturningThread(target=func, args=[5,"t1"])
	t2 = ReturningThread(target=func, args=[7, "t2"])
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("return: "+str(t1.getReturnValue()))
	print("return: "+str(t2.getReturnValue()))