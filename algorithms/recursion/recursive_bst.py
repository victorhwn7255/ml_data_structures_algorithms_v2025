class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class RecursiveBST:
  def __init__(self):
    self.root = None
    
  def __recursive_contains(self, current_node, value):
    if current_node == None:
      return False
    if value == current_node.value:
      return True
    elif value < current_node.value:
      return self.__recursive_contains(current_node.left, value)
    else:
      return self.__recursive_contains(current_node.right, value)
  
  def __recursive_insert(self, current_node, value):
    if current_node == None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__recursive_insert(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__recursive_insert(current_node.right, value)
    return current_node
  
  def contains_with_recursive(self, value):
    return self.__recursive_contains(self.root, value)
  
  def insert_with_recursive(self, value):
    if self.root == None:
      self.root = Node(value)
    self.__recursive_insert(self.root, value)