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
    
  def BFS(self):
    current_node: Node = self.root
    queue = []
    results = []
    
    queue.append(current_node)
    while len(queue) > 0:
      current_node = queue.pop(0)
      results.append(current_node.value)
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)
    
    return results
    
  def DFS_Pre_Order(self):
    results = []
    
    def traverse(current_node: Node):
      results.append(current_node.value)
      if current_node.left is not None:
        traverse(current_node.left)
      if current_node.right is not None:
        traverse(current_node.right)
      
    traverse(self.root)
    return results
  
  def DFS_Post_Order(self):
    results = []
    
    def traverse(current_node: Node):
      if current_node.left is not None:
        traverse(current_node.left)
      if current_node.right is not None:
        traverse(current_node.right)
      results.append(current_node.value)
      
    traverse(self.root)
    return results
      
    
my_BST = BinarySearchTree()

my_BST.insert(3)
my_BST.insert(1)
my_BST.insert(6)

print(my_BST.root.value)
print(my_BST.root.left.value)
print(my_BST.root.right.value)

print(my_BST.BFS())