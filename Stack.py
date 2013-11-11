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

class FancyStack(Stack):
	"Posibilitatea de a inspecta elementele din stiva"
	def peek(self, n):
		"peek(0) returns top, peek(-1) returns the element below that; etc."
		size = len(self.items)
		assert 0 <= n < size
		return self.items[size-1-n]

class LimitedStack(FancyStack):
	"Fancy stack with limit on stack size"
	def __init__(self, limit):
		self.limit = limit
		FancyStack.__init__(self)
        def push(self, x):
		assert len(self.items) < self.limit
		FancyStack.push(self, x)


x = Stack()
print x.empty()
x.push(1)
print x.empty()
x.push("hello")
print x.pop()

print "-----------LimitedStack------------"
ls = LimitedStack(5)
print ls.empty()
ls.push(7)
print ls.empty()
ls.push(47)
print ls.pop()

