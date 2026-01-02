import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
  start = ListNode(0)
  current = start
  carry = 0
  
  while l1 or l2 or carry:
    digit1 = l1.val if l1 else 0
    digit2 = l2.val if l2 else 0
    total = digit1 + digit2 + carry
    new_digit = total % 10
    carry = total // 10
    current.next = ListNode(new_digit)
    current = current.next
    if l1:
      l1 = l1.next
    if l2:
      l2 = l2.next
  
  return start.next


l1_test = build_linked_list([2,4,3])
l2_test = build_linked_list([5,6,4])

test_result = addTwoNumbers(l1_test, l2_test)

print(linked_list_to_list(test_result))