class Stack:
	"implementarea unei stive"
	def __init__(self):
		self.items = []
	def push(self, x):
		self.items.append(x)
	def pop(self):
		x = self.items[-1]
		del self.items[-1]
		return x
	def empty(self):
		return len(self.items) == 0

x = Stack()
print x.empty()
x.push(1)
print x.empty()
x.push("hello")
print x.pop()
