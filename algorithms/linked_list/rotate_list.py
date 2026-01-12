import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

l1_test = build_linked_list([1,2,3,4,5])
l2_test = build_linked_list([0,1,2])

def rotateRight(head: ListNode, k: int):
  if head is None:
    return None
  if head.next is None:
    return head
  if k == 0:
    return head
  
  current = head
  tail = head
  count = 0
  while current:
    count += 1
    tail = current
    current = current.next

  tail.next = head
  
  k = k % count # eg. 5%2 = 1; 2%5 = 2
  new_tail = head
  for _ in range(count - k- 1):
    new_tail = new_tail.next
  
  new_head = new_tail.next
  new_tail.next = None
  
  return new_head

result_1 = rotateRight(l1_test, 2)
result_2 = rotateRight(l2_test, 4)

print(linked_list_to_list(result_1))
print(linked_list_to_list(result_2))