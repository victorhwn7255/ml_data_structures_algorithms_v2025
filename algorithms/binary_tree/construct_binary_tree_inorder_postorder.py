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
      
def buildTree(inorder: list[int], postorder: list[int]):
  if len(inorder) == 0 or len(postorder) == 0:
     return None 
  
  root_value = postorder[-1]
  root_node = TreeNode(root_value)
  
  root_index = inorder.index(root_value)
  left_inorder = inorder[ : root_index]
  right_inorder = inorder[ root_index+1 : ]
  
  left_size = len(left_inorder)
  left_postorder = postorder[ : left_size]
  right_postorder = postorder[ left_size : -1]
  
  root_node.left = buildTree(left_inorder, left_postorder)
  root_node.right = buildTree(right_inorder, right_postorder)
  
  return root_node