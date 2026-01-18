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
      
root_test_1 = build_tree([3,1,4,None,2], TreeNode)
root_test_2 = build_tree([5,3,6,2,4,None,None,1], TreeNode)

from collections import deque
def kthSmallest(root: TreeNode, k:int):
  node_list = []
  def dfs(node:TreeNode):
    if node is None:
      return
    dfs(node.left)
    node_list.append(node.val)
    dfs(node.right)
  
  dfs(root)
  
  return node_list[k-1]

print(kthSmallest(root_test_1, 1))
print(kthSmallest(root_test_2, 3))