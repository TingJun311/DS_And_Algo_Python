class Stack:

  def __init__(self):
    self.arr = []
    self.length = 0
  
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[self.length - 1]

  def push(self,value):
    self.arr.append(value)
    self.length += 1

  def pop(self):
    popped_item = self.arr[self.length-1]
    del self.arr[self.length - 1]
    self.length -= 1
    return popped_item

myStack = Stack()
myStack.push('google')
myStack.push('microsoft')
myStack.push('facebook')
myStack.push('apple')
print(myStack)
x = myStack.peek()
print(x)
myStack.pop()
print(myStack)


