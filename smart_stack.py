"""
__author__: Jared Langenauer
__challenge__: http://www.reddit.com/r/dailyprogrammer/comments/2j5929/10132014_challenge_184_easy_smart_stack_list/
"""

class Node:
	""" Nodes used in List """
	def __init__(self, data):
		self.next = None
		self.prev = None
		self.data = data

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

class Stack: 
	""" The Stack itself """
	def __init__(self):
		""" Initialize a first node with data = 0 """
		self.order = []
		self.top = None
		self.size = 0

	def Push(self, data):
		new_node = Node(data)
		self.order.append(data)
		if self.top == None: 
			self.top = new_node
			self.top.next = None
			self.top.prev = None
		else:
			self.top.next = new_node
			new_node.prev = self.top
			self.top = new_node
		self.size += 1
		print "Pushed: " + str(new_node.data)

	def Pop(self):
		self.order.remove(self.top.data)

		self.top = self.top.prev
		self.top.next = None
		self.size -= 1

	def getSize(self):
		print self.size

	def removeGreater(self, number):
		while top.data > number:
			Pop()

	def displayStack(self):
		print "Displaying Stack:"
		ptr = self.top
		while ptr != None:
			print ptr.data
			ptr = ptr.prev	


	def displayOrder(self):
		self.order.sort()
		print self.order

def main():
	print "Push 5 and 3\n"
	stack = Stack()
	stack.Push(5)
	stack.Push(3)
	print "Size\n"
	stack.getSize()
	print "Push 20\n"
	stack.Push(20)
	#stack.Push(15)
	print "Size\n"
	stack.getSize()
	print "Pop 20\n"
	stack.Pop()
	print "Size\n"
	stack.getSize()
	print "DisplayStack"
	stack.displayStack()
	print "Dispaly Order"
	stack.displayOrder()

if __name__ == "__main__":
	main()
