class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self, x):
		# super(LinkedList, self).__i nit__()
		self.val = x
		self.next = None
	def addLast(self,aNode):
		cur = self
		while cur.next:
			cur = cur.next
		cur.next = aNode

	def add(self,aNumb):
		newNode = LinkedList(aNumb)
		self.addLast(newNode)

	def toString(self):
		ans = ''
		cur = self
		while cur.next:
			ans += str(cur.val) +'->'
			cur = cur.next
		return ans

def main():
	a = LinkedList(2)
	b = LinkedList(3)
	c = LinkedList(4)
	a.addLast(b)
	a.addLast(c)
	a.add(11)
	a.add(12)
	a.add(9)
	print(a.toString())

if __name__ == '__main__':
	main()