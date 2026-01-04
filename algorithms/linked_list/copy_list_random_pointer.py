import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
def copyRandomList(head: Node):
  if head is None:
    return None
  
  table = {}
  
  current = head
  while current is not None:
    copy = Node(current.val)
    table[current] = copy
    current = current.next
  
  current = head
  while current is not None:
    copy = table[current]
    
    if current.next:
      copy.next = table[current.next]
    else:
      copy.next = None
      
    if current.random:
      copy.random = table[current.random]
    else:
      copy.random = None
    
    current = current.next
  
  return table[head]

