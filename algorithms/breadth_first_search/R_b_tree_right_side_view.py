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

from collections import deque
def rightSideView(root: TreeNode):
  if root is None:
    return []
  
  queue = deque([root])
  result = []
  
  while len(queue) > 0:
    level_size = len(queue)
    for _ in range(level_size):
      node = queue.popleft()
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    result.append(node.val)
      
  return result
    