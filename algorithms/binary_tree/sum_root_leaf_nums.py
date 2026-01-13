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
      
def sumNumbers(root: TreeNode):
  def dfs(node: TreeNode, curr_val: int):
    if node is None:
      return 0
    curr_val = curr_val * 10 + node.val
    if node.left is None and node.right is None:
      return curr_val
    return dfs(node.left, curr_val) + dfs(node.right, curr_val)
  
  return dfs(root, 0)

test_root_1 = build_tree([1,2,3], TreeNode)
test_root_2 = build_tree([4,9,0,5,1], TreeNode)

print(sumNumbers(test_root_1))
print(sumNumbers(test_root_2))

