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
		while cur:
			ans += str(cur.val) +'->'
			cur = cur.next
		return ans

def main():
	a = LinkedList(1)
	a.add(2)
	a.add(3)
	a.add(4)
	a.add(5)
	print(a.toString())
	reverse_in_place(a)
def reverse_in_place(a):
	cur = a
	head = a
	nex = None
	prev = None
	while cur:
		nex = cur.next
		cur.next = prev
		prev = cur
		cur = nex
	a = prev
	print(a.toString())
if __name__ == '__main__':
	main()
