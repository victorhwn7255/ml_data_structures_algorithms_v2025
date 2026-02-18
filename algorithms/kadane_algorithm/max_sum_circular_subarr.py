def maxSubarraySumCircular(nums: list[int]):
  global_max = nums[0]
  global_min = nums[0]
  total_sum = 0
  current_max = 0
  current_min = 0
  
  for num in nums:
    total_sum += num
    current_max = max(num, current_max + num)
    global_max = max(global_max, current_max)
    current_min = min(num, current_min + num)
    global_min = min(global_min, current_min)
  
  if global_max < 0:
    return global_max
  
  return max(global_max, total_sum - global_min)

print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([5,-3,5]))
print(maxSubarraySumCircular([-3,-2,-3]))