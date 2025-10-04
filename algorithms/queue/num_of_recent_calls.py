class RecentCounter:
  def __init__(self):
    self.queue = []
  
  def ping(self, t: int) -> int:
    self.queue.append(t)
    while self.queue and self.queue[0] < t - 3000:
      self.queue.pop(0)
      
    return len(self.queue)
    
    
    
obj = RecentCounter()

param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)

print(param_1)
print(param_2)
print(param_3)
print(param_4)