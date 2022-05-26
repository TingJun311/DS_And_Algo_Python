
class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,val):
    new_node = Node(val)
    if self.root == None:
      self.root = new_node
      return 
    temp = self.root
    while True:
      if new_node.val < temp.val:
        if temp.left == None:
          temp.left = new_node
          break
        else:
          temp = temp.left
      elif new_node.val > temp.val:
        if temp.right == None:
          temp.right = new_node
          break
        else:
          temp = temp.right

  def lookup(self,val):
    temp = self.root
    while True:
      if temp.val == val:
        return True
      elif temp == None:
        return False
      elif val < temp.val:
        temp = temp.left
      elif val > temp.val:
        temp = temp.right

  def inOrder(self,currentNode, myList):
    if currentNode != None:
      self.inOrder(currentNode.left, myList)
      myList.append(currentNode.val)
      self.inOrder(currentNode.right, myList)
    return myList

  def preOrder(self,currentNode, myList):
    if currentNode != None:
      myList.append(currentNode.val)
      self.preOrder(currentNode.left, myList)
      self.preOrder(currentNode.right, myList)
    return myList

#According to Andre's video , below is easily understandable

  def postOrder(self,currentNode, myList):
    if currentNode.left:
      self.postOrder(currentNode.left, myList)
    if currentNode.right:
      self.postOrder(currentNode.right, myList)
    myList.append(currentNode.val)
    return myList

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.inOrder(tree.root, []))
print(tree.preOrder(tree.root, []))
print(tree.postOrder(tree.root, []))

