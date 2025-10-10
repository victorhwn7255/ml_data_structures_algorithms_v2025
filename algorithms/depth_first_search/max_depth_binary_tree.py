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
      
def maxDepth(root: TreeNode):
  if root is None:
    return 0
  
  max_depth = 1 + max(maxDepth(root.left), maxDepth(root.right))
  
  return max_depth


tree_test = TreeNode(3)
tree_test.left = TreeNode(9)
tree_test.right = TreeNode(20)
tree_test.left.left = TreeNode(15)
tree_test.left.right = TreeNode(7)

tree_test.print_tree()

print(maxDepth(tree_test))