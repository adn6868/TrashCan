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
		return float(self.i.readline().strip('\n'))
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

def solve(n,t):
	'''
	write your code here
	'''
	n = sorted(n)
	i = 0
	j = len(n) - 1
	cur = n[i] + n[j]
	while cur != t:
		cur = n[i] + n[j]
		if cur < t:
			i +=1
		if cur > t:
			j -= 1
	return cur

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	query = I.readInt()
	for i in range(query):
		O.writeln(solve(I.readToIntList()),I.readInt())
