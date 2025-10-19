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
      
def deleteNode(root: TreeNode, key: int):
  def findMin(node:TreeNode):
    while node.left:
      node = node.left
    return node
  
  def dfs_delete(node: TreeNode, key):
    if node is None:
      return None
    
    if node.val > key:
      node.left = dfs_delete(node.left, key)
    elif node.val < key:
      node.right = dfs_delete(node.right, key)
    else:
      if node.left is None and node.right is None:
        return None
      if node.left is None:
        return node.right
      if node.right is None:
        return node.left
  
      successor = findMin(node.right)
      node.val = successor.val
      node.right = dfs_delete(node.right, successor.val)
    
    return node
  
  return dfs_delete(root, key)


tree_1 = TreeNode(5)
tree_1.left = TreeNode(3)
tree_1.right = TreeNode(6)
tree_1.left.left = TreeNode(2)
tree_1.left.right = TreeNode(4)
tree_1.right.right = TreeNode(7)

tree_1.print_tree()

print(deleteNode(tree_1, 3))