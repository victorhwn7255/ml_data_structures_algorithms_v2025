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
      
      
def reverseList(head: ListNode):
  prev = None
  current = head
  
  while current:
    after = current.next
    current.next = prev
    prev = current
    current = after
  
  return prev

head_1 = ListNode(1)
head_1.next = ListNode(2)
head_1.next.next = ListNode(3)
head_1.next.next.next = ListNode(4)
head_1.next.next.next.next = ListNode(5)

print(reverseList(head_1))