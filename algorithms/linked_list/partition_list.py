import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
l1_test = build_linked_list([1,4,3,2,5,2])
l2_test = build_linked_list([2,1])

def partition(head: ListNode, x: int):
  if head is None:
    return None
  
  dummy_ge = ListNode(0)
  dummy_less = ListNode(0)
  less_tail = dummy_less
  ge_tail = dummy_ge
  
  current = head
  while current:
    next_node = current.next
    if current.val < x:
      less_tail.next = current
      less_tail = less_tail.next
    else:
      ge_tail.next = current
      ge_tail = ge_tail.next
    current = next_node
  
  ge_tail.next = None
  less_tail.next = dummy_ge.next
  
  return dummy_less.next

result_1 = partition(l1_test, 3)
result_2 = partition(l2_test, 2)

print(linked_list_to_list(result_1))
print(linked_list_to_list(result_2))