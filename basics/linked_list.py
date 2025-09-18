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
    
  def print_list(self):
    print("-------")
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
    
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True
  
  def pop(self):
    temp = self.head
    pre = self.head
    
    if self.length == 0:
      return None
    
    while temp.next is not None:
      pre = temp
      temp = temp.next
    
    self.tail = pre
    pre.next = None
    self.length -= 1
    
    if self.length == 0:
      self.head = None
      self.tail = None
      
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    temp = self.head
    if self.length == 0:
      return None
    elif self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
    
    temp.next = None
    self.length -= 1
    return temp
    
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    
    temp = self.head
    for _ in range(index):
      temp = temp.next
      
    return temp
  
  def set_value(self, index, value):
    if index < 0 or index >= self.length:
      return None
    
    temp = self.head
    for _ in range(index):
      temp = temp.next
    temp.value = value
    
    return temp.value
      
  
  def insert(self, index, value):
    if index < 0 or index >= self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    
    new_node = Node(value)
    temp = self.get(index-1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
    
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if self.length == 0:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    
    temp = self.get(index)
    prev = self.get(index-1)
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp
    
  def reverse(self):
    if self.length == 0:
      return None
    if self.length == 1:
      return self.head()
    
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
      
    
    

myLinkedList = LinkedList(4)
myLinkedList.append(3)
myLinkedList.append(6)

myLinkedList.prepend(9)

myLinkedList.set_value(2, 42)

myLinkedList.insert(2, 69)

myLinkedList.reverse()

myLinkedList.print_list()

