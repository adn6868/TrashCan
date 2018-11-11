import sys
import math
class Output:
	def __init__(self):
		self.o = sys.stdout
	def write( self, aline ):
		self.o.write(str(aline))
	def writeln(self, aline):
		self.o.write(str(aline) + '\n')

class Input:
	def __init__( self ):
		self.i = sys.stdin
	def readline( self ):
		return self.i.readline()
	def readInt( self ):
		return int ( self.i.readline())
	def readFlt( self ):
		return float(self.i.readline())
	def readToList(self,splitter = " "):
		return list(self.i.readline().strip('\n').split(splitter))
	def readToIntList(self,splitter = " "):
		return list(map(int, self.i.readline().strip('\n').split(splitter)))
	def readToFltList(self,splitter = " "):
		return list(map(float, self.i.readline().strip('\n').split(splitter)))

class Error:
	def __init__(self):
		self.e = sys.stderr
	def write( self, aline ):
		self.e.write(str(aline))
	def writeln(self, aline):
		self.e.write(str(aline) + '\n')

def solve1(X,A,B):
	'''
	write your code here
	'''
	E.writeln((B[0]- A[0]+X[1]))
	dientic = abs((B[0]-A[0])*(X[1]-A[1]) - (X[0]-A[0])*(B[1]-A[1]))
	k = math.sqrt((A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1]))
	# E.writeln([dis(X,(0,A[1])), dis(X,(A[0],0)), dis(X,(0,B[1])), dis(X,(B[0],0))])
	# E.writeln(dis( (1,1), (1 ,0)))
	# return min( abs(X[0] - A[0]) ,  abs(X[1] - A[1]) , abs(X[0] - B[0]) , abs(X[1] - B[1]))
	return dientic / k


def solve(X,A,B):
	C = (A[0],B[1])
	D = (B[0],A[1])
	ad = solve1(X,A,D)
	bd = solve1(X,B,D)
	cb = solve1(X,C,B)
	ac = solve1(X,A,C)
	E.writeln(X)
	E.writeln(B)
	E.writeln(D)
	
	E.write([ad,bd,cb,ac])
	return min (ad, bd,cb,ac)


def dis(A,B):
	return math.sqrt((A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1]))

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()
	line= I.readToIntList()
	X = (line[0],line[1])
	A = (line[2],line[3])
	B = (line[4],line[5])
	# E.writeln((B))
	O.write(solve(X,A,B))