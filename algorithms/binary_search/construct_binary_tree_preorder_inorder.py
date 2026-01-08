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
      
def buildTree(preorder: list[int], inorder: list[int]):
  if len(preorder) == 0 or len(inorder) == 0:
    return None
  
  root_value = preorder[0]
  root_node = TreeNode(root_value)
  root_index = inorder.index(root_value)

  left_inorder = inorder[ : root_index]
  right_inorder = inorder[root_index + 1: ]
      
  left_size = len(left_inorder)
  left_preorder = preorder[1: 1 + left_size]
  right_preorder = preorder[1 + left_size :]
    
      
  root_node.left = buildTree(left_preorder, left_inorder)
  root_node.right = buildTree(right_preorder, right_inorder)
  
  return root_node

