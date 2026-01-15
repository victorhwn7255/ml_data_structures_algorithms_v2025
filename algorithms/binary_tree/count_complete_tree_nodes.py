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
      
def countNodes(root: TreeNode):
  if root is None:
    return 0
  
  def left_depth(node: TreeNode):
    d = 0
    while node:
      d += 1
      node = node.left
    return d
  def right_depth(node: TreeNode):
    d = 0
    while node:
      d += 1
      node = node.right
    return d
  
  left_d = left_depth(root)
  right_d = right_depth(root)
  
  if left_d == right_d:
    return (2**left_d) - 1
  
  return 1 + countNodes(root.right) + countNodes(root.left)

root_test_1 = build_tree([1,2,3,4,5,6], TreeNode)

print(countNodes(root_test_1))