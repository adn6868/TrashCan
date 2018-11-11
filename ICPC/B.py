import sys

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
		return self.i.readline().strip('\n')
	def readInt( self ):
		return int ( self.i.readline().strip('\n'))
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

def solve(S,a,b):
	'''
	write your code here
	'''
	diff = 0
	maxx = len(a)
	for i in range(len(a)):
		if a[i] != b[i]:
			diff += 1
	if S + diff < maxx:
		return S + diff
	else:
		return abs(maxx - ( diff - (maxx - S)))

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	S = I.readInt()
	a = I.readline()
	b = I.readline()
	O.write(solve(S,a,b))