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
      
def searchBST(root: TreeNode, val: int):
  if root is None:
    return None
  if root.val == val:
    return root
  
  if val < root.val:
    return searchBST(root.left, val)
  else:
    return searchBST(root.right, val)


tree_1 = TreeNode(4)
tree_1.left = TreeNode(2)
tree_1.right = TreeNode(7)
tree_1.left.left = TreeNode(1)
tree_1.left.right = TreeNode(3)

tree_1.print_tree()

print(searchBST(tree_1, 2))