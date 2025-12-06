import random

class RandomizedSet:
  def __init__(self):
    self.values = []
    self.indices = {}
    
  def insert(self, val: int):
    if val in self.indices:
      return False
    
    self.indices[val] = len(self.values)
    self.values.append(val)
    return True
  
  def remove(self, val: int):
    if val not in self.indices:
      return False
    
    index = self.indices[val]
    last_num = self.values[-1]
    
    self.values[index] = last_num
    self.indices[last_num] = index
    
    self.values.pop()
    del self.indices[val]
        
    return True
    
  def getRandom(self):
    
    return random.choice(self.values)
    
    
obj_1 = RandomizedSet()

print(obj_1.getRandom)

