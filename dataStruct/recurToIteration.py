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
		return list(self.i.readline().split(splitter))
	def readToIntList(self,splitter = " "):
		return list(map(int, self.i.readline().split(splitter)))
	def readToFltList(self,splitter = " "):
		return list(map(float, self.i.readline().split(splitter)))

class Error:
	def __init__(self):
		self.e = sys.stderr
	def write( self, aline ):
		self.e.write(str(aline))
	def writeln(self, aline):
		self.e.write(str(aline) + '\n')

class Stack:
	def __init__(self):
		self.s = []
	def put(self,a):
		self.s.append(a)
	def pop(self):
		if self.size() != 0:
			return self.s.pop(0)
	def empty(self):
		return len(self.s) == 0
	def size(self):
		return len(self.s)
	def toString(self):
		return "Stack size " + str(self.size()) +": \n" + str(self.s) 


def recurFib(n):
	if n <= 2:
		return 1
	else:
		return recurFib(n-1) + recurFib(n-2)

def interativeFib(n):
	'''
	this have the same complexity with the recursion one
	but save a lot of space on the call stack of compiler
	'''
	s = Stack()
	s.put(n)
	ans = 0
	while not s.empty():
		cur = s.pop()
		if cur <= 2:
			ans+= 1
		else:
			s.put(cur-1)
			s.put(cur-2)
	return ans

def dynamicFib(n):
	l = [None]*n
	i = 2;
	l[0] = 1
	l[1] = 1

	while i < n:
		l[i]= l[i-1] + l[i-2]
		i +=1
	return l[-1]


def solve(n):
	'''
	I hear any recursion can transform into iteration. by using a stack. let's see how it goes
	'''
	a = str(interativeFib(n))
	b = str(recurFib(n))
	c = str(dynamicFib(n))
	return "using recursion:" + b +'\n'+"using iteration:"+a +'\n'+"using dynamic: " + c
	# b = str(recurFib(n))
	# ans = "using recursion:" + b +'\n'+"using iteration:"+a



	return ans





if __name__ == '__main__':
	E = Error()
	I = Input()
	O = Output()

	query = I.readInt()
	for i in range(query):
		O.writeln(solve(I.readInt()))
