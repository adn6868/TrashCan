class Node:
	def __init__(self,data = None):
		self.data = data
		self.l = None
		self.r = None
	def isLeaf(self):
		return self.l == self.r == None
	def _addNode(self,newNode):
		if newNode.data <= self.data:
			if self.l == None:
				self.l = newNode
			else:
				self.l._addNode(newNode)
		else:
			if self.r == None:
				self.r = newNode
			else:
				self.r._addNode(newNode)
	def _toString(self):
		if self.isLeaf():
			return str(self.data)
		elif self.l == None:
			return '('+str(self.data)+':'+" " +','+self.r._toString()+')'
		elif self.r == None:
			return '('+str(self.data)+':'+self.l._toString()+','+" " +')'
		return '('+str(self.data)+':'+self.l._toString()+','+self.r._toString()+')'
class BST:
	def __init__(self,data = None):
		self.root = Node(data)
		self.size = 1

	def getSize(self):
		return self.size
	def empty(self):
		return self.size == 0
	
	def add(self,data):
		newNode = Node(data)
		self.root._addNode(newNode)
		self.size += 1
	def toString(self):
		return "tree size "+ str(self.size)+'\n'+self.root._toString()





