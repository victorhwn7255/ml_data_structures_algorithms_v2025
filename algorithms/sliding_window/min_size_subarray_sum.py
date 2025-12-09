def minSubArrayLen(nums: list[int], target: int):
  left = 0
  current_sum = 0
  min_length = float('inf')
  
  for right in range(len(nums)):
    current_sum += nums[right]
    
    while current_sum >= target:
      min_length = min(min_length, right - left + 1)
      current_sum -= nums[left]
      left += 1
  
  return min_length if min_length != float('inf') else 0


print(minSubArrayLen([2,3,1,2,4,3], 7))
print(minSubArrayLen([1,4,4], 4))
print(minSubArrayLen([1,1,1,1,1,1,1,1], 11))