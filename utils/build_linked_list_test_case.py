class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def build_linked_list(values):
  if not values:
    return None
  
  head = ListNode(values[0])
  current = head
  
  for val in values[1:]:
    current.next = ListNode(val)
    current = current.next
  
  return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def create_test_case(values, pos):
      head = build_linked_list(values)

      if pos == -1:  # No cycle
          return head

      # Create cycle: find the node at position 'pos'
      cycle_node = head
      for i in range(pos):
          cycle_node = cycle_node.next

      # Find the tail and connect it to cycle_node
      current = head
      while current.next:
          current = current.next
      current.next = cycle_node

      return head