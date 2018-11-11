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
	# def readChar


class Error:
	def __init__(self):
		self.e = sys.stderr
	def write( self, aline ):
		self.e.write(str(aline))
	def writeln(self, aline):
		self.e.write(str(aline) + '\n')

def depthFirstSearch(graph,S,D):
	if S not in graph.keys() or D not in graph.keys():
		return False

def breathFirstSearch(graph,S,D):
	Q = [S]
	if S not in graph.keys() or D not in graph.keys():
		return False
	while len(Q) != 0:
		cur = Q.pop()
		neighbor = graph[cur]
		if D in neighbor:
			return True
		else:
			for n in neighbor:
				Q.append(n)
	return False


def solve(graph):
	'''
	write your code here
	'''
	return breathFirstSearch(graph,"A","C")

if __name__ == '__main__':
	O = Output()
	E = Error()
	I = Input()

	query = I.readInt()
	for i in range(query):
		nodeNum = I.readInt()
		nodeList = I.readToList()
		graph = {}
		for node in nodeList:
			graph[node] = I.readToList()
		O.writeln(solve(graph))
