import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.tree_utils import print_tree

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
   
   def __str__(self):
      return f"TreeNode({self.val})"
   
   def print_tree(self):
      print_tree(self)
      
def longestZigZag(root: TreeNode): 
  max_length = 0
  
  def zigzag(node: TreeNode, direction, length):
    nonlocal max_length
    if node is None:
      return
    
    max_length = max(max_length, length)
    
    if direction == "left":
      zigzag(node.right, "right", length + 1)
      zigzag(node.left, "left", 1)
    if direction == "right":
      zigzag(node.left, "left", length + 1)
      zigzag(node.right, "right", 1)
    
  zigzag(root.left, "left", 1)
  zigzag(root.right, "right", 1)
  
  return max_length


tree_test = TreeNode(1)
tree_test.right = TreeNode(1)
tree_test.right.left = TreeNode(1)
tree_test.right.right = TreeNode(1)
tree_test.right.right.left = TreeNode(1)
tree_test.right.right.right = TreeNode(1)
tree_test.right.right.left.right = TreeNode(1)
tree_test.right.right.left.right.right = TreeNode(1)

tree_test.print_tree()

print(longestZigZag(tree_test))
