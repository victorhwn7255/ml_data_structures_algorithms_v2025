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
  max_sum = 0
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  def reverse(head: ListNode):
    prev = None
    while head:
      after = head.next
      head.next = prev
      prev = head
      head = after
    return prev
  
  second_half = reverse(slow)
  first_half = head
  
  while second_half:
    max_sum = max(max_sum, first_half.val + second_half.val)
    first_half = first_half.next
    second_half = second_half.next
    
  return max_sum


head_1 = ListNode(5)
head_1.next = ListNode(4)
head_1.next.next = ListNode(2)
head_1.next.next.next = ListNode(1)

print(pairSum(head_1))