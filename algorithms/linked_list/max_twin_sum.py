class ListNode:
  def __init__(self, val=0, next=None):
     self.val = val
     self.next = next
     
  def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
      
def pairSum(head: ListNode):
  original_vals = []
  current = head
  while current:
    original_vals.append(current.val)
    current = current.next
    
  def reverse(head: ListNode):
    prev = None
    current = head
    
    while current:
      after = current.next
      current.next = prev
      prev = current
      current = after
      
    return prev
  
  reversed_head = reverse(head)
  max_sum = 0
  current_reversed = reversed_head
  
  for val in original_vals:
    max_sum = max(max_sum, val + current_reversed.val)
    current_reversed = current_reversed.next
  
  return max_sum


head_1 = ListNode(5)
head_1.next = ListNode(4)
head_1.next.next = ListNode(2)
head_1.next.next.next = ListNode(1)

print(pairSum(head_1))