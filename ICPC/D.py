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

def solve(n):
	
	adict ={}
	for card in n:
		if card[0] not in adict.keys():
			adict[card[0]] = 1
		else:
			adict[card[0]] += 1
	maxx = 0
	for card in adict.keys():
		if maxx < adict[card]:
			maxx = adict[card]
	return maxx


	return n

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()
	O.writeln(solve(I.readToList()))
