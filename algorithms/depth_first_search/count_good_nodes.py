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
      
def goodNodes(root: TreeNode):
  def dfs(node: TreeNode, current_max: int):
    if node is None:
      return 0
    
    if node.val >= current_max:
      count = 1
    else:
      count = 0
      
    new_max = max(current_max, node.val)
    
    count += dfs(node.left, new_max)
    count += dfs(node.right, new_max)
    
    return count
  
  return dfs(root, float('-inf'))


tree_1 = TreeNode(3)
tree_1.left = TreeNode(1)
tree_1.right = TreeNode(4)
tree_1.left.left = TreeNode(3)
tree_1.right.left = TreeNode(1)
tree_1.right.right = TreeNode(5)

tree_1.print_tree()

print(goodNodes(tree_1))


