import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from utils.build_linked_list_test_case import build_linked_list, linked_list_to_list

import heapq

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def mergeKLists(lists: list[ListNode]):
  heap = []
  counter = 0
  for each_head in lists:
    if each_head:
      heapq.heappush(heap, (each_head.val, counter, each_head))
      counter += 1
  
  dummy = ListNode()
  current = dummy
  
  while heap:
    val, count, node = heapq.heappop(heap)
    current.next = node
    current = current.next
    
    if node.next:
      heapq.heappush(heap, (node.next.val, counter, node.next))
      counter += 1
  
  return dummy.next

