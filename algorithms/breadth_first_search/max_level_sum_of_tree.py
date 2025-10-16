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
      
      
def maxLevelSum(root: TreeNode):
  queue = []
  sum_list = []
  index = 0
  
  queue.append(root)
  while index < len(queue):
    level_size = len(queue) - index
    current_level_val = []
    
    for _ in range(level_size):
      node: TreeNode = queue[index]
      index += 1
      current_level_val.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    
    sum_list.append(sum(current_level_val))
  
  return sum_list.index(max(sum_list)) + 1


tree_1 = TreeNode(1)
tree_1.left = TreeNode(7)
tree_1.right = TreeNode(0)
tree_1.left.left = TreeNode(7)
tree_1.left.right = TreeNode(-8)

tree_1.print_tree()

print(maxLevelSum(tree_1))