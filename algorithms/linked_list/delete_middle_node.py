class ListNode:
    def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

def deleteMiddle(head: ListNode) -> list[ListNode]:
    if not head:
      return None
    if not head.next:
      return None
    
    count = 0
    current = head
    while current:
      count += 1
      current = current.next
    
    middle_index = count // 2
    
    temp = head
    for i in range(middle_index - 1):
      temp = temp.next
      
    temp.next = temp.next.next
    
    return head

head_1 = ListNode(1)
head_1.next = ListNode(2)
head_1.next.next = ListNode(3)
head_1.next.next.next = ListNode(6)
head_1.next.next.next.next = ListNode(9)

print(deleteMiddle(head_1))
