# Definition for singly-linked list.
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

def oddEvenList(head: ListNode):
  if not head or not head.next:
    return head
  
  odd = head
  even = head.next
  even_head = even
  
  while even and even.next:
    odd.next = even.next
    odd = odd.next
    
    even.next = odd.next
    even = even.next
  
  odd.next = even_head
  
  return head


head_1 = ListNode(1)
head_1.next = ListNode(2)
head_1.next.next = ListNode(3)
head_1.next.next.next = ListNode(4)
head_1.next.next.next.next = ListNode(5)

print(oddEvenList(head_1))