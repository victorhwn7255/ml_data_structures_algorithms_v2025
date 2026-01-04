import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def mergeTwoLists(list1: ListNode, list2: ListNode):
  dummy = ListNode(0)
  current = dummy

  while list1 and list2:
    if list1.val >= list2.val:
      current.next = list2
      list2 = list2.next
    else:
      current.next = list1
      list1 = list1.next
    current = current.next
  
  current.next = list1 or list2
  
  return dummy.next

l1_test = build_linked_list([1,2,4])
l2_test = build_linked_list([1,3,4])

test_result = mergeTwoLists(l1_test, l2_test)

print(linked_list_to_list(test_result))