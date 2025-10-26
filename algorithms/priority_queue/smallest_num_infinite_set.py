import heapq

class SmallestInfiniteSet:
    def __init__(self):
      self.next = 1
      self.added_back = []
      self.in_heap = set()

    def popSmallest(self) -> int:
      if self.added_back:
        smallest = heapq.heappop(self.added_back)
        self.in_heap.remove(smallest)
        return smallest
      else:
        smallest = self.next
        self.next += 1
        return smallest

    def addBack(self, num: int) -> None:
      if num < self.next and num not in self.in_heap:
        heapq.heappush(self.added_back, num)
        self.in_heap.add(num)
      
