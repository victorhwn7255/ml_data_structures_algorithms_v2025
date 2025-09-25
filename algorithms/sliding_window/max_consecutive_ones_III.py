def longestOnes (nums, k):
  max_window = 0
  left = 0
  count = 0
  
  for right in range(len(nums)):
    if nums[right] == 0:
      count += 1
      
    while count > k:
      if nums[left] == 0:
        count -= 1
      left += 1
    
    max_window = max(max_window, right - left + 1)
  
  return max_window


nums_1 = [1,1,1,0,0,0,1,1,1,1,0]
nums_2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]

k_1 = 2
k_2 = 3

print(longestOnes(nums_1, k_1))
print(longestOnes(nums_2, k_2))