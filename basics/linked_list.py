class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
    
  #def append(self, value):
    
  
  #def prepend(self, value):
  
  
  #def insert(self, index, value):
  
  

myLinkedList = LinkedList(4)

print(myLinkedList.tail.value)