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
  
  return max_sum


head_1 = ListNode(5)
head_1.next = ListNode(4)
head_1.next.next = ListNode(2)
head_1.next.next.next = ListNode(1)

print(pairSum(head_1))