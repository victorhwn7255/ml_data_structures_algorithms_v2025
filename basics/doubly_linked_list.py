class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    
class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
    
  def print_List(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
      
  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    
    self.length -= 1
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      temp.next = None
      self.head.prev = None
    self.length -= 1
    return temp
  
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    
    temp = self.head
    if index < self.length/2:
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length-1, index, -1):
        temp = temp.prev
    return temp
      
  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    
  def inset(self, index, value):
    new_node = Node(value)
    
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
      
    temp = self.get(index)
    next = temp.next
    temp.next = new_node
    new_node.prev = temp
    next.prev = new_node
    new_node.next = next
    self.length += 1
    
    return True
    
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    else:
      temp = self.get(index)
      before = temp.prev
      after = temp.next
      before.next = after
      after.prev = before
      temp.prev = None
      temp.next = None
      self.length -= 1
      return temp
    
  
######################################################
new_list = DoublyLinkedList(3)

new_list.append(6)
new_list.append(9)
new_list.append(12)

new_list.pop()

new_list.prepend(42)
new_list.prepend(99)

new_list.pop_first()
new_list.set_value(2, 66)
new_list.inset(2, 99)

new_list.remove(1)

new_list.print_List()


print("index 2: ", new_list.get(0).value)