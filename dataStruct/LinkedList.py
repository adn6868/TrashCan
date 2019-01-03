class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self, x):
		# super(LinkedList, self).__i nit__()
		self.val = x
		self.next = None
	def addLast(self,aNode): #O(n)
		cur = self
		while cur.next:
			cur = cur.next
		cur.next = aNode
 
	def add(self,aNumb): #O(n)
		newNode = LinkedList(aNumb)
		self.addLast(newNode)

	def toString(self): #O(n)
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
	a.add(3)
	a.add(2)
	a.add(1)
	print(a.toString())
	print (isPalidrome(a))

def reverse_in_place(a): #O(n)
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
	return a

def isPalidrome(a): #O(n)
	it1 = a
	it2 = a
	while it2.next: #O(n)
		it1 = it1.next
		it2 = it2.next.next
	it2 = a
	it1 = reverse_in_place(it1)
	print(it1.toString())
	print(it2.toString())
	while it2:  #O(n)
		if it2.val != it1.val:
			return False
		it2 = it2.next
		it1 = it1.next
	return True
if __name__ == '__main__':
	main()
