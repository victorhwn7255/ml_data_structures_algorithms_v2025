import heapq

def maxScore(nums1: list[int], nums2: list[int], k: int):
  pairs = sorted(zip(nums2, nums1), reverse=True)
  heap = []
  sum_nums1 = 0
  max_score = 0
  
  for num2, num1 in pairs:
    heapq.heappush(heap, num1)
    sum_nums1 += num1
      
    if len(heap) > k:
      sum_nums1 -= heapq.heappop(heap)
      
    if len(heap) == k:
      max_score = max(max_score, sum_nums1 * num2)
  
  return max_score

test_1_1 = [1,3,3,2]
test_1_2 = [2,1,3,4]
k_1 = 3


test_2_1 = [4,2,3,1,1]
test_2_2 = [7,5,10,9,6]
k_2 = 1

print(maxScore(test_1_1, test_1_2, k_1))
print(maxScore(test_2_1, test_2_2, k_2))