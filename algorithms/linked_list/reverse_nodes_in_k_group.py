import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
list_test = build_linked_list([1,2,3,4,5])

def reverseKGroup(head: ListNode, k: int):
  if head is None or k == 1:
    return head
  
  dummy = ListNode(0)
  dummy.next = head
  prev_group_tail = dummy
  current = head
  
  while True:
    k_th = current
    for _ in range(1, k+1):
      if k_th is None:
        return dummy.next
      k_th = k_th.next
    
    group_head = current
    prev = None
    for _ in range(1, k+1):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
      
    prev_group_tail.next = prev
    group_head.next = current
    
    prev_group_tail =group_head
  

test_result = reverseKGroup(list_test, 2)

print(linked_list_to_list(test_result))