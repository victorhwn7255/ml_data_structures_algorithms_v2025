def pivotIndex(nums):
  total_sum = sum(nums)
  left_sum = 0
  
  for i in range(len(nums)):
    if left_sum == total_sum - left_sum - nums[i]:
      return i
    left_sum += nums[i]
  
  return -1

nums_1 = [1,7,3,6,5,6]
nums_2 = [1,2,3]
nums_3 = [2,1,-1]

print(pivotIndex(nums_1))
print(pivotIndex(nums_2))
print(pivotIndex(nums_3))