def longestSubarray(nums):
  left = 0
  max_length = 0
  zero_count = 0
  
  for right in range(len(nums)):
    if nums[right] == 0:
      zero_count += 1
      
    while zero_count > 1:
      if nums[left] == 0:
        zero_count -= 1
      left += 1

    max_length = max(right - left + 1, max_length)
  
  return max_length - 1


nums_1 = [1,1,0,1]
nums_2 = [0,1,1,1,0,1,1,0,1]
nums_3 = [1,1,1]

print(longestSubarray(nums_1))
print(longestSubarray(nums_2))
print(longestSubarray(nums_3))