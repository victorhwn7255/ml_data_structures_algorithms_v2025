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


def hasPathSum(root: TreeNode, targetSum: int):
  if root is None:
    return False
  if root.left is None and root.right is None:
    return root.val == targetSum

  next = targetSum - root.val

  return hasPathSum(root.left, next) or hasPathSum(root.right, next)


root_test_1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1], TreeNode)
target_sum_1 = 22

print(hasPathSum(root_test_1, target_sum_1))