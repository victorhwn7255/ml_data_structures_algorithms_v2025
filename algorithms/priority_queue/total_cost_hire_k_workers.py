import heapq

def totalCost(costs: list[int], k: int, candidates: int):
  total_cost = 0
  left = 0
  right = len(costs) - 1
  left_heap = []
  right_heap = []
  
  for _ in range(candidates):
    if left <= right:
      heapq.heappush(left_heap, (costs[left], left))
      left += 1
    if left <= right:
      heapq.heappush(right_heap, (costs[right], right))
      right -= 1
      
  for _ in range(k):
    if len(right_heap) == 0 or (left_heap and left_heap[0][0] <= right_heap[0][0]):
      cost, idx = heapq.heappop(left_heap)
      total_cost += cost
      if left <= right:
        heapq.heappush(left_heap, (costs[left], left))
        left += 1
    else:
      cost, idx = heapq.heappop(right_heap)
      total_cost += cost
      if left <= right:
        heapq.heappush(right_heap, (costs[right], right))
        right -= 1
  
  return total_cost


test_costs_1 = [17,12,10,2,7,2,11,20,8]
test_k_1 = 3
test_candidates_1 = 4

test_costs_2 = [1,2,4,1]
test_k_2 = 3
test_candidates_2 = 3

print(totalCost(test_costs_1, test_k_1, test_candidates_1))
print(totalCost(test_costs_2, test_k_2, test_candidates_2))