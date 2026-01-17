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
      
root_test_1 = build_tree([4,2,6,1,3], TreeNode)
root_test_2 = build_tree([1,0,48,None,None,12,49], TreeNode)

def getMinimumDifference(root: TreeNode):
  min_diff = float('inf')
  prev = None
  
  def dfs(node: TreeNode):
    nonlocal min_diff, prev
    if node is None:
      return
    dfs(node.left)
    if prev is not None:
      min_diff = min(min_diff, node.val - prev.val)
    prev = node
    dfs(node.right)
    
  dfs(root)
  
  return min_diff

print(getMinimumDifference(root_test_1))
print(getMinimumDifference(root_test_2))