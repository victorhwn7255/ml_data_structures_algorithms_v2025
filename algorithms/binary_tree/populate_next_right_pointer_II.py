import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.tree_utils import print_tree

class TreeNode:
   def __init__(self, val=0, left:"TreeNode"=None, right:"TreeNode"=None, next:"TreeNode"=None):
      self.val = val
      self.left = left
      self.right = right
      self.next = next
   
   def __str__(self):
      return f"TreeNode({self.val})"
   
   def print_tree(self):
      print_tree(self)

def connect(root: TreeNode):
  if root is None:
    return None

  current_level_start = root
  while current_level_start:
    dummy = TreeNode(0)
    tail = dummy
    current = current_level_start
    while current:
      if current.left:
        tail.next = current.left
        tail = tail.next
      if current.right:
        tail.next = current.right
        tail = tail.next
      current = current.next
    current_level_start = dummy.next
  
  return root


from collections import deque

def connect_BFS(root: TreeNode):
  if root is None:
    return None
  
  queue = deque([root])
  while queue:
    level_size = len(queue)
    for i in range(level_size):
      current_node = queue.popleft()
      if i < level_size - 1:
        current_node.next = queue[0]
      else:
        current_node.next = None

      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)
      
  return root