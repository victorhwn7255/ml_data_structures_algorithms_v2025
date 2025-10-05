class ListNode:
    def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

# use FAST and SLOW pointers
def deleteMiddle(head: ListNode) -> list[ListNode]:
    if not head or not head.next:
      return None
    
    prev = head
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    
    prev.next = slow.next
    
    return head

head_1 = ListNode(1)
head_1.next = ListNode(2)
head_1.next.next = ListNode(3)
head_1.next.next.next = ListNode(6)
head_1.next.next.next.next = ListNode(9)

print(deleteMiddle(head_1))