import heapq

def findKthLargest(nums: list[int], k: int):
  heap = nums[:k]
  heapq.heapify(heap)
  
  for num in nums[k:]:
    if num > heap[0]:
      heapq.heapreplace(heap, num)
  
  return heap[0]


test_1 = [3,2,1,5,6,4]
test_2 = [3,2,3,1,2,4,5,5,6]

print(findKthLargest(test_1, 2))
print(findKthLargest(test_2, 4))
