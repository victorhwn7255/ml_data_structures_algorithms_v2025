import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def removeNthFromEnd(head: ListNode, n: int):
  dummy = ListNode(0)
  dummy.next = head
  prev = dummy
  slow = head
  fast = head
  for _ in range(1, n+1):
    fast = fast.next
  
  while fast is not None:
    slow = slow.next
    prev = prev.next
    fast = fast.next
  
  prev.next = slow.next
  
  return dummy.next


list_test = build_linked_list([1,2,3,4,5])
results = removeNthFromEnd(list_test, 2)
print(linked_list_to_list(results))