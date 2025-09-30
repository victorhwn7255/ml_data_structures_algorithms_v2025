class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
class RecursiveBST:
  def __init__(self):
    self.root = None
  
  def __recursive_contains(self, current_node: Node, value):
    if current_node == None:
      return False
    if value == current_node.value:
      return True
    elif value < current_node.value:
      return self.__recursive_contains(current_node.left, value)
    else:
      return self.__recursive_contains(current_node.right, value)
  
  def __recursive_insert(self, current_node: Node, value):
    if current_node == None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__recursive_insert(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__recursive_insert(current_node.right, value)
    return current_node
  
  def min_value(self, current_node: Node):
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.value
  
  def __delete_node(self, current_node: Node, value):
    if current_node == None:
      return None
    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__delete_node(current_node.right, value)
    else:
      if current_node.left == None and current_node.right == None:
        return None
      elif current_node.left == None:
        current_node = current_node.right
      elif current_node.right == None:
        current_node = current_node.left
      else:
        sub_tree_min = self.min_value(current_node.right)
        current_node.value = sub_tree_min
        current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node
  
  def contains_with_recursive(self, value):
    return self.__recursive_contains(self.root, value)
  
  def insert_with_recursive(self, value):
    if self.root == None:
      self.root = Node(value)
    self.__recursive_insert(self.root, value)
    
  def delete_with_recursive(self, value):
    self.root = self.__delete_node(self.root, value)
    
    
    
my_tree = RecursiveBST()
my_tree.insert_with_recursive(42)
my_tree.insert_with_recursive(33)
my_tree.insert_with_recursive(69)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print("--------------------")

my_tree.delete_with_recursive(42)

print(my_tree.root.value)
print(my_tree.root.left.value)