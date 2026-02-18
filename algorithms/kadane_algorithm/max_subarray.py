def maxSubArray(nums: list[int]):
  best_ending = nums[0]
  best_result = nums[0]
  
  for i in range(1, len(nums)):
    x = nums[i]
    
    best_ending = max(x, best_ending + x)
    best_result = max(best_result, best_ending)
  
  return best_result

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))