def findMaxAverage(nums: list[int], k: int) -> float:
  curent_sum = sum(nums[:k])
  max_sum = curent_sum
  
  for i in range (k, len(nums)):
    curent_sum = curent_sum - nums[i-k] + nums[i]
    max_sum = max(max_sum, curent_sum)
  
  return max_sum / k

nums_1 = [1,12,-5,-6,50,3]
k_1 = 4

nums_2 = [5]
k_2 = 1

print(findMaxAverage(nums_1, k_1))
print(findMaxAverage(nums_2, k_2))