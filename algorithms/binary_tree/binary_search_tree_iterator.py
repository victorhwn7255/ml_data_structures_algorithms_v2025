import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.tree_utils import print_tree, build_tree

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
   
   def __str__(self):
      return f"TreeNode({self.val})"
   
   def print_tree(self):
      print_tree(self)
      
class BSTIterator:
  def __init__(self, root: TreeNode):
    self.stack = []
    current = root
    while current is not None:
      self.stack.append(current)
      current = current.left
    
  def next(self) -> int:
    result = self.stack.pop()
    if result.right:
      current = result.right
      while current:
        self.stack.append(current)
        current = current.left
    
    return result.val
    
  def hasNext(self) -> bool:
    return len(self.stack) != 0