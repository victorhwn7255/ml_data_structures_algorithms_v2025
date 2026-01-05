import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
l1_test = build_linked_list([1,2,3,4,5])
l2_test = build_linked_list([5])

def reverseBetween(head: ListNode, left, right):
  if left == right:
    return head
  
  current = head
  position = 1
  
  dummy = ListNode(0)
  dummy.next = head
  prev = dummy
  
  while position < left:
    prev = current
    current = current.next
    position += 1
  
  prev_left = prev
  left_node = current
  
  prev = None
  for _ in range(right - left + 1):
    temp = current.next
    current.next = prev
    prev = current
    current = temp
  
  prev_left.next = prev
  left_node.next = current
  
  return dummy.next

result_1 = reverseBetween(l1_test, 2, 4)
result_2 = reverseBetween(l2_test, 1, 1)

print(linked_list_to_list(result_1))
print(linked_list_to_list(result_2))