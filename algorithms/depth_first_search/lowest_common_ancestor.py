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
      
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
  if root is None:
    return None
  if root == p or root == q:
    return root
  
  left = lowestCommonAncestor(root.left, p, q)
  right = lowestCommonAncestor(root.right, p, q)
  
  if left and right:
    return root
  else:
    return left if left else right



tree_test = TreeNode(3)
tree_test.left = TreeNode(5)
tree_test.right = TreeNode(1)
tree_test.left.left = TreeNode(6)
tree_test.left.right = TreeNode(2)
tree_test.right.left = TreeNode(0)
tree_test.right.right = TreeNode(8)
tree_test.left.right.left = TreeNode(7)
tree_test.left.right.right = TreeNode(4)

tree_test.print_tree()

p_node = tree_test.left  # This is the node with value 5
q_node = tree_test.left.right.right  # This is the node with value 4
print(lowestCommonAncestor(tree_test, p_node, q_node))