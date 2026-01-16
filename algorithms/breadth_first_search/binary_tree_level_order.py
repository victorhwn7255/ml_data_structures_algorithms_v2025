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
      
root_test_1 = build_tree([3,9,20,None,None,15,7], TreeNode)
root_test_2 = build_tree([1], TreeNode)

from collections import deque
def levelOrder(root: TreeNode):
  if root is None:
    return []
  results = []
  queue = deque([root])
  while queue:
    level_size = len(queue)
    current_level = []
    for _ in range(level_size):
      node = queue.popleft()
      current_level.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    results.append(current_level)
  
  return results

print(levelOrder(root_test_1))
print(levelOrder(root_test_2))