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
      
def sortedArrayToBST(nums: list[int]):
  def dfs(left, right):
    if left > right:
      return None
    
    middle = (left + right) // 2
    node = TreeNode(nums[middle])
    
    node.left = dfs(left, middle-1)
    node.right = dfs(middle + 1, right)
    
    return node
  
  return dfs(0, len(nums)-1)

print(sortedArrayToBST([-10,-3,0,5,9]))


