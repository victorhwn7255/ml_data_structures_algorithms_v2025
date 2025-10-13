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
      
def pathSum(root: TreeNode, targetSum: int) -> int:
  prefix_sum = {0 : 1}
  
  def dfs(node: TreeNode, currentSum):
    if node is None:
      return 0
    
    currentSum += node.val
    count = prefix_sum.get(currentSum - targetSum, 0)
    
    prefix_sum[currentSum] = prefix_sum.get(currentSum, 0) + 1
    
    count += dfs(node.left, currentSum)
    count += dfs(node.right, currentSum)
    
    prefix_sum[currentSum] -= 1
    
    return count

  return dfs(root, 0)


tree_test = TreeNode(10)
tree_test.left = TreeNode(5)
tree_test.right = TreeNode(-3)
tree_test.left.left = TreeNode(3)
tree_test.left.right = TreeNode(2)
tree_test.right.right = TreeNode(11)
tree_test.left.left.left = TreeNode(3)
tree_test.left.left.right = TreeNode(-2)
tree_test.left.right.right = TreeNode(1)

tree_test.print_tree()

print(pathSum(tree_test, 8))