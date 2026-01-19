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
      
root_test_1 = build_tree([2,1,3], TreeNode)
root_test_2 = build_tree([5,1,4,None,None,3,6], TreeNode)

def isValidBST(root: TreeNode):
  def dfs(node: TreeNode, low, high):
    if node is None:
      return True
    if node.val <= low or node.val >= high:
      return False
    
    left_is_valid = dfs(node.left, low, node.val)
    right_is_valid = dfs(node.right, node.val, high)
    
    return left_is_valid and right_is_valid
  
  return dfs(root, -float('inf'), float('inf'))


print(isValidBST(root_test_1))
print(isValidBST(root_test_2))