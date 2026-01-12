import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.tree_utils import print_tree

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left :TreeNode = left
      self.right :TreeNode = right
   
   def __str__(self):
      return f"TreeNode({self.val})"
   
   def print_tree(self):
      print_tree(self)
      
def flatten(root: TreeNode):
  if root is None:
    return None
  
  current = root
  while current:
    if current.left:
      right_most = current.left
      while right_most.right:
        right_most = right_most.right
        
      right_most.right = current.right
      
      current.right = current.left
      current.left = None
    
    current = current.right