import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import create_test_case

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def hasCycle(head: ListNode):
  slow = head
  fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      return True
  
  return False

list_with_cycle = create_test_case([3,2,0,-4], 1)
list_with_cycle_2 = create_test_case([1, 2], 0)
list_with_cycle_3 = create_test_case([1], -1)

print(hasCycle(list_with_cycle))
print(hasCycle(list_with_cycle_2))
print(hasCycle(list_with_cycle_3))



