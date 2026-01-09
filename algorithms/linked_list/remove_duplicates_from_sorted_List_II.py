import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
l1_test = build_linked_list([1,2,3,3,4,4,5])
l2_test = build_linked_list([1,1,1,2,3])

def deleteDuplicates(head: ListNode):
  dummy = ListNode(0)
  dummy.next = head
  current = head
  prev = dummy
  
  while current:
    if current.next and current.val == current.next.val:
      dup_val = current.val
      while current and current.val == dup_val:
        current = current.next
      prev.next = current
    else:
      prev = prev.next
      current = current.next
      
  return dummy.next

result_1 = deleteDuplicates(l1_test)
result_2 = deleteDuplicates(l2_test)

print(linked_list_to_list(result_1))
print(linked_list_to_list(result_2))