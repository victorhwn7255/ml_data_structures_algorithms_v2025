import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def sortList(head: ListNode):
  if head is None or head.next is None:
    return head
  
  dummy = ListNode(0)
  current = dummy
  slow = head
  fast = head.next
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
  middle = slow
  
  right_head = middle.next
  middle.next = None
  
  left_list = sortList(head)
  right_list = sortList(right_head)
  
  while left_list and right_list:
    if left_list.val <= right_list.val:
      current.next = left_list
      left_list = left_list.next
    else:
      current.next = right_list
      right_list = right_list.next
    current = current.next
  
  if left_list:
    current.next = left_list
  else:
    current.next = right_list
  
  return dummy.next


l1_test = build_linked_list([4,2,1,3])
l2_test = build_linked_list([-1,5,3,4,0])

test_result_1 = sortList(l1_test)
test_result_2 = sortList(l2_test)

print(linked_list_to_list(test_result_1))
print(linked_list_to_list(test_result_2))