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
      
def maxPathSum(root:TreeNode):
  max_sum = -float('inf')
  
  def dfs(node: TreeNode):
    nonlocal max_sum
    if node is None:
      return 0
    
    left_gain = max(dfs(node.left, 0))
    right_gain = max(dfs(node.right, 0))
    
    current_path_sum = node.val + left_gain + right_gain
    max_sum = max(max_sum, current_path_sum)
    
    return node.val + max(left_gain, right_gain)
  
  dfs(root)
  return max_sum

