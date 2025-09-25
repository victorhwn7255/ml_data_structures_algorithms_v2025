class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class BinarySearchTree:
  def __init__(self):
    self.root = None
    
  def insert(self, value):
    new_node = Node(value)
    
    if self.root == None:
      self.root = new_node
      return True
      
    temp = self.root
    while (True):
      if new_node.value == temp.value:
        return False
      
      if new_node.value < temp.value:
        if temp.left == None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right == None:
          temp.right = new_node
          return True
        temp = temp.right
        
  def contains(self, value):
    if self.root == None:
      return False
    
    temp = self.root
    while(True):
      if value < temp.value:
        if temp.left == None:
          return False
        temp = temp.left
      elif value > temp.value:
        if temp.right == None:
          return False
        temp = temp.right
      else:
        return True
    
    
my_BST = BinarySearchTree()

my_BST.insert(3)
my_BST.insert(1)
my_BST.insert(6)



print(my_BST.root.value)
print(my_BST.root.left.value)
print(my_BST.root.right.value)

print(my_BST.contains(9))