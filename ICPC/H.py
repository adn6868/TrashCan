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


def good(a):
	b = list(str(a))
	if '0' in b:
		return False
	if len( list(set(b))) != len(b):
		return False
	for num in b:
		num = int(num)
		if a%num != 0:
			return False
	return True


def solve(n):
	'''
	write your code here
	'''
	a = int(n[0])
	b = int(n[1])
	ans = 0
	for i in range(a,b):
		if good(i):
			ans += 1
	return ans

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()
	O.writeln(solve(I.readToList()))
