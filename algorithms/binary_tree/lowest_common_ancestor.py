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
      
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):
  def dfs(node: TreeNode):
    if node is None:
      return None
    if node == p or node == q:
      return node
    
    left = dfs(node.left)
    right = dfs(node.right)
    
    if left and right:
      return node
    
    return left or right
  
  return dfs(root)

root_test_1 = build_tree([3,5,1,6,2,0,8,None,None,7,4], TreeNode)
root_test_2 = build_tree([[1,2]], TreeNode)

node_5 = TreeNode(5)
node_1 = TreeNode(1)
node_4 = TreeNode(4)

print(lowestCommonAncestor(root_test_1, node_5, node_1))
print(lowestCommonAncestor(root_test_1, node_5, node_4))